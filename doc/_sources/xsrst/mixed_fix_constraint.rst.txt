!!!!!!!!!!!!!!!!!!!!
mixed_fix_constraint
!!!!!!!!!!!!!!!!!!!!

.. toctree::
   :maxdepth: 1
   :hidden:

   mixed_fix_constraint_xam_py

.. include:: ../preamble.rst

.. meta::
   :keywords: mixed_fix_constraint, fixed, effects, constraint, function

.. index:: mixed_fix_constraint, fixed, effects, constraint, function

.. _mixed_fix_constraint:

Fixed Effects Constraint Function
#################################
.. contents::
   :local:

.. meta::
   :keywords: syntax

.. index:: syntax

.. _mixed_fix_constraint.syntax:

Syntax
******
*v* = *fix_constraint*\ ``.forward`` (0, *theta* )

.. meta::
   :keywords: fix_constraint

.. index:: fix_constraint

.. _mixed_fix_constraint.fix_constraint:

fix_constraint
***************
is a :ref:`d_fun<py_fun_ctor.syntax.d_fun>` representation
of the fixed effects constraint function

.. math::
    g( \theta )
    =
    [ v_0 ( \theta ) , \cdots , v_{m-1} ( \theta ) ]^\R{T}

The functions :math:`v_i ( \theta )` for :math:`i = 0 , \ldots , m-1`
are assumed to be a smooth w.r.t the vector :math:`\theta`.
The bounds for :math:`g( \theta )` are specified by
:ref:`mixed_optimize_fixed.fix_constraint_lower_(fix_constraint_upper)` .

.. meta::
   :keywords: theta

.. index:: theta

.. _mixed_fix_constraint.theta:

theta
*****
is a numpy vector with ``float`` elements and size
:ref:`mixed_ctor.fixed_init.n_fixed`
containing a value for the fixed effects.

.. meta::
   :keywords: v

.. index:: v

.. _mixed_fix_constraint.v:

v
*
is a numpy vector with ``float`` elements and size *m*.

.. meta::
   :keywords: none

.. index:: none

.. _mixed_fix_constraint.none:

None
****
The value *fix_constraint* = ``None``
corresponds to not fixed effects constraint function; i.e.,
:math:`m = 0`.

.. meta::
   :keywords: example

.. index:: example

.. _mixed_fix_constraint.example:

Example
*******
:ref:`mixed_fix_constraint_xam_py<mixed_fix_constraint_xam_py>`

----

xsrst input file: ``lib/python/cppad_py/mixed.py``
