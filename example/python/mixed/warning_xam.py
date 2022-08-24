# -----------------------------------------------------------------------------
#         cppad_py: A C++ Object Library and Python Interface to Cppad
#          Copyright (C) 2017-22 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# -----------------------------------------------------------------------------
# mixed warning
# -----------------------------------------------------------------------------
# BEGIN SOURCE
def warning_xam() :
   import cppad_py
   import numpy
   #
   ok_list = list()
   def my_warning(message) :
      if message == 'Testing warning' :
         ok_list.append(True)
   #
   fixed_init = numpy.array( [ 1 ], dtype=float )
   mixed_obj  = cppad_py.mixed(
      fixed_init = fixed_init, warning = my_warning
   )
   mixed_obj.post_warning('Testing warning')
   #
   ok = len(ok_list) == 1
   for i in range( len(ok_list) ) :
      ok = ok and ok_list[i] == True
   return ok
# END SOURCE
'''
{xrst_begin mixed_warning_xam_py}

Warnings: Example and Test
##########################
{xrst_literal
  # BEGIN SOURCE
  # END SOURCE
}
{xrst_end mixed_warning_xam_py}
'''
