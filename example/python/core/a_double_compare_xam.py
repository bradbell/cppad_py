# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileCopyrightText: Bradley M. Bell <bradbell@seanet.com>
# SPDX-FileContributor: 2017-23 Bradley M. Bell
# ----------------------------------------------------------------------------
# a_double comparision operators
# -----------------------------------------------------------------------------
# BEGIN SOURCE
def a_double_compare_xam() :
   #
   import numpy
   import cppad_py
   ok = True
   a2 = cppad_py.a_double(2.0)
   a3 = cppad_py.a_double(3.0)
   # ---------------------------------------------------------------------
   ok = ok and a2   <  a3
   ok = ok and a2   <= a3
   ok = ok and a3 >  a2
   ok = ok and a3 >= a2
   ok = ok and a3 != a2
   ok = ok and a3 == a3
   #
   ok = ok and not (a2 >  a3)
   ok = ok and not (a2 >= a3)
   ok = ok and not (a2 == a3)
   # ---------------------------------------------------------------------
   ok = ok and a2   <  3.0
   ok = ok and a2   <= 3.0
   ok = ok and a3 >  2.0
   ok = ok and a3 >= 2.0
   ok = ok and a3 != 2.0
   ok = ok and a3 == 3.0
   #
   ok = ok and not (a2 >  3.0)
   ok = ok and not (a2 >= 3.0)
   ok = ok and not (a2 == 3.0)
   #
   return( ok )
#
# END SOURCE
#
#
# {xrst_begin a_double_compare_xam.py}
# {xrst_comment_ch #}
#
# Python: a_double Comparison Operators: Example and Test
# #######################################################
# {xrst_literal
#  # BEGIN SOURCE
#  # END SOURCE
# }
# {xrst_end a_double_compare_xam.py}
#
def test_a_double_compare_xam() :
   assert a_double_compare_xam()
