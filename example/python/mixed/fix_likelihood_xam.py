# -----------------------------------------------------------------------------
#         cppad_py: A C++ Object Library and Python Interface to Cppad
#          Copyright (C) 2017-20 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# -----------------------------------------------------------------------------
# mixed fix_likelihood
# -----------------------------------------------------------------------------
'''
{xsrst_begin mixed_fix_likelihood_xam_py}
{xsrst_spell
    \hat
}

.. include:: ../preamble.rst

Mixed Class fix_likelihood: Example and Test
############################################


p(z|theta)
**********
In this example math:`z` given :math:`( \theta )`
is distributed normally with mean :math:`\theta`
and standard deviation :math:`\sigma`; i.e.

.. math::

    - \log [ \B{p} ( z | \theta ) ]
    =
    \log \left[ \sigma  \sqrt{ 2 \pi } \right]
    +
    \frac{1}{2} \left( \frac{z - \theta}{ \sigma } \right)^2

p(theta)
********
In this example, the prior for :math:`\theta`
is a normal with mean :math:`\bar{\theta}` and
standard deviation :math:`\sigma`; i.e.

.. math::

    - \log [ \B{p} ( \theta ) ]
    =
    \log \left[ \sigma  \sqrt{ 2 \pi } \right]
    +
    \frac{1}{2} \left( \frac{\theta - \bar{\theta}}{ \sigma } \right)^2

Optimal Fixed Effects
*********************
For this example there is no random effects likelihood or constraints.
Hence the optimal fixed effects minimizes the following expression
w.r.t :math:`\theta`:

.. math::

    \frac{1}{2} \left( \frac{z - \theta}{ \sigma } \right)^2
    +
    \frac{1}{2} \left( \frac{\theta - \bar{\theta}}{ \sigma } \right)^2

Taking the derivative w.r.t. :math:`\theta` and setting
it equal to zero, the optimal fixed effects
:math:`\hat{\theta}` solves the equations

.. math::

    \begin{align*}
    0 & = \frac{ \hat{\theta} - \bar{\theta}}{ \sigma^2 }
        - \frac{z - \hat{\theta} }{ \sigma^2 }
    \\
    \hat{\theta} & = \frac{ \bar{\theta} + z }{2}
    \end{align*}

{xsrst_file
    # BEGIN SOURCE
    # END SOURCE
}

{xsrst_end mixed_fix_likelihood_xam_py}
'''
# BEGIN SOURCE
def fix_likelihood_xam() :
    import cppad_py
    import numpy
    ok         = True
    #
    theta_bar = 1.5 # mean of prior for theta
    z         = 2.0 # data that does not depend on random effects
    sigma     = 0.5 # standard deviation of both data and prior
    #
    # value of theta at which we will record fix_likelihood( theta )
    theta      = numpy.array([ theta_bar ], dtype=float )
    #
    # indpeendent variables during the recording
    atheta     = cppad_py.independent(theta)
    #
    # - log[ p(theta) ] (dropping terms that are constant w.r.t theta)
    ares     = ( atheta[0] - theta_bar ) / sigma
    ap_theta = 0.5 * ares * ares
    #
    # - log[ p(z|theta) ] (dropping terms that are constant w.r.t. theta)
    ares       = ( z  - atheta[0] ) / sigma
    ap_z_theta = 0.5 * ares * ares
    #
    # - log[ p(z|theta) p(theta) ]
    av_0 = ap_z_theta + ap_theta
    #
    # function mapping theta -> v
    av   = numpy.array( [ av_0 ] )
    fun  = cppad_py.d_fun(atheta, av)
    #
    # mixed_obj
    mixed_obj = cppad_py.mixed(
        fixed_init     = theta ,
        fix_likelihood = fun,
    )
    #
    # optimize_fixed
    options  = 'String  sb    yes\n'     # suppress optimizer banner
    options += 'Integer print_level 0\n' # suppress optimizer trace
    solution  = mixed_obj.optimize_fixed(
        fixed_ipopt_options = options
    )
    #
    # optimal value for theta
    theta_opt = solution.fixed_opt[0]
    theta_hat = (theta_bar + z) / 2.0
    #
    # check solution
    ok = ok and abs( theta_opt - theta_hat ) < 1e-10
    return ok
# END SOURCE
