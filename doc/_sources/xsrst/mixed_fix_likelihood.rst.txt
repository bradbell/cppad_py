!!!!!!!!!!!!!!!!!!!!
mixed_fix_likelihood
!!!!!!!!!!!!!!!!!!!!

.. toctree::
   :maxdepth: 1
   :hidden:

   mixed_fix_likelihood_xam_py

.. include:: ../preamble.rst

.. meta::
   :keywords: mixed_fix_likelihood, fixed, effects, likelihood

.. index:: mixed_fix_likelihood, fixed, effects, likelihood

.. _mixed_fix_likelihood:

Fixed Effects Likelihood
########################
.. contents::
   :local:

.. meta::
   :keywords: syntax

.. index:: syntax

.. _mixed_fix_likelihood.syntax:

Syntax
******
*v* = *fix_likelihood*\ ``.forward`` (0, *theta* )

.. meta::
   :keywords: fix_likelihood

.. index:: fix_likelihood

.. _mixed_fix_likelihood.fix_likelihood:

fix_likelihood
***************
is a :ref:`d_fun<py_fun_ctor.syntax.d_fun>` representation
of the negative log of the
:ref:`fixed effects likelihood <mixed.notation.fixed_effects_likelihood>`

.. math::

    f( \theta )
    =
    v_0 ( \theta ) + | v_1 ( \theta)  | + \cdots + | v_{m-1} ( \theta ) |
    =
    - \log [ \B{p} ( z | \theta ) \B{p} ( \theta ) ]

The functions :math:`v_i ( \theta )` for :math:`i = 0 , \ldots , m-1`
are assumed to be a smooth w.r.t the vector :math:`\theta`.

.. meta::
   :keywords: theta

.. index:: theta

.. _mixed_fix_likelihood.theta:

theta
*****
is a numpy vector with ``float`` elements and size
:ref:`mixed_ctor.fixed_init.n_fixed`
containing a value for the fixed effects.

.. meta::
   :keywords: v

.. index:: v

.. _mixed_fix_likelihood.v:

v
*
is a numpy vector with ``float`` elements and size *m*.

.. meta::
   :keywords: none

.. index:: none

.. _mixed_fix_likelihood.none:

None
****
The value *fix_likelihood* = ``None``
corresponds to the fixed effects likelihood
being constant w.r.t. :math:`\theta`.

.. meta::
   :keywords: example

.. index:: example

.. _mixed_fix_likelihood.example:

Example
*******
:ref:`mixed_fix_likelihood_xam_py<mixed_fix_likelihood_xam_py>`

----

xsrst input file: ``lib/python/cppad_py/mixed.py``
