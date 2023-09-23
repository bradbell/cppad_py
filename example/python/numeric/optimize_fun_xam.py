# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileCopyrightText: Bradley M. Bell <bradbell@seanet.com>
# SPDX-FileContributor: 2017-23 Bradley M. Bell
# ----------------------------------------------------------------------------
#
# {xrst_begin numeric_optimize_fun_xam.py}
# {xrst_spell
#     constr
#     cr
#     ipopt
#     scipy
# }
# {xrst_comment_ch #}
#
#
# Example Using optimize_fun_class with Scipy Optimization
# ########################################################
#
# Reference
# *********
# This problem comes form the
# `Interfaces <https://coin-or.github.io/Ipopt/INTERFACES.html>`_
# section of the Ipopt documentation.
#
# Problem
# *******
#
# .. math::
#
#    \begin{array}{cr}
#    {\rm minimize}      & x_0 x_3 ( x_0 + x_1 + x_2 ) + x_2   \\
#    {\rm subject \; to} &             x_0 x_1 x_2 x_3 \geq 25 \\
#                         & x_0^2 + x_1^2 + x_2^2 + x_3^2 = 40  \\
#                         &                    1 \leq x \leq 5
#    \end{array}
#
# with the starting point :math:`x = (1, 5, 5, 1)`.
# The optimal value for :math:`x` is
#
# .. math::
#
#  \newcommand{\W}[1]{{\; #1 \;}}
#  (1.00000000 \W{,} 4.74299963 \W{,} 3.82114998 \W{,} 1.37940829)
#
# trust_constr
# ************
# This is one of the
# `scipy.optimize
# <https://docs.scipy.org/doc/scipy/reference/optimize.html>`_
# methods.
#
# Source Code
# ***********
# {xrst_literal
#  # BEGIN_PYTHON
#  # END_PYTHON
# }
#
# {xrst_end numeric_optimize_fun_xam.py}
# BEGIN_PYTHON
def optimize_fun_xam() :
   #
   import numpy
   import cppad_py
   import scipy.optimize
   from optimize_fun_class import optimize_fun_class
   #
   ok = True
   #
   def a_objective(ax)  :
      return ax[0] * ax[3] * ( ax[0] + ax[1] + ax[2] ) + ax[2]
   def a_constraint(ax) :
      return [ numpy.prod(ax), numpy.sum( ax * ax) ]
   #
   # objective_ad
   x = numpy.array( [ 1.0, 2.0, 3.0, 4.0 ] )
   ax = cppad_py.independent(x)
   ay = numpy.array( [a_objective(ax)] )
   objective_ad = cppad_py.d_fun(ax, ay)
   #
   # constraint_ad
   ax = cppad_py.independent(x)
   ay = numpy.array( a_constraint(ax) )
   constraint_ad = cppad_py.d_fun(ax, ay)
   #
   # optimize_fun
   optimize_fun = optimize_fun_class(objective_ad, constraint_ad)
   #
   # constraints
   lower_bound = [      25.0, 40.0 ]
   upper_bound = [ numpy.inf, 40.0 ]
   nonlinear_constraint = scipy.optimize.NonlinearConstraint(
      optimize_fun.constraint_fun,
      lower_bound,
      upper_bound,
      jac           = optimize_fun.constraint_jac,
      hess          = optimize_fun.constraint_hess,
      keep_feasible = False
   )
   constraints       = [nonlinear_constraint]
   #
   # bounds
   lower_bound = 4 * [ 1.0 ]
   upper_bound = 4 * [ 5.0 ]
   bounds = scipy.optimize.Bounds(
      lower_bound,
      upper_bound,
      keep_feasible = False
   )
   #
   # start_point
   start_point = [ 1.0, 5.0, 5.0, 1.0 ]
   #
   options = {
                             'gtol' : 1e-8,
                             'xtol' : 1e-8,
                      'barrier_tol' : 1e-8,
            'initial_tr_radius' : 1.0,
           'initial_constr_penalty' : 1.0,
      'initial_barrier_tolerance' : 0.1,
      'initial_barrier_parameter' : 0.1,
             'factorization_method' : None,
             'finite_diff_rel_step' : None,
                          'maxiter' : 50,
                          'verbose' : 0,
   }
   #
   result = scipy.optimize.minimize(
      optimize_fun.objective_fun,
      start_point,
      method      = 'trust-constr',
      jac         = optimize_fun.objective_grad,
      hess        = optimize_fun.objective_hess,
      constraints = constraints,
      options     = options,
      bounds      = bounds,
   )
   ok = ok and result.success
   #
   optimal_point = result.x
   check         = [ 1.00000000, 4.74299963, 3.82114998, 1.37940829 ]
   rel_error     = optimal_point / check - 1.0
   ok = ok and numpy.all( abs(rel_error) < 1e-5 )
   return ok
# END_PYTHON
def test_optimize_fun_xam() :
   assert optimize_fun_xam()
