.. _py_hes_sparsity-name:

!!!!!!!!!!!!!!!
py_hes_sparsity
!!!!!!!!!!!!!!!

.. raw:: html

   <a href="_sources/py_hes_sparsity.rst.txt">View page source</a>

.. meta::
   :keywords: py_hes_sparsity, hessian, sparsity, patterns

.. index:: py_hes_sparsity, hessian, sparsity, patterns

.. _py_hes_sparsity-title:

Hessian Sparsity Patterns
#########################

.. meta::
   :keywords: syntax

.. index:: syntax

.. _py_hes_sparsity@Syntax:

Syntax
******

| *f*\ ``.for_hes_sparsity`` ( *select_domain* , *select_range* , *pattern_out* )

*f*\ ``.rev_hes_sparsity`` ( *select_domain* , *select_range* , *pattern_out* )

.. meta::
   :keywords: purpose

.. index:: purpose

.. _py_hes_sparsity@Purpose:

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

.. _py_hes_sparsity@x:

x
*
Note that a sparsity pattern for :math:`H(x)` corresponds to the
operation sequence stored in *f* and does not depend on
the argument *x* .

.. meta::
   :keywords: f

.. index:: f

.. _py_hes_sparsity@f:

f
*
This object must have been returned by a previous call to the python
:ref:`d_fun<py_fun_ctor-name>` constructor.

.. meta::
   :keywords: select_domain

.. index:: select_domain

.. _py_hes_sparsity@select_domain:

select_domain
*************
The argument is a numpy vector with ``bool`` elements.
It has size *n* and is a sparsity pattern for the diagonal of
:math:`D`; i.e., *select_domain* [ *j* ] is true if and only if
:math:`D_{j,j}` is possibly non-zero.

.. meta::
   :keywords: select_range

.. index:: select_range

.. _py_hes_sparsity@select_range:

select_range
************
The argument is a numpy vector with ``bool`` elements.
It has size *m* and is a sparsity pattern for the vector
:math:`r`; i.e., *select_range* [ *i* ] is true if and only if
:math:`r_i` is possibly non-zero.

.. meta::
   :keywords: pattern_out

.. index:: pattern_out

.. _py_hes_sparsity@pattern_out:

pattern_out
***********
This argument must have be a :ref:`pattern<py_sparse_rc@pattern>`
returned by the ``sparse_rc`` constructor.
This input value of *pattern_out* does not matter.
Upon return *pattern_out* is a sparsity pattern for
:math:`H(x)`.

.. meta::
   :keywords: sparsity, for, component, wise, hessian

.. index:: sparsity, for, component, wise, hessian

.. _py_hes_sparsity@Sparsity for Component Wise Hessian:

Sparsity for Component Wise Hessian
***********************************
Suppose that :math:`D` is the identity matrix,
and only the *i*-th component of *r* is possibly non-zero.
In this case, *pattern_out* is a sparsity pattern for
:math:`F_i^{(2)} ( x )`.

.. meta::
   :keywords: example

.. index:: example

.. _py_hes_sparsity@Example:

Example
*******
:ref:`python<sparse_hes_pattern_xam_py-name>`

.. toctree::
   :maxdepth: 1
   :hidden:

   sparse_hes_pattern_xam_py
