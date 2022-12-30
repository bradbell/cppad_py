.. _mixed_optimize_random-name:

!!!!!!!!!!!!!!!!!!!!!
mixed_optimize_random
!!!!!!!!!!!!!!!!!!!!!

.. raw:: html

   <a href="_sources/mixed_optimize_random.rst.txt">View page source</a>

.. meta::
   :keywords: mixed_optimize_random, optimize, the, random, effects

.. index:: mixed_optimize_random, optimize, the, random, effects

.. _mixed_optimize_random-title:

Optimize The Random Effects
###########################

.. meta::
   :keywords: syntax

.. index:: syntax

.. _mixed_optimize_random@Syntax:

Syntax
******

.. literalinclude:: ../../lib/python/cppad_py/mixed.py
   :lines: 853-859
   :language: py

.. meta::
   :keywords: purpose

.. index:: purpose

.. _mixed_optimize_random@Purpose:

Purpose
*******
Given a value for the fixed effects :math:`\theta`,
this routine maximizes the :ref:`mixed_ran_likelihood-title`
with respect to the fixed effect :math:`u`; i.e.,

.. math::

   \B{p} ( y | \theta , u ) \B{p}( u | \theta )

If there is no data, this routine maximizes :math:`\B{p} ( u | \theta )`.

.. meta::
   :keywords: argument, types

.. index:: argument, types

.. _mixed_optimize_random@Argument Types:

Argument Types
**************
The argument *random_ipopt_options*
has type ``str``.  All the other arguments are
numpy vectors with elements of type ``float``.

.. meta::
   :keywords: fixed_vec

.. index:: fixed_vec

.. _mixed_optimize_random@fixed_vec:

fixed_vec
*********
has length *n_fixed* and is the value of the fixed effects
:math:`\theta` in the objective function.
This vector can't be ``None``.

.. meta::
   :keywords: random_lower, (random_upper)

.. index:: random_lower, (random_upper)

.. _mixed_optimize_random@random_lower (random_upper):

random_lower (random_upper)
***************************
has length *n_random* and is the lower (upper) limit for the random effects.
As a lower (upper) limit, the value ``None`` is minus (plus) infinity;
i.e., no lower (upper) limit.

.. meta::
   :keywords: random_in

.. index:: random_in

.. _mixed_optimize_random@random_in:

random_in
*********
has length *n_random* and is the initial value used during
optimization of the random effects.
If *random_in* is ``None`` the value *random_init* is used; see
:ref:`mixed_ctor@random_init` .

.. meta::
   :keywords: random_opt

.. index:: random_opt

.. _mixed_optimize_random@random_opt:

random_opt
**********
The return value *random_opt* is a numpy vector,
with length *n_random* an elements of type ``float``,
that maximizes the random likelihood with respect to the random effects.

.. meta::
   :keywords: examples

.. index:: examples

.. _mixed_optimize_random@Examples:

Examples
********

-  :ref:`mixed_optimize_random_xam_py-title`

.. toctree::
   :maxdepth: 1
   :hidden:

   mixed_optimize_random_xam_py
