# ifndef CPPAD_SWIG_SPARSE_HPP
# define CPPAD_SWIG_SPARSE_HPP
/* -----------------------------------------------------------------------------
           cppad_swig: A C++ Object Library and Swig Interface to Cppad
            Copyright (C) 2017-17 Bradley M. Bell (bradbell@seanet.com)
                This program is distributed under the terms of the
                GNU General Public License version 3.0 or later see
                      https://www.gnu.org/licenses/gpl-3.0.txt
----------------------------------------------------------------------------- */
# include <vector>
# ifdef SWIG
#	define CPPAD_SWIG_LIB_PUBLIC
# else
#	include <cppad_swig_lib_export.h>
# endif

// declarations without definitions
namespace CppAD {
	template <class SizeVector> class sparse_rc;
}


namespace cppad_swig { // BEGIN_CPPAD_SWIG_NAMESPACE

// Swig class that acts the same as CppAD::sparse_rc< std::vector<size_t> >
class CPPAD_SWIG_LIB_PUBLIC sparse_rc
{	public:
	// s_vector: type used for row and column index vectors
	typedef std::vector<size_t> s_vector;
	// private members are not in Swig interface
	private:
	// sparse_rc<s_vector> representation
	CppAD::sparse_rc<s_vector>* ptr_;
	// -----------------------------------------------------------------------
	// public members are in Swig interface
	public:
	// default ctor
	sparse_rc(void);
	// destructor
	~sparse_rc(void);
	// resize
	void resize(size_t nr, size_t nc, size_t nnz);
	// number of rows in matrix
	size_t nr(void) const;
	// number of columns in matrix
	size_t nc(void) const;
	// number of possibly non-zero elements in matrix
	size_t nnz(void) const;
# if 0
	// set row and column for a possibly non-zero element
	void set(size_t k, size_t r, size_t c);
	// row indices
	const s_vector& row(void) const;
	// column indices
	const s_vector& col(void) const;
	// row-major order
	s_vector row_major(void) const;
	// column-major order
	s_vector col_major(void) const;
# endif
};

} // END_CPPAD_SWIG_NAMESPACE

# endif
