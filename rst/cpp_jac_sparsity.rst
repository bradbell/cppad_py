.. _cpp_jac_sparsity-name:

!!!!!!!!!!!!!!!!
cpp_jac_sparsity
!!!!!!!!!!!!!!!!

.. raw:: html

   <a href="_sources/cpp_jac_sparsity.rst.txt">View page source</a>

.. meta::
   :keywords: cpp_jac_sparsity, jacobian, sparsity, patterns

.. index:: cpp_jac_sparsity, jacobian, sparsity, patterns

.. _cpp_jac_sparsity-title:

Jacobian Sparsity Patterns
##########################

.. meta::
   :keywords: syntax

.. index:: syntax

.. _cpp_jac_sparsity@Syntax:

Syntax
******

| *f*\ ``.for_jac_sparsity`` ( *pattern_in* , *pattern_out* )
| *f*\ ``.rev_jac_sparsity`` ( *pattern_in* , *pattern_out* )

.. meta::
   :keywords: purpose

.. index:: purpose

.. _cpp_jac_sparsity@Purpose:

Purpose
*******
We use :math:`F : \B{R}^n \rightarrow \B{R}^m` to denote the
function corresponding to the operation sequence stored in *f* .

.. meta::
   :keywords: for_jac_sparsity

.. index:: for_jac_sparsity

.. _cpp_jac_sparsity@Purpose@for_jac_sparsity:

for_jac_sparsity
================
Fix :math:`R \in \B{R}^{n \times \ell}` and define the function

.. math::

   J(x) = F^{(1)} ( x ) * R

Given a sparsity pattern for :math:`R`,
``for_jac_sparsity`` computes a sparsity pattern for :math:`J(x)`.

.. meta::
   :keywords: rev_jac_sparsity

.. index:: rev_jac_sparsity

.. _cpp_jac_sparsity@Purpose@rev_jac_sparsity:

rev_jac_sparsity
================
Fix :math:`R \in \B{R}^{\ell \times m}` and define the function

.. math::

   J(x) = R * F^{(1)} ( x )

Given a sparsity pattern for :math:`R`,
``rev_jac_sparsity`` computes a sparsity pattern for :math:`J(x)`.

.. meta::
   :keywords: x

.. index:: x

.. _cpp_jac_sparsity@x:

x
*
Note that a sparsity pattern for :math:`J(x)` corresponds to the
operation sequence stored in *f* and does not depend on
the argument *x* .

.. meta::
   :keywords: f

.. index:: f

.. _cpp_jac_sparsity@f:

f
*
The object *f* has prototype

| |tab| ``d_fun`` *f*

The object *f* is not ``const`` when using
``for_jac_sparsity`` .
After a call to ``for_jac_sparsity`` , a sparsity pattern
for each of the variables in the operation sequence
is held in *f* for possible later use during
reverse Hessian sparsity calculations.

.. meta::
   :keywords: pattern_in

.. index:: pattern_in

.. _cpp_jac_sparsity@pattern_in:

pattern_in
**********
The argument *pattern_in* has prototype

| |tab| ``const sparse_rc&`` *pattern_in*

see :ref:`cpp_sparse_rc-name`.
This is a sparsity pattern for :math:`R`.

.. meta::
   :keywords: pattern_out

.. index:: pattern_out

.. _cpp_jac_sparsity@pattern_out:

pattern_out
***********
This argument has prototype

| |tab| ``sparse_rc<``\ *SizeVector*\ ``>&`` *pattern_out*

This input value of *pattern_out* does not matter.
Upon return *pattern_out* is a sparsity pattern for
:math:`J(x)`.

.. meta::
   :keywords: sparsity, for, entire, jacobian

.. index:: sparsity, for, entire, jacobian

.. _cpp_jac_sparsity@Sparsity for Entire Jacobian:

Sparsity for Entire Jacobian
****************************
Suppose that :math:`R` is the identity matrix.
In this case, *pattern_out* is a sparsity pattern for
:math:`F^{(1)} ( x )`.

.. meta::
   :keywords: example

.. index:: example

.. _cpp_jac_sparsity@Example:

Example
*******
:ref:`c++<sparse_jac_pattern_xam_cpp-name>`

.. toctree::
   :maxdepth: 1
   :hidden:

   sparse_jac_pattern_xam_cpp
