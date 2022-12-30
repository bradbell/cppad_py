.. _cpp_sparse_rcv-name:

!!!!!!!!!!!!!!
cpp_sparse_rcv
!!!!!!!!!!!!!!

.. raw:: html

   <a href="_sources/cpp_sparse_rcv.rst.txt">View page source</a>

.. meta::
   :keywords: cpp_sparse_rcv, sparse, matrices

.. index:: cpp_sparse_rcv, sparse, matrices

.. _cpp_sparse_rcv-title:

Sparse Matrices
###############

.. meta::
   :keywords: syntax

.. index:: syntax

.. _cpp_sparse_rcv@Syntax:

Syntax
******

| ``cppad_py::sparse_rcv`` *matrix* ( *pattern* )
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
   :keywords: pattern

.. index:: pattern

.. _cpp_sparse_rcv@pattern:

pattern
*******
This argument has prototype

| |tab| ``const sparse_rc&`` *pattern*

It specifies the number of rows, number of columns and
the possibly non-zero entries in the *matrix* .

.. meta::
   :keywords: matrix

.. index:: matrix

.. _cpp_sparse_rcv@matrix:

matrix
******
This is a sparse matrix object with the sparsity specified by *pattern* .
Only the *val* vector can be changed. All other values returned by
*matrix* are fixed during the constructor and constant there after.
The *val* vector is only changed by the constructor
and the ``set`` function.

.. meta::
   :keywords: nr

.. index:: nr

.. _cpp_sparse_rcv@nr:

nr
**
This return value has prototype

| |tab| ``int`` *nr*

and is the number of rows in the matrix.

.. meta::
   :keywords: nc

.. index:: nc

.. _cpp_sparse_rcv@nc:

nc
**
This return value has prototype

| |tab| ``int`` *nc*

and is the number of columns in the matrix.

.. meta::
   :keywords: nnz

.. index:: nnz

.. _cpp_sparse_rcv@nnz:

nnz
***
This return value has prototype

| |tab| ``int`` *nnz*

and is the number of possibly non-zero values in the matrix.

.. meta::
   :keywords: put

.. index:: put

.. _cpp_sparse_rcv@put:

put
***
This function sets the value

| |tab| *val* [ *k* ] = *v*

(The name ``set`` is used by Cppad, but not used here,
because ``set`` it is a built-in name in Python.)

.. meta::
   :keywords: k

.. index:: k

.. _cpp_sparse_rcv@put@k:

k
=
This argument has type

| |tab| ``int`` *k*

and must be non-negative and less than *nnz* .

.. meta::
   :keywords: v

.. index:: v

.. _cpp_sparse_rcv@put@v:

v
=
This argument has type

| |tab| ``double`` *v*

It specifies the value assigned to *val* [ *k* ] .

.. meta::
   :keywords: row

.. index:: row

.. _cpp_sparse_rcv@row:

row
***
This result has type

| |tab| ``vec_int`` *row*

and its size is *nnz* .
For *k* = 0, ... , *nnz* -1 ,
*row* [ *k* ] is the row index for the *k*-th possibly non-zero
entry in the matrix.

.. meta::
   :keywords: col

.. index:: col

.. _cpp_sparse_rcv@col:

col
***
This result has type

| |tab| ``vec_int`` *col*

and its size is *nnz* .
For *k* = 0, ... , *nnz* -1 ,
*col* [ *k* ] is the column index for the *k*-th possibly non-zero
entry in the matrix.

.. meta::
   :keywords: val

.. index:: val

.. _cpp_sparse_rcv@val:

val
***
This result has type

| |tab| ``vec_double`` *val*

and its size is *nnz* .
For *k* = 0, ... , *nnz* -1 ,
*val* [ *k* ] is the value of the *k*-th possibly non-zero
entry in the matrix (the value may be zero).

.. meta::
   :keywords: row_major

.. index:: row_major

.. _cpp_sparse_rcv@row_major:

row_major
*********
This vector has prototype

| |tab| ``vec_int`` *row_major*

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

.. _cpp_sparse_rcv@col_major:

col_major
*********
This vector has prototype

| |tab| ``vec_int`` *col_major*

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

.. _cpp_sparse_rcv@Example:

Example
*******
:ref:`sparse_rcv_xam_cpp-name`

.. toctree::
   :maxdepth: 1
   :hidden:

   sparse_rcv_xam_cpp
