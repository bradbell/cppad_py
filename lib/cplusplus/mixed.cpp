# if INCLUDE_MIXED
/* -----------------------------------------------------------------------------
           cppad_py: A C++ Object Library and Python Interface to Cppad
            Copyright (C) 2017-20 Bradley M. Bell (bradbell@seanet.com)
                This program is distributed under the terms of the
                GNU General Public License version 3.0 or later see
                      https://www.gnu.org/licenses/gpl-3.0.txt
----------------------------------------------------------------------------- */
# include <cppad/py/mixed.hpp>

// ---------------------------------------------------------------------------
// mixed_derived class
// ---------------------------------------------------------------------------
// ctor
mixed_derived::mixed_derived(
    size_t                                n_fixed       ,
    size_t                                n_random      ,
    bool                                  quasi_fixed   ,
    bool                                  bool_sparsity ,
    const  CppAD::mixed::d_sparse_rcv&    A_rcv         ,
    PyObject*                             warning       )
    :
    cppad_mixed(
        n_fixed, n_random, quasi_fixed, bool_sparsity, A_rcv
    ) ,
    warning_(warning)
    {   if( ! PyCallable_Check(warning_) )
        {   PyErr_SetString(
                PyExc_RuntimeError, "mixed ctor: warning is not callable"
            );
        }
    }

// warning
void mixed_derived::warning(const std::string& message)
{   PyObject* arglist = Py_BuildValue("(s)", message.c_str() );
    PyEval_CallObject(warning_, arglist);
    Py_DECREF(arglist);
}

// ---------------------------------------------------------------------------
// mixed class
// ---------------------------------------------------------------------------
// ctor
mixed::mixed(
    size_t                         n_fixed       ,
    size_t                         n_random      ,
    bool                           quasi_fixed   ,
    bool                           bool_sparsity ,
    const  cppad_py::sparse_rcv&   A_rcv         ,
    PyObject*                      warning       )
{   // tmp_rc
    size_t nr  = A_rcv.nr();
    size_t nc  = A_rcv.nc();
    size_t nnz = A_rcv.nnz();
    CppAD::mixed::sparse_rc tmp_rc(nr, nc, nnz);
    for(size_t k = 0; k < nnz; ++k)
        tmp_rc.set(k, A_rcv.row()[k], A_rcv.col()[k]);
    // tmp_rcv
    CppAD::mixed::d_sparse_rcv tmp_rcv( tmp_rc );
    for(size_t k = 0; k < nnz; ++k)
        tmp_rcv.set(k, A_rcv.val()[k]);
    // ptr_
    ptr_ = new mixed_derived(
        n_fixed, n_random, quasi_fixed, bool_sparsity, tmp_rcv, warning
    );
    assert( ptr_ != CPPAD_NULL );
}
// destructor
mixed::~mixed(void)
{   delete ptr_;
}

# endif
