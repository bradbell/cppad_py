# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileCopyrightText: Bradley M. Bell <bradbell@seanet.com>
# SPDX-FileContributor: 2017-23 Bradley M. Bell
# ----------------------------------------------------------------------------
# a_double assignment
# -----------------------------------------------------------------------------
# BEGIN SOURCE
def a_double_assign_xam() :
   #
   import numpy
   import cppad_py
   #
   # initialize return variable
   ok = True
   # ---------------------------------------------------------------------
   #
   ax = cppad_py.a_double(3.0);
   ok = ok and ax == 3.0
   #
   ax += cppad_py.a_double(2.0);
   ok = ok and ax == 5.0
   #
   ax -= 1.0;
   ok = ok and ax == cppad_py.a_double(4.0)
   #
   ax *= cppad_py.a_double(3.0);
   ok = ok and ax == 12.0
   #
   ax /= 4.0;
   ok = ok and ax == cppad_py.a_double(3.0)
   #
   return( ok )
#
# END SOURCE
#
#
# {xrst_begin a_double_assign_xam.py}
# {xrst_comment_ch #}
#
# Python: a_double Assignment Operators: Example and Test
# #######################################################
# {xrst_literal
#  # BEGIN SOURCE
#  # END SOURCE
# }
# {xrst_end a_double_assign_xam.py}
#
def test_a_double_assign_xam() :
   assert a_double_assign_xam()
