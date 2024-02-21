# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileCopyrightText: Bradley M. Bell <bradbell@seanet.com>
# SPDX-FileContributor: 2017-23 Bradley M. Bell
# ----------------------------------------------------------------------------
# BEGIN_ROSEN3_STEP
import numpy
from simple_inv import simple_inv
import cppad_py
def rosen3_step(fun, ti, yi, h) :
   #
   r1_2     = 1.0   / 2.0
   r3_2     = 3.0   / 2.0
   r3_5     = 3.0   / 5.0
   r24_25   = 24.0  / 25.0
   r3_25    = 3.0   / 25.0
   r121_50  = 121.0 / 50.0
   r186_25  = 186.0 / 25.0
   r6_5     = 6.0   / 5.0
   r97_108  = 97.0  / 108.0
   r11_72   = 11.0  / 72.0
   r25_216  = 25.0  / 216.0
   #
   # Einv
   ny   = yi.size
   I    = numpy.identity(ny, dtype=float)
   E    = I - r1_2 * h * fun.f_y(ti, yi)
   Einv = simple_inv(E)
   #
   # f_t
   f_t  = fun.f_t(ti, yi)
   #
   # k1
   k1   = fun.f(ti, yi)
   k1  += r1_2 * h * f_t
   k1   = numpy.matmul(Einv , k1)
   #
   # k2
   k2   = fun.f(ti + h, yi + h * k1)
   k2  -= r3_2 * h * f_t
   k2  -= 4.0 * k1
   k2   = numpy.matmul(Einv , k2)
   #
   # k3
   t    = ti + r3_5 * h
   y    = yi + r24_25 * h * k1 + r3_25 * h * k2
   k3   = fun.f(t, y)
   k3  += r121_50 * h * f_t
   k3  += r186_25 * k1 + r6_5 * k2
   k3   = numpy.matmul(Einv , k3)
   #
   yf   = yi + h * ( r97_108 * k1 + r11_72 * k2 + r25_216 * k3)
   #
   return yf
# END_ROSEN3_STEP
# BEGIN_CHECK_ROSEN3_STEP
def check_rosen3_step(fun, ti, yi, h) :
   ok    = True
   eps99 = 99.0 * numpy.finfo(float).eps
   #
   ny    = yi.size
   both  = numpy.concatenate( (yi, [ti]) )
   aboth = cppad_py.independent(both)
   az    = fun.f(aboth[ny], aboth[0:ny] )
   fun_d = cppad_py.d_fun(aboth, az)
   #
   J     = fun_d.jacobian(both)
   #
   # check fun.f_t(t, y)
   fun_t   = fun.f_t(ti, yi)
   printed = False
   for i in range(ny) :
      if J[i, ny] == 0.0 :
         ok = ok and fun_t[i] == 0.0
      else :
         rel_error = fun_t[i] / J[i,ny] - 1.0
         if abs(rel_error) > eps99 :
            ok = False
            if not printed :
               print('check_rosen3_step: fun.f_t check failed')
               printed = True
            print('fun_t[', i, '] = ', fun_t[i], ', check = ', J[i,ny])
   #
   # check fun.f_y(t, y)
   fun_y = fun.f_y(ti, yi)
   printed = False
   for i in range(ny) :
      for j in range(ny) :
         if J[i, j] == 0.0 :
            ok_ij =fun_y[i, j] == 0.0
         else :
            rel_error = fun_y[i, j] / J[i, j] - 1.0
            ok_ij = abs( rel_error ) < eps99
         if (not ok_ij) and (not printed) :
            print('check_rosen3_step: fun.f_y check failed')
            printed = True
         if not ok_ij :
            msg  = 'fun_y[' + str(i) + ',' + str(j) + '] ='
            msg += str( fun_y[i, j] )
            msg += ', check = ' + str( J[i, j] )
            print(msg)
   #
   return ok
