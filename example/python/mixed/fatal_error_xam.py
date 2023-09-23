# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileCopyrightText: Bradley M. Bell <bradbell@seanet.com>
# SPDX-FileContributor: 2017-23 Bradley M. Bell
# ----------------------------------------------------------------------------
# mixed fatal_error
# -----------------------------------------------------------------------------
# BEGIN SOURCE
def fatal_error_xam() :
   import cppad_py
   import numpy
   #
   ok_list       = list()
   #
   fixed_init = numpy.array( [ 1 ], dtype=float )
   mixed_obj  = cppad_py.mixed(fixed_init = fixed_init)
   try :
      mixed_obj.post_fatal_error('Testing fatal error')
   except RuntimeError as error :
      if str(error) == 'Testing fatal error' :
         ok_list.append(True)
   #
   ok = len(ok_list) == 1
   for i in range( len(ok_list) ) :
      ok = ok and ok_list[i] == True
   return ok
# END SOURCE
r'''
{xrst_begin mixed_fatal_error_xam.py}

fatal_error: Example and Test
#############################

{xrst_literal
  # BEGIN SOURCE
  # END SOURCE
}
{xrst_end mixed_fatal_error_xam.py}
'''
def test_fatal_error_xam() :
   assert fatal_error_xam()
