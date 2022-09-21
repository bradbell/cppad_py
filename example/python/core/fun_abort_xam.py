# -----------------------------------------------------------------------------
#         cppad_py: A C++ Object Library and Python Interface to Cppad
#          Copyright (C) 2017-22 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# -----------------------------------------------------------------------------
# abort_recording
# -----------------------------------------------------------------------------
# BEGIN SOURCE
def fun_abort_xam() :
   #
   import numpy
   import cppad_py
   #
   # initialize return variable
   ok = True
   # ---------------------------------------------------------------------
   n_ind = 2
   #
   # create ax
   x = numpy.empty(n_ind, dtype=float)
   for i in range( n_ind  ) :
      x[i] = i + 1.0
   #
   ax = cppad_py.independent(x)
   #
   # preform some a_double operations
   ax0 = ax[0]
   ax1 = ax[1]
   ay = ax0 + ax1
   #
   # check that ay is a variable; its value depends on the value of ax
   ok = ok and ay.variable()
   #
   # abort this recording
   cppad_py.abort_recording()
   #
   # check that ay is now a parameter, no longer a variable.
   ok = ok and ay.parameter()
   #
   # since it is a parameter, we can retrieve its value
   y = ay.value()
   #
   # its value should be x0 + x1
   ok = ok and y  == x[0] + x[1]
   #
   # an abort when not recording has no effect
   cppad_py.abort_recording()
   #
   return( ok )
#
# END SOURCE
#
#
# {xrst_begin fun_abort_xam_py}
# {xrst_comment_ch #}
#
# {xrst_spell
# }
# Python: Abort Recording a_double Operations: Example and Test
# #############################################################
# {xrst_literal
#  # BEGIN SOURCE
#  # END SOURCE
# }
# {xrst_end fun_abort_xam_py}
#
