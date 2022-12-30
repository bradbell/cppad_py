.. _mixed_ran_likelihood_xam_py-name:

!!!!!!!!!!!!!!!!!!!!!!!!!!!
mixed_ran_likelihood_xam_py
!!!!!!!!!!!!!!!!!!!!!!!!!!!

.. raw:: html

   <a href="_sources/mixed_ran_likelihood_xam_py.rst.txt">View page source</a>

.. meta::
   :keywords: mixed_ran_likelihood_xam_py, ran_likelihood:, example, test

.. index:: mixed_ran_likelihood_xam_py, ran_likelihood:, example, test

.. _mixed_ran_likelihood_xam_py-title:

ran_likelihood: Example and Test
################################

.. meta::
   :keywords: p(y|theta,, u)

.. index:: p(y|theta,, u)

.. _mixed_ran_likelihood_xam_py@p(y|theta, u):

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

.. _mixed_ran_likelihood_xam_py@p(u|theta):

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

.. _mixed_ran_likelihood_xam_py@p(y|theta):

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
   :keywords: optimal, fixed, effects

.. index:: optimal, fixed, effects

.. _mixed_ran_likelihood_xam_py@Optimal Fixed Effects:

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

.. literalinclude:: ../../example/python/mixed/ran_likelihood_xam.py
   :lines: 93-149
   :language: py
