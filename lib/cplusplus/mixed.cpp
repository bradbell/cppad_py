# ifdef INCLUDE_MIXED
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
    const  CppAD::mixed::d_sparse_rcv&    A_rcv         )
:
cppad_mixed(
    n_fixed, n_random, quasi_fixed, bool_sparsity, A_rcv
)
{ }

// ---------------------------------------------------------------------------
// mixed class
// ---------------------------------------------------------------------------
// ctor
mixed::mixed(
    size_t                         n_fixed       ,
    size_t                         n_random      ,
    bool                           quasi_fixed   ,
    bool                           bool_sparsity ,
    cppad_py::sparse_rcv&          A_rcv         )
{   // copy_A_rc
    size_t nr  = A_rcv.nr();
    size_t nc  = A_rcv.nc();
    size_t nnz = A_rcv.nnz();
    CppAD::mixed::sparse_rc copy_A_rc(nr, nc, nnz);
    for(size_t k = 0; k < nnz; ++k)
        copy_A_rc.set(k, A_rcv.row()[k], A_rcv.col()[k]);
    // copy_A_rcv
    CppAD::mixed::d_sparse_rcv copy_A_rcv( copy_A_rc );
    for(size_t k = 0; k < nnz; ++k)
        copy_A_rcv.set(k, A_rcv.val()[k]);
    // ptr_
    ptr_ = new mixed_derived(
        n_fixed,
        n_random,
        quasi_fixed,
        bool_sparsity,
        copy_A_rcv
    );
    assert( ptr_ != CPPAD_NULL );
}
// destructor
mixed::~mixed(void)
{   delete ptr_;
}

# endif // INCLUDE_MIXED
