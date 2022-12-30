.. _py_sparse_rcv-name:

!!!!!!!!!!!!!
py_sparse_rcv
!!!!!!!!!!!!!

.. raw:: html

   <a href="_sources/py_sparse_rcv.rst.txt">View page source</a>

.. meta::
   :keywords: py_sparse_rcv, sparse, matrices

.. index:: py_sparse_rcv, sparse, matrices

.. _py_sparse_rcv-title:

Sparse Matrices
###############

.. meta::
   :keywords: syntax

.. index:: syntax

.. _py_sparse_rcv@Syntax:

Syntax
******

| *matrix* =  ``cppad_py.sparse_rcv()``
| *matrix*.pat ( *pattern* )
| *nr* = *matrix*\ ``.nr()``
| *nc* = *matrix*\ ``.nc()``
| *nnz* =  *matrix*\ ``.nnz()``
| *matrix*\ ``.put`` ( *k* , *v* )
| *row* = *matrix*\ ``.row()``
| *col* = *matrix*\ ``.col()``
| *val* = *matrix*\ ``.val()``
| *row_major* = *matrix*\ ``.row_major()``
| *col_major* = *matrix*\ ``.col_major()``

.. meta::
   :keywords: matrix

.. index:: matrix

.. _py_sparse_rcv@matrix:

matrix
******
This result is used ot hold a sparse matrix.
It has zero row *nr*, zero columns *nc*, and zero non-zero values *nnz*
when it is first created.
It is constant except for the ``pat`` and ``put`` operations.

.. meta::
   :keywords: pat

.. index:: pat

.. _py_sparse_rcv@pat:

pat
***
This changes the sparsity pattern for the matrix to *pattern*.
The argument *pattern* is a ``cppad_py.sparse_rc`` object,
it is not changed, and it specifies *nr*, *nc*, *nnz*, *row*, and *col*.
The values in the *val* vector are unspecified after this operation.
The ``put`` operation can be used to set these values.

.. meta::
   :keywords: nr

.. index:: nr

.. _py_sparse_rcv@nr:

nr
**
This return value is an ``int``
and is the number of rows in the matrix.

.. meta::
   :keywords: nc

.. index:: nc

.. _py_sparse_rcv@nc:

nc
**
This return value is an ``int``
and is the number of columns in the matrix.

.. meta::
   :keywords: nnz

.. index:: nnz

.. _py_sparse_rcv@nnz:

nnz
***
This return value is an ``int``
and is the number of possibly non-zero values in the matrix.

.. meta::
   :keywords: put

.. index:: put

.. _py_sparse_rcv@put:

put
***
This function sets the value

| |tab| *val* [ *k* ] = *v*

(The name ``set`` is used by Cppad, but not used here,
because ``set`` it is a built-in name in Python.)

.. meta::
   :keywords: k

.. index:: k

.. _py_sparse_rcv@put@k:

k
=
This is a non-negative ``int`` and must be less than *nnz* .

.. meta::
   :keywords: v

.. index:: v

.. _py_sparse_rcv@put@v:

v
=
This argument has type ``float`` and
specifies the value assigned to *val* [ *k* ] .

.. meta::
   :keywords: row

.. index:: row

.. _py_sparse_rcv@row:

row
***
This result is a numpy vector with ``int`` elements
and its size is *nnz* .
For *k* = 0, ... , *nnz* -1 ,
*row* [ *k* ] is the row index for the *k*-th possibly non-zero
entry in the matrix.

.. meta::
   :keywords: col

.. index:: col

.. _py_sparse_rcv@col:

col
***
This result is a numpy vector with ``int`` elements
and its size is *nnz* .
For *k* = 0, ... , *nnz* -1 ,
*col* [ *k* ] is the column index for the *k*-th possibly non-zero
entry in the matrix.

.. meta::
   :keywords: val

.. index:: val

.. _py_sparse_rcv@val:

val
***
This result is a numpy vector with ``float`` elements
and its size is *nnz* .
For *k* = 0, ... , *nnz* -1 ,
*val* [ *k* ] is the value of the *k*-th possibly non-zero
entry in the matrix (the value may be zero).

.. meta::
   :keywords: row_major

.. index:: row_major

.. _py_sparse_rcv@row_major:

row_major
*********
This result is a numpy vector with ``int`` elements
and its size *nnz* .
It sorts the sparsity pattern in row-major order.
To be specific,

| |tab| *col* [ *row_major* [ *k* ] ] <= *col* [ *row_major* [ *k* +1] ]

and if *col* [ *row_major* [ *k* ] ] == *col* [ *row_major* [ *k* +1] ] ,

| |tab| *row* [ *row_major* [ *k* ] ] < *row* [ *row_major* [ *k* +1] ]

This routine generates an assert if there are two entries with the same
row and column values (if ``NDEBUG`` is not defined).

.. meta::
   :keywords: col_major

.. index:: col_major

.. _py_sparse_rcv@col_major:

col_major
*********
This result is a numpy vector with ``int`` elements
and its size *nnz* .
It sorts the sparsity pattern in column-major order.
To be specific,

| |tab| *row* [ *col_major* [ *k* ] ] <= *row* [ *col_major* [ *k* +1] ]

and if *row* [ *col_major* [ *k* ] ] == *row* [ *col_major* [ *k* +1] ] ,

| |tab| *col* [ *col_major* [ *k* ] ] < *col* [ *col_major* [ *k* +1] ]

This routine generates an assert if there are two entries with the same
row and column values (if ``NDEBUG`` is not defined).

.. meta::
   :keywords: example

.. index:: example

.. _py_sparse_rcv@Example:

Example
*******
:ref:`sparse_rcv_xam_py-name`

.. toctree::
   :maxdepth: 1
   :hidden:

   sparse_rcv_xam_py
