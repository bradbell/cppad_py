// SPDX-License-Identifier: GPL-3.0-or-later
// SPDX-FileCopyrightText: Bradley M. Bell <bradbell@seanet.com>
// SPDX-FileContributor: 2017-22 Bradley M. Bell
// ----------------------------------------------------------------------------
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
{xrst_begin sparse_rc_xam_cpp}

C++: Sparsity Patterns: Example and Test
########################################
{xrst_literal
   // BEGIN SOURCE
   // END SOURCE
}
{xrst_end sparse_rc_xam_cpp}
*/
//
