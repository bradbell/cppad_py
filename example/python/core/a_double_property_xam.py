# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileCopyrightText: Bradley M. Bell <bradbell@seanet.com>
# SPDX-FileContributor: 2017-23 Bradley M. Bell
# ----------------------------------------------------------------------------
# a_double properties
# -----------------------------------------------------------------------------
# BEGIN SOURCE
def a_double_property_xam() :
   #
   import numpy
   import cppad_py
   #
   # initialize return variable
   ok = True
   # ---------------------------------------------------------------------
   a3 = cppad_py.a_double(3.0)
   #
   ok = ok and a3   == 3.0
   ok = ok and a3.parameter()
   ok = ok and not a3.variable()
   #
   # near_equal
   r3 = a3.sqrt()
   ok = ok and a3.near_equal( r3 * r3)
   #
   # var2par
   p3  = a3.var2par()
   ok  = ok and p3.value() == 3.0
   #
   return( ok )
#
# END SOURCE
#
#
# {xrst_begin a_double_property_xam.py}
# {xrst_comment_ch #}
#
# Python: a_double Properties: Example and Test
# #############################################
# {xrst_literal
#  # BEGIN SOURCE
#  # END SOURCE
# }
# {xrst_end a_double_property_xam.py}
#
