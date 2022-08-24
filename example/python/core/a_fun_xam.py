# -----------------------------------------------------------------------------
#         cppad_py: A C++ Object Library and Python Interface to Cppad
#          Copyright (C) 2017-22 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# -----------------------------------------------------------------------------
# BEGIN SOURCE
def a_fun_xam() :
    #
    import numpy
    import cppad_py
    #
    # initialize return variable
    ok = True
    # ---------------------------------------------------------------------
    # number of dependent and independent variables
    m = 1
    n = 3
    #
    # Record the function
    #   f(x) = 0.5 * ( x[0]^2 + ... + x[n-1]^2 )
    x = numpy.empty(n, dtype=float)
    for i in range(n) :
        x[i] = i
    ax   = cppad_py.independent(x)
    ay   = numpy.empty(m, dtype=cppad_py.a_double)
    asum = cppad_py.a_double(0.0)
    for i in range(n) :
        asum = asum + ax[i] * ax[i]
    ay[0] = cppad_py.a_double(0.5) * asum
    f     = cppad_py.d_fun(ax, ay)
    af    = cppad_py.a_fun(f)
    #
    # Record the function
    #   g(x) = f'(x) * v
    au   = numpy.empty(m, dtype=cppad_py.a_double)
    av   = numpy.empty(n, dtype=cppad_py.a_double)
    for i in range(n) :
        av[i] = cppad_py.a_double(i)
    ax   = cppad_py.independent(x)
    af.forward(0, ax)
    au = af.forward(1, av)
    g  = cppad_py.d_fun(ax, au)
    #
    # compute g(x)
    u  = g.forward(0, x)
    #
    # compute g'(x)
    uq       = numpy.empty( (m, 1), dtype=float )
    uq[0, 0] = 1.0
    xq       = g.reverse(1, uq)
    #
    # g'(x) = f''(x) * v = v
    for i in range(n) :
        ok = ok and cppad_py.a_double(xq[i, 0]) == av[i]
    return ok
# END SOURCE
#
# {xrst_comment_ch #}
#
# {xrst_begin a_fun_xam_py}
#
# Python: Purpose of a_fun Objects: Example and Test
# ##################################################
# {xrst_literal
#   # BEGIN SOURCE
#   # END SOURCE
# }
# {xrst_end a_fun_xam_py}
