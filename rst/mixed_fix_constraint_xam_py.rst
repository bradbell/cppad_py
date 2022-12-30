.. _mixed_fix_constraint_xam_py-name:

!!!!!!!!!!!!!!!!!!!!!!!!!!!
mixed_fix_constraint_xam_py
!!!!!!!!!!!!!!!!!!!!!!!!!!!

.. raw:: html

   <a href="_sources/mixed_fix_constraint_xam_py.rst.txt">View page source</a>

.. meta::
   :keywords: mixed_fix_constraint_xam_py, fix_constraint:, example, test

.. index:: mixed_fix_constraint_xam_py, fix_constraint:, example, test

.. _mixed_fix_constraint_xam_py-title:

fix_constraint: Example and Test
################################

.. meta::
   :keywords: random, effects

.. index:: random, effects

.. _mixed_fix_constraint_xam_py@Random Effects:

Random Effects
**************
For this example there is no random effects.

.. meta::
   :keywords: fix_likelihood

.. index:: fix_likelihood

.. _mixed_fix_constraint_xam_py@fix_likelihood:

fix_likelihood
**************
For this example, the fixed likelihood is

.. math::

   f( \theta ) = ( \theta - 1 )^2

.. meta::
   :keywords: fix_constraint

.. index:: fix_constraint

.. _mixed_fix_constraint_xam_py@fix_constraint:

fix_constraint
**************
For this example, the fixed constraint is

.. math::

   g( \theta ) = ( \theta + 2)^2

.. meta::
   :keywords: fixed, constraint, bounds

.. index:: fixed, constraint, bounds

.. _mixed_fix_constraint_xam_py@Fixed Constraint Bounds:

Fixed Constraint Bounds
***********************
For this example, there is no fixed constraint upper bound
and the lower bound is :math:`g^L \leq g(\theta)`

.. meta::
   :keywords: optimal, fixed, effects

.. index:: optimal, fixed, effects

.. _mixed_fix_constraint_xam_py@Optimal Fixed Effects:

Optimal Fixed Effects
*********************
If :math:`g^L \leq g(1) = 9`, the optimal value for the fixed effects is
:math:`\hat{\theta} = 1`.
Otherwise, the optimal value satisfies the equation
:math:`c ( \hat{\theta} ) = g^L`; i.e,
:math:`\hat{\theta} = \sqrt{g^L} - 2`.
