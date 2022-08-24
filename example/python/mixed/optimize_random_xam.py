# -----------------------------------------------------------------------------
#         cppad_py: A C++ Object Library and Python Interface to Cppad
#          Copyright (C) 2017-22 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# -----------------------------------------------------------------------------
# mixed optimize_random
# -----------------------------------------------------------------------------
"""
{xrst_begin mixed_optimize_random_xam_py}
{xrst_spell
}

optimize_random: Example and Test
#################################

p(y|theta, u)
*************
In this example math:`y` given :math:`( \theta , u )`
is distributed normally with mean :math:`u`
and variance one; i.e.,

.. math::

    - \log [ \B{p} ( y | \theta , u ) ]
    =
    \log \left[ \sqrt{ 2 \pi } \right]
    +
    \frac{1}{2} ( y - u )^2


p(u|theta)
**********
In this example, the prior for :math:`u` given :math:`\theta`
is a normal with mean :math:`\theta` and  variance one; i.e.

.. math::

    - \log [ \B{p} ( u | \theta ) ]
    =
    \log \left[ \sqrt{ 2 \pi } \right]
    +
    \frac{1}{2} (u - \theta )^2

Optimal Random Effects
**********************
Given a value for the fixed effects :math:`\theta`,
the optimal random effects minimizes the following expression
w.r.t :math:`u`:

.. math::

    \frac{1}{2} ( u - y )^2 + \frac{1}{2} (u - \theta )^2

Taking the derivative w.r.t. :math:`u` and setting
it equal to zero, the optimal ranomd effects,
as a function of the fixed effects,
:math:`\hat{u} ( \theta )` solves the equations

.. math::

    0 & = \hat{u} ( \theta ) - y + \hat{u} ( \theta ) - \theta
    \\
    \hat{u} ( \theta ) & = \frac{y + \theta}{2}

{xrst_literal
    # BEGIN SOURCE
    # END SOURCE
}

{xrst_end mixed_optimize_random_xam_py}
"""
# BEGIN SOURCE
def optimize_random_xam() :
    import cppad_py
    import numpy
    ok         = True
    #
    theta  = 1.0  # value of theta at which will will optimize u
    y      = 2.0 # data that depends on random effects
    #
    # value of theta and u at which we will record ran_likelihood( theta , u)
    theta_u  = numpy.array([ theta , 0.0 ], dtype=float)
    #
    # independent variables during the recording
    atheta_u = cppad_py.independent(theta_u)
    #
    # split out theta and u
    atheta   = atheta_u[0]
    au       = atheta_u[1]
    #
    # - log[ p(y|theta,u) ] (dropping terms that are constant w.r.t. theta,u)
    atmp          = ( y  - au )
    ap_y_theta_u  = 0.5 * atmp * atmp
    #
    # - log[ p(u|theta) ] (dropping terms that are constant w.r.t. theta, u)
    atmp          = ( au - atheta )
    ap_u_theta    = 0.5 * atmp * atmp
    #
    # - log[ p(y|theta, u) p(u|theta) ]
    av_0 = ap_y_theta_u + ap_u_theta
    #
    # function mapping (theta,u) -> v
    av   = numpy.array( [ av_0 ] )
    r    = cppad_py.d_fun(atheta_u, av)
    #
    # mixed_obj
    mixed_obj = cppad_py.mixed(
        fixed_init     = theta_u[0:1] ,
        random_init    = theta_u[1:2] ,
        ran_likelihood = r,
    )
    #
    # optimize_random
    options    = 'String  sb    yes\n'     # suppress optimizer banner
    options   += 'Integer print_level 0\n' # suppress optimizer trace
    fixed_vec  = numpy.array( [ theta ] )
    random_opt = mixed_obj.optimize_random(
        random_ipopt_options = options      ,
        fixed_vec            = fixed_vec    ,
    )
    #
    # optimal value for the random effects
    u_hat = 0.5 * ( y + theta )
    #
    # check solution
    ok = ok and abs( random_opt[0] / u_hat - 1.0) < 1e-8
    return ok
# END SOURCE