# END_CHECK_ROSEN3_STEP
#
#
# {xrst_begin numeric_rosen3_step}
# {xrst_spell
#     june
#     ok
#     rosenbrock
#     shampine
#     vol
#     yf
#     yi
#     yp
# }
# {xrst_comment_ch #}
#
#
# One Third Order Rosenbrock ODE Step
# ###################################
#
# Syntax
# ******
#
# | *yf* =  ``rosen3_step`` ( *fun* , *ti* , *yi* , *h* )
# | *ok* =  ``check_rosen3_step`` ( *fun* , *ti* , *yi* , *h* )
#
# Purpose
# *******
# The routine ``rosen3_step`` can be used with
# ``ad_double`` to solve an initial value ODE
#
# .. math::
#
#    y^{(1)} (t)  = f( t , y )
#
# Reference
# *********
# The formulas in this method are taken from page 100 of the following
# reference (except that 98/108 was correct to 97/108):
# Shampine, L.F.,
# *Implementation of Rosenbrock Methods* ,
# ACM Transactions on Mathematical Software, Vol. 8, No. 2, June 1982.
#
# fun
# ***
# This is a function that evaluates the ordinary differential equation,
# and its partial derivatives,
#
# t
# =
# The argument *t* below is the current time.
# It can be a ``float`` or ``a_double`` .
#
# y
# =
# The argument *y* below is the current value of :math:`y(t)`.
# The type of the elements of *y*
# can be ``float`` or ``ad_double`` .
#
# f
# =
# The syntax
#
# | |tab| *yp* = *fun*\ ``.f`` ( *t* , *y* )
#
# sets *yp* to the value of :math:`f(t, y)`.
#
# f_t
# ===
# The syntax
#
# | |tab| *yp_t* = *fun*\ ``.f_t`` ( *t* , *y* )
#
# set *yp_t* to the value of :math:`\partial_t f(t, y)`.
#
# f_y
# ===
# The syntax
#
# | |tab| *yp_y* = *fun*\ ``.f_y`` ( *t* , *y* )
#
# sets *yp_y* to the value of :math:`\partial_y f(t, y)`.
#
# ti
# **
# This is the initial time for the Rosenbrock step.
# It can have type ``float`` or ``a_double`` .
# (For ``check_rosen3_step`` only ``float`` is allowed.)
#
# yi
# **
# This is the numpy vector containing the
# value of :math:`y(t)` at the initial time.
# The type of its elements can be ``float`` or ``a_double`` .
# (For ``check_rosen3_step`` only ``float`` is allowed.)
#
# h
# *
# This is the step size in time; i.e., the time at the end of the step
# minus the initial time.
# It can have type ``float`` or ``a_double`` .
# (This is not used by ``check_rosen3_step`` .)
#
# yf
# **
# This is the approximate solution for :math:`y(t)` at the final time
# as a numpy vector.
# This solution is 3-th order accurate in time :math:`t`; e.g., if
# :math:`y(t)` is a polynomial in :math:`t` of order three or lower,
# the solution has no truncation error, only round off error.
#
# ok
# **
# This is true if the function *fun*\ ``.f`` *t* , *y* )
# and the partials *fun*\ ``.f_t`` ( *t* , *y* ) ,
# *fun*\ ``.f_y`` ( *t* , *y* ) agree.
# Otherwise AD has detected an error in these functions.
#
# {xrst_toc_hidden
#  example/python/numeric/rosen3_step_xam.py
# }
# Example
# *******
# :ref:`numeric_rosen3_step_xam.py-name`
#
# Source Code
# ***********
#
# rosen3_step
# ===========
# {xrst_literal
#  # BEGIN_ROSEN3_STEP
#  # END_ROSEN3_STEP
# }
#
# check_rosen3_step
# =================
# {xrst_literal
#  # BEGIN_CHECK_ROSEN3_STEP
#  # END_CHECK_ROSEN3_STEP
# }
#
# {xrst_end numeric_rosen3_step}
