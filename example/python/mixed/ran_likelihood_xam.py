# -----------------------------------------------------------------------------
#         cppad_py: A C++ Object Library and Python Interface to Cppad
#          Copyright (C) 2017-20 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# -----------------------------------------------------------------------------
# mixed ran_likelihood
# -----------------------------------------------------------------------------
'''
{xsrst_begin mixed_ran_likelihood_xam_py}
{xsrst_spell
    \hat
}

.. include:: ../preamble.rst

ran_likelihood: Example and Test
################################

p(y|theta, u)
*************
In this example math:`y` given :math:`( \theta , u )`
is distributed normally with mean :math:`\bar{y} + u`
and variance :math:`\theta`; i.e.

.. math::

    - \log [ \B{p} ( y | \theta , u ) ]
    =
    \log \left[ \sqrt{ 2 \pi \theta } \right]
    +
    \frac{1}{2} ( y - \bar{y} - u )^2 / \theta

p(u|theta)
**********
In this example, the prior for :math:`u` given :math:`\theta`
is a normal with mean zero and
standard deviation :math:`\sigma`; i.e.

.. math::

    - \log [ \B{p} ( u | \theta ) ]
    =
    \log \left[ \sqrt{ 2 \pi \sigma^2 } \right]
    +
    \frac{1}{2} u^2 / \sigma^2

p(y|theta)
**********
For this example, Laplace approximation is equal to :math:`\B{p}(y|\theta)`
i.e, it is exact. Furthermore,

.. math::

    - \log[ \B{p}(y|\theta) ]
    =
    \log \left[ \sqrt{ 2 \pi ( \theta + \sigma^2) } \right]
    +
    \frac{1}{2} ( y - \bar{y} )^2 / ( \theta + \sigma^2 )


Optimal Fixed Effects
*********************
For this example there is no fixed effects likelihood or constraints.
Hence the optimal fixed effects minimizes the following expression
w.r.t :math:`\theta`:

.. math::

    \frac{1}{2} \log \left[ \theta + \sigma^2 \right]
    +
    \frac{1}{2} ( y - \bar{y} )^2 / ( \theta + \sigma^2 )

Taking the derivative w.r.t. :math:`\theta` and setting
it equal to zero, the optimal fixed effects
:math:`\hat{\theta}` solves the equations

.. math::

    0 & = ( \hat{\theta} + \sigma^2 )^{-1}
    -
    ( y - \bar{y} )^2 ( \hat{\theta} + \sigma^2 )^{-2}
    \\
    1 & =
    ( y - \bar{y} )^2 ( \hat{\theta} + \sigma^2 )^{-1}
    \\
    \hat{\theta} & = (y - \bar{y})^2 - \sigma^2

{xsrst_file
    # BEGIN SOURCE
    # END SOURCE
}

{xsrst_end mixed_ran_likelihood_xam_py}
'''
# BEGIN SOURCE
def ran_likelihood_xam() :
    import cppad_py
    import numpy
    ok         = True
    #
    y_bar  = 1.0 # mean of the data y
    y      = 2.0 # data that depends on random effects
    sigma  = 0.5 # standard deviation for the random effects
    #
    # value of theta and u at which we will record ran_likelihood( theta , u)
    theta_u  = numpy.array([ sigma*sigma, 0.0 ], dtype=float)
    #
    # independent variables during the recording
    atheta_u = cppad_py.independent(theta_u)
    #
    # split out theta and u
    atheta   = atheta_u[0]
    au       = atheta_u[1]
    #
    # - log[ p(y|theta,u) ] (dropping terms that are constant w.r.t. theta,u)
    atmp          = ( y  - y_bar - au )
    ap_y_theta_u  = 0.5 * atmp * atmp / atheta
    ap_y_theta_u += 0.5 * numpy.log( atheta )
    #
    # - log[ p(u|theta) ] (dropping terms that are constant w.r.t. theta,u)
    atmp          = au / sigma
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
    # optimize_fixed
    options  = 'String  sb    yes\n'     # suppress optimizer banner
    options += 'Integer print_level 0\n' # suppress optimizer trace
    solution  = mixed_obj.optimize_fixed(
        fixed_ipopt_options  = options      ,
        random_ipopt_options = options      ,
    )
    #
    # optimal value for theta
    theta_opt = solution.fixed_opt[0]
    theta_hat = (y - y_bar) * (y - y_bar) - sigma * sigma
    #
    # check solution
    ok = ok and abs(theta_opt / theta_hat - 1.0) < 1e-8
    return ok
# END SOURCE
