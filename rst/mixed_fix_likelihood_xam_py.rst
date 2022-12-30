.. _mixed_fix_likelihood_xam_py-name:

!!!!!!!!!!!!!!!!!!!!!!!!!!!
mixed_fix_likelihood_xam_py
!!!!!!!!!!!!!!!!!!!!!!!!!!!

.. raw:: html

   <a href="_sources/mixed_fix_likelihood_xam_py.rst.txt">View page source</a>

.. meta::
   :keywords: mixed_fix_likelihood_xam_py, fix_likelihood:, example, test

.. index:: mixed_fix_likelihood_xam_py, fix_likelihood:, example, test

.. _mixed_fix_likelihood_xam_py-title:

fix_likelihood: Example and Test
################################

.. meta::
   :keywords: p(z|theta)

.. index:: p(z|theta)

.. _mixed_fix_likelihood_xam_py@p(z|theta):

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

.. meta::
   :keywords: p(theta)

.. index:: p(theta)

.. _mixed_fix_likelihood_xam_py@p(theta):

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

.. meta::
   :keywords: optimal, fixed, effects

.. index:: optimal, fixed, effects

.. _mixed_fix_likelihood_xam_py@Optimal Fixed Effects:

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

   0 & = \frac{ \hat{\theta} - \bar{\theta}}{ \sigma^2 }
      - \frac{z - \hat{\theta} }{ \sigma^2 }
   \\
   \hat{\theta} & = \frac{ \bar{\theta} + z }{2}

.. literalinclude:: ../example/python/mixed/fix_likelihood_xam.py
   :lines: 73-122
   :language: py
