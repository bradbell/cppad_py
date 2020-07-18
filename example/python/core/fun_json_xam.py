# -----------------------------------------------------------------------------
#         cppad_py: A C++ Object Library and Python Interface to Cppad
#          Copyright (C) 2017-20 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# -----------------------------------------------------------------------------
# d_fun json
# -----------------------------------------------------------------------------
# BEGIN_TO_JSON_XAM
def to_json_xam() :
    #
    import numpy
    import cppad_py
    import re
    #
    # initialize return variable
    ok = True
    # ---------------------------------------------------------------------
    n = 1 # number of independent variables
    m = 2 # number of dependent variables
    #
    # independent variables
    x  = numpy.array( [ 1.0 ] )
    ax = cppad_py.independent(x)
    #
    # f(x) = [ x0 + x0, sin(x0) ]
    ay = numpy.empty(m, dtype=cppad_py.a_double)
    ay[0] = ax[0] + ax[0]
    ay[1] = ax[0].sin()
    f     = cppad_py.d_fun(ax, ay)
    #
    # check f.to_json
    json     = f.to_json()
    pattern  = r'"op_code" *: *([^,]*),'
    match    = re.search(pattern, json)
    op_code  = int( match.group(1) )
    ok      &= op_code == 1
    pattern  = r'"name" *: *"([^"]*)" *,'
    match    = re.search(pattern, json)
    name     = match.group(1);
    ok      &= name == 'add' or name == 'sub'
    #
    return ok
# END_TO_JSON_XAM
#
# $begin fun_to_json_xam.py$$ $newlinech #$$
# $spell
#     json
# $$
# $section Python to_json: Example and Test$$
# $srcthisfile|0|# BEGIN_TO_JSON_XAM|# END_TO_JSON_XAM|$$
# $end
# -----------------------------------------------------------------------------
# BEGIN_FROM_JSON_XAM
def from_json_xam() :
    #
    import numpy
    import cppad_py
    import math
    #
    # initialize return variable
    ok = True
    # ---------------------------------------------------------------------
    # AD graph repersentation of f(x) = sin(x) / cos(x)
    #
    # node_1 : x[0]
    # node_2 : sin( x[0] )
    # node_3 : cos( x[0] )
    # node_4 : sin( x[0] ) / cos( x[0] )
    # y[0]   = sin( x[0] ) / cos( x[0] )
    json = '''
        {
            "function_name" : "tangent function",
            "op_define_vec" : [ 3, [
                { "op_code":1, "name":"sin", "n_arg":1 } ,
                { "op_code":2, "name":"cos", "n_arg":1 } ,
                { "op_code":3, "name":"div", "n_arg":2 } ]
            ],
            "n_dynamic_ind"  : 0,
            "n_variable_ind" : 1,
            "constant_vec"   : [ 0, [ ] ],
            "op_usage_vec"   : [ 3, [
                [ 1, 1 ]   ,
                [ 2, 1 ]   ,
                [ 3, 2, 3] ]
            ],
            "dependent_vec" : [ 1, [4] ]
        };
    '''
    # convert json to a fucntion object
    f = cppad_py.d_fun();
    f.from_json(json);
    #
    # compute y = f(x)
    x  = numpy.array( [ 1.0 ] );
    y  = f.forward(0, x);
    #
    # check the function value
    eps99     = 99.0 * numpy.finfo(float).eps
    check     = math.tan(x[0]);
    rel_error = y[0] / check - 1.0;
    ok       &= abs( rel_error ) < eps99;
    #
    return ok
# END_FROM_JSON_XAM
#
# $begin fun_from_json_xam.py$$ $newlinech #$$
# $spell
#     json
# $$
# $section Python from_json: Example and Test$$
# $srcthisfile|0|# BEGIN_FROM_JSON_XAM|# END_FROM_JSON_XAM|$$
# $end
# -----------------------------------------------------------------------------
def fun_json_xam() :
    ok  = to_json_xam()
    ok &= from_json_xam()
    return ok
