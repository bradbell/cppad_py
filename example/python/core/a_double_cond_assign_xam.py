# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileCopyrightText: Bradley M. Bell <bradbell@seanet.com>
# SPDX-FileContributor: 2017-23 Bradley M. Bell
# ----------------------------------------------------------------------------
# a_double conditional assignment
# -----------------------------------------------------------------------------
# BEGIN SOURCE
def a_double_cond_assign_xam() :
   #
   import numpy
   import cppad_py
   #
   # initialize return variable
   ok = True
   # ---------------------------------------------------------------------
   n_ind = 4
   n_dep = 1
   #
   # create ax (value of independent variables does not matter)
   x = numpy.empty(n_ind, dtype=float)
   x[0] = 0.0
   x[1] = 1.0
   x[2] = 2.0
   x[3] = 3.0
   ax = cppad_py.independent(x)
   #
   # arguments to conditional assignment
   left = ax[0]
   right = ax[1]
   if_true = ax[2]
   if_false = ax[3]
   #
   # assignment
   target = cppad_py.a_double()
   target.cond_assign(
      "<",
      left,
      right,
      if_true,
      if_false
   )
   #
   # f(x) = taget
   ay = numpy.empty(n_dep, dtype=cppad_py.a_double)
   ay[0] = target
   f  = cppad_py.d_fun(ax, ay)
   #
   # assignment with different independent variable values
   x[0] = 9.0 # left
   x[1] = 8.0 # right
   x[2] = 7.0 # if_true
   x[3] = 6.0 # if_false
   p = 0
   y = f.forward(p, x)
   ok = ok and y[0] == 6.0
   #
   return( ok  )
#
# END SOURCE
#
#
# {xrst_begin a_double_cond_assign_xam.py}
# {xrst_comment_ch #}
#
# Python: a_double Conditional Assignment: Example and Test
# #########################################################
# {xrst_literal
#  # BEGIN SOURCE
#  # END SOURCE
# }
# {xrst_end a_double_cond_assign_xam.py}
#
def test_a_double_cond_assign_xam() :
   assert a_double_cond_assign_xam()
