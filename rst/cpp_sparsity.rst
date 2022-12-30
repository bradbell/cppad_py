.. _cpp_sparsity-name:

!!!!!!!!!!!!
cpp_sparsity
!!!!!!!!!!!!

.. raw:: html

   <a href="_sources/cpp_sparsity.rst.txt">View page source</a>

.. meta::
   :keywords: cpp_sparsity, hessian, sparsity, patterns

.. index:: cpp_sparsity, hessian, sparsity, patterns

.. _cpp_sparsity-title:

Hessian Sparsity Patterns
#########################

.. meta::
   :keywords: syntax

.. index:: syntax

.. _cpp_sparsity@Syntax:

Syntax
******

| *f*\ ``.for_hes_sparsity`` ( *select_domain* , *select_range* , *pattern_out* )
| *f*\ ``.rev_hes_sparsity`` ( *select_domain* , *select_range* , *pattern_out* )

.. meta::
   :keywords: purpose

.. index:: purpose

.. _cpp_sparsity@Purpose:

Purpose
*******
We use :math:`F : \B{R}^n \rightarrow \B{R}^m` to denote the
function corresponding to the operation sequence stored in *f* .
Fix a diagonal matrix :math:`D \in \B{R}^{n \times n}`, fix a vector
:math:`r \in \B{R}^m`, and define

.. math::

   H(x) = D (r^\R{T} F)^{(2)} ( x ) D

Given a sparsity pattern for :math:`D` and :math:`r`,
these routines compute a sparsity pattern for :math:`H(x)`.

.. meta::
   :keywords: x

.. index:: x

.. _cpp_sparsity@x:

x
*
Note that a sparsity pattern for :math:`H(x)` corresponds to the
operation sequence stored in *f* and does not depend on
the argument *x* .

.. meta::
   :keywords: f

.. index:: f

.. _cpp_sparsity@f:

f
*
The object *f* has prototype

| |tab| ``d_fun`` *f*

.. meta::
   :keywords: select_domain

.. index:: select_domain

.. _cpp_sparsity@select_domain:

select_domain
*************
The argument *select_domain* has prototype

| |tab| ``const vec_bool&`` *select_domain*

It has size *n* and is a sparsity pattern for the diagonal of
:math:`D`; i.e., *select_domain* [ *j* ] is true if and only if
:math:`D_{j,j}` is possibly non-zero.

.. meta::
   :keywords: select_range

.. index:: select_range

.. _cpp_sparsity@select_range:

select_range
************
The argument *select_range* has prototype

| |tab| ``const vec_bool&`` *select_range*

It has size *m* and is a sparsity pattern for the vector
:math:`r`; i.e., *select_range* [ *i* ] is true if and only if
:math:`r_i` is possibly non-zero.

.. meta::
   :keywords: pattern_out

.. index:: pattern_out

.. _cpp_sparsity@pattern_out:

pattern_out
***********
This argument has prototype

| |tab| ``sparse_rc<``\ *SizeVector*\ ``>&`` *pattern_out*

This input value of *pattern_out* does not matter.
Upon return *pattern_out* is a sparsity pattern for
:math:`J(x)`.

.. meta::
   :keywords: sparsity, for, component, wise, hessian

.. index:: sparsity, for, component, wise, hessian

.. _cpp_sparsity@Sparsity for Component Wise Hessian:

Sparsity for Component Wise Hessian
***********************************
Suppose that :math:`D` is the identity matrix,
and only the *i*-th component of *r* is possibly non-zero.
In this case, *pattern_out* is a sparsity pattern for
:math:`F_i^{(2)} ( x )`.

.. meta::
   :keywords: example

.. index:: example

.. _cpp_sparsity@Example:

Example
*******
:ref:`c++<sparse_hes_pattern_xam_cpp-name>`

.. toctree::
   :maxdepth: 1
   :hidden:

   sparse_hes_pattern_xam_cpp
