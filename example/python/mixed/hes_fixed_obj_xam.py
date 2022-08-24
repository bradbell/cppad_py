# -----------------------------------------------------------------------------
#         cppad_py: A C++ Object Library and Python Interface to Cppad
#          Copyright (C) 2017-22 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# -----------------------------------------------------------------------------
# mixed hes_fixed_obj_xam
# -----------------------------------------------------------------------------
'''
{xrst_begin mixed_hes_fixed_obj_xam_py}

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


Derivative
**********
For this example there is no fixed effects likelihood or constraints.
Hence the derivative of the fixed effects objective,
w.r.t the fixed effects :math:`\theta`, is

.. math::

   \frac{1}{2} ( \theta + \sigma^2 )^{-1}
   -
   \frac{1}{2} ( y - \bar{y} )^2 ( \theta + \sigma^2 )^{-2}

Hessian
*******
Taking the derivative of the expression above
w.r.t the fixed effects :math:`\theta` we obtain the Hessian:

.. math::

   ( y - \bar{y} )^2 ( \theta + \sigma^2 )^{-3}
   -
   \frac{1}{2} ( \theta + \sigma^2 )^{-2}


{xrst_literal
   # BEGIN SOURCE
   # END SOURCE
}

{xrst_end mixed_hes_fixed_obj_xam_py}
'''
# BEGIN SOURCE
def hes_fixed_obj_xam() :
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
   theta = theta_u[0:1]
   u     = theta_u[1:2]
   mixed_obj = cppad_py.mixed(
      fixed_init     = theta        ,
      random_init    = u            ,
      ran_likelihood = r,
   )
   #
   # optimal random effects
   options    = 'String  sb    yes\n'     # suppress optimizer banner
   options   += 'Integer print_level 0\n' # suppress optimizer trace
   random_opt = mixed_obj.optimize_random(
      random_ipopt_options  = options    ,
      fixed_vec             = theta      ,
   )
   #
   # hes_fixed_obj_rcv
   hes_fixed_obj_rcv = cppad_py.sparse_rcv()
   mixed_obj.hes_fixed_obj(
      hes_fixed_obj_rcv        ,
      fixed_vec  = theta       ,
      random_opt = random_opt  ,
   )
   #
   theta = theta[0]
   term1 = (theta + sigma * sigma)
   term2 = (y - y_bar) * (y - y_bar)
   check = term2 / (term1 * term1 * term1)  - 0.5 / (term1 * term1 )
   #
   # check solution
   ok = ok and hes_fixed_obj_rcv.nr()     == 1
   ok = ok and hes_fixed_obj_rcv.nc()     == 1
   ok = ok and hes_fixed_obj_rcv.nnz()    == 1
   ok = ok and hes_fixed_obj_rcv.row()[0] == 0
   ok = ok and hes_fixed_obj_rcv.col()[0] == 0
   ok = ok and abs( hes_fixed_obj_rcv.val()[0] / check - 1.0 ) < 1e-8
   return ok
# END SOURCE
