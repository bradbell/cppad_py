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

bool sparse_jac_xam(void) {
	using cppad_py::a_double;
	using cppad_py::vec_int;
	using cppad_py::vec_double;
	using cppad_py::vec_a_double;
	using cppad_py::d_fun;
	using cppad_py::sparse_rc;
	using cppad_py::sparse_rcv;
	using cppad_py::sparse_jac_work;
	//
	// initialize return variable
	bool ok = true;
	//------------------------------------------------------------------------
	// number of dependent and independent variables
	int n = 3;
	// one
	a_double aone = a_double(1.0);
	//
	// create the independent variables ax
	vec_double x = vec_double(n);
	for(int i = 0; i < n ; i++) {
		x[i] = i + 2.0;
	}
	vec_a_double ax = cppad_py::independent(x);
	//
	// create dependent variables ay with ay[i] = (j+1) * ax[j]
	// where i = mod(j + 1, n)
	vec_a_double ay = vec_a_double(n);
	for(int j = 0; j < n ; j++) {
		int i = j+1;
		if( i >= n  ) {
			i = i - n;
		}
		a_double aj = a_double(j);
		a_double ay_i = (aj + aone) * ax[j];
		ay[i] = ay_i;
	}
	//
	// define af corresponding to f(x)
	d_fun f = d_fun(ax, ay);
	//
	// sparsity pattern for identity matrix
	sparse_rc pat_eye = sparse_rc();
	pat_eye.resize(n, n, n);
	for(int k = 0; k < n; k++) {
		pat_eye.put(k, k, k);
	}
	//
	// sparsity pattern for the Jacobian
	sparse_rc pat_jac = sparse_rc();
	f.for_jac_sparsity(pat_eye, pat_jac);
	//
	// loop over forward and reverse mode
	for(int mode = 0; mode < 2; mode++) {
		// compute all possibly non-zero entries in Jacobian
		sparse_rcv subset = sparse_rcv(pat_jac);
		// work space used to save time for multiple calls
		sparse_jac_work work = sparse_jac_work();
		if( mode == 0  ) {
			f.sparse_jac_for(subset, x, pat_jac, work);
		}
		if( mode == 1  ) {
			f.sparse_jac_rev(subset, x, pat_jac, work);
		}
		//
		// check result
		ok = ok && n == subset.nnz();
		vec_int col_major = subset.col_major();
		vec_int row = subset.row();
		vec_int col = subset.col();
		vec_double val = subset.val();
		for(int k = 0; k < n; k++) {
			int ell = col_major[k];
			int r = row[ell];
			int c = col[ell];
			double v = val[ell];
			int i = c+1;
			if( i >=  n  ) {
				i = i - n;
			}
			ok = ok && c == k;
			ok = ok && r == i;
			ok = ok && v == c + 1.0;
		}
	}
	//
	return( ok );
}
// END SOURCE
//
/*
$begin sparse_jac_xam.cpp$$
$spell
	cplusplus
	cppad
	py
	xam
	Jacobian
	Jacobians
$$
$section C++: Computing Sparse Jacobians: Example and Test$$
$srcfile|lib/example/cplusplus/sparse_jac_xam.cpp|0|// BEGIN SOURCE|// END SOURCE|$$
$end
*/
//
