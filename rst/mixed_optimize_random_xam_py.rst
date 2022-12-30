.. _mixed_optimize_random_xam_py-name:

!!!!!!!!!!!!!!!!!!!!!!!!!!!!
mixed_optimize_random_xam_py
!!!!!!!!!!!!!!!!!!!!!!!!!!!!

.. raw:: html

   <a href="_sources/mixed_optimize_random_xam_py.rst.txt">View page source</a>

.. meta::
   :keywords: mixed_optimize_random_xam_py, optimize_random:, example, test

.. index:: mixed_optimize_random_xam_py, optimize_random:, example, test

.. _mixed_optimize_random_xam_py-title:

optimize_random: Example and Test
#################################

.. meta::
   :keywords: p(y|theta,, u)

.. index:: p(y|theta,, u)

.. _mixed_optimize_random_xam_py@p(y|theta, u):

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

.. meta::
   :keywords: p(u|theta)

.. index:: p(u|theta)

.. _mixed_optimize_random_xam_py@p(u|theta):

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

.. meta::
   :keywords: optimal, random, effects

.. index:: optimal, random, effects

.. _mixed_optimize_random_xam_py@Optimal Random Effects:

Optimal Random Effects
**********************
Given a value for the fixed effects :math:`\theta`,
the optimal random effects minimizes the following expression
w.r.t :math:`u`:

.. math::

   \frac{1}{2} ( u - y )^2 + \frac{1}{2} (u - \theta )^2

Taking the derivative w.r.t. :math:`u` and setting
it equal to zero, the optimal random effects,
as a function of the fixed effects,
:math:`\hat{u} ( \theta )` solves the equations

.. math::

   0 & = \hat{u} ( \theta ) - y + \hat{u} ( \theta ) - \theta
   \\
   \hat{u} ( \theta ) & = \frac{y + \theta}{2}

.. literalinclude:: ../../example/python/mixed/optimize_random_xam.py
   :lines: 72-126
   :language: py
