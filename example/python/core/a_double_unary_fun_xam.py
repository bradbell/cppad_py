# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileCopyrightText: Bradley M. Bell <bradbell@seanet.com>
# SPDX-FileContributor: 2017-23 Bradley M. Bell
# ----------------------------------------------------------------------------
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
#
# {xrst_begin a_double_unary_fun_xam.py}
# {xrst_comment_ch #}
#
# Python: a_double Unary Functions with AD Result: Example and Test
# #################################################################
# {xrst_literal
#  # BEGIN SOURCE
#  # END SOURCE
# }
# {xrst_end a_double_unary_fun_xam.py}
#
def test_a_double_unary_fun_xam() :
   assert a_double_unary_fun_xam()
