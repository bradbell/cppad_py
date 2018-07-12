# ifndef CPPAD_PY_A_FUN_HPP
# define CPPAD_PY_A_FUN_HPP
/* -----------------------------------------------------------------------------
           cppad_py: A C++ Object Library and Python Interface to Cppad
            Copyright (C) 2017-18 Bradley M. Bell (bradbell@seanet.com)
                This program is distributed under the terms of the
                GNU General Public License version 3.0 or later see
                      https://www.gnu.org/licenses/gpl-3.0.txt
----------------------------------------------------------------------------- */
# include <vector>
# include <cppad/py/a_double.hpp>
# include <cppad/py/public_lib.hpp>
# include <cppad/py/sparse.hpp>

// declarations without definitions
namespace CppAD {
	template <class Base> class ADFun;
	class sparse_jac_work;
	class sparse_hes_work;
}


namespace cppad_py { // BEGIN_CPPAD_PY_NAMESPACE

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
	// jacobian
	std::vector<double> jacobian(const std::vector<double>& x);
	// hessian
	std::vector<double> hessian(
		const std::vector<double>& x ,
		const std::vector<double>& w
	);
	// forward
	std::vector<double> forward(int p, const std::vector<double>& xp );
	// reverse
	std::vector<double> reverse(int q, const std::vector<double>& yq );
	// optimize
	void optimize(void);
	// a_fun properties
	int size_domain(void) const;
	int size_range(void) const;
	int size_var() const;
	int size_op() const;
	// ------------------------------------------------------------------------
	// public member in Swig interface that compute sparse results
	// (these are implemented in sparse.cpp instead of a_fun.cpp).
	void for_jac_sparsity(
		const sparse_rc&  pattern_in    ,
		sparse_rc&        pattern_out
	);
	void rev_jac_sparsity(
		const sparse_rc&  pattern_in    ,
		sparse_rc&        pattern_out
	);
	void for_hes_sparsity(
		const std::vector<bool>& select_domain,
		const std::vector<bool>& select_range ,
		sparse_rc&               pattern_out
	);
	void rev_hes_sparsity(
		const std::vector<bool>& select_domain,
		const std::vector<bool>& select_range ,
		sparse_rc&               pattern_out
	);
	int sparse_jac_for(
		sparse_rcv&                subset   ,
		const std::vector<double>& x        ,
		const sparse_rc&           pattern  ,
		sparse_jac_work&           work
	);
	int sparse_jac_rev(
		sparse_rcv&                subset  ,
		const std::vector<double>& x       ,
		const sparse_rc&           pattern ,
		sparse_jac_work&           work
	);
	int sparse_hes(
		sparse_rcv&                subset  ,
		const std::vector<double>& x       ,
		const std::vector<double>& r       ,
		const sparse_rc&           pattern ,
		sparse_hes_work&           work
	);
};

} // END_CPPAD_PY_NAMESPACE

# endif
