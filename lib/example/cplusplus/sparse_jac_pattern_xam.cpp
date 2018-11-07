// -----------------------------------------------------------------------------
//         cppad_py: A C++ Object Library and Python Interface to Cppad
//          Copyright (C) 2017-18 Bradley M. Bell (bradbell@seanet.com)
//              This program is distributed under the terms of the
//              GNU General Public License version 3.0 or later see
//                    https://www.gnu.org/licenses/gpl-3.0.txt
// -----------------------------------------------------------------------------
// for_jac_sparsity, rev_jac_sparsity
// -----------------------------------------------------------------------------
// BEGIN SOURCE
# include <cstdio>
# include <cppad/py/cppad_py.hpp>

bool sparse_jac_pattern_xam(void) {
	using cppad_py::a_double;
	using cppad_py::vec_int;
	using cppad_py::vec_double;
	using cppad_py::vec_a_double;
	using cppad_py::d_fun;
	using cppad_py::sparse_rc;
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
	// create dependent variables ay with ay[i] = ax[j]
	// where i = mod(j + 1, n)
	vec_a_double ay(n);
	for(int j = 0; j < n ; j++) {
		int i = j+1;
		if( i >= n  ) {
			i = i - n;
		}
		a_double ay_i = ax[j];
		ay[i] = ay_i;
	}
	//
	// define af corresponding to f(x)
	d_fun f(ax, ay);
	//
	// sparsity pattern for identity matrix
	sparse_rc pat_in = sparse_rc();
	pat_in.resize(n, n, n);
	for(int k = 0; k < n; k++) {
		pat_in.put(k, k, k);
	}
	//
	// loop over forward and reverse mode
	for(int mode = 0; mode < 2; mode++) {
		sparse_rc pat_out = sparse_rc();
		if( mode == 0  ) {
			f.for_jac_sparsity(pat_in, pat_out);
		}
		if( mode == 1  ) {
			f.rev_jac_sparsity(pat_in, pat_out);
		}
		//
		// check that result is sparsity pattern for Jacobian
		ok = ok && n == pat_out.nnz();
		vec_int col_major = pat_out.col_major();
		vec_int row = pat_out.row();
		vec_int col = pat_out.col();
		for(int k = 0; k < n; k++) {
			int ell = col_major[k];
			int r = row[ell];
			int c = col[ell];
			int i = c+1;
			if( i >=  n  ) {
				i = i - n;
			}
			ok = ok && c == k;
			ok = ok && r == i;
		}
	}
	//
	return( ok );
}
// END SOURCE
//
/*
$begin sparse_jac_pattern_xam.cpp$$
$spell
	cplusplus
	cppad
	py
	xam
	Jacobian
	Jacobians
$$
$section C++: Jacobian Sparsity Patterns: Example and Test$$
$srcfile|lib/example/cplusplus/sparse_jac_pattern_xam.cpp|0|// BEGIN SOURCE|// END SOURCE|$$
$end
*/
//
