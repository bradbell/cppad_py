# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileCopyrightText: Bradley M. Bell <bradbell@seanet.com>
# SPDX-FileContributor: 2017-23 Bradley M. Bell
# ----------------------------------------------------------------------------
# exception
# -----------------------------------------------------------------------------
# BEGIN SOURCE
def exception_xam() :
   #
   import numpy
   import cppad_py
   import sys
   #
   ok_list = list()
   try :
      left     = cppad_py.a_double(1.0)
      right    = cppad_py.a_double(2.0)
      if_true  = cppad_py.a_double(3.0)
      if_false = cppad_py.a_double(4.0)
      target   = cppad_py.a_double()
      target.cond_assign(
         '<>', left, right, if_true, if_false
      )
   except RuntimeError as e: # catch
      message = str(e)
      index   = message.find("'<>' is not a valid comparison operator")
      ok      = 0 <= index
      ok_list.append( ok )
   #
   if len( ok_list ) == 0 :
      ok_list.append(False)
   return( ok_list[0]  )
#
# END SOURCE
# -----------------------------------------------------------------------------
#
# {xrst_begin exception_xam.py}
# {xrst_spell
# }
# {xrst_comment_ch #}
#
# Python: CppAD Py Exception Handling: Example and Test
# #####################################################
# {xrst_literal
#  # BEGIN SOURCE
#  # END SOURCE
# }
# {xrst_end exception_xam.py}
#
def test_exception_xam() :
   assert exception_xam()
