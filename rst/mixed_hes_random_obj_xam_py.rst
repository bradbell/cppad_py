.. _mixed_hes_random_obj_xam_py-name:

!!!!!!!!!!!!!!!!!!!!!!!!!!!
mixed_hes_random_obj_xam_py
!!!!!!!!!!!!!!!!!!!!!!!!!!!

.. raw:: html

   <a href="_sources/mixed_hes_random_obj_xam_py.rst.txt">View page source</a>

.. meta::
   :keywords: mixed_hes_random_obj_xam_py, ran_likelihood:, example, test

.. index:: mixed_hes_random_obj_xam_py, ran_likelihood:, example, test

.. _mixed_hes_random_obj_xam_py-title:

ran_likelihood: Example and Test
################################

.. meta::
   :keywords: p(u|theta)

.. index:: p(u|theta)

.. _mixed_hes_random_obj_xam_py@p(u|theta):

p(u|theta)
**********
In this example there is not date and

.. math::

   - \log [ \B{p} ( u | \theta ]
   =
   \theta_0 u_0 u_1 + \theta_1 u_1 u_2 + \cdots + \theta_{m-1} u_{m-1} u_0

where :math:`m` is the number of fixed and random effects.

.. meta::
   :keywords: derivative

.. index:: derivative

.. _mixed_hes_random_obj_xam_py@Derivative:

Derivative
**********
For this example there is no data.
Hence the partial of the random effects objective,
w.r.t the random effect :math:`u_i` is

.. math::

   \theta_i u_{i+1 \mod m} + \theta_{i-1 \mod m} u_{i-1 \mod m}

.. meta::
   :keywords: hessian

.. index:: hessian

.. _mixed_hes_random_obj_xam_py@Hessian:

Hessian
*******
Taking the partial of the expression above
w.r.t the random effects :math:`u_{i-1 \mod m}` we obtain

.. math::

   \theta_{i-1 \mod m}

Taking the partial of the expression above
w.r.t the random effects :math:`u_{i+1 \mod m}` we obtain

.. math::

.. literalinclude:: ../../example/python/mixed/hes_random_obj_xam.py
   :lines: 61-125
   :language: py
