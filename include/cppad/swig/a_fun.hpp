# ifndef CPPAD_SWIG_A_FUN_HPP
# define CPPAD_SWIG_A_FUN_HPP
/* -----------------------------------------------------------------------------
           cppad_swig: A C++ Object Library and Swig Interface to Cppad
            Copyright (C) 2017-17 Bradley M. Bell (bradbell@seanet.com)
                This program is distributed under the terms of the
            GNU Affero General Public License version 3.0 or later see
                       http://www.gnu.org/licenses/agpl.txt
----------------------------------------------------------------------------- */
# include <vector>
# include <cppad/swig/a_double.hpp>
# ifdef SWIG
#	define CPPAD_SWIG_LIB_PUBLIC
# else
#	include <cppad_swig_lib_export.h>
# endif

// declarations without definitions
namespace CppAD {
	template <class Base> class ADFun;
}


namespace cppad_swig { // BEGIN_CPPAD_SWIG_NAMESPACE

// independent
CPPAD_SWIG_LIB_PUBLIC
std::vector<a_double> independent(const std::vector<double>& x);

// abort_recording
CPPAD_SWIG_LIB_PUBLIC void abort_recording(void);


// Swig class that acts the same as CppAD::ADFun<double>
class CPPAD_SWIG_LIB_PUBLIC a_fun
{	// private members are not in Swig interface
	private:
	// ADFun<double> representation
	CppAD::ADFun<double>* ptr_;
	// -----------------------------------------------------------------------
	// public members are in Swig interface
	public:
	// default ctor
	a_fun(void);
	// destructor
	~a_fun(void);
	// constrtuctor
	a_fun( const std::vector<a_double>& ax, const std::vector<a_double>& ay );
	// forward
	std::vector<double> forward(size_t p, const std::vector<double>& xp );
	// reverse
	std::vector<double> reverse(size_t q, const std::vector<double>& yq );
};

} // END_CPPAD_SWIG_NAMESPACE

# endif
