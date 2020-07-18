// -----------------------------------------------------------------------------
//         cppad_py: A C++ Object Library and Python Interface to Cppad
//          Copyright (C) 2017-20 Bradley M. Bell (bradbell@seanet.com)
//              This program is distributed under the terms of the
//              GNU General Public License version 3.0 or later see
//                    https://www.gnu.org/licenses/gpl-3.0.txt
// -----------------------------------------------------------------------------
// sparse_rcv
// -----------------------------------------------------------------------------
// BEGIN SOURCE
# include <cstdio>
# include <cppad/py/cppad_py.hpp>

bool sparse_rcv_xam(void) {
    using cppad_py::vec_int;
    using cppad_py::vec_double;
    using cppad_py::sparse_rc;
    using cppad_py::sparse_rcv;
    //
    // initialize return variable
    bool ok = true;
    //------------------------------------------------------------------------
    //
    // create sparsity pattern for n by n identity matrix
    sparse_rc pattern = sparse_rc();
    int n = 5;
    pattern.resize(n, n, n);
    for(int k = 0; k < n; k++) {
        pattern.put(k, k, k);
    }
    //
    // create n by n sparse representation of identity matrix
    sparse_rcv matrix = sparse_rcv(pattern);
    for(int k = 0; k < n; k++) {
        matrix.put(k, 1.0);
    }
    //
    // row, column indices
    vec_int row = matrix.row();
    vec_int col = matrix.col();
    vec_double val = matrix.val();
    //
    // check results
    for(int k = 0; k < n; k++) {
        ok = ok && row[k] == k;
        ok = ok && col[k] == k;
        ok = ok && val[k] == 1.0;
    }
    //
    // For this case, row_major and col_major order are same as original order
    vec_int row_major = matrix.row_major();
    vec_int col_major = matrix.col_major();
    for(int k = 0; k < n; k++) {
        ok = ok && row_major[k] == k;
        ok = ok && col_major[k] == k;
    }
    //
    return( ok );
}
// END SOURCE
//
/*
$begin sparse_rcv_xam.cpp$$
$spell
    cplusplus
    cppad
    py
    xam
    Jacobian
    Jacobians
$$
$section C++: Sparsity Patterns: Example and Test$$
$srcthisfile|0|// BEGIN SOURCE|// END SOURCE|$$
$end
*/
//
