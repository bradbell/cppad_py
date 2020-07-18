// -----------------------------------------------------------------------------
//         cppad_py: A C++ Object Library and Python Interface to Cppad
//          Copyright (C) 2017-20 Bradley M. Bell (bradbell@seanet.com)
//              This program is distributed under the terms of the
//              GNU General Public License version 3.0 or later see
//                    https://www.gnu.org/licenses/gpl-3.0.txt
// -----------------------------------------------------------------------------
// sparse_hes
// -----------------------------------------------------------------------------
// BEGIN SOURCE
# include <cstdio>
# include <cppad/py/cppad_py.hpp>

bool sparse_hes_xam(void) {
    using cppad_py::a_double;
    using cppad_py::vec_bool;
    using cppad_py::vec_int;
    using cppad_py::vec_double;
    using cppad_py::vec_a_double;
    using cppad_py::d_fun;
    using cppad_py::sparse_rc;
    using cppad_py::sparse_rcv;
    using cppad_py::sparse_hes_work;
    //
    // initialize return variable
    bool ok = true;
    //------------------------------------------------------------------------
    // number of dependent and independent variables
    int n = 3;
    //
    // create the independent variables ax
    vec_double x(n);
    for(int i = 0; i < n ; i++) {
        x[i] = i + 2.0;
    }
    vec_a_double ax = cppad_py::independent(x);
    //
    // ay[i] = j * ax[j] * ax[i]
    // where i = mod(j + 1, n)
    vec_a_double ay(n);
    for(int j = 0; j < n ; j++) {
        int i = j+1;
        if( i >= n  ) {
            i = i - n;
        }
        a_double aj(j);
        a_double ax_j = ax[j];
        a_double ax_i = ax[i];
        ay[i] = aj * ax_j * ax_i;
    }
    //
    // define af corresponding to f(x)
    d_fun f(ax, ay);
    //
    // Set select_d (domain) to all true,
    // initial select_r (range) to all false
    // initialize r to all zeros
    vec_bool select_d = vec_bool(n);
    vec_bool select_r = vec_bool(n);
    vec_double r(n);
    for(int i = 0; i < n; i++) {
        select_d[i] = true;
        select_r[i] = false;
        r[i] = 0.0;
    }
    //
    // only select component n-1 of the range function
    // f_0 (x) = (n-1) * x_{n-1} * x_0
    select_r[0] = true;
    r[0] = 1.0;
    //
    // sparisty pattern for Hessian
    sparse_rc pattern = sparse_rc();
    f.for_hes_sparsity(select_d, select_r, pattern);
    //
    // compute all possibly non-zero entries in Hessian
    // (should only compute lower triangle becuase matrix is symmetric)
    sparse_rcv subset = sparse_rcv(pattern);
    //
    // work space used to save time for multiple calls
    sparse_hes_work work = cppad_py::sparse_hes_work();
    //
    f.sparse_hes(subset, x, r, pattern, work);
    //
    // check that result is sparsity pattern for Hessian of f_0 (x)
    ok = ok && subset.nnz() == 2 ;
    vec_int row = subset.row();
    vec_int col = subset.col();
    vec_double val = subset.val();
    for(int k = 0; k < 2; k++) {
        int i = row[k];
        int j = col[k];
        double v = val[k];
        if( i <= j  ) {
            ok = ok && i == 0;
            ok = ok && j == n-1;
        }
        if( i >= j  ) {
            ok = ok && i == n-1;
            ok = ok && j == 0;
        }
        ok = ok && v == n-1;
    }
    //
    return( ok );
}
// END SOURCE
//
/*
$begin sparse_hes_xam.cpp$$
$spell
    cplusplus
    cppad
    py
    xam
    Jacobian
    Jacobians
$$
$section C++: Hessian Sparsity Patterns: Example and Test$$
$srcthisfile|0|// BEGIN SOURCE|// END SOURCE|$$
$end
*/
//
