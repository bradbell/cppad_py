# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileCopyrightText: Bradley M. Bell <bradbell@seanet.com>
# SPDX-FileContributor: 2017-23 Bradley M. Bell
# ----------------------------------------------------------------------------
#
# {xrst_begin numeric_runge4_step_xam.py}
# {xrst_spell
#     kutta
#     rl
#     runge
# }
# {xrst_comment_ch #}
#
#
# Example Computing Derivative A Runge-Kutta Ode Solution
# #######################################################
#
# ODE
# ***
#
# .. math::
#
#    \partial_t y_i (t, x) =  f(t, y, x) \left\{ \begin{array}{rl}
#         x_0               & {\rm if} \; i = 0 \\
#         x_i y_{i-1} (t)   & {\rm otherwise}
#    \end{array} \right.
#
# with the initial condition :math:`y(0) = 0`
#
# Solution
# ********
# This is a special case for which we know the solution
#
# .. math::
#
#    y_i (t, x) = \left\{ \begin{array}{rl}
#         t  x_0                            & {\rm if} \; i = 0 \\
#         ( t^i / (i+1) ! ) \prod_{j=0}^i x_j   & {\rm otherwise}
#    \end{array} \right.
#
# Derivative of Solution
# **********************
# For this special case, the partial derivative of the solution with respect
# to the j-th component of the vector :math:`x` is
#
# .. math::
#
#    \partial_{x(j)} y_i (t, x) =  \left\{ \begin{array}{rl}
#         y_i (t, x) / x_j      & {\rm if} \; j \leq i \\
#         0                     & {\rm otherwise}
#    \end{array} \right.
#
# Source Code
# ***********
# {xrst_literal
#  # BEGIN_PYTHON
#  # END_PYTHON
# }
#
# {xrst_end numeric_runge4_step_xam.py}
# BEGIN_PYTHON
import numpy
from  scipy.special import factorial
import cppad_py
from runge4_step import runge4_step
#
class fun_class :
   #
   def __init__(self, x) :
      self.x = x
   #
   def f(self, t, y) :
      y_shift = numpy.concatenate( ( [1.0] , y[0:-1] ) )
      return self.x * y_shift
#
def runge4_step_xam() :
   ok    = True
   nx    = 4
   eps99 = 99.0 * numpy.finfo(float).eps
   #
   # independent variables for this g(x) = y(1, x)
   x  = numpy.array( nx * [ 1.0 ] )
   ax = cppad_py.independent(x)
   #
   # function to pass to runge4_step
   fun = fun_class(ax)
   #
   # initiali value for the ODE
   ay_start =  numpy.array( nx * [ cppad_py.a_double(0.0) ] )
   t_start  = 0.0
   t_step   = 0.75
   #
   # take one step
   ay = runge4_step(fun, t_start, ay_start, t_step)
   #
   # g(x) = y(t_step, x)
   g = cppad_py.d_fun(ax, ay)
   #
   # Check g_i (x) = prod_{j=0}^i x[j] t^(i+1) / (i+1) !
   # 4th order method should be very accutate for functions
   # or order 4 or less in t.
   x  = numpy.arange(0, nx) + 1.0
   gx = g.forward(0, x)
   prod = 1.0
   for i in range(nx) :
      prod      = prod * x[i]
      check     = prod * numpy.power(t_step, i+1) / factorial(i+1)
      rel_error = gx[i] / check - 1.0
      ok       &= abs(rel_error) < eps99
   #
   # Check derivative of g_i (x) w.r.t x_j
   # is zero for i < j and  g_i(x) / x_j otherwise
   J = g.jacobian(x)
   for j in range(nx) :
      for i in range(nx) :
         if i < j :
            ok &= J[i,j] == 0.0
         else :
            check     = gx[i] / x[j]
            rel_error = J[i,j] / check - 1.0
            ok       &= abs(rel_error) < eps99

   return ok
# END_PYTHON
def test_runge4_step_xam() :
   assert runge4_step_xam()
