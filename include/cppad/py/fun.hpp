# ifndef CPPAD_PY_A_FUN_HPP
# define CPPAD_PY_A_FUN_HPP
/* -----------------------------------------------------------------------------
           cppad_py: A C++ Object Library and Python Interface to Cppad
            Copyright (C) 2017-20 Bradley M. Bell (bradbell@seanet.com)
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
    template <class Base, class RecBase> class ADFun;
    class sparse_jac_work;
    class sparse_hes_work;
}


namespace cppad_py { // BEGIN_CPPAD_PY_NAMESPACE

// ax = independent(x)
CPPAD_PY_LIB_PUBLIC
std::vector<a_double> independent(const std::vector<double>& x);

// a_both = independent(x, dynamic)
CPPAD_PY_LIB_PUBLIC
std::vector<a_double> independent(
    const std::vector<double>& x, const std::vector<double>& dynamic
);

// abort_recording
CPPAD_PY_LIB_PUBLIC void abort_recording(void);

// forward declare a_fun as a class
class a_fun;

// ---------------------------------------------------------------------------
// Swig class that acts the same as CppAD::ADFun<double>
class CPPAD_PY_LIB_PUBLIC d_fun
{   friend a_fun;
    //
    // private members are not in Swig interface
    private:
    // ADFun<double> representation
    CppAD::ADFun<double, double>* ptr_;
    // -----------------------------------------------------------------------
    // public members are in Swig interface
    public:
    // constrtuctor
    d_fun( const std::vector<a_double>& ax, const std::vector<a_double>& ay );
    // properties
    int size_domain(void) const;
    int size_range(void) const;
    int size_var(void) const;
    int size_op(void) const;
    int size_order(void) const;
    // new_dynamic
    void new_dynamic(const std::vector<double>& dynamic);
    // forward
    std::vector<double> forward(int p, const std::vector<double>& xp );
    // reverse
    std::vector<double> reverse(int q, const std::vector<double>& yq );
    // jacobian
    std::vector<double> jacobian(const std::vector<double>& x);
    // hessian
    std::vector<double> hessian(
        const std::vector<double>& x ,
        const std::vector<double>& w
    );
    // optimize
    void optimize(void);
    // json
    std::string to_json(void) const;
    void from_json(const std::string& json);
    // ------------------------------------------------------------------------
    // public member in Swig interface that compute sparse results
    // (these are implemented in sparse.cpp instead of fun.cpp).
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

// ---------------------------------------------------------------------------
// Swig class that acts like CppAD::ADFun<a_double>
class CPPAD_PY_LIB_PUBLIC a_fun
{   //
    // private members are not in Swig interface
    private:
    // ADFun<a_double, double> representation
    CppAD::ADFun< CppAD::AD<double>, double>* a_ptr_;
    // -----------------------------------------------------------------------
    // public members are in Swig interface
    public:
    // constructor
    a_fun(const d_fun& g);
    // destructor
    ~a_fun(void);
    // properties
    int size_domain(void) const;
    int size_range(void) const;
    int size_var(void) const;
    int size_op(void) const;
    int size_order(void) const;
    // new_dynamic
    void new_dynamic(const std::vector<a_double>& adynamic);
    // forward
    std::vector<a_double> forward(int p, const std::vector<a_double>& axp );
    // reverse
    std::vector<a_double> reverse(int q, const std::vector<a_double>& ayq );
    // jacobian
    std::vector<a_double> jacobian(const std::vector<a_double>& ax);
    // hessian
    std::vector<a_double> hessian(
        const std::vector<a_double>& ax ,
        const std::vector<a_double>& aw
    );
};

} // END_CPPAD_PY_NAMESPACE

# endif
