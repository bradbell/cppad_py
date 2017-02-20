/* -----------------------------------------------------------------------------
           cppad_swig: A C++ Object Library and Swig Interface to Cppad
            Copyright (C) 2017-17 Bradley M. Bell (bradbell@seanet.com)
                This program is distributed under the terms of the
                GNU General Public License version 3.0 or later see
                      https://www.gnu.org/licenses/gpl-3.0.txt
----------------------------------------------------------------------------- */
# include <cppad/cppad.hpp>
# include <cppad/swig/sparse.hpp>
# include <cppad/swig/vector.hpp>

namespace cppad_swig { // BEGIN_CPPAD_SWIG_NAMESPACE

/*
-------------------------------------------------------------------------------
$begin sparse_rc$$
$spell
	rc
	Perl
	nr
	nc
	nnz
	resize
	const
	Cppad
	vec
$$

$section Sparsity Pattern Constructor$$

$head Under Construction$$
This class is under construction and not yet ready for general use.

$head Syntax$$
$icode%pattern% = %model_ref_%sparse_rc()
%$$
$icode%pattern%.resize(%nr%, %nc%, %nnz%)
%$$
$icode%pattern%.nr()
%$$
$icode%pattern%.nc()
%$$
$icode%pattern%.nnz()
%$$
$icode%pattern%.put(%k%, %r%, %c%)
%$$
$icode%row% = %pattern%.row()
%$$
$icode%col% = %pattern%.col()
%$$

$head pattern$$
The result has prototype
$codei%
	sparse_rc %pattern%
%$$
It is used to hold a sparsity pattern for a matrix.
The sparsity $icode pattern$$ is $code const$$
except during its constructor, $code resize$$, and $code put$$.

$head nr$$
This argument has prototype
$codei%
	size_t %nr%
%$$
It specifies the number of rows in the sparsity pattern.
The function call $code nr()$$ returns the value of $icode nr$$.

$head nc$$
This argument has prototype
$codei%
	size_t %nc%
%$$
It specifies the number of columns in the sparsity pattern.
The function call $code nc()$$ returns the value of $icode nc$$.

$head nnz$$
This argument has prototype
$codei%
	size_t %nnz%
%$$
It specifies the number of possibly non-zero
index pairs in the sparsity pattern.
The function call $code nnz()$$ returns the value of $icode nnz$$.

$head resize$$
The current sparsity pattern is lost and a new one is started
with the specified parameters. The elements in the $icode row$$
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
	size_t %k%
%$$
and must be less than $icode nnz$$.

$subhead r$$
This argument has type
$codei%
	size_t %r%
%$$
It specifies the value assigned to $icode%row%[%k%]%$$ and must
be less than $icode nr$$.

$subhead c$$
This argument has type
$codei%
	size_t %c%
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

$children%
	build/lib/example/cplusplus/sparse_rc_xam.cpp%
	build/lib/example/octave/sparse_rc_xam.m%
	build/lib/example/perl/sparse_rc_xam.pm%
	build/lib/example/python/sparse_rc_xam.py
%$$
$head Example$$
$cref/C++/sparse_rc_xam.cpp/$$,
$cref/Octave/sparse_rc_xam.m/$$,
$cref/Perl/sparse_rc_xam.pm/$$,
$cref/Python/sparse_rc_xam.py/$$.

$end
*/
// sparse_rc ctor
sparse_rc::sparse_rc(void)
{	ptr_ = new CppAD::sparse_rc< std::vector<size_t> >();
	CPPAD_ASSERT_UNKNOWN( ptr_ != CPPAD_NULL );
}
// destructor
sparse_rc::~sparse_rc(void)
{	CPPAD_ASSERT_UNKNOWN( ptr_ != CPPAD_NULL );
	delete ptr_;
}
// resize
void sparse_rc::resize(size_t nr, size_t nc, size_t nnz)
{	CPPAD_ASSERT_UNKNOWN( ptr_ != CPPAD_NULL );
	ptr_->resize(nr, nc, nnz);
	return;
}
// number of rows in matrix
size_t sparse_rc::nr(void) const
{	CPPAD_ASSERT_UNKNOWN( ptr_ != CPPAD_NULL );
	return ptr_->nr();
}
// number of columns in matrix
size_t sparse_rc::nc(void) const
{	CPPAD_ASSERT_UNKNOWN( ptr_ != CPPAD_NULL );
	return ptr_->nc();
}
// number of columns in matrix
size_t sparse_rc::nnz(void) const
{	CPPAD_ASSERT_UNKNOWN( ptr_ != CPPAD_NULL );
	return ptr_->nnz();
}
// set row and column for a possibly non-zero element
void sparse_rc::put(size_t k, size_t r, size_t c)
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
// ----------------------------------------------------------------------------
} // END_CPPAD_SWIG_NAMESPACE
