.. _py_sparse_hes-name:

!!!!!!!!!!!!!
py_sparse_hes
!!!!!!!!!!!!!

.. raw:: html

   <a href="_sources/py_sparse_hes.rst.txt">View page source</a>

.. meta::
   :keywords: py_sparse_hes, computing, sparse, hessians

.. index:: py_sparse_hes, computing, sparse, hessians

.. _py_sparse_hes-title:

Computing Sparse Hessians
#########################

.. meta::
   :keywords: syntax

.. index:: syntax

.. _py_sparse_hes@Syntax:

Syntax
******

| *work* =  ``cppad_py.sparse_hes_work`` ()
| *n_sweep* = *f*\ ``.sparse_hes`` ( *subset* , *x* , *r* , *pattern* , *work* )

.. meta::
   :keywords: purpose

.. index:: purpose

.. _py_sparse_hes@Purpose:

Purpose
*******
We use :math:`F : \B{R}^n \rightarrow \B{R}^m` to denote the
function corresponding to *f* .
Given a vector :math:`r \in \B{R}^m`, define

.. math::

   H(x) = (r^\R{T} F)^{(2)} ( x )

This routine takes advantage of sparsity when computing elements
of the Hessian :math:`H(x)`.

.. meta::
   :keywords: f

.. index:: f

.. _py_sparse_hes@f:

f
*
This object must have been returned by a previous call to the python
:ref:`d_fun<py_fun_ctor-name>` constructor.
Note that the Taylor coefficients stored in *f* are affected
by this operation; see
:ref:`uses_forward<py_sparse_hes@Uses Forward>` below.

.. meta::
   :keywords: subset

.. index:: subset

.. _py_sparse_hes@subset:

subset
******
This argument must have be a :ref:`matrix<py_sparse_rcv@matrix>`
returned by the ``sparse_rcv`` constructor.
Its row size and column size is *n* ; i.e.,
*subset*\ ``.nr`` () == *n* and *subset*\ ``.nc`` () == *n* .
It specifies which elements of the Hessian are computed.
The input value of its value vector
*subset*\ ``.val`` () does not matter.
Upon return it contains the value of the corresponding elements
of the Jacobian.
All of the row, column pairs in *subset* must also appear in
*pattern* ; i.e., they must be possibly non-zero.

.. meta::
   :keywords: x

.. index:: x

.. _py_sparse_hes@x:

x
*
This argument is a numpy vector with ``float`` elements
and size *n* .
It specifies the point at which to evaluate the Hessian :math:`H(x)`.

.. meta::
   :keywords: r

.. index:: r

.. _py_sparse_hes@r:

r
*
This argument is a numpy vector with ``float`` elements
and size *m* .
It specifies the multiplier for each component of :math:`F(x)`;
i.e., :math:`r_i` is the multiplier for :math:`F_i (x)`.

.. meta::
   :keywords: pattern

.. index:: pattern

.. _py_sparse_hes@pattern:

pattern
*******
This argument must have be a :ref:`pattern<py_sparse_rc@pattern>`
returned by the ``sparse_rc`` constructor.
Its row size and column sizes are *n* ; i.e.,
*pattern*\ ``.nr`` () == *n* and *pattern*\ ``.nc`` () == *n* .
It is a sparsity pattern for the Hessian :math:`H(x)`.
This argument is not used (and need not satisfy any conditions),
when :ref:`work<py_sparse_hes@work>` is non-empty.

.. meta::
   :keywords: work

.. index:: work

.. _py_sparse_hes@work:

work
****
This argument must have been constructed by the call

| |tab| *work* =  ``cppad_py.sparse_hes_work`` ()

We refer to its initial value,
and its value after *work*\ ``.clear`` () , as empty.
If it is empty, information is stored in *work* .
This can be used to reduce computation when
a future call is for the same object *f* ,
and the same subset of the Hessian.
If either of these values change, use *work*\ ``.clear`` () to
empty this structure.

.. meta::
   :keywords: n_sweep

.. index:: n_sweep

.. _py_sparse_hes@n_sweep:

n_sweep
*******
The return value *n_sweep* has prototype

| |tab| ``int`` *n_sweep*

It is the number of first order forward sweeps
used to compute the requested Hessian values.
Each first forward sweep is followed by a second order reverse sweep
so it is also the number of reverse sweeps.
This is proportional to the total computational work,
not counting the zero order forward sweep,
or combining multiple columns and rows into a single sweep.

.. meta::
   :keywords: uses, forward

.. index:: uses, forward

.. _py_sparse_hes@Uses Forward:

Uses Forward
************
After each call to :ref:`py_fun_forward-name`,
the object *f* contains the corresponding Taylor coefficients
for all the variables in the operation sequence..
After a call to ``sparse_hes``
the zero order coefficients correspond to

| |tab| *f*\ ``.forward(0`` , *x* )

All the other forward mode coefficients are unspecified.

.. meta::
   :keywords: example

.. index:: example

.. _py_sparse_hes@Example:

Example
*******
:ref:`sparse_hes_xam_py-name`

.. toctree::
   :maxdepth: 1
   :hidden:

   sparse_hes_xam_py
