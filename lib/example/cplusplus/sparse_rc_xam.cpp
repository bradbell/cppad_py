// This file can be generated in the lib/xam directory using the command:
// m4 -D Language_=cplusplus sparse/sparse_rc.xam
// -----------------------------------------------------------------------------
//         cppad_py: A C++ Object Library and Python Interface to Cppad
//          Copyright (C) 2017-18 Bradley M. Bell (bradbell@seanet.com)
//              This program is distributed under the terms of the
//              GNU General Public License version 3.0 or later see
//                    https://www.gnu.org/licenses/gpl-3.0.txt
// -----------------------------------------------------------------------------
// sparse_rc
// -----------------------------------------------------------------------------
// BEGIN SOURCE
# include <cstdio>
# include <string>
# include <cppad/py/cppad_py.hpp>

bool sparse_rc_xam(void) {
	using cppad_py::a_double;
	using cppad_py::vec_bool;
	using cppad_py::vec_int;
	using cppad_py::vec_double;
	using cppad_py::vec_a_double;
	using cppad_py::a_fun;
	using cppad_py::sparse_rc;
	using cppad_py::sparse_rcv;
	using cppad_py::sparse_jac_work;
	using cppad_py::sparse_hes_work;
	using std::string;
	//
	// initialize return variable
	bool ok = true;
	//------------------------------------------------------------------------
	//
	// create a sparsity pattern
	sparse_rc pattern = cppad_py::sparse_rc();
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
$begin sparse_rc_xam.cpp$$
$spell
	cplusplus
	cppad
	py
	xam
	Jacobian
	Jacobians
$$
$section C++: Sparsity Patterns: Example and Test$$
$srcfile|lib/example/cplusplus/sparse_rc_xam.cpp|0|// BEGIN SOURCE|// END SOURCE|$$
$end
*/
//
