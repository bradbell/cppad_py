# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileCopyrightText: Bradley M. Bell <bradbell@seanet.com>
# SPDX-FileContributor: 2017-22 Bradley M. Bell
# ----------------------------------------------------------------------------
# jacobian
# -----------------------------------------------------------------------------
# BEGIN SOURCE
def fun_jacobian_xam() :
   #
   import numpy
   import cppad_py
   #
   # initialize return variable
   ok = True
   # ---------------------------------------------------------------------
   # number of dependent and independent variables
   n_dep = 1
   n_ind = 3
   #
   # create the independent variables ax
   x = numpy.empty(n_ind, dtype=float)
   for i in range( n_ind  ) :
      x[i] = i + 2.0
   #
   ax = cppad_py.independent(x)
   #
   # create dependent variables ay with ay0 = ax_0 * ax_1 * ax_2
   ax_0  = ax[0]
   ax_1  = ax[1]
   ax_2  = ax[2]
   ay    = numpy.empty(n_dep, dtype=cppad_py.a_double)
   ay[0] = ax_0 * ax_1 * ax_2
   #
   # define af corresponding to f(x) = x_0 * x_1 * x_2
   f  = cppad_py.d_fun(ax, ay)
   #
   # compute the Jacobian f'(x) = ( x_1*x_2, x_0*x_2, x_0*x_1 )
   fp = f.jacobian(x)
   #
   # check Jacobian
   x_0 = x[0]
   x_1 = x[1]
   x_2 = x[2]
   ok = ok and fp[0, 0] == x_1 * x_2
   ok = ok and fp[0, 1] == x_0 * x_2
   ok = ok and fp[0, 2] == x_0 * x_1
   # ---------------------------------------------------------------------
   af = cppad_py.a_fun(f)
   #
   ax   = numpy.empty(n_ind, dtype=cppad_py.a_double)
   for i in range( n_ind ) :
      ax[i] = x[i]
   #
   # compute the Jacobian f'(x) = ( x_1*x_2, x_0*x_2, x_0*x_1 )
   afp = af.jacobian(ax)
   #
   # check Jacobian
   ok = ok and afp[0, 0] == cppad_py.a_double(x_1 * x_2)
   ok = ok and afp[0, 1] == cppad_py.a_double(x_0 * x_2)
   ok = ok and afp[0, 2] == cppad_py.a_double(x_0 * x_1)
   #
   return( ok )
#
# END SOURCE
#
#
# {xrst_begin fun_jacobian_xam_py}
# {xrst_comment_ch #}
#
# Python: Dense Jacobian Using AD: Example and Test
# #################################################
# {xrst_literal
#  # BEGIN SOURCE
#  # END SOURCE
# }
# {xrst_end fun_jacobian_xam_py}
#
