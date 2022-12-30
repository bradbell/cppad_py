.. _py_jac_sparsity-name:

!!!!!!!!!!!!!!!
py_jac_sparsity
!!!!!!!!!!!!!!!

.. raw:: html

   <a href="_sources/py_jac_sparsity.rst.txt">View page source</a>

.. meta::
   :keywords: py_jac_sparsity, jacobian, sparsity, patterns

.. index:: py_jac_sparsity, jacobian, sparsity, patterns

.. _py_jac_sparsity-title:

Jacobian Sparsity Patterns
##########################

.. meta::
   :keywords: syntax

.. index:: syntax

.. _py_jac_sparsity@Syntax:

Syntax
******

| *f*\ ``.for_jac_sparsity`` ( *pattern_in* , *pattern_out* )
| *f*\ ``.rev_jac_sparsity`` ( *pattern_in* , *pattern_out* )

.. meta::
   :keywords: purpose

.. index:: purpose

.. _py_jac_sparsity@Purpose:

Purpose
*******
We use :math:`F : \B{R}^n \rightarrow \B{R}^m` to denote the
function corresponding to the operation sequence stored in *f* .

.. meta::
   :keywords: for_jac_sparsity

.. index:: for_jac_sparsity

.. _py_jac_sparsity@Purpose@for_jac_sparsity:

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

.. _py_jac_sparsity@Purpose@rev_jac_sparsity:

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

.. _py_jac_sparsity@x:

x
*
Note that a sparsity pattern for :math:`J(x)` corresponds to the
operation sequence stored in *f* and does not depend on
the argument *x* .

.. meta::
   :keywords: f

.. index:: f

.. _py_jac_sparsity@f:

f
*
This object must have been returned by a previous call to the python
:ref:`d_fun<py_fun_ctor-name>` constructor.
The object *f* is not constant when using
``for_jac_sparsity`` .
After a call to ``for_jac_sparsity`` , a sparsity pattern
for each of the variables in the operation sequence
is held in *f* for possible later use during
reverse Hessian sparsity calculations.

.. meta::
   :keywords: pattern_in

.. index:: pattern_in

.. _py_jac_sparsity@pattern_in:

pattern_in
**********
This argument must have be a :ref:`pattern<py_sparse_rc@pattern>`
returned by the ``sparse_rc`` constructor.
It specifies the sparsity pattern for :math:`R`.

.. meta::
   :keywords: pattern_out

.. index:: pattern_out

.. _py_jac_sparsity@pattern_out:

pattern_out
***********
This argument must have be a :ref:`pattern<py_sparse_rc@pattern>`
returned by the ``sparse_rc`` constructor.
This input value of *pattern_out* does not matter.
Upon return *pattern_out* is a sparsity pattern for
:math:`J(x)`.

.. meta::
   :keywords: sparsity, for, entire, jacobian

.. index:: sparsity, for, entire, jacobian

.. _py_jac_sparsity@Sparsity for Entire Jacobian:

Sparsity for Entire Jacobian
****************************
Suppose that :math:`R` is the identity matrix.
In this case, *pattern_out* is a sparsity pattern for
:math:`F^{(1)} ( x )`.

.. meta::
   :keywords: example

.. index:: example

.. _py_jac_sparsity@Example:

Example
*******
:ref:`python<sparse_jac_pattern_xam_py-name>`

.. toctree::
   :maxdepth: 1
   :hidden:

   sparse_jac_pattern_xam_py
