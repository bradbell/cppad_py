/* -----------------------------------------------------------------------------
           cppad_py: A C++ Object Library and Python Interface to Cppad
         Copyright (C) 2017-22 Bradley M. Bell (bradbell@seanet.com)
            This program is distributed under the terms of the
            GNU General Public License version 3.0 or later see
                      https://www.gnu.org/licenses/gpl-3.0.txt
----------------------------------------------------------------------------- */
# include <cppad/cppad.hpp>
# include <cppad/py/sparse.hpp>
# include <cppad/py/vector.hpp>
# include <cppad/py/fun.hpp>
# include <cppad/py/assert.hpp>

namespace cppad_py { // BEGIN_CPPAD_PY_NAMESPACE

/*
-------------------------------------------------------------------------------
{xrst_begin cpp_sparse_rc}
{xrst_spell
   cppad
   nnz
}


Sparsity Patterns
#################

Syntax
******

| ``cppad_py::sparse_rc`` pattern;
| *pattern*\ ``.resize`` ( *nr* , *nc* , *nnz* )
| *nr* = *pattern*\ ``.nr`` ()
| *nc* = *pattern*\ ``.nc`` ()
| *nnz* = *pattern*\ ``.nnz`` ()
| *pattern*\ ``.put`` ( *k* , *r* , *c* )
| *row* = *pattern*\ ``.row`` ()
| *col* = *pattern*\ ``.col`` ()
| *row_major* = *pattern*\ ``.row_major`` ()
| *col_major* = *pattern*\ ``.col_major`` ()

pattern
*******
This result has prototype

| |tab| ``sparse_rc`` *pattern*

It is used to hold a sparsity pattern for a matrix.
The sparsity *pattern* is ``const``
except during the ``resize`` and ``put`` operations.

nr
**
This argument has prototype

| |tab| ``int`` *nr*

is non-negative, and specifies
the number of rows in the sparsity pattern.
The function ``nr()`` returns the value of
*nr* in the previous ``resize`` operation.

nc
**
This argument has prototype

| |tab| ``int`` *nc*

is non-negative, and specifies
the number of columns in the sparsity pattern.
The function ``nc()`` returns the value of
*nc* in the previous ``resize`` operation.

nnz
***
This argument and result has prototype

| |tab| ``int`` *nnz*

It is the number of possibly non-zero
index pairs in the sparsity pattern.
The function ``nnz()`` returns the value of
*nnz* in the previous ``resize`` operation.

resize
******
The current sparsity pattern is lost and a new one is started
with the specified parameters.
After each ``resize`` , the elements in the *row*
and *col* vectors should be assigned using ``put`` .

put
***
This function sets the values

| |tab| *row* [ *k* ] = *r*
| |tab| *col* [ *k* ] = *c*

(The name ``set`` is used by Cppad, but not used here,
because ``set`` it is a built-in name in Python.)

k
=
This argument has type

| |tab| ``int`` *k*

is non-negative,
and must be less than *nnz* .

r
=
This argument has type

| |tab| ``int`` *r*

is non-negative, and must be less than *nr* .
It specifies the value assigned to *row* [ *k* ] and must

c
=
This argument has type

| |tab| ``int`` *c*

It specifies the value assigned to *col* [ *k* ] and must
be less than *nc* .

row
***
This result has type

| |tab| ``vec_int`` *row*

and its size is *nnz* .
For *k* = 0, ... , *nnz* -1 ,
*row* [ *k* ] is the row index for the *k*-th possibly non-zero
entry in the matrix.

col
***
This result has type

| |tab| ``vec_int`` *col*

and its size is *nnz* .
For *k* = 0, ... , *nnz* -1 ,
*col* [ *k* ] is the column index for the *k*-th possibly non-zero
entry in the matrix.

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

{xrst_toc_hidden
   example/cplusplus/sparse_rc_xam.cpp
}
Example
*******
:ref:`sparse_rc_xam_cpp`

{xrst_end cpp_sparse_rc}
*/
// ---------------------------------------------------------------------------
// public member function not in Swig interface (see %ignore ptr)
const CppAD::sparse_rc< std::vector<size_t> >* sparse_rc::ptr(void) const
{  return ptr_; }
CppAD::sparse_rc< std::vector<size_t> >* sparse_rc::ptr(void)
{  return ptr_; }
// ---------------------------------------------------------------------------
// sparse_rc ctor
sparse_rc::sparse_rc(void)
{  ptr_ = new CppAD::sparse_rc< std::vector<size_t> >();
   CPPAD_PY_ASSERT_UNKNOWN( ptr_ != CPPAD_NULL );
}
// destructor
sparse_rc::~sparse_rc(void)
{  // destructor should not throw exception
   assert( ptr_ != CPPAD_NULL );
   delete ptr_;
   ptr_ = CPPAD_NULL;
}
// resize
void sparse_rc::resize(int nr, int nc, int nnz)
{  CPPAD_PY_ASSERT_UNKNOWN( ptr_ != CPPAD_NULL );
   ptr_->resize(nr, nc, nnz);
   return;
}
// number of rows in matrix
int sparse_rc::nr(void) const
{  CPPAD_PY_ASSERT_UNKNOWN( ptr_ != CPPAD_NULL );
   return ptr_->nr();
}
// number of columns in matrix
int sparse_rc::nc(void) const
{  CPPAD_PY_ASSERT_UNKNOWN( ptr_ != CPPAD_NULL );
   return ptr_->nc();
}
// number of possibley non-zero elements in matrix
int sparse_rc::nnz(void) const
{  CPPAD_PY_ASSERT_UNKNOWN( ptr_ != CPPAD_NULL );
   return ptr_->nnz();
}
// set row and column for a possibly non-zero element
void sparse_rc::put(int k, int r, int c)
{  ptr_->set(k, r, c);
   return;
}
// row indices
std::vector<int> sparse_rc::row(void) const
{  size_t nnz = ptr_->nnz();
   std::vector<int> row(nnz);
   for(size_t k = 0; k < nnz; k++)
      row[k] = static_cast<int>( ptr_->row()[k] );
   return row;
}
// col indices
std::vector<int> sparse_rc::col(void) const
{  size_t nnz = ptr_->nnz();
   std::vector<int> col(nnz);
   for(size_t k = 0; k < nnz; k++)
      col[k] = static_cast<int>( ptr_->col()[k] );
   return col;
}
// row_major
std::vector<int> sparse_rc::row_major(void) const
{  size_t nnz = ptr_->nnz();
   std::vector<size_t> row_major = ptr_->row_major();
   std::vector<int> result(nnz);
   for(size_t k = 0; k < nnz; k++)
      result[k] = static_cast<int>( row_major[k] );
   return result;
}
// col_major
std::vector<int> sparse_rc::col_major(void) const
{  size_t nnz = ptr_->nnz();
   std::vector<size_t> col_major = ptr_->col_major();
   std::vector<int> result(nnz);
   for(size_t k = 0; k < nnz; k++)
      result[k] = static_cast<int>( col_major[k] );
   return result;
}
/*
-------------------------------------------------------------------------------
{xrst_begin cpp_sparse_rcv}
{xrst_spell
   cppad
   nnz
   rcv
}


Sparse Matrices
###############

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

pattern
*******
This argument has prototype

| |tab| ``const sparse_rc&`` *pattern*

It specifies the number of rows, number of columns and
the possibly non-zero entries in the *matrix* .

matrix
******
This is a sparse matrix object with the sparsity specified by *pattern* .
Only the *val* vector can be changed. All other values returned by
*matrix* are fixed during the constructor and constant there after.
The *val* vector is only changed by the constructor
and the ``set`` function.

nr
**
This return value has prototype

| |tab| ``int`` *nr*

and is the number of rows in the matrix.

nc
**
This return value has prototype

| |tab| ``int`` *nc*

and is the number of columns in the matrix.

nnz
***
This return value has prototype

| |tab| ``int`` *nnz*

and is the number of possibly non-zero values in the matrix.

put
***
This function sets the value

| |tab| *val* [ *k* ] = *v*

(The name ``set`` is used by Cppad, but not used here,
because ``set`` it is a built-in name in Python.)

k
=
This argument has type

| |tab| ``int`` *k*

and must be non-negative and less than *nnz* .

v
=
This argument has type

| |tab| ``double`` *v*

It specifies the value assigned to *val* [ *k* ] .

row
***
This result has type

| |tab| ``vec_int`` *row*

and its size is *nnz* .
For *k* = 0, ... , *nnz* -1 ,
*row* [ *k* ] is the row index for the *k*-th possibly non-zero
entry in the matrix.

col
***
This result has type

| |tab| ``vec_int`` *col*

and its size is *nnz* .
For *k* = 0, ... , *nnz* -1 ,
*col* [ *k* ] is the column index for the *k*-th possibly non-zero
entry in the matrix.

val
***
This result has type

| |tab| ``vec_double`` *val*

and its size is *nnz* .
For *k* = 0, ... , *nnz* -1 ,
*val* [ *k* ] is the value of the *k*-th possibly non-zero
entry in the matrix (the value may be zero).

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

{xrst_toc_hidden
   example/cplusplus/sparse_rcv_xam.cpp
}
Example
*******
:ref:`sparse_rcv_xam_cpp`

{xrst_end cpp_sparse_rcv}
*/
// ---------------------------------------------------------------------------
// public member functions not in Swig interface (see %ignore ptr)
CppAD::sparse_rcv< std::vector<size_t> , std::vector<double> >*
   sparse_rcv::ptr(void)
   {  return ptr_; }
// ---------------------------------------------------------------------------
// sparse_rcv ctor
sparse_rcv::sparse_rcv(const sparse_rc& pattern)
{  ptr_ = new CppAD::sparse_rcv< std::vector<size_t> , std::vector<double> >(
      *pattern.ptr()
   );
   CPPAD_PY_ASSERT_UNKNOWN( ptr_ != CPPAD_NULL );
}
sparse_rcv::sparse_rcv(const sparse_rcv& other)
{  typedef std::vector<size_t> size_vector;
   typedef std::vector<double> double_vector;
   size_t nr  = other.nr();
   size_t nc  = other.nc();
   size_t nnz = other.nnz();
   const std::vector<int>&    row = other.row();
   const std::vector<int>&    col = other.col();
   const std::vector<double>& val = other.val();
   CppAD::sparse_rc<size_vector> pattern(nr, nc, nnz);
   for(size_t k = 0; k < nnz; ++k)
      pattern.set(k, size_t(row[k]), size_t(col[k]) );
   ptr_ = new CppAD::sparse_rcv<size_vector, double_vector>( pattern );
   for(size_t k = 0; k < nnz; ++k)
      ptr_->set(k, val[k]);
}
// destructor
sparse_rcv::~sparse_rcv(void)
{  // destructor should not throw exception
   assert( ptr_ != CPPAD_NULL );
   delete ptr_;
   ptr_ = CPPAD_NULL;
}
// number of rows in matrix
int sparse_rcv::nr(void) const
{  CPPAD_PY_ASSERT_UNKNOWN( ptr_ != CPPAD_NULL );
   return ptr_->nr();
}
// number of columns in matrix
int sparse_rcv::nc(void) const
{  CPPAD_PY_ASSERT_UNKNOWN( ptr_ != CPPAD_NULL );
   return ptr_->nc();
}
// number of possibley non-zero elements in matrix
int sparse_rcv::nnz(void) const
{  CPPAD_PY_ASSERT_UNKNOWN( ptr_ != CPPAD_NULL );
   return ptr_->nnz();
}
// set row and column for a possibly non-zero element
void sparse_rcv::put(int k, double v)
{  ptr_->set(k, v);
   return;
}
// row indices
std::vector<int> sparse_rcv::row(void) const
{  size_t nnz = ptr_->nnz();
   std::vector<int> row(nnz);
   for(size_t k = 0; k < nnz; k++)
      row[k] = static_cast<int>( ptr_->row()[k] );
   return row;
}
// col indices
std::vector<int> sparse_rcv::col(void) const
{  size_t nnz = ptr_->nnz();
   std::vector<int> col(nnz);
   for(size_t k = 0; k < nnz; k++)
      col[k] = static_cast<int>( ptr_->col()[k] );
   return col;
}
// values
std::vector<double> sparse_rcv::val(void) const
{  return ptr_->val(); }
// row_major
std::vector<int> sparse_rcv::row_major(void) const
{  size_t nnz = ptr_->nnz();
   std::vector<size_t> row_major = ptr_->row_major();
   std::vector<int> result(nnz);
   for(size_t k = 0; k < nnz; k++)
      result[k] = static_cast<int>( row_major[k] );
   return result;
}
// col_major
std::vector<int> sparse_rcv::col_major(void) const
{  size_t nnz = ptr_->nnz();
   std::vector<size_t> col_major = ptr_->col_major();
   std::vector<int> result(nnz);
   for(size_t k = 0; k < nnz; k++)
      result[k] = static_cast<int>( col_major[k] );
   return result;
}
// ----------------------------------------------------------------------------
/*
{xrst_begin cpp_jac_sparsity}
{xrst_spell
   jac
}


Jacobian Sparsity Patterns
##########################

Syntax
******

| *f*\ ``.for_jac_sparsity`` ( *pattern_in* , *pattern_out* )
| *f*\ ``.rev_jac_sparsity`` ( *pattern_in* , *pattern_out* )

Purpose
*******
We use :math:`F : \B{R}^n \rightarrow \B{R}^m` to denote the
function corresponding to the operation sequence stored in *f* .

for_jac_sparsity
================
Fix :math:`R \in \B{R}^{n \times \ell}` and define the function

.. math::

   J(x) = F^{(1)} ( x ) * R

Given a sparsity pattern for :math:`R`,
``for_jac_sparsity`` computes a sparsity pattern for :math:`J(x)`.

rev_jac_sparsity
================
Fix :math:`R \in \B{R}^{\ell \times m}` and define the function

.. math::

   J(x) = R * F^{(1)} ( x )

Given a sparsity pattern for :math:`R`,
``rev_jac_sparsity`` computes a sparsity pattern for :math:`J(x)`.

x
*
Note that a sparsity pattern for :math:`J(x)` corresponds to the
operation sequence stored in *f* and does not depend on
the argument *x* .

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

pattern_in
**********
The argument *pattern_in* has prototype

| |tab| ``const sparse_rc&`` *pattern_in*

see :ref:`cpp_sparse_rc`.
This is a sparsity pattern for :math:`R`.

pattern_out
***********
This argument has prototype

| |tab| ``sparse_rc<``\ *SizeVector*\ ``>&`` *pattern_out*

This input value of *pattern_out* does not matter.
Upon return *pattern_out* is a sparsity pattern for
:math:`J(x)`.

Sparsity for Entire Jacobian
****************************
Suppose that :math:`R` is the identity matrix.
In this case, *pattern_out* is a sparsity pattern for
:math:`F^{(1)} ( x )`.

{xrst_toc_hidden
   example/cplusplus/sparse_jac_pattern_xam.cpp
}
Example
*******
:ref:`c++<sparse_jac_pattern_xam_cpp>`

{xrst_end cpp_jac_sparsity}
*/
void d_fun::for_jac_sparsity(
   const sparse_rc&  pattern_in    ,
   sparse_rc&        pattern_out   )
{  const CppAD::sparse_rc< std::vector<size_t> >* ptr_in  = pattern_in.ptr();
   CppAD::sparse_rc< std::vector<size_t> >*       ptr_out = pattern_out.ptr();
   bool transpose     = false;
   bool dependency    = false;
   bool internal_bool = false;
   ptr_->for_jac_sparsity(
      *ptr_in, transpose, dependency, internal_bool, *ptr_out
   );
   CPPAD_PY_ASSERT_UNKNOWN( ptr_->size_forward_bool() == 0 );
   CPPAD_PY_ASSERT_UNKNOWN( ptr_->size_forward_set() != 0 );
   // free stored forward pattern
   ptr_->size_forward_set(0);
   //
   return;
}
void d_fun::rev_jac_sparsity(
   const sparse_rc&  pattern_in    ,
   sparse_rc&        pattern_out   )
{  const CppAD::sparse_rc< std::vector<size_t> >* ptr_in  = pattern_in.ptr();
   CppAD::sparse_rc< std::vector<size_t> >*       ptr_out = pattern_out.ptr();
   bool transpose     = false;
   bool dependency    = false;
   bool internal_bool = false;
   ptr_->rev_jac_sparsity(
      *ptr_in, transpose, dependency, internal_bool, *ptr_out
   );
   return;
}
// ----------------------------------------------------------------------------
/*
{xrst_begin cpp_sparsity}
{xrst_spell
   bool
   hes
}


Hessian Sparsity Patterns
#########################

Syntax
******

| *f*\ ``.for_hes_sparsity`` ( *select_domain* , *select_range* , *pattern_out* )
| *f*\ ``.rev_hes_sparsity`` ( *select_domain* , *select_range* , *pattern_out* )

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

x
*
Note that a sparsity pattern for :math:`H(x)` corresponds to the
operation sequence stored in *f* and does not depend on
the argument *x* .

f
*
The object *f* has prototype

| |tab| ``d_fun`` *f*

select_domain
*************
The argument *select_domain* has prototype

| |tab| ``const vec_bool&`` *select_domain*

It has size *n* and is a sparsity pattern for the diagonal of
:math:`D`; i.e., *select_domain* [ *j* ] is true if and only if
:math:`D_{j,j}` is possibly non-zero.

select_range
************
The argument *select_range* has prototype

| |tab| ``const vec_bool&`` *select_range*

It has size *m* and is a sparsity pattern for the vector
:math:`r`; i.e., *select_range* [ *i* ] is true if and only if
:math:`r_i` is possibly non-zero.

pattern_out
***********
This argument has prototype

| |tab| ``sparse_rc<``\ *SizeVector*\ ``>&`` *pattern_out*

This input value of *pattern_out* does not matter.
Upon return *pattern_out* is a sparsity pattern for
:math:`J(x)`.

Sparsity for Component Wise Hessian
***********************************
Suppose that :math:`D` is the identity matrix,
and only the *i*-th component of *r* is possibly non-zero.
In this case, *pattern_out* is a sparsity pattern for
:math:`F_i^{(2)} ( x )`.

{xrst_toc_hidden
   example/cplusplus/sparse_hes_pattern_xam.cpp
}
Example
*******
:ref:`c++<sparse_hes_pattern_xam_cpp>`

{xrst_end cpp_sparsity}
*/
void d_fun::for_hes_sparsity(
   const std::vector<bool>& select_domain ,
   const std::vector<bool>& select_range  ,
   sparse_rc&               pattern_out   )
{  CppAD::sparse_rc< std::vector<size_t> >* ptr_out = pattern_out.ptr();
   bool internal_bool = false;
   ptr_->for_hes_sparsity(
      select_domain, select_range, internal_bool, *ptr_out
   );
   return;
}
void d_fun::rev_hes_sparsity(
   const std::vector<bool>& select_domain ,
   const std::vector<bool>& select_range  ,
   sparse_rc&               pattern_out   )
{  CPPAD_PY_ASSERT_KNOWN(
      select_domain.size() == ptr_->Domain() ,
      "rev_hes_sparsity: select_domain does not have proper size"
   );
   CPPAD_PY_ASSERT_KNOWN(
      select_range.size() == ptr_->Range() ,
      "rev_hes_sparsity: select_range does not have proper size"
   );
   typedef std::vector<size_t> vec_size_t;
   CppAD::sparse_rc<vec_size_t>* ptr_out = pattern_out.ptr();
   //
   // count the number of domain components present
   size_t n        = select_domain.size();
   size_t n_subset = 0;
   for(size_t j = 0; j < n; j++)
      if( select_domain[j] )
         ++n_subset;
   //
   // compute forward Jacobian sparsity with R a diagonal matrix
   // that only includes the specified subset of the domain vector
   CppAD::sparse_rc<vec_size_t> pattern_R;
   pattern_R.resize(n, n_subset, n_subset);
   vec_size_t subset2domain(n_subset);
   size_t ell = 0;
   for(size_t j = 0; j < n; j++)
   {  if( select_domain[j] )
      {  pattern_R.set(j, j, ell);
         subset2domain[ell] = j;
         ++ell;
      }
   }
   bool transpose     = false;
   bool dependency    = false;
   bool internal_bool = false;
   CppAD::sparse_rc<vec_size_t> pattern_jac;
   ptr_->for_jac_sparsity(
      pattern_R, transpose, dependency, internal_bool, pattern_jac
   );
   CPPAD_PY_ASSERT_UNKNOWN( ptr_->size_forward_bool() == 0 );
   CPPAD_PY_ASSERT_UNKNOWN( ptr_->size_forward_set() != 0 );
   //
   // CppAD's version of rev_hes_sparsity computes a sparsity pattern for
   // R^T (r^T * F)^{(2)} (x)
   CppAD::sparse_rc<vec_size_t> pattern_hes;
   ptr_->rev_hes_sparsity(
      select_range, transpose, internal_bool, pattern_hes
   );
   //
   // map row indices from subset used to speed calculation to
   // entire set of domain indices
   size_t nnz = pattern_hes.nnz();
   const vec_size_t& row( pattern_hes.row() );
   const vec_size_t& col( pattern_hes.col() );
   ptr_out->resize(n, n, nnz);
   for(size_t k = 0; k < nnz; k++)
      ptr_out->set(k, subset2domain[ row[k] ], col[k] );
   //
   // free memory used for forward sparstiy pattern
   ptr_->size_forward_set(0);
   //
   return;
}
/*
------------------------------------------------------------------------------
{xrst_begin cpp_sparse_jac}
{xrst_spell
   cppad
   jac
   rcv
}


Computing Sparse Jacobians
##########################

Syntax
******

| *work* =  ``cppad_py::sparse_jac_work`` ()
| *n_sweep* = *f*\ ``.sparse_jac_for`` ( *subset* , *x* , *pattern* , *work* )
| *n_sweep* = *f*\ ``.sparse_jac_rev`` ( *subset* , *x* , *pattern* , *work* )

Purpose
*******
We use :math:`F : \B{R}^n \rightarrow \B{R}^m` to denote the
function corresponding to *f* .
The syntax above takes advantage of sparsity when computing the Jacobian

.. math::

   J(x) = F^{(1)} (x)

In the sparse case, this should be faster and take less memory than
:ref:`cpp_fun_jacobian`.
We use the notation :math:`J_{i,j} (x)` to denote the partial of
:math:`F_i (x)` with respect to :math:`x_j`.

sparse_jac_for
**************
This function uses first order forward mode sweeps :ref:`cpp_fun_forward`
to compute multiple columns of the Jacobian at the same time.

sparse_jac_rev
**************
This function uses first order reverse mode sweeps :ref:`cpp_fun_reverse`
to compute multiple rows of the Jacobian at the same time.

f
*
This object has prototype

| |tab| ``ADFun`` *<Base>* *f*

Note that the Taylor coefficients stored in *f* are affected
by this operation; see
:ref:`uses_forward<cpp_sparse_jac@Uses Forward>` below.

subset
******
This argument has prototype

| |tab| ``sparse_rcv&`` *subset*

Its row size is *subset*\ ``.nr`` () == *m* ,
and its column size is *subset*\ ``.nc`` () == *n* .
It specifies which elements of the Jacobian are computed.
The input value of its value vector
*subset*\ ``.val`` () does not matter.
Upon return it contains the value of the corresponding elements
of the Jacobian.
All of the row, column pairs in *subset* must also appear in
*pattern* ; i.e., they must be possibly non-zero.

x
*
This argument has prototype

| |tab| ``const vec_double&`` *x*

and its size is *n* .
It specifies the point at which to evaluate the Jacobian :math:`J(x)`.

pattern
*******
This argument has prototype

| |tab| ``const sparse_rc&`` *pattern*

Its row size is *pattern*\ ``.nr`` () == *m* ,
and its column size is *pattern*\ ``.nc`` () == *n* .
It is a sparsity pattern for the Jacobian :math:`J(x)`.
This argument is not used (and need not satisfy any conditions),
when :ref:`work<cpp_sparse_jac@work>` is non-empty.

work
****
This argument has prototype

| |tab| ``sparse_jac_work&`` *work*

We refer to its initial value,
and its value after *work*\ ``.clear`` () , as empty.
If it is empty, information is stored in *work* .
This can be used to reduce computation when
a future call is for the same object *f* ,
the same member function ``sparse_jac_for`` or ``sparse_jac_rev`` ,
and the same subset of the Jacobian.
If any of these values change, use *work*\ ``.clear`` () to
empty this structure.

n_sweep
*******
The return value *n_sweep* has prototype

| |tab| ``int`` *n_sweep*

If ``sparse_jac_for`` ( ``sparse_jac_rev`` ) is used,
*n_sweep* is the number of first order forward (reverse) sweeps
used to compute the requested Jacobian values.
This is proportional to the total computational work,
not counting the zero order forward sweep,
or combining multiple columns (rows) into a single sweep.

Uses Forward
************
After each call to :ref:`cpp_fun_forward`,
the object *f* contains the corresponding Taylor coefficients
for all the variables in the operation sequence..
After a call to ``sparse_jac_forward`` or ``sparse_jac_rev`` ,
the zero order coefficients correspond to

| |tab| *f*\ ``.forward(0`` , *x* )

All the other forward mode coefficients are unspecified.

{xrst_toc_hidden
   example/cplusplus/sparse_jac_xam.cpp
}
Example
*******
:ref:`sparse_jac_xam_cpp`

{xrst_end cpp_sparse_jac}
*/
// ---------------------------------------------------------------------------
// public member function not in Swig interface (see %ignore ptr)
CppAD::sparse_jac_work* sparse_jac_work::ptr(void)
{  return ptr_; }
//
// sparse_jac_work ctor
sparse_jac_work::sparse_jac_work(void)
{  ptr_ = new CppAD::sparse_jac_work();
   CPPAD_PY_ASSERT_UNKNOWN( ptr_ != CPPAD_NULL );
}
// sparse_jac_work destructor
sparse_jac_work::~sparse_jac_work(void)
{  // destructor should not throw exception
   assert( ptr_ != CPPAD_NULL );
   delete ptr_;
   ptr_ = CPPAD_NULL;
}
// sparse_jac_work clear
void sparse_jac_work::clear(void)
{  CPPAD_PY_ASSERT_UNKNOWN( ptr_ != CPPAD_NULL );
   ptr_->clear();
   return;
}
// sparse_jac_for
int d_fun::sparse_jac_for(
   sparse_rcv&                subset   ,
   const std::vector<double>& x        ,
   const sparse_rc&           pattern  ,
   sparse_jac_work&           work     )
{  size_t      group_max = 1;
   std::string coloring  = "cppad";
   size_t n_sweep = ptr_->sparse_jac_for(
      group_max, x, *subset.ptr(), *pattern.ptr(), coloring, *work.ptr()
   );
   return int(n_sweep);
}
// sparse_jac_rev
int d_fun::sparse_jac_rev(
   sparse_rcv&                subset   ,
   const std::vector<double>& x        ,
   const sparse_rc&           pattern  ,
   sparse_jac_work&           work     )
{  std::string coloring  = "cppad";
   size_t n_sweep = ptr_->sparse_jac_rev(
      x, *subset.ptr(), *pattern.ptr(), coloring, *work.ptr()
   );
   return int(n_sweep);
}
/*
------------------------------------------------------------------------------
{xrst_begin cpp_sparse_hes}
{xrst_spell
   cppad
   hes
   multiplier
   rcv
}


Computing Sparse Hessians
#########################

Syntax
******

| *work* =  ``cppad_py::sparse_hes_work`` ()
| *n_sweep* = *f*\ ``.sparse_hes`` ( *subset* , *x* , *r* , *pattern* , *work* )

Purpose
*******
We use :math:`F : \B{R}^n \rightarrow \B{R}^m` to denote the
function corresponding to *f* .
Given a vector :math:`r \in \B{R}^m`, define

.. math::

   H(x) = (r^\R{T} F)^{(2)} ( x )

This routine takes advantage of sparsity when computing elements
of the Hessian :math:`H(x)`.

f
*
This object has prototype

| |tab| ``ADFun`` *<Base>* *f*

Note that the Taylor coefficients stored in *f* are affected
by this operation; see
:ref:`uses_forward<cpp_sparse_hes@Uses Forward>` below.

subset
******
This argument has prototype

| |tab| ``sparse_rcv&`` *subset*

Its row size and column size is *n* ; i.e.,
*subset*\ ``.nr`` () == *n* and *subset*\ ``.nc`` () == *n* .
It specifies which elements of the Hessian are computed.
The input value of its value vector
*subset*\ ``.val`` () does not matter.
Upon return it contains the value of the corresponding elements
of the Jacobian.
All of the row, column pairs in *subset* must also appear in
*pattern* ; i.e., they must be possibly non-zero.

x
*
This argument has prototype

| |tab| ``const vec_double&`` *x*

and its size is *n* .
It specifies the point at which to evaluate the Hessian :math:`H(x)`.

r
*
This argument has prototype

| |tab| ``const vec_double&`` *r*

and its size is *m* .
It specifies the multiplier for each component of :math:`F(x)`;
i.e., :math:`r_i` is the multiplier for :math:`F_i (x)`.

pattern
*******
This argument has prototype

| |tab| ``const sparse_rc&`` *pattern*

Its row size and column sizes are *n* ; i.e.,
*pattern*\ ``.nr`` () == *n* and *pattern*\ ``.nc`` () == *n* .
It is a sparsity pattern for the Hessian :math:`H(x)`.
This argument is not used (and need not satisfy any conditions),
when :ref:`work<cpp_sparse_hes@work>` is non-empty.

work
****
This argument has prototype

| |tab| ``sparse_hes_work&`` *work*

We refer to its initial value,
and its value after *work*\ ``.clear`` () , as empty.
If it is empty, information is stored in *work* .
This can be used to reduce computation when
a future call is for the same object *f* ,
and the same subset of the Hessian.
If either of these values change, use *work*\ ``.clear`` () to
empty this structure.

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

Uses Forward
************
After each call to :ref:`cpp_fun_forward`,
the object *f* contains the corresponding Taylor coefficients
for all the variables in the operation sequence..
After a call to ``sparse_hes``
the zero order coefficients correspond to

| |tab| *f*\ ``.forward(0`` , *x* )

All the other forward mode coefficients are unspecified.

{xrst_toc_hidden
   example/cplusplus/sparse_hes_xam.cpp
}
Example
*******
:ref:`sparse_hes_xam_cpp`

{xrst_end cpp_sparse_hes}
*/
// ---------------------------------------------------------------------------
// public member function not in Swig interface (see %ignore ptr)
CppAD::sparse_hes_work* sparse_hes_work::ptr(void)
{  return ptr_; }
//
// sparse_hes_work ctor
sparse_hes_work::sparse_hes_work(void)
{  ptr_ = new CppAD::sparse_hes_work();
   CPPAD_PY_ASSERT_UNKNOWN( ptr_ != CPPAD_NULL );
}
// sparse_hes_work destructor
sparse_hes_work::~sparse_hes_work(void)
{  // destructor should not throw exception
   assert( ptr_ != CPPAD_NULL );
   delete ptr_;
   ptr_ = CPPAD_NULL;
}
// sparse_hes_work clear
void sparse_hes_work::clear(void)
{  CPPAD_PY_ASSERT_UNKNOWN( ptr_ != CPPAD_NULL );
   ptr_->clear();
   return;
}
// sparse_hes
int d_fun::sparse_hes(
   sparse_rcv&                subset   ,
   const std::vector<double>& x        ,
   const std::vector<double>& r        ,
   const sparse_rc&           pattern  ,
   sparse_hes_work&           work     )
{  std::string coloring  = "cppad.symmetric";
   size_t n_sweep = ptr_->sparse_hes(
      x, r, *subset.ptr(), *pattern.ptr(), coloring, *work.ptr()
   );
   return int(n_sweep);
}

} // END_CPPAD_PY_NAMESPACE
