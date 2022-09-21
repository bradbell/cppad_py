# -----------------------------------------------------------------------------
#         cppad_py: A C++ Object Library and Python Interface to Cppad
#          Copyright (C) 2017-22 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# -----------------------------------------------------------------------------
# BEGIN_RUNGE4_STEP
def runge4_step(fun, ti, yi, h) :
   k1     = h * fun.f(ti,           yi)
   k2     = h * fun.f(ti + h / 2.0, yi + k1 / 2.0)
   k3     = h * fun.f(ti + h / 2.0, yi + k2 / 2.0)
   k4     = h * fun.f(ti + h,       yi + k3 )
   yf     = yi + (k1 + 2.0 * k2 + 2.0 * k3 + k4) / 6.0
   return yf
# END_RUNGE4_STEP
#
#
# {xrst_begin numeric_runge4_step}
# {xrst_comment_ch #}
#
# {xrst_spell
#  runge
#  kutta
#  yf
#  yi
#  yp
# }
#
# One Fourth Order Runge-Kutta ODE Step
# #####################################
#
# Syntax
# ******
# *yf* =  ``runge4_step`` ( *fun* , *ti* , *yi* , *h* )
#
# Purpose
# *******
# The routine can be used with ``ad_double``
# to solve the initial value ODE
#
# .. math::
#
#    y^{(1)} (t)  = f( t , y )
#
# fun
# ***
# This is a function that evaluates the ordinary differential equation
# using the syntax
#
# | |tab| *yp* = *fun*\ ``.f`` ( *t* , *y* )
#
# where *t* is the current time,
# *y* is the current value of :math:`y(t)`, and
# *yp* is the current derivative :math:`y^{(1)} (t)`.
# The type of the elements of *t* and *y*
# can be ``float`` or ``ad_double`` .
#
# ti
# **
# This is the initial time for the Runge-Kutta step.
# It can have type ``float`` or ``a_double`` .
#
# yi
# **
# This is the numpy vector containing the
# value of :math:`y(t)` at the initial time.
# The type of its elements can be ``float`` or ``a_double`` .
#
# h
# *
# This is the step size in time; i.e., the time at the end of the step
# minus the initial time.
# It can have type ``float`` or ``a_double`` .
#
# yf
# **
# This is the approximate solution for :math:`y(t)` at the final time
# as a numpy vector.
# This solution is 4-th order accurate in time :math:`t`; e.g., if
# :math:`y(t)` is a polynomial in :math:`t` of order four or lower,
# the solution has no truncation error, only round off error.
#
# {xrst_toc_hidden
#  example/python/numeric/runge4_step_xam.py
# }
# Example
# *******
# :ref:`numeric_runge4_step_xam_py`
#
# Source Code
# ***********
# {xrst_literal
#  # BEGIN_RUNGE4_STEP
#  # END_RUNGE4_STEP
# }
#
# {xrst_end numeric_runge4_step}
