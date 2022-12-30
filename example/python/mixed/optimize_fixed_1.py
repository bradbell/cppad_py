# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileCopyrightText: Bradley M. Bell <bradbell@seanet.com>
# SPDX-FileContributor: 2017-22 Bradley M. Bell
# ----------------------------------------------------------------------------
# mixed optimize_fixed
# -----------------------------------------------------------------------------
# BEGIN SOURCE
def optimize_fixed_1() :
   import cppad_py
   import numpy
   ok         = True
   #
   theta_true = 2.0
   #
   theta      = numpy.array([ 1 ], dtype=float )
   atheta     = cppad_py.independent(theta)
   av_0       = (atheta[0] - theta_true) * (atheta[0] - theta_true) / 2.0
   av         = numpy.array( [ av_0 ] )
   f          = cppad_py.d_fun(atheta, av)
   #
   mixed_obj = cppad_py.mixed(
      fixed_init = theta ,
      fix_likelihood = f,
   )
   #
   options  = 'String  sb    yes\n'     # suppress optimizer banner
   options += 'Integer print_level 0\n' # suppress optimizer trace
   solution  = mixed_obj.optimize_fixed(
      fixed_ipopt_options = options
   )
   theta_opt = solution.fixed_opt[0]
   ok        = ok and abs( theta_true - theta_opt ) < 1e-10
   return ok
# END SOURCE
'''
{xrst_begin mixed_optimize_fixed_1_py}

A Very Simple Optimize Fixed Effects: Example and Test
######################################################
{xrst_literal
  # BEGIN SOURCE
  # END SOURCE
}
{xrst_end mixed_optimize_fixed_1_py}
'''
