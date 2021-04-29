# -----------------------------------------------------------------------------
#         cppad_py: A C++ Object Library and Python Interface to Cppad
#          Copyright (C) 2017-21 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# -----------------------------------------------------------------------------
# check_for_nan
# -----------------------------------------------------------------------------
# BEGIN SOURCE
def fun_check_for_nan_xam() :
    #
    import numpy
    import cppad_py
    #
    # initialize return variable
    ok = True
    # ---------------------------------------------------------------------
    n_ind = 2 # number of independent variables
    n_dep = 2 # number of dependent variables
    #
    # dimension some vectors
    x  = numpy.empty(n_ind, dtype=float)
    ay = numpy.empty(n_dep, dtype=cppad_py.a_double)
    #
    # independent variables
    x[0] = -1.0
    x[1] = 2.0
    ax    = cppad_py.independent(x)
    #
    # dependent variables
    ay[0] = ax[0] ** ax[1]
    ay[1] = ax[0] ** 2.0
    #
    # define f(x) = y
    f = cppad_py.d_fun(ax, ay)
    #
    # turn off checking for nan
    f.check_for_nan(False)
    #
    # funtion values are not nan
    y  = f.forward(0, x)
    ok = ok and y[0] == 1.0    # y[0] = f(x)
    ok = ok and y[1] == 1.0    # y[1] = f(x)
    #
    # Derivative of pow is nan. This would case an assert
    # if build_type were debug and check_for_nan were true.
    dx  = numpy.ones(n_ind, dtype=float)
    dy  = f.forward(1, dx)
    ok  = ok and numpy.isnan(dy[0])
    ok  = ok and dy[1] == -2.0      # dy[1] = f'(x)
    #
    # Second derivative of pow in also nan
    ddx = numpy.zeros(n_ind, dtype=float)
    ddy = f.forward(2, ddx)
    ok  = ok and numpy.isnan(ddy[0])
    ok  = ok and ddy[1] == 1.0      # ddy[1] = 1/2 * f''(x)
    #
    return ok
#
# END SOURCE
# -----------------------------------------------------------------------------
# {xsrst_comment_ch #}
#
# {xsrst_begin check_for_nan_xam_py}
#
# .. include:: ../preamble.rst
#
# {xsrst_spell
# }
# Python: Example Turning of Checking For Nan
# ###########################################
# {xsrst_file
#   # BEGIN SOURCE
#   # END SOURCE
# }
# {xsrst_end check_for_nan_xam_py}
