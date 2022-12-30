.. _mixed-name:

!!!!!
mixed
!!!!!

.. raw:: html

   <a href="_sources/mixed.rst.txt">View page source</a>

.. meta::
   :keywords: mixed, laplace, approximation, mixed, effects, models

.. index:: mixed, laplace, approximation, mixed, effects, models

.. _mixed-title:

Laplace Approximation of Mixed Effects Models
#############################################

.. meta::
   :keywords: notation

.. index:: notation

.. _mixed@Notation:

Notation
********

.. meta::
   :keywords: theta

.. index:: theta

.. _mixed@Notation@theta:

theta
=====
We use :math:`\theta` to denote a value for the fixed effects vector.

.. meta::
   :keywords: u

.. index:: u

.. _mixed@Notation@u:

u
=
We use :math:`u` to denote a value for the random effects vector.

.. meta::
   :keywords: z

.. index:: z

.. _mixed@Notation@z:

z
=
We use :math:`z` to denote
the data that does not depend on the random effects.

.. meta::
   :keywords: y

.. index:: y

.. _mixed@Notation@y:

y
=
We use :math:`y` to denote
the data that depends on the random effects.

.. meta::
   :keywords: p(theta)

.. index:: p(theta)

.. _mixed@Notation@p(theta):

p(theta)
========
We use :math:`\B{p} ( \theta )` to denote the prior density for :math:`\theta`.

.. meta::
   :keywords: p(z|theta)

.. index:: p(z|theta)

.. _mixed@Notation@p(z|theta):

p(z|theta)
==========
We use :math:`\B{p} (z | \theta )` to denote the density of :math:`z`
given :math:`\theta`.

.. meta::
   :keywords: p(u|theta)

.. index:: p(u|theta)

.. _mixed@Notation@p(u|theta):

p(u|theta)
==========
We use :math:`\B{p} (u | \theta )` to denote the density of :math:`u`
given :math:`\theta`.

.. meta::
   :keywords: p(y|theta,u)

.. index:: p(y|theta,u)

.. _mixed@Notation@p(y|theta,u):

p(y|theta,u)
============
We use :math:`\B{p} (y | \theta , u)` to denote the density of :math:`y`
given :math:`\theta` and :math:`u`.

.. meta::
   :keywords: fixed, effects, likelihood

.. index:: fixed, effects, likelihood

.. _mixed@Notation@Fixed Effects Likelihood:

Fixed Effects Likelihood
========================
We refer to :math:`\B{p} (z | \theta ) \B{p} ( \theta )`
as the fixed effects likelihood.
The negative log of this, as function of :math:`\theta`, is computed by
:ref:`mixed_ctor@fix_likelihood` .

.. meta::
   :keywords: random, effects, likelihood

.. index:: random, effects, likelihood

.. _mixed@Notation@Random Effects Likelihood:

Random Effects Likelihood
=========================
We refer to :math:`\B{p} (y | \theta , u ) \B{p} ( u | \theta )`
as the random effects likelihood.
The negative log of this, as function of :math:`\theta, u`, is computed by
:ref:`mixed_ctor@ran_likelihood` .

.. meta::
   :keywords: children

.. index:: children

.. _mixed@Children:

Children
********

.. csv-table::
   :header:  "Child", "Title"
   :widths: auto

   "mixed_ctor", :ref:`mixed_ctor-title`
   "mixed_warning", :ref:`mixed_warning-title`
   "mixed_fatal_error", :ref:`mixed_fatal_error-title`
   "mixed_fix_likelihood", :ref:`mixed_fix_likelihood-title`
   "mixed_fix_constraint", :ref:`mixed_fix_constraint-title`
   "mixed_ran_likelihood", :ref:`mixed_ran_likelihood-title`
   "mixed_optimize_fixed", :ref:`mixed_optimize_fixed-title`
   "mixed_optimize_random", :ref:`mixed_optimize_random-title`
   "mixed_hes_fixed_obj", :ref:`mixed_hes_fixed_obj-title`
   "mixed_hes_random_obj", :ref:`mixed_hes_random_obj-title`

.. toctree::
   :maxdepth: 1
   :hidden:

   mixed_ctor
   mixed_warning
   mixed_fatal_error
   mixed_fix_likelihood
   mixed_fix_constraint
   mixed_ran_likelihood
   mixed_optimize_fixed
   mixed_optimize_random
   mixed_hes_fixed_obj
   mixed_hes_random_obj
