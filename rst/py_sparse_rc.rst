.. _py_sparse_rc-name:

!!!!!!!!!!!!
py_sparse_rc
!!!!!!!!!!!!

.. raw:: html

   <a href="_sources/py_sparse_rc.rst.txt">View page source</a>

.. meta::
   :keywords: py_sparse_rc, sparsity, patterns

.. index:: py_sparse_rc, sparsity, patterns

.. _py_sparse_rc-title:

Sparsity Patterns
#################

.. meta::
   :keywords: syntax

.. index:: syntax

.. _py_sparse_rc@Syntax:

Syntax
******

| *pattern* =  ``cppad_py.sparse_rc()``
| *pattern*\ ``.resize`` ( *nr* , *nc* , *nnz* )
| *nr* = *pattern*\ ``.nr()``
| *nc* = *pattern*\ ``.nc()``
| *nnz* = *pattern*\ ``.nnz()``
| *pattern*\ ``.put`` ( *k* , *r* , *c* )
| *row* = *pattern*\ ``.row()``
| *col* = *pattern*\ ``.col()``
| *row_major* = *pattern*\ ``.row_major()``
| *col_major* = *pattern*\ ``.col_major()``

.. meta::
   :keywords: pattern

.. index:: pattern

.. _py_sparse_rc@pattern:

pattern
*******
This result is used to hold a sparsity pattern for a matrix.
It has zero rows *nr*, zero columns *nc*, and zero non-zero values *nnz*
when it is first created.
It is constant
except during the ``resize`` and ``put`` operations.

.. meta::
   :keywords: nr

.. index:: nr

.. _py_sparse_rc@nr:

nr
**
This argument is a non-negative ``int``
and is the number of rows in the sparsity pattern.
The function ``nr()`` returns the value of
*nr* in the previous ``resize`` operation.

.. meta::
   :keywords: nc

.. index:: nc

.. _py_sparse_rc@nc:

nc
**
This argument is a non-negative ``int``
and is the number of columns in the sparsity pattern.
The function ``nc()`` returns the value of
*nc* in the previous ``resize`` operation.

.. meta::
   :keywords: nnz

.. index:: nnz

.. _py_sparse_rc@nnz:

nnz
***
This argument is a non-negative ``int``
and is the number of possibly non-zero
index pairs in the sparsity pattern.
The function ``nnz()`` returns the value of
*nnz* in the previous ``resize`` operation.

.. meta::
   :keywords: resize

.. index:: resize

.. _py_sparse_rc@resize:

resize
******
The current sparsity pattern is lost and a new one is started
with the specified parameters.
After each ``resize`` , the elements in the *row*
and *col* vectors should be assigned using ``put`` .

.. meta::
   :keywords: put

.. index:: put

.. _py_sparse_rc@put:

put
***
This function sets the values

| |tab| *row* [ *k* ] = *r*
| |tab| *col* [ *k* ] = *c*

(The name ``set`` is used by Cppad, but not used here,
because ``set`` it is a built-in name in Python.)

.. meta::
   :keywords: k

.. index:: k

.. _py_sparse_rc@put@k:

k
=
This argument is a non-negative ``int``
and must be less than *nnz* .

.. meta::
   :keywords: r

.. index:: r

.. _py_sparse_rc@put@r:

r
=
This argument is a non-negative ``int``
and must be less than *nr* .
It specifies the value assigned to *row* [ *k* ] .

.. meta::
   :keywords: c

.. index:: c

.. _py_sparse_rc@put@c:

c
=
This argument is a non-negative ``int``
and must be less than *nc* .
It specifies the value assigned to *col* [ *k* ] .

.. meta::
   :keywords: row

.. index:: row

.. _py_sparse_rc@row:

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

.. _py_sparse_rc@col:

col
***
This result is a numpy vector with ``int`` elements
and its size is *nnz* .
For *k* = 0, ... , *nnz* -1 ,
*col* [ *k* ] is the column index for the *k*-th possibly non-zero
entry in the matrix.

.. meta::
   :keywords: row_major

.. index:: row_major

.. _py_sparse_rc@row_major:

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

.. _py_sparse_rc@col_major:

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

.. _py_sparse_rc@Example:

Example
*******
:ref:`sparse_rc_xam_py-name`

.. toctree::
   :maxdepth: 1
   :hidden:

   sparse_rc_xam_py
