// -----------------------------------------------------------------------------
//         cppad_py: A C++ Object Library and Python Interface to Cppad
//          Copyright (C) 2017-20 Bradley M. Bell (bradbell@seanet.com)
//              This program is distributed under the terms of the
//              GNU General Public License version 3.0 or later see
//                    https://www.gnu.org/licenses/gpl-3.0.txt
// -----------------------------------------------------------------------------
// sparse_rc
// -----------------------------------------------------------------------------
// BEGIN SOURCE
# include <cstdio>
# include <cppad/py/cppad_py.hpp>

bool sparse_rc_xam(void) {
    using cppad_py::vec_int;
    using cppad_py::sparse_rc;
    //
    // initialize return variable
    bool ok = true;
    //------------------------------------------------------------------------
    //
    // create a sparsity pattern
    sparse_rc pattern;
    //
    int nr = 6;
    int nc = 5;
    int nnz = 4;
    //
    // resize
    pattern.resize(nr, nc, nnz);
    //
    ok = ok && pattern.nr()  == nr ;
    ok = ok && pattern.nc()  == nc ;
    ok = ok && pattern.nnz() == nnz ;
    //
    // indices corresponding to upper-diagonal
    for(int k = 0; k < nnz; k++) {
        pattern.put(k, k, k+1);
    }
    //
    // row and column indices
    vec_int row = pattern.row();
    vec_int col = pattern.col();
    //
    // check row and column indices
    for(int k = 0; k < nnz; k++) {
        ok = ok && row[k] == k;
        ok = ok && col[k] == k+1;
    }
    //
    // For this case, row_major and col_major order are same as original order
    vec_int row_major = pattern.row_major();
    vec_int col_major = pattern.col_major();
    for(int k = 0; k < nnz; k++) {
        ok = ok && row_major[k] == k;
        ok = ok && col_major[k] == k;
    }
    //
    return( ok );
}
// END SOURCE
//
/*
{xsrst_begin sparse_rc_xam_cpp}

.. include:: ../preamble.rst

{xsrst_spell
}
C++: Sparsity Patterns: Example and Test
########################################
{xsrst_file
    // BEGIN SOURCE
    // END SOURCE
}
{xsrst_end sparse_rc_xam_cpp}
*/
//
