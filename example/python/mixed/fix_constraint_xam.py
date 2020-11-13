# -----------------------------------------------------------------------------
#         cppad_py: A C++ Object Library and Python Interface to Cppad
#          Copyright (C) 2017-20 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# -----------------------------------------------------------------------------
# mixed fix_constraint
# -----------------------------------------------------------------------------
'''
{xsrst_begin mixed_fix_constraint_xam_py}
{xsrst_spell
    \hat
}

.. include:: ../preamble.rst

fix_constraint: Example and Test
################################

Random Effects
**************
For this example there is no random effects.

fix_likelihood
**************
For this example, the fixed likelihood is

.. math::

    f( \theta ) = ( \theta - 1 )^2

fix_constraint
**************
For this example, the fixed constraint is

.. math::

    g( \theta ) = ( \theta + 2)^2

Fixed Constraint Bounds
***********************
For this example, there is no fixed constraint upper bound
and the lower bound is :math:`g^L \leq g(\theta)`

Optimal Fixed Effects
*********************
If :math:`g^L \leq g(1) = 9`, the optimal value for the fixed effects is
:math:`\hat{\theta} = 1`.
Otherwise, the optimal value satisfies the equation
:math:`c ( \hat{\theta} ) = g^L`; i.e,
:math:`\hat{\theta} = \sqrt{g^L} - 2`.

{xsrst_end mixed_fix_constraint_xam_py}
'''
# BEGIN SOURCE
def fix_constraint_xam() :
    import cppad_py
    import numpy
    ok         = True
    #
    g_L        = 10.0
    theta_hat  = numpy.sqrt(g_L) - 2
    #
    # value of theta at which we will record fix_likelihood( theta )
    theta      = numpy.array([ 0 ], dtype=float )
    #
    # fix_likelihood
    atheta  = cppad_py.independent(theta)
    av_0    =  ( atheta[0] - 1.0 ) * ( atheta[0] - 1.0 )
    av      = numpy.array( [ av_0 ] )
    f       = cppad_py.d_fun(atheta, av)
    #
    # fix_constraint
    atheta  = cppad_py.independent(theta)
    av_0    =  ( atheta[0] + 2.0 ) * ( atheta[0] + 2.0 )
    av      = numpy.array( [ av_0] )
    g       = cppad_py.d_fun(atheta, av)
    #
    #
    # mixed_obj
    mixed_obj = cppad_py.mixed(
        fixed_init     = theta ,
        fix_likelihood = f,
        fix_constraint = g,
    )
    #
    # optimize_fixed
    options  = 'String  sb    yes\n'     # suppress optimizer banner
    options += 'Integer print_level 0\n' # suppress optimizer trace
    solution  = mixed_obj.optimize_fixed(
        fixed_ipopt_options  = options,
        fix_constraint_lower = numpy.array( [g_L], dtype=float)
    )
    #
    # optimal value for theta
    theta_opt = solution.fixed_opt[0]
    #
    # check solution
    ok = ok and abs(theta_opt / theta_hat - 1.0 ) < 1e-9
    return ok
# END SOURCE
