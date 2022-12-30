# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileCopyrightText: Bradley M. Bell <bradbell@seanet.com>
# SPDX-FileContributor: 2017-22 Bradley M. Bell
# ----------------------------------------------------------------------------
# a_double unary operators
# -----------------------------------------------------------------------------
# BEGIN SOURCE
def a_double_unary_op_xam() :
   #
   import numpy
   import cppad_py
   #
   # initialize return variable
   ok = True
   # ---------------------------------------------------------------------
   a2 = cppad_py.a_double(2.0)
   aplus2 = + a2
   a2_minus = - a2
   #
   ok = ok and aplus2 == 2.0
   ok = ok and a2_minus == -2.0
   #
   return( ok )
#
# END SOURCE
#
#
# {xrst_begin a_double_unary_op_xam_py}
# {xrst_comment_ch #}
#
# Python: a_double Unary Plus and Minus: Example and Test
# #######################################################
# {xrst_literal
#  # BEGIN SOURCE
#  # END SOURCE
# }
# {xrst_end a_double_unary_op_xam_py}
#
