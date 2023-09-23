# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileCopyrightText: Bradley M. Bell <bradbell@seanet.com>
# SPDX-FileContributor: 2017-23 Bradley M. Bell
# ----------------------------------------------------------------------------
# optimize
# -----------------------------------------------------------------------------
# BEGIN SOURCE
def fun_optimize_xam() :
   #
   import numpy
   import cppad_py
   #
   # initialize return variable
   ok = True
   # ---------------------------------------------------------------------
   n_ind = 1 # number of independent variables
   n_dep = 1 # number of dependent variables
   n_var = 1 # phantom variable at address 0
   n_op  = 1 # special operator at beginning
   #
   # dimension some vectors
   x  = numpy.empty(n_ind, dtype=float)
   ay = numpy.empty(n_dep, dtype=cppad_py.a_double)
   #
   # independent variables
   x[0]  = 1.0
   ax    = cppad_py.independent(x)
   n_var = n_var + n_ind # one for each indpendent
   n_op  = n_op + n_ind
   #
   # accumulate summation
   ax0   = ax[0]
   csum  = cppad_py.a_double(0.0)
   csum  = ax0 + ax0 + ax0 + ax0
   n_var = n_var + 3 # one per + operator
   n_op  = n_op + 3
   #
   # define f(x) = y_0 = csum
   ay[0] = csum
   f     = cppad_py.d_fun(ax, ay)
   n_op  = n_op + 1 # speical operator at end
   #
   # check number of variables and operators
   ok = ok and f.size_var() == n_var
   ok = ok and f.size_op() == n_op
   #
   # optimize
   f.optimize()
   #
   # number of variables and operators has decreased by two
   ok = ok and f.size_var() == n_var-2
   ok = ok and f.size_op() == n_op-2
   #
   return( ok  )
#
# END SOURCE
# -----------------------------------------------------------------------------
#
# {xrst_begin fun_optimize_xam.py}
# {xrst_comment_ch #}
#
# Python: Optimize an d_fun: Example and Test
# ###########################################
# {xrst_literal
#  # BEGIN SOURCE
#  # END SOURCE
# }
# {xrst_end fun_optimize_xam.py}
#
def test_fun_optimize_xam() :
   assert fun_optimize_xam()
