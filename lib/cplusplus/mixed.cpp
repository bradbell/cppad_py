# ifdef INCLUDE_MIXED
/* -----------------------------------------------------------------------------
           cppad_py: A C++ Object Library and Python Interface to Cppad
            Copyright (C) 2017-20 Bradley M. Bell (bradbell@seanet.com)
                This program is distributed under the terms of the
                GNU General Public License version 3.0 or later see
                      https://www.gnu.org/licenses/gpl-3.0.txt
----------------------------------------------------------------------------- */
# include <cppad/py/mixed.hpp>

namespace cppad_py { // BEGIN_CPPAD_PY_NAMESPACE

// ---------------------------------------------------------------------------
// mixed_derived class
// ---------------------------------------------------------------------------
// ctor
mixed_derived::mixed_derived(
    size_t                                n_fixed        ,
    size_t                                n_random       ,
    bool                                  quasi_fixed    ,
    bool                                  bool_sparsity  ,
    const  CppAD::mixed::d_sparse_rcv&    A_rcv          ,
    PyObject*                             warning        ,
    d_fun&                                fix_likelihood )
:
cppad_mixed( n_fixed, n_random, quasi_fixed, bool_sparsity, A_rcv ) ,
warning_(warning)                                                   ,
fix_likelihood_(fix_likelihood)
{ }
//
// warning
void mixed_derived::warning(const std::string& message)
{   PyObject* arglist = Py_BuildValue("(s)", message.c_str() );
    PyEval_CallObject(warning_, arglist);
    Py_DECREF(arglist);
}
//
// fatal_error
void mixed_derived::fatal_error(const std::string& message)
{   // swig exceptions are set up to catch std::runtime_error
    throw std::runtime_error(message);
}

// ---------------------------------------------------------------------------
// mixed class
// ---------------------------------------------------------------------------
// ctor
mixed::mixed(
    size_t                         n_fixed          ,
    size_t                         n_random         ,
    bool                           quasi_fixed      ,
    bool                           bool_sparsity    ,
    sparse_rcv&                    A_rcv            ,
    PyObject*                      warning          ,
    d_fun&                         fix_likelihood   )
{   // --------------------------------------------------
    // copy_A_rc as CppAD::mixed::sparse_rc
    size_t nr  = A_rcv.nr();
    size_t nc  = A_rcv.nc();
    size_t nnz = A_rcv.nnz();
    CppAD::mixed::sparse_rc copy_A_rc(nr, nc, nnz);
    for(size_t k = 0; k < nnz; ++k)
        copy_A_rc.set(k, A_rcv.row()[k], A_rcv.col()[k]);
    // --------------------------------------------------
    // copy_A_rcv as CppAD::mixed::sparse_rcv
    CppAD::mixed::d_sparse_rcv copy_A_rcv( copy_A_rc );
    for(size_t k = 0; k < nnz; ++k)
        copy_A_rcv.set(k, A_rcv.val()[k]);
    // --------------------------------------------------
    // ptr_
    ptr_ = new mixed_derived(
        n_fixed,
        n_random,
        quasi_fixed,
        bool_sparsity,
        copy_A_rcv,
        warning,
        fix_likelihood
    );
    assert( ptr_ != CPPAD_NULL );
}
// destructor
mixed::~mixed(void)
{   delete ptr_;
}
// post_warning
void mixed::post_warning(const char* message)
{   ptr_->warning( std::string(message) );
}
// post_fatal_error
void mixed::post_fatal_error(const char* message)
{   ptr_->fatal_error( std::string(message) );
}

} // END_CPPAD_PY_NAMESPACE

# endif // INCLUDE_MIXED
