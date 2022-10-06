# -----------------------------------------------------------------------------
#         cppad_py: A C++ Object Library and Python Interface to Cppad
#          Copyright (C) 2017-22 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# -----------------------------------------------------------------------------
# a_double binary operations
# -----------------------------------------------------------------------------
# BEGIN SOURCE
def a_double_binary_xam() :
   #
   import numpy
   from cppad_py import a_double
   from cppad_py import pow_int
   ok = True
   a2 = a_double(2.0)
   a3 = a_double(3.0)
   # ---------------------------------------------------------------------
   # a_double op a_double
   a5       = a2 + a3
   a6       = a2 * a3
   a1_minus = a2 - a3
   a23      = a2 / a3
   #
   ok = ok and a5 == 5.0
   ok = ok and a6 == 6.0
   ok = ok and a1_minus == -1.0
   ok = ok and a23.near_equal( a_double(2.0 / 3.0) )
   # ---------------------------------------------------------------------
   # a_double op double
   a5       = a2 + 3.0
   a6       = a2 * 3.0
   a1_minus = a2 - 3.0
   a23      = a2 / 3.0
   #
   ok = ok and a5 == 5.0
   ok = ok and a6 == 6.0
   ok = ok and a1_minus == -1.0
   ok = ok and a23.near_equal( a_double(2.0 / 3.0) )
   # ---------------------------------------------------------------------
   # double op a_double
   a5       = 3.0 + a2
   a6       = 3.0 * a2
   a1       = 3.0 - a2
   a32      = 3.0 / a2
   #
   ok = ok and a5 == 5.0
   ok = ok and a6 == 6.0
   ok = ok and a1 == 1.0
   ok = ok and a32.near_equal( a_double(3.0 / 2.0) )
   # ---------------------------------------------------------------------
   # pow
   a8 = a2  ** a3
   a9 = a3  ** 2.0
   a4 = 2.0 ** a2
   ok = ok and a8.near_equal( a_double(8.0) )
   ok = ok and a9.near_equal( a_double(9.0) )
   ok = ok and a4.near_equal( a_double(4.0) )
   # ---------------------------------------------------------------------
   # pow_int
   a8 = pow_int(a2, 3)
   a9 = pow_int(a3, 2)
   ok = ok and a8.near_equal( a_double(8.0) )
   ok = ok and a9.near_equal( a_double(9.0) )
   #
   return( ok )
#
# END SOURCE
#
#
# {xrst_begin a_double_binary_xam_py}
# {xrst_comment_ch #}
#
# Python: a_double Binary Operators With AD Result: Example and Test
# ##################################################################
# {xrst_literal
#  # BEGIN SOURCE
#  # END SOURCE
# }
# {xrst_end a_double_binary_xam_py}
#
