# -----------------------------------------------------------------------------
#         cppad_py: A C++ Object Library and Python Interface to Cppad
#          Copyright (C) 2017-20 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# -----------------------------------------------------------------------------
# a_double unary operators
# -----------------------------------------------------------------------------
# BEGIN SOURCE
def a_double_unary_fun_xam() :
    #
    import numpy
    import cppad_py
    #
    # initialize return variable
    ok = True
    # ---------------------------------------------------------------------
    #
    # abs
    # numpy syntax does not work for this function
    a1   = cppad_py.a_double(-1.0)
    abs1 = a1.abs()
    ok   = ok and abs1 == 1.0
    # fabs
    a1   = cppad_py.a_double(1.0)
    abs1 = numpy.fabs( a1 )
    ok   = ok and abs1 == 1.0
    #
    # pi/4
    pi_4 = a1.atan()
    #
    # sqrt(2)
    atmp = cppad_py.a_double(2.0)
    r2 = numpy.sqrt( atmp )
    #
    # sin(pi/4)  * sqrt(2) = 1.0
    atmp = r2 * pi_4.sin()
    ok = ok and atmp.near_equal(a1)
    #
    # cos(pi/4)  * sqrt(2) = 1.0
    atmp = r2 * numpy.cos( pi_4 )
    ok = ok and atmp.near_equal(a1)
    #
    # tan(pi/4)  = 1.0
    atmp = pi_4.tan()
    ok = ok and atmp.near_equal(a1)
    #
    # erf(0.5) = 0.5204998778130465
    acheck = cppad_py.a_double(0.5204998778130465)
    atmp   = cppad_py.a_double(0.5)
    atmp   = atmp.erf()
    ok     = ok and atmp.near_equal(acheck)
    #
    return( ok )
#
# END SOURCE
#
# {xsrst_comment_ch #}
#
# {xsrst_begin a_double_unary_fun_xam_py}
#
# .. include:: ../preamble.rst
#
# {xsrst_spell
# }
# Python: a_double Unary Functions with AD Result: Example and Test
# #################################################################
# {xsrst_file
#   # BEGIN SOURCE
#   # END SOURCE
# }
# {xsrst_end a_double_unary_fun_xam_py}
#
