/* -----------------------------------------------------------------------------
           cppad_swig: A C++ Object Library and Swig Interface to Cppad
            Copyright (C) 2017-17 Bradley M. Bell (bradbell@seanet.com)
                This program is distributed under the terms of the
                GNU General Public License version 3.0 or later see
                      https://www.gnu.org/licenses/gpl-3.0.txt
----------------------------------------------------------------------------- */
# include <cppad/cppad.hpp>
# include <cppad/swig/sparse.hpp>

namespace cppad_swig { // BEGIN_CPPAD_SWIG_NAMESPACE

/*
-------------------------------------------------------------------------------
$begin sparse_rc$$
$spell
	rc
	Perl
$$

$section Sparsity Pattern Constructor$$

$head Under Construction$$
This class is under construction and not yet ready for general use.

$head Syntax$$
$icode%pattern% = %model_ref_%sparse_rc%$$

$head p$$
The result has prototype
$codei%
	sparse_rc %pattern%
%$$
It can be used to hold a sparsity pattern for a sparse matrix.

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
{	ptr_ = new CppAD::sparse_rc<s_vector>();
	CPPAD_ASSERT_UNKNOWN( ptr_ != CPPAD_NULL );
}
// destructor
sparse_rc::~sparse_rc(void)
{	CPPAD_ASSERT_UNKNOWN( ptr_ != CPPAD_NULL );
	delete ptr_;
}

// ----------------------------------------------------------------------------
} // END_CPPAD_SWIG_NAMESPACE
