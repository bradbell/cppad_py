// This file can be generated in the lib/xam directory using the command:
// m4 -D Language_=cplusplus sparse/hes_pattern_xam.xam
// -----------------------------------------------------------------------------
//         cppad_py: A C++ Object Library and Python Interface to Cppad
//          Copyright (C) 2017-18 Bradley M. Bell (bradbell@seanet.com)
//              This program is distributed under the terms of the
//              GNU General Public License version 3.0 or later see
//                    https://www.gnu.org/licenses/gpl-3.0.txt
// -----------------------------------------------------------------------------
// for_hes_sparsity, rev_hes_sparsity
// -----------------------------------------------------------------------------
// BEGIN SOURCE
# include <cstdio>
# include <cppad/py/cppad_py.hpp>

bool sparse_hes_pattern_xam(void) {
	using cppad_py::a_double;
	using cppad_py::vec_bool;
	using cppad_py::vec_int;
	using cppad_py::vec_double;
	using cppad_py::vec_a_double;
	using cppad_py::a_fun;
	using cppad_py::sparse_rc;
	//
	// initialize return variable
	bool ok = true;
	//------------------------------------------------------------------------
	// number of dependent and independent variables
	int n = 3;
	//
	// create the independent variables ax
	vec_double x = vec_double(n);
	for(int i = 0; i < n ; i++) {
		x[i] = i + 2.0;
	}
	vec_a_double ax = cppad_py::independent(x);
	//
	// create dependent variables ay with ay[i] = ax[j] * ax[i]
	// where i = mod(j + 1, n)
	vec_a_double ay = vec_a_double(n);
	for(int j = 0; j < n ; j++) {
		int i = j+1;
		if( i >= n  ) {
			i = i - n;
		}
		a_double ay_i = ax[i] * ax[j];
		ay[i] = ay_i;
	}
	//
	// define af corresponding to f(x)
	a_fun af = a_fun(ax, ay);
	//
	// Set select_d (domain) to all true, initial select_r (range) to all false
	vec_bool select_d = vec_bool(n);
	vec_bool select_r = vec_bool(n);
	for(int i = 0; i < n; i++) {
		select_d[i] = true;
		select_r[i] = false;
	}
	//
	// only select component 0 of the range function
	// f_0 (x) = x_0 * x_{n-1}
	select_r[0] = true;
	//
	// loop over forward and reverse mode
	for(int mode = 0; mode < 2; mode++) {
		sparse_rc pat_out = sparse_rc();
		if( mode == 0  ) {
			af.for_hes_sparsity(select_d, select_r, pat_out);
		}
		if( mode == 1  ) {
			af.rev_hes_sparsity(select_d, select_r, pat_out);
		}
		//
		// check that result is sparsity pattern for Hessian of f_0 (x)
		ok = ok && pat_out.nnz() == 2 ;
		vec_int row = pat_out.row();
		vec_int col = pat_out.col();
		for(int k = 0; k < 2; k++) {
			int r = row[k];
			int c = col[k];
			if( r <= c  ) {
				ok = ok && r == 0;
				ok = ok && c == n-1;
			}
			if( r >= c  ) {
				ok = ok && r == n-1;
				ok = ok && c == 0;
			}
		}
	}
	//
	return( ok );
}
// END SOURCE
//
/*
$begin sparse_hes_pattern_xam.cpp$$
$spell
	cplusplus
	cppad
	py
	xam
	Jacobian
	Jacobians
$$
$section C++: Hessian Sparsity Patterns: Example and Test$$
$srcfile|lib/example/cplusplus/sparse_hes_pattern_xam.cpp|0|// BEGIN SOURCE|// END SOURCE|$$
$end
*/
//
