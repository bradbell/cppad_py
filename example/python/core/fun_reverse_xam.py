# -----------------------------------------------------------------------------
#         cppad_py: A C++ Object Library and Python Interface to Cppad
#          Copyright (C) 2017-20 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# -----------------------------------------------------------------------------
# reverse
# -----------------------------------------------------------------------------
# BEGIN SOURCE
def fun_reverse_xam() :
    #
    import numpy
    import cppad_py
    #
    # initialize return variable
    ok = True
    # ---------------------------------------------------------------------
    # number of dependent and independent variables
    n_dep = 1
    n_ind = 3
    #
    # create the independent variables ax
    xp = numpy.empty(n_ind, dtype=float)
    for i in range( n_ind  ) :
        xp[i] = i
    #
    ax = cppad_py.independent(xp)
    #
    # create dependent variables ay with ay0 = ax_0 * ax_1 * ax_2
    ax_0  = ax[0]
    ax_1  = ax[1]
    ax_2  = ax[2]
    ay    = numpy.empty(n_dep, dtype=cppad_py.a_double)
    ay[0] = ax_0 * ax_1 * ax_2
    #
    # define af corresponding to f(x) = x_0 * x_1 * x_2
    f  = cppad_py.d_fun(ax, ay)
    # -----------------------------------------------------------------------
    # define          X(t) = (x_0 + t, x_1 + t, x_2 + t)
    # it follows that Y(t) = f(X(t)) = (x_0 + t) * (x_1 + t) * (x_2 + t)
    # and that       Y'(0) = x_1 * x_2 + x_0 * x_2 + x_0 * x_1
    # -----------------------------------------------------------------------
    # zero order forward mode
    p     = 0
    xp[0] = 2.0
    xp[1] = 3.0
    xp[2] = 4.0
    yp = f.forward(p, xp)
    ok = ok and yp[0] == 24.0
    # -----------------------------------------------------------------------
    # first order reverse (derivative of zero order forward)
    # define G( Y ) = y_0 = x_0 * x_1 * x_2
    m         = f.size_range()
    q         = 1
    yq1       = numpy.empty( (m, q), dtype=float)
    yq1[0, 0] = 1.0
    xq1       = f.reverse(q, yq1)
    # partial G w.r.t x_0
    ok = ok and xq1[0,0] == 3.0 * 4.0
    # partial G w.r.t x_1
    ok = ok and xq1[1,0] == 2.0 * 4.0
    # partial G w.r.t x_2
    ok = ok and xq1[2,0] == 2.0 * 3.0
    # -----------------------------------------------------------------------
    # first order forward mode
    p     = 1
    xp[0] = 1.0
    xp[1] = 1.0
    xp[2] = 1.0
    yp    = f.forward(p, xp)
    ok    = ok and yp[0] == 3.0*4.0 + 2.0*4.0 + 2.0*3.0
    # -----------------------------------------------------------------------
    # second order reverse (derivative of first order forward)
    # define G( y_0^0 , y_0^1 ) = y_0^1
    # = x_1^0 * x_2^0  +  x_0^0 * x_2^0  +  x_0^0  *  x_1^0
    q         = 2
    yq2       = numpy.empty( (m, q), dtype=float)
    yq2[0, 0] = 0.0 # partial of G w.r.t y_0^0
    yq2[0, 1] = 1.0 # partial of G w.r.t y_0^1
    xq2       = f.reverse(q, yq2)
    # partial G w.r.t x_0^0
    ok = ok and xq2[0, 0] == 3.0 + 4.0
    # partial G w.r.t x_1^0
    ok = ok and xq2[1, 0] == 2.0 + 4.0
    # partial G w.r.t x_2^0
    ok = ok and xq2[2, 0] == 2.0 + 3.0
    # -----------------------------------------------------------------------
    af = cppad_py.a_fun(f)
    #
    # zero order forward
    axp   = numpy.empty(n_ind, dtype=cppad_py.a_double)
    p     = 0
    axp[0] = 2.0
    axp[1] = 3.0
    axp[2] = 4.0
    ayp = af.forward(p, axp)
    ok = ok and ayp[0] == cppad_py.a_double(24.0)
    #
    # first order reverse
    q          = 1
    ayq1       = numpy.empty( (m, q), dtype=cppad_py.a_double)
    ayq1[0, 0] = 1.0
    axq1       = af.reverse(q, ayq1)
    # partial G w.r.t x_0
    ok = ok and axq1[0,0] == cppad_py.a_double(3.0 * 4.0)
    # partial G w.r.t x_1
    ok = ok and axq1[1,0] == cppad_py.a_double(2.0 * 4.0)
    # partial G w.r.t x_2
    ok = ok and axq1[2,0] == cppad_py.a_double(2.0 * 3.0)
    #
    return( ok )
#
# END SOURCE
#
# $begin fun_reverse_xam.py$$ $newlinech #$$
# $spell
#   py
#   perl
#   cppad
#   py
#   xam
#   Jacobian
#   Jacobians
# $$
# $section Python: Reverse Mode AD: Example and Test$$
# $srcthisfile|0|# BEGIN SOURCE|# END SOURCE|$$
# $end
#
