# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileCopyrightText: Bradley M. Bell <bradbell@seanet.com>
# SPDX-FileContributor: 2017-23 Bradley M. Bell
# ----------------------------------------------------------------------------
# forward
# -----------------------------------------------------------------------------
# BEGIN SOURCE
def fun_forward_xam() :
   #
   import numpy
   import cppad_py
   #
   # initialize return variable
   ok = True
   # ---------------------------------------------------------------------
   # number of dependent and independent variables
   n_dep = 1
   n_ind = 2
   #
   # create the independent variables ax
   xp = numpy.empty(n_ind, dtype=float)
   for i in range( n_ind  ) :
      xp[i] = i + 1.0
   #
   ax = cppad_py.independent(xp)
   #
   # create dependent varialbes ay with ay0 = ax0 * ax1
   ax0    = ax[0]
   ax1    = ax[1]
   ay    = numpy.empty(n_dep, dtype=cppad_py.a_double)
   ay[0] = ax0 * ax1
   #
   # define af corresponding to f(x) = x0 * x1
   f  = cppad_py.d_fun(ax, ay)
   #
   # define X(t) = (3 + t, 2 + t)
   # it follows that Y(t) = f(X(t)) = (3 + t) * (2 + t)
   #
   # Y(0) = 6 and p ! = 1
   p     = 0
   xp[0] = 3.0
   xp[1] = 2.0
   yp = f.forward(p, xp)
   ok = ok and yp[0] == 6.0
   #
   # first order Taylor coefficients for X(t)
   p     = 1
   xp[0] = 1.0
   xp[1] = 1.0
   #
   # first order Taylor coefficient for Y(t)
   # Y'(0) = 3 + 2 = 5 and p ! = 1
   yp = f.forward(p, xp)
   ok = ok and yp[0] == 5.0
   #
   # second order Taylor coefficients for X(t)
   p     = 2
   xp[0] = 0.0
   xp[1] = 0.0
   #
   # second order Taylor coefficient for Y(t)
   # Y''(0) = 2.0 and p ! = 2
   yp = f.forward(p, xp)
   ok = ok and yp[0] == 1.0
   # ---------------------------------------------------------------------
   af = cppad_py.a_fun(f)
   ok = ok and af.size_order() == 0
   #
   # zero order forward
   p   = 0
   axp = numpy.empty(n_ind, dtype=cppad_py.a_double)
   axp[0] = 3.0
   axp[1] = 2.0
   ayp    = af.forward(p, axp)
   ok     = ok and ayp[0] == cppad_py.a_double(6.0)
   ok     = ok and af.size_order() == 1
   #
   return( ok )
#
# END SOURCE
#
#
# {xrst_begin fun_forward_xam.py}
# {xrst_comment_ch #}
#
# Python: Forward Mode AD: Example and Test
# #########################################
# {xrst_literal
#  # BEGIN SOURCE
#  # END SOURCE
# }
# {xrst_end fun_forward_xam.py}
#
