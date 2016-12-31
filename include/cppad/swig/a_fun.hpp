// $Id$
# ifndef CPPAD_SWIG_A_FUN_HPP
# define CPPAD_SWIG_A_FUN_HPP
/* -----------------------------------------------------------------------------
           cppad_swig: A C++ Object Library and SWIG Interface to CppAD
            Copyright (C) 2017-17 Bradley M. Bell (bradbell@seanet.com)
                This program is distributed under the terms of the
            GNU Affero General Public License version 3.0 or later see
                       http://www.gnu.org/licenses/agpl.txt
----------------------------------------------------------------------------- */
# include <vector>
# include <cppad/swig/a_double.hpp>

// declarations without definitions
namespace CppAD {
	template <class Base> class ADFun;
}

/// swig class that acts the same as CppAD::ADFun<double>
class a_fun
{	// private members are not in swig interface
	private:
	/// ADFun<double> representation
	CppAD::ADFun<double>* ptr_;
	// -----------------------------------------------------------------------
	// public members are in swig interface
	public:
	/// default ctor
	a_fun(void);
	/// destructor
	~a_fun(void);
	/// constrtuctor
	a_fun( const std::vector<a_double>& ax, const std::vector<a_double>& ay );
	/// forward
	std::vector<double> forward(int p, const std::vector<double>& xp );
};

# endif
