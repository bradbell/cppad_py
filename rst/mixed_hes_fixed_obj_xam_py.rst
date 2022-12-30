.. _mixed_hes_fixed_obj_xam_py-name:

!!!!!!!!!!!!!!!!!!!!!!!!!!
mixed_hes_fixed_obj_xam_py
!!!!!!!!!!!!!!!!!!!!!!!!!!

.. raw:: html

   <a href="_sources/mixed_hes_fixed_obj_xam_py.rst.txt">View page source</a>

.. meta::
   :keywords: mixed_hes_fixed_obj_xam_py, ran_likelihood:, example, test

.. index:: mixed_hes_fixed_obj_xam_py, ran_likelihood:, example, test

.. _mixed_hes_fixed_obj_xam_py-title:

ran_likelihood: Example and Test
################################

.. meta::
   :keywords: p(y|theta,, u)

.. index:: p(y|theta,, u)

.. _mixed_hes_fixed_obj_xam_py@p(y|theta, u):

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

.. meta::
   :keywords: p(u|theta)

.. index:: p(u|theta)

.. _mixed_hes_fixed_obj_xam_py@p(u|theta):

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

.. meta::
   :keywords: p(y|theta)

.. index:: p(y|theta)

.. _mixed_hes_fixed_obj_xam_py@p(y|theta):

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

.. meta::
   :keywords: derivative

.. index:: derivative

.. _mixed_hes_fixed_obj_xam_py@Derivative:

Derivative
**********
For this example there is no fixed effects likelihood or constraints.
Hence the derivative of the fixed effects objective,
w.r.t the fixed effects :math:`\theta`, is

.. math::

   \frac{1}{2} ( \theta + \sigma^2 )^{-1}
   -
   \frac{1}{2} ( y - \bar{y} )^2 ( \theta + \sigma^2 )^{-2}

.. meta::
   :keywords: hessian

.. index:: hessian

.. _mixed_hes_fixed_obj_xam_py@Hessian:

Hessian
*******
Taking the derivative of the expression above
w.r.t the fixed effects :math:`\theta` we obtain the Hessian:

.. math::

   ( y - \bar{y} )^2 ( \theta + \sigma^2 )^{-3}
   -
   \frac{1}{2} ( \theta + \sigma^2 )^{-2}

.. literalinclude:: ../../example/python/mixed/hes_fixed_obj_xam.py
   :lines: 90-162
   :language: py
