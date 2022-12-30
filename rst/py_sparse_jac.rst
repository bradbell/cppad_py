.. _py_sparse_jac-name:

!!!!!!!!!!!!!
py_sparse_jac
!!!!!!!!!!!!!

.. raw:: html

   <a href="_sources/py_sparse_jac.rst.txt">View page source</a>

.. meta::
   :keywords: py_sparse_jac, computing, sparse, jacobians

.. index:: py_sparse_jac, computing, sparse, jacobians

.. _py_sparse_jac-title:

Computing Sparse Jacobians
##########################

.. meta::
   :keywords: syntax

.. index:: syntax

.. _py_sparse_jac@Syntax:

Syntax
******

| *work* =  ``cppad_py.sparse_jac_work`` ()
| *n_sweep* = *f*\ ``.sparse_jac_for`` ( *subset* , *x* , *pattern* , *work* )
| *n_sweep* = *f*\ ``.sparse_jac_rev`` ( *subset* , *x* , *pattern* , *work* )

.. meta::
   :keywords: purpose

.. index:: purpose

.. _py_sparse_jac@Purpose:

Purpose
*******
We use :math:`F : \B{R}^n \rightarrow \B{R}^m` to denote the
function corresponding to *f* .
The syntax above takes advantage of sparsity when computing the Jacobian

.. math::

   J(x) = F^{(1)} (x)

In the sparse case, this should be faster and take less memory than
:ref:`py_fun_jacobian-name`.
We use the notation :math:`J_{i,j} (x)` to denote the partial of
:math:`F_i (x)` with respect to :math:`x_j`.

.. meta::
   :keywords: sparse_jac_for

.. index:: sparse_jac_for

.. _py_sparse_jac@sparse_jac_for:

sparse_jac_for
**************
This function uses first order forward mode sweeps :ref:`py_fun_forward-name`
to compute multiple columns of the Jacobian at the same time.

.. meta::
   :keywords: sparse_jac_rev

.. index:: sparse_jac_rev

.. _py_sparse_jac@sparse_jac_rev:

sparse_jac_rev
**************
This function uses first order reverse mode sweeps :ref:`py_fun_reverse-name`
to compute multiple rows of the Jacobian at the same time.

.. meta::
   :keywords: f

.. index:: f

.. _py_sparse_jac@f:

f
*
This object must have been returned by a previous call to the python
:ref:`d_fun<py_fun_ctor-name>` constructor.
Note that the Taylor coefficients stored in *f* are affected
by this operation; see
:ref:`uses_forward<py_sparse_jac@Uses Forward>` below.

.. meta::
   :keywords: subset

.. index:: subset

.. _py_sparse_jac@subset:

subset
******
This argument must have be a :ref:`matrix<py_sparse_rcv@matrix>`
returned by the ``sparse_rcv`` constructor.
Its row size is *subset*\ ``.nr`` () == *m* ,
and its column size is *subset*\ ``.nc`` () == *n* .
It specifies which elements of the Jacobian are computed.
The input value of its value vector
*subset*\ ``.val`` () does not matter.
Upon return it contains the value of the corresponding elements
of the Jacobian.
All of the row, column pairs in *subset* must also appear in
*pattern* ; i.e., they must be possibly non-zero.

.. meta::
   :keywords: x

.. index:: x

.. _py_sparse_jac@x:

x
*
This argument is a numpy vector with ``float`` elements
and size *n* .
It specifies the point at which to evaluate the Jacobian :math:`J(x)`.

.. meta::
   :keywords: pattern

.. index:: pattern

.. _py_sparse_jac@pattern:

pattern
*******
This argument must have be a :ref:`pattern<py_sparse_rc@pattern>`
returned by the ``sparse_rc`` constructor.
Its row size is *pattern*\ ``.nr`` () == *m* ,
and its column size is *pattern*\ ``.nc`` () == *n* .
It is a sparsity pattern for the Jacobian :math:`J(x)`.
This argument is not used (and need not satisfy any conditions),
when :ref:`work<py_sparse_jac@work>` is non-empty.

.. meta::
   :keywords: work

.. index:: work

.. _py_sparse_jac@work:

work
****
This argument must have been constructed by the call

| |tab| *work* =  ``cppad_py.sparse_jac_work`` ()

We refer to its initial value,
and its value after *work*\ ``.clear`` () , as empty.
If it is empty, information is stored in *work* .
This can be used to reduce computation when
a future call is for the same object *f* ,
the same member function ``sparse_jac_for`` or ``sparse_jac_rev`` ,
and the same subset of the Jacobian.
If any of these values change, use *work*\ ``.clear`` () to
empty this structure.

.. meta::
   :keywords: n_sweep

.. index:: n_sweep

.. _py_sparse_jac@n_sweep:

n_sweep
*******
This return value is and ``int`` .
If ``sparse_jac_for`` ( ``sparse_jac_rev`` ) is used,
*n_sweep* is the number of first order forward (reverse) sweeps
used to compute the requested Jacobian values.
This is proportional to the total computational work,
not counting the zero order forward sweep,
or combining multiple columns (rows) into a single sweep.

.. meta::
   :keywords: uses, forward

.. index:: uses, forward

.. _py_sparse_jac@Uses Forward:

Uses Forward
************
After each call to :ref:`py_fun_forward-name`,
the object *f* contains the corresponding Taylor coefficients
for all the variables in the operation sequence..
After a call to ``sparse_jac_forward`` or ``sparse_jac_rev`` ,
the zero order coefficients correspond to

| |tab| *f*\ ``.forward(0`` , *x* )

All the other forward mode coefficients are unspecified.

.. meta::
   :keywords: example

.. index:: example

.. _py_sparse_jac@Example:

Example
*******
:ref:`sparse_jac_xam_py-name`

.. toctree::
   :maxdepth: 1
   :hidden:

   sparse_jac_xam_py
