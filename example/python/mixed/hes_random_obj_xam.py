# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileCopyrightText: Bradley M. Bell <bradbell@seanet.com>
# SPDX-FileContributor: 2017-23 Bradley M. Bell
# ----------------------------------------------------------------------------
# mixed hes_random_obj_xam
# -----------------------------------------------------------------------------
r'''
{xrst_begin mixed_hes_random_obj_xam.py}

ran_likelihood: Example and Test
################################

p(u|theta)
**********
In this example there is not date and

.. math::

   - \log [ \B{p} ( u | \theta ]
   =
   \theta_0 u_0 u_1 + \theta_1 u_1 u_2 + \cdots + \theta_{m-1} u_{m-1} u_0

where :math:`m` is the number of fixed and random effects.


Derivative
**********
For this example there is no data.
Hence the partial of the random effects objective,
w.r.t the random effect :math:`u_i` is

.. math::

   \theta_i u_{i+1 \mod m} + \theta_{i-1 \mod m} u_{i-1 \mod m}


Hessian
*******
Taking the partial of the expression above
w.r.t the random effects :math:`u_{i-1 \mod m}` we obtain

.. math::

   \theta_{i-1 \mod m}

Taking the partial of the expression above
w.r.t the random effects :math:`u_{i+1 \mod m}` we obtain

.. math::



{xrst_literal
   # BEGIN SOURCE
   # END SOURCE
}

{xrst_end mixed_hes_random_obj_xam.py}
'''
# BEGIN SOURCE
def hes_random_obj_xam() :
   import cppad_py
   import numpy
   ok         = True
   #
   n_fixed    = 5
   n_random   = n_fixed
   #
   # value of theta and u at which we will record ran_likelihood( theta , u)
   theta_u  = numpy.ones(n_fixed + n_random, dtype=float)
   for i in range(n_fixed ) :
      theta_u[i] = float(i + 1)
   #
   # independent variables during the recording
   atheta_u = cppad_py.independent(theta_u)
   #
   # split out theta and u
   atheta   = atheta_u[0 : n_fixed]
   au       = atheta_u[n_fixed : n_fixed + n_random]
   #
   # - log[ p(u|theta) ] (dropping terms that are constant w.r.t. theta,u)
   asum = 0.0
   for i in range(n_fixed) :
      ip     = (i + 1) % n_fixed
      asum  += atheta[i] * au[i] * au[ip]
   #
   # function mapping (theta,u) -> sum
   av   = numpy.array( [ asum ] )
   r    = cppad_py.d_fun(atheta_u, av)
   #
   # mixed_obj
   theta = theta_u[0 : n_fixed]
   u     = theta_u[n_fixed : n_fixed + n_random]
   mixed_obj = cppad_py.mixed(
      fixed_init     = theta        ,
      random_init    = u            ,
      ran_likelihood = r,
   )
   #
   # hes_random_obj_rcv
   hes_random_obj_rcv = cppad_py.sparse_rcv()
   mixed_obj.hes_random_obj(
      hes_random_obj_rcv       ,
      fixed_vec  = theta       ,
      random_vec = u           ,
   )
   #
   # check lower triangle of the Hessian
   ok  = ok and hes_random_obj_rcv.nr()  == n_random
   ok  = ok and hes_random_obj_rcv.nc()  == n_random
   ok  = ok and hes_random_obj_rcv.nnz() == n_random
   row = hes_random_obj_rcv.row()
   col = hes_random_obj_rcv.col()
   val = hes_random_obj_rcv.val()
   for k in range( hes_random_obj_rcv.nnz() ) :
      i  = row[k]
      j  = col[k]
      ok = ok and j < i
      if j+1 == i :
         ok = ok and val[k] == theta[(i-1) % n_random]
      elif j == 0 and i == n_random - 1 :
         ok = ok and val[k] == theta[i]
      else :
         ok = False
   return ok
# END SOURCE
def test_hes_random_obj_xam() :
   assert hes_random_obj_xam()
