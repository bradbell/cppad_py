/* -----------------------------------------------------------------------------
           cppad_py: A C++ Object Library and Python Interface to Cppad
            Copyright (C) 2017-18 Bradley M. Bell (bradbell@seanet.com)
                This program is distributed under the terms of the
                GNU General Public License version 3.0 or later see
                      https://www.gnu.org/licenses/gpl-3.0.txt
----------------------------------------------------------------------------- */
# include <cppad/cppad.hpp>
# include <cppad/py/sparse.hpp>
# include <cppad/py/vector.hpp>
# include <cppad/py/fun.hpp>
# include <cppad/py/error.hpp>

namespace cppad_py { // BEGIN_CPPAD_PY_NAMESPACE

/*
-------------------------------------------------------------------------------
$begin cpp_sparse_rc$$
$spell
	rc
	nr
	nc
	nnz
	resize
	const
	Cppad
	Py
	vec
	cppad_py
$$

$section Sparsity Patterns$$

$head Syntax$$
$icode%pattern%   = cppad_py::sparse_rc()
%$$
$icode%pattern%.resize(%nr%, %nc%, %nnz%)
%$$
$icode%nr%        = %pattern%.nr()
%$$
$icode%nc%        = %pattern%.nc()
%$$
$icode%nnz%       = %pattern%.nnz()
%$$
$icode%pattern%.put(%k%, %r%, %c%)
%$$
$icode%row%       = %pattern%.row()
%$$
$icode%col%       = %pattern%.col()
%$$
$icode%row_major% = %pattern%.row_major()
%$$
$icode%col_major% = %pattern%.col_major()
%$$

$head pattern$$
This result has prototype
$codei%
	sparse_rc %pattern%
%$$
It is used to hold a sparsity pattern for a matrix.
The sparsity $icode pattern$$ is $code const$$
except during the $code resize$$ and $code put$$ operations.

$head nr$$
This argument has prototype
$codei%
	int %nr%
%$$
is non-negative, and specifies
the number of rows in the sparsity pattern.
The function $code nr()$$ returns the value of
$icode nr$$ in the previous $code resize$$ operation.

$head nc$$
This argument has prototype
$codei%
	int %nc%
%$$
is non-negative, and specifies
the number of columns in the sparsity pattern.
The function $code nc()$$ returns the value of
$icode nc$$ in the previous $code resize$$ operation.

$head nnz$$
This argument and result has prototype
$codei%
	int %nnz%
%$$
It is the number of possibly non-zero
index pairs in the sparsity pattern.
The function $code nnz()$$ returns the value of
$icode nnz$$ in the previous $code resize$$ operation.

$head resize$$
The current sparsity pattern is lost and a new one is started
with the specified parameters.
After each $code resize$$, the elements in the $icode row$$
and $icode col$$ vectors should be assigned using $code put$$.

$head put$$
This function sets the values
$codei%
	%row%[%k%] = %r%
	%col%[%k%] = %c%
%$$
(The name $code set$$ is used by Cppad, but not used here,
because $code set$$ it is a built-in name in Python.)

$subhead k$$
This argument has type
$codei%
	int %k%
%$$
is non-negative,
and must be less than $icode nnz$$.

$subhead r$$
This argument has type
$codei%
	int %r%
%$$
is non-negative, and must be less than $icode nr$$.
It specifies the value assigned to $icode%row%[%k%]%$$ and must

$subhead c$$
This argument has type
$codei%
	int %c%
%$$
It specifies the value assigned to $icode%col%[%k%]%$$ and must
be less than $icode nc$$.

$head row$$
This result has type
$codei%
	vec_int %row%
%$$
and its size is $icode nnz$$.
For $icode%k% = 0, %...%, %nnz%-1%$$,
$icode%row%[%k%]%$$ is the row index for the $th k$$ possibly non-zero
entry in the matrix.

$head col$$
This result has type
$codei%
	vec_int %col%
%$$
and its size is $icode nnz$$.
For $icode%k% = 0, %...%, %nnz%-1%$$,
$icode%col%[%k%]%$$ is the column index for the $th k$$ possibly non-zero
entry in the matrix.

$head row_major$$
This vector has prototype
$codei%
	vec_int %row_major%
%$$
and its size $icode nnz$$.
It sorts the sparsity pattern in row-major order.
To be specific,
$codei%
	%col%[ %row_major%[%k%] ] <= %col%[ %row_major%[%k%+1] ]
%$$
and if $icode%col%[ %row_major%[%k%] ] == %col%[ %row_major%[%k%+1] ]%$$,
$codei%
	%row%[ %row_major%[%k%] ] < %row%[ %row_major%[%k%+1] ]
%$$
This routine generates an assert if there are two entries with the same
row and column values (if $code NDEBUG$$ is not defined).

$head col_major$$
This vector has prototype
$codei%
	vec_int %col_major%
%$$
and its size $icode nnz$$.
It sorts the sparsity pattern in column-major order.
To be specific,
$codei%
	%row%[ %col_major%[%k%] ] <= %row%[ %col_major%[%k%+1] ]
%$$
and if $icode%row%[ %col_major%[%k%] ] == %row%[ %col_major%[%k%+1] ]%$$,
$codei%
	%col%[ %col_major%[%k%] ] < %col%[ %col_major%[%k%+1] ]
%$$
This routine generates an assert if there are two entries with the same
row and column values (if $code NDEBUG$$ is not defined).

$children%
	lib/example/cplusplus/sparse_rc_xam.cpp
%$$
$head Example$$
$cref sparse_rc_xam.cpp$$

$end
*/
// ---------------------------------------------------------------------------
// public member function not in Swig interface (see %ignore ptr)
const CppAD::sparse_rc< std::vector<size_t> >* sparse_rc::ptr(void) const
{	return ptr_; }
CppAD::sparse_rc< std::vector<size_t> >* sparse_rc::ptr(void)
{	return ptr_; }
// ---------------------------------------------------------------------------
// sparse_rc ctor
sparse_rc::sparse_rc(void)
{	ptr_ = new CppAD::sparse_rc< std::vector<size_t> >();
	CPPAD_PY_ASSERT_UNKNOWN( ptr_ != CPPAD_NULL );
}
// destructor
sparse_rc::~sparse_rc(void)
{	CPPAD_PY_ASSERT_UNKNOWN( ptr_ != CPPAD_NULL );
	delete ptr_;
}
// resize
void sparse_rc::resize(int nr, int nc, int nnz)
{	CPPAD_PY_ASSERT_UNKNOWN( ptr_ != CPPAD_NULL );
	ptr_->resize(nr, nc, nnz);
	return;
}
// number of rows in matrix
int sparse_rc::nr(void) const
{	CPPAD_PY_ASSERT_UNKNOWN( ptr_ != CPPAD_NULL );
	return ptr_->nr();
}
// number of columns in matrix
int sparse_rc::nc(void) const
{	CPPAD_PY_ASSERT_UNKNOWN( ptr_ != CPPAD_NULL );
	return ptr_->nc();
}
// number of possibley non-zero elements in matrix
int sparse_rc::nnz(void) const
{	CPPAD_PY_ASSERT_UNKNOWN( ptr_ != CPPAD_NULL );
	return ptr_->nnz();
}
// set row and column for a possibly non-zero element
void sparse_rc::put(int k, int r, int c)
{	ptr_->set(k, r, c);
	return;
}
// row indices
std::vector<int> sparse_rc::row(void) const
{	size_t nnz = ptr_->nnz();
	std::vector<int> row(nnz);
	for(size_t k = 0; k < nnz; k++)
		row[k] = static_cast<int>( ptr_->row()[k] );
	return row;
}
// col indices
std::vector<int> sparse_rc::col(void) const
{	size_t nnz = ptr_->nnz();
	std::vector<int> col(nnz);
	for(size_t k = 0; k < nnz; k++)
		col[k] = static_cast<int>( ptr_->col()[k] );
	return col;
}
// row_major
std::vector<int> sparse_rc::row_major(void) const
{	size_t nnz = ptr_->nnz();
	std::vector<size_t> row_major = ptr_->row_major();
	std::vector<int> result(nnz);
	for(size_t k = 0; k < nnz; k++)
		result[k] = static_cast<int>( row_major[k] );
	return result;
}
// col_major
std::vector<int> sparse_rc::col_major(void) const
{	size_t nnz = ptr_->nnz();
	std::vector<size_t> col_major = ptr_->col_major();
	std::vector<int> result(nnz);
	for(size_t k = 0; k < nnz; k++)
		result[k] = static_cast<int>( col_major[k] );
	return result;
}
/*
-------------------------------------------------------------------------------
$begin cpp_sparse_rcd$$
$spell
	rc
	rcv
	nr
	nc
	nnz
	resize
	const
	Cppad
	Py
	vec
	cppad_py
$$

$section Sparse Matrices$$

$head Syntax$$
$icode%matrix%    = cppad_py::sparse_rcd(%pattern%)
%$$
$icode%nr%        = %matrix%.nr()
%$$
$icode%nc%        = %matrix%.nc()
%$$
$icode%nnz%       = matrix%.nnz()
%$$
$icode%matrix%.put(%k%, %v%)
%$$
$icode%row%       = %matrix%.row()
%$$
$icode%col%       = %matrix%.col()
%$$
$icode%val%       = %matrix%.val()
%$$
$icode%row_major% = %matrix%.row_major()
%$$
$icode%col_major% = %matrix%.col_major()
%$$

$head pattern$$
This argument has prototype
$codei%
	const sparse_rc& %pattern%
%$$
It specifies the number of rows, number of columns and
the possibly non-zero entries in the $icode matrix$$.

$head matrix$$
This is a sparse matrix object with the sparsity specified by $icode pattern$$.
Only the $icode val$$ vector can be changed. All other values returned by
$icode matrix$$ are fixed during the constructor and constant there after.
The $icode val$$ vector is only changed by the constructor
and the $code set$$ function.

$head nr$$
This return value has prototype
$codei%
	int %nr%
%$$
and is the number of rows in the matrix.

$head nc$$
This return value has prototype
$codei%
	int %nc%
%$$
and is the number of columns in the matrix.

$head nnz$$
This return value has prototype
$codei%
	int %nnz%
%$$
and is the number of possibly non-zero values in the matrix.

$head put$$
This function sets the value
$codei%
	%val%[%k%] = %v%
%$$
(The name $code set$$ is used by Cppad, but not used here,
because $code set$$ it is a built-in name in Python.)

$subhead k$$
This argument has type
$codei%
	int %k%
%$$
and must be non-negative and less than $icode nnz$$.

$subhead v$$
This argument has type
$codei%
	double %v%
%$$
It specifies the value assigned to $icode%val%[%k%]%$$.

$head row$$
This result has type
$codei%
	vec_int %row%
%$$
and its size is $icode nnz$$.
For $icode%k% = 0, %...%, %nnz%-1%$$,
$icode%row%[%k%]%$$ is the row index for the $th k$$ possibly non-zero
entry in the matrix.

$head col$$
This result has type
$codei%
	vec_int %col%
%$$
and its size is $icode nnz$$.
For $icode%k% = 0, %...%, %nnz%-1%$$,
$icode%col%[%k%]%$$ is the column index for the $th k$$ possibly non-zero
entry in the matrix.

$head val$$
This result has type
$codei%
	vec_double %val%
%$$
and its size is $icode nnz$$.
For $icode%k% = 0, %...%, %nnz%-1%$$,
$icode%val%[%k%]%$$ is the value of the $th k$$ possibly non-zero
entry in the matrix (the value may be zero).

$head row_major$$
This vector has prototype
$codei%
	vec_int %row_major%
%$$
and its size $icode nnz$$.
It sorts the sparsity pattern in row-major order.
To be specific,
$codei%
	%col%[ %row_major%[%k%] ] <= %col%[ %row_major%[%k%+1] ]
%$$
and if $icode%col%[ %row_major%[%k%] ] == %col%[ %row_major%[%k%+1] ]%$$,
$codei%
	%row%[ %row_major%[%k%] ] < %row%[ %row_major%[%k%+1] ]
%$$
This routine generates an assert if there are two entries with the same
row and column values (if $code NDEBUG$$ is not defined).

$head col_major$$
This vector has prototype
$codei%
	vec_int %col_major%
%$$
and its size $icode nnz$$.
It sorts the sparsity pattern in column-major order.
To be specific,
$codei%
	%row%[ %col_major%[%k%] ] <= %row%[ %col_major%[%k%+1] ]
%$$
and if $icode%row%[ %col_major%[%k%] ] == %row%[ %col_major%[%k%+1] ]%$$,
$codei%
	%col%[ %col_major%[%k%] ] < %col%[ %col_major%[%k%+1] ]
%$$
This routine generates an assert if there are two entries with the same
row and column values (if $code NDEBUG$$ is not defined).

$children%
	lib/example/cplusplus/sparse_rcd_xam.cpp
%$$
$head Example$$
$cref sparse_rcd_xam.cpp$$

$end
*/
// ---------------------------------------------------------------------------
// public member function not in Swig interface (see %ignore ptr)
CppAD::sparse_rcv< std::vector<size_t> , std::vector<double> >*
	sparse_rcd::ptr(void)
		{	return ptr_; }
// ---------------------------------------------------------------------------
// sparse_rcd ctor
sparse_rcd::sparse_rcd(const sparse_rc& pattern)
{	ptr_ = new CppAD::sparse_rcv< std::vector<size_t> , std::vector<double> >(
		*pattern.ptr()
	);
	CPPAD_PY_ASSERT_UNKNOWN( ptr_ != CPPAD_NULL );
}
// destructor
sparse_rcd::~sparse_rcd(void)
{	CPPAD_PY_ASSERT_UNKNOWN( ptr_ != CPPAD_NULL );
	delete ptr_;
}
// number of rows in matrix
int sparse_rcd::nr(void) const
{	CPPAD_PY_ASSERT_UNKNOWN( ptr_ != CPPAD_NULL );
	return ptr_->nr();
}
// number of columns in matrix
int sparse_rcd::nc(void) const
{	CPPAD_PY_ASSERT_UNKNOWN( ptr_ != CPPAD_NULL );
	return ptr_->nc();
}
// number of possibley non-zero elements in matrix
int sparse_rcd::nnz(void) const
{	CPPAD_PY_ASSERT_UNKNOWN( ptr_ != CPPAD_NULL );
	return ptr_->nnz();
}
// set row and column for a possibly non-zero element
void sparse_rcd::put(int k, double v)
{	ptr_->set(k, v);
	return;
}
// row indices
std::vector<int> sparse_rcd::row(void) const
{	size_t nnz = ptr_->nnz();
	std::vector<int> row(nnz);
	for(size_t k = 0; k < nnz; k++)
		row[k] = static_cast<int>( ptr_->row()[k] );
	return row;
}
// col indices
std::vector<int> sparse_rcd::col(void) const
{	size_t nnz = ptr_->nnz();
	std::vector<int> col(nnz);
	for(size_t k = 0; k < nnz; k++)
		col[k] = static_cast<int>( ptr_->col()[k] );
	return col;
}
// values
std::vector<double> sparse_rcd::val(void) const
{	return ptr_->val(); }
// row_major
std::vector<int> sparse_rcd::row_major(void) const
{	size_t nnz = ptr_->nnz();
	std::vector<size_t> row_major = ptr_->row_major();
	std::vector<int> result(nnz);
	for(size_t k = 0; k < nnz; k++)
		result[k] = static_cast<int>( row_major[k] );
	return result;
}
// col_major
std::vector<int> sparse_rcd::col_major(void) const
{	size_t nnz = ptr_->nnz();
	std::vector<size_t> col_major = ptr_->col_major();
	std::vector<int> result(nnz);
	for(size_t k = 0; k < nnz; k++)
		result[k] = static_cast<int>( col_major[k] );
	return result;
}
// ----------------------------------------------------------------------------
/*
$begin cpp_jac_sparsity$$
$spell
	af
	Jacobian
	jac
	bool
	const
	rc
	cpp
$$

$section Jacobian Sparsity Patterns$$

$head Syntax$$
$icode%f%.for_jac_sparsity(%pattern_in%, %pattern_out%)
%$$
$icode%f%.rev_jac_sparsity(%pattern_in%, %pattern_out%)%$$

$head Purpose$$
We use $latex F : \B{R}^n \rightarrow \B{R}^m$$ to denote the
function corresponding to the operation sequence stored in $icode f$$.

$subhead for_jac_sparsity$$
Fix $latex R \in \B{R}^{n \times \ell}$$ and define the function
$latex \[
	J(x) = F^{(1)} ( x ) * R
\] $$
Given a sparsity pattern for $latex R$$,
$code for_jac_sparsity$$ computes a sparsity pattern for $latex J(x)$$.

$subhead rev_jac_sparsity$$
Fix $latex R \in \B{R}^{\ell \times m}$$ and define the function
$latex \[
	J(x) = R * F^{(1)} ( x )
\] $$
Given a sparsity pattern for $latex R$$,
$code rev_jac_sparsity$$ computes a sparsity pattern for $latex J(x)$$.

$head x$$
Note that a sparsity pattern for $latex J(x)$$ corresponds to the
operation sequence stored in $icode f$$ and does not depend on
the argument $icode x$$.

$head f$$
The object $icode f$$ has prototype
$codei%
	d_fun %f%
%$$
The object $icode f$$ is not $code const$$ when using
$code for_jac_sparsity$$.
After a call to $code for_jac_sparsity$$, a sparsity pattern
for each of the variables in the operation sequence
is held in $icode f$$ for possible later use during
reverse Hessian sparsity calculations.

$head pattern_in$$
The argument $icode pattern_in$$ has prototype
$codei%
	const sparse_rc& %pattern_in%
%$$
see $cref cpp_sparse_rc$$.
This is a sparsity pattern for $latex R$$.

$head pattern_out$$
This argument has prototype
$codei%
	sparse_rc<%SizeVector%>& %pattern_out%
%$$
This input value of $icode pattern_out$$ does not matter.
Upon return $icode pattern_out$$ is a sparsity pattern for
$latex J(x)$$.

$head Sparsity for Entire Jacobian$$
Suppose that $latex R$$ is the identity matrix.
In this case, $icode pattern_out$$ is a sparsity pattern for
$latex F^{(1)} ( x )$$.

$children%
	lib/example/cplusplus/sparse_jac_pattern_xam.cpp
%$$
$head Example$$
$cref/C++/sparse_jac_pattern_xam.cpp/$$

$end
*/
void d_fun::for_jac_sparsity(
	const sparse_rc&  pattern_in    ,
	sparse_rc&        pattern_out   )
{	const CppAD::sparse_rc< std::vector<size_t> >* ptr_in  = pattern_in.ptr();
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
{	const CppAD::sparse_rc< std::vector<size_t> >* ptr_in  = pattern_in.ptr();
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
$begin cpp_sparsity$$
$spell
	hes
	af
	const
	vec
	bool
	rc
$$

$section Hessian Sparsity Patterns$$

$head Syntax$$
$icode%f%.for_hes_sparsity(%select_domain%, %select_range%, %pattern_out%)
%$$
$icode%f%.rev_hes_sparsity(%select_domain%, %select_range%, %pattern_out%)%$$

$head Purpose$$
We use $latex F : \B{R}^n \rightarrow \B{R}^m$$ to denote the
function corresponding to the operation sequence stored in $icode f$$.
Fix a diagonal matrix $latex D \in \B{R}^{n \times n}$$, fix a vector
$latex r \in \B{R}^m$$, and define
$latex \[
	H(x) = D (r^\R{T} F)^{(2)} ( x ) D
\] $$
Given a sparsity pattern for $latex D$$ and $latex r$$,
these routines compute a sparsity pattern for $latex H(x)$$.

$head x$$
Note that a sparsity pattern for $latex H(x)$$ corresponds to the
operation sequence stored in $icode f$$ and does not depend on
the argument $icode x$$.

$head f$$
The object $icode f$$ has prototype
$codei%
	d_fun %f%
%$$

$head select_domain$$
The argument $icode select_domain$$ has prototype
$codei%
	const vec_bool& %select_domain%
%$$
It has size $icode n$$ and is a sparsity pattern for the diagonal of
$latex D$$; i.e., $icode%select_domain%[%j%]%$$ is true if and only if
$latex D_{j,j}$$ is possibly non-zero.

$head select_range$$
The argument $icode select_range$$ has prototype
$codei%
	const vec_bool& %select_range%
%$$
It has size $icode m$$ and is a sparsity pattern for the vector
$latex r$$; i.e., $icode%select_range%[%i%]%$$ is true if and only if
$latex r_i$$ is possibly non-zero.

$head pattern_out$$
This argument has prototype
$codei%
	sparse_rc<%SizeVector%>& %pattern_out%
%$$
This input value of $icode pattern_out$$ does not matter.
Upon return $icode pattern_out$$ is a sparsity pattern for
$latex J(x)$$.

$head Sparsity for Component Wise Hessian$$
Suppose that $latex D$$ is the identity matrix,
and only the $th i$$ component of $icode r$$ is possibly non-zero.
In this case, $icode pattern_out$$ is a sparsity pattern for
$latex F_i^{(2)} ( x )$$.

$children%
	lib/example/cplusplus/sparse_hes_pattern_xam.cpp
%$$
$head Example$$
$cref/C++/sparse_hes_pattern_xam.cpp/$$

$end
*/
void d_fun::for_hes_sparsity(
	const std::vector<bool>& select_domain ,
	const std::vector<bool>& select_range  ,
	sparse_rc&               pattern_out   )
{	CppAD::sparse_rc< std::vector<size_t> >* ptr_out = pattern_out.ptr();
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
{	CPPAD_PY_ASSERT_KNOWN(
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
	{	if( select_domain[j] )
		{	pattern_R.set(j, j, ell);
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
$begin cpp_sparse_jac$$
$spell
	Jacobians
	jac
	af
	Jacobian
	Taylor
	rcv
	nr
	nc
	const
	vec
	rc
	cppad_py
$$

$section Computing Sparse Jacobians$$

$head Syntax$$
$icode%work% = cppad_py::sparse_jac_work()
%$$
$icode%n_sweep% = %f%.sparse_jac_for(%subset%, %x%, %pattern%, %work%)
%$$
$icode%n_sweep% = %f%.sparse_jac_rev(%subset%, %x%, %pattern%, %work%)%$$

$head Purpose$$
We use $latex F : \B{R}^n \rightarrow \B{R}^m$$ to denote the
function corresponding to $icode f$$.
The syntax above takes advantage of sparsity when computing the Jacobian
$latex \[
	J(x) = F^{(1)} (x)
\] $$
In the sparse case, this should be faster and take less memory than
$cref cpp_fun_jacobian$$.
We use the notation $latex J_{i,j} (x)$$ to denote the partial of
$latex F_i (x)$$ with respect to $latex x_j$$.

$head sparse_jac_for$$
This function uses first order forward mode sweeps $cref cpp_fun_forward$$
to compute multiple columns of the Jacobian at the same time.

$head sparse_jac_rev$$
This function uses first order reverse mode sweeps $cref cpp_fun_reverse$$
to compute multiple rows of the Jacobian at the same time.

$head f$$
This object has prototype
$codei%
	ADFun<%Base%> %f%
%$$
Note that the Taylor coefficients stored in $icode f$$ are affected
by this operation; see
$cref/uses forward/cpp_sparse_jac/Uses Forward/$$ below.

$head subset$$
This argument has prototype
$codei%
	sparse_rcd& %subset%
%$$
Its row size is $icode%subset%.nr() == %m%$$,
and its column size is $icode%subset%.nc() == %n%$$.
It specifies which elements of the Jacobian are computed.
The input value of its value vector
$icode%subset%.val()%$$ does not matter.
Upon return it contains the value of the corresponding elements
of the Jacobian.
All of the row, column pairs in $icode subset$$ must also appear in
$icode pattern$$; i.e., they must be possibly non-zero.

$head x$$
This argument has prototype
$codei%
	const vec_double& %x%
%$$
and its size is $icode n$$.
It specifies the point at which to evaluate the Jacobian $latex J(x)$$.

$head pattern$$
This argument has prototype
$codei%
	const sparse_rc& %pattern%
%$$
Its row size is $icode%pattern%.nr() == %m%$$,
and its column size is $icode%pattern%.nc() == %n%$$.
It is a sparsity pattern for the Jacobian $latex J(x)$$.
This argument is not used (and need not satisfy any conditions),
when $cref/work/cpp_sparse_jac/work/$$ is non-empty.

$head work$$
This argument has prototype
$codei%
	sparse_jac_work& %work%
%$$
We refer to its initial value,
and its value after $icode%work%.clear()%$$, as empty.
If it is empty, information is stored in $icode work$$.
This can be used to reduce computation when
a future call is for the same object $icode f$$,
the same member function $code sparse_jac_for$$ or $code sparse_jac_rev$$,
and the same subset of the Jacobian.
If any of these values change, use $icode%work%.clear()%$$ to
empty this structure.

$head n_sweep$$
The return value $icode n_sweep$$ has prototype
$codei%
	int %n_sweep%
%$$
If $code sparse_jac_for$$ ($code sparse_jac_rev$$) is used,
$icode n_sweep$$ is the number of first order forward (reverse) sweeps
used to compute the requested Jacobian values.
This is proportional to the total computational work,
not counting the zero order forward sweep,
or combining multiple columns (rows) into a single sweep.

$head Uses Forward$$
After each call to $cref cpp_fun_forward$$,
the object $icode f$$ contains the corresponding Taylor coefficients
for all the variables in the operation sequence..
After a call to $code sparse_jac_forward$$ or $code sparse_jac_rev$$,
the zero order coefficients correspond to
$codei%
	%f%.forward(0, %x%)
%$$
All the other forward mode coefficients are unspecified.

$children%
	lib/example/cplusplus/sparse_jac_xam.cpp
%$$
$head Example$$
$cref sparse_jac_xam.cpp$$

$end
*/
// ---------------------------------------------------------------------------
// public member function not in Swig interface (see %ignore ptr)
CppAD::sparse_jac_work* sparse_jac_work::ptr(void)
{	return ptr_; }
//
// sparse_jac_work ctor
sparse_jac_work::sparse_jac_work(void)
{	ptr_ = new CppAD::sparse_jac_work();
	CPPAD_PY_ASSERT_UNKNOWN( ptr_ != CPPAD_NULL );
}
// sparse_jac_work destructor
sparse_jac_work::~sparse_jac_work(void)
{	CPPAD_PY_ASSERT_UNKNOWN( ptr_ != CPPAD_NULL );
	delete ptr_;
}
// sparse_jac_work clear
void sparse_jac_work::clear(void)
{	CPPAD_PY_ASSERT_UNKNOWN( ptr_ != CPPAD_NULL );
	ptr_->clear();
	return;
}
// sparse_jac_for
int d_fun::sparse_jac_for(
	sparse_rcd&                subset   ,
	const std::vector<double>& x        ,
	const sparse_rc&           pattern  ,
	sparse_jac_work&           work     )
{	size_t      group_max = 1;
	std::string coloring  = "cppad";
	size_t n_sweep = ptr_->sparse_jac_for(
		group_max, x, *subset.ptr(), *pattern.ptr(), coloring, *work.ptr()
	);
	return int(n_sweep);
}
// sparse_jac_rev
int d_fun::sparse_jac_rev(
	sparse_rcd&                subset   ,
	const std::vector<double>& x        ,
	const sparse_rc&           pattern  ,
	sparse_jac_work&           work     )
{	std::string coloring  = "cppad";
	size_t n_sweep = ptr_->sparse_jac_rev(
		x, *subset.ptr(), *pattern.ptr(), coloring, *work.ptr()
	);
	return int(n_sweep);
}
/*
------------------------------------------------------------------------------
$begin cpp_sparse_hes$$
$spell
	af
	Jacobian
	Taylor
	rcv
	nr
	nc
	const
	vec
	rc
	hes
	cppad_py
$$

$section Computing Sparse Hessians$$

$head Syntax$$
$icode%work% = cppad_py::sparse_hes_work()
%$$
$icode%n_sweep% = %f%.sparse_hes(%subset%, %x%, %r%, %pattern%, %work%)
%$$

$head Purpose$$
We use $latex F : \B{R}^n \rightarrow \B{R}^m$$ to denote the
function corresponding to $icode f$$.
Given a vector $latex r \in \B{R}^m$$, define
$latex \[
	H(x) = (r^\R{T} F)^{(2)} ( x )
\] $$
This routine takes advantage of sparsity when computing elements
of the Hessian $latex H(x)$$.

$head f$$
This object has prototype
$codei%
	ADFun<%Base%> %f%
%$$
Note that the Taylor coefficients stored in $icode f$$ are affected
by this operation; see
$cref/uses forward/cpp_sparse_hes/Uses Forward/$$ below.

$head subset$$
This argument has prototype
$codei%
	sparse_rcd& %subset%
%$$
Its row size and column size is $icode n$$; i.e.,
$icode%subset%.nr() == %n%$$ and $icode%subset%.nc() == %n%$$.
It specifies which elements of the Hessian are computed.
The input value of its value vector
$icode%subset%.val()%$$ does not matter.
Upon return it contains the value of the corresponding elements
of the Jacobian.
All of the row, column pairs in $icode subset$$ must also appear in
$icode pattern$$; i.e., they must be possibly non-zero.

$head x$$
This argument has prototype
$codei%
	const vec_double& %x%
%$$
and its size is $icode n$$.
It specifies the point at which to evaluate the Hessian $latex H(x)$$.

$head r$$
This argument has prototype
$codei%
	const vec_double& %r%
%$$
and its size is $icode m$$.
It specifies the multiplier for each component of $latex F(x)$$;
i.e., $latex r_i$$ is the multiplier for $latex F_i (x)$$.

$head pattern$$
This argument has prototype
$codei%
	const sparse_rc& %pattern%
%$$
Its row size and column sizes are $icode n$$; i.e.,
$icode%pattern%.nr() == %n%$$ and $icode%pattern%.nc() == %n%$$.
It is a sparsity pattern for the Hessian $latex H(x)$$.
This argument is not used (and need not satisfy any conditions),
when $cref/work/cpp_sparse_hes/work/$$ is non-empty.

$head work$$
This argument has prototype
$codei%
	sparse_hes_work& %work%
%$$
We refer to its initial value,
and its value after $icode%work%.clear()%$$, as empty.
If it is empty, information is stored in $icode work$$.
This can be used to reduce computation when
a future call is for the same object $icode f$$,
and the same subset of the Hessian.
If either of these values change, use $icode%work%.clear()%$$ to
empty this structure.

$head n_sweep$$
The return value $icode n_sweep$$ has prototype
$codei%
	int %n_sweep%
%$$
It is the number of first order forward sweeps
used to compute the requested Hessian values.
Each first forward sweep is followed by a second order reverse sweep
so it is also the number of reverse sweeps.
This is proportional to the total computational work,
not counting the zero order forward sweep,
or combining multiple columns and rows into a single sweep.

$head Uses Forward$$
After each call to $cref cpp_fun_forward$$,
the object $icode f$$ contains the corresponding Taylor coefficients
for all the variables in the operation sequence..
After a call to $code sparse_hes$$
the zero order coefficients correspond to
$codei%
	%f%.forward(0, %x%)
%$$
All the other forward mode coefficients are unspecified.

$children%
	lib/example/cplusplus/sparse_hes_xam.cpp
%$$
$head Example$$
$cref sparse_hes_xam.cpp$$

$end
*/
// ---------------------------------------------------------------------------
// public member function not in Swig interface (see %ignore ptr)
CppAD::sparse_hes_work* sparse_hes_work::ptr(void)
{	return ptr_; }
//
// sparse_hes_work ctor
sparse_hes_work::sparse_hes_work(void)
{	ptr_ = new CppAD::sparse_hes_work();
	CPPAD_PY_ASSERT_UNKNOWN( ptr_ != CPPAD_NULL );
}
// sparse_hes_work destructor
sparse_hes_work::~sparse_hes_work(void)
{	CPPAD_PY_ASSERT_UNKNOWN( ptr_ != CPPAD_NULL );
	delete ptr_;
}
// sparse_hes_work clear
void sparse_hes_work::clear(void)
{	CPPAD_PY_ASSERT_UNKNOWN( ptr_ != CPPAD_NULL );
	ptr_->clear();
	return;
}
// sparse_hes
int d_fun::sparse_hes(
	sparse_rcd&                subset   ,
	const std::vector<double>& x        ,
	const std::vector<double>& r        ,
	const sparse_rc&           pattern  ,
	sparse_hes_work&           work     )
{	std::string coloring  = "cppad.symmetric";
	size_t n_sweep = ptr_->sparse_hes(
		x, r, *subset.ptr(), *pattern.ptr(), coloring, *work.ptr()
	);
	return int(n_sweep);
}

} // END_CPPAD_PY_NAMESPACE
