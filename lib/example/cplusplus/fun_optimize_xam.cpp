// -----------------------------------------------------------------------------
//         cppad_py: A C++ Object Library and Python Interface to Cppad
//          Copyright (C) 2017-18 Bradley M. Bell (bradbell@seanet.com)
//              This program is distributed under the terms of the
//              GNU General Public License version 3.0 or later see
//                    https://www.gnu.org/licenses/gpl-3.0.txt
// -----------------------------------------------------------------------------
// optimize
// -----------------------------------------------------------------------------
// BEGIN SOURCE
# include <cstdio>
# include <cppad/py/cppad_py.hpp>

bool d_fun_optimize_xam(void) {
	using cppad_py::a_double;
	using cppad_py::vec_double;
	using cppad_py::vec_a_double;
	using cppad_py::d_fun;
	//
	// initialize return variable
	bool ok = true;
	//------------------------------------------------------------------------
	int n_ind = 1; // number of independent variables
	int n_dep = 1; // number of dependent variables
	int n_var = 1; // phantom variable at address 0
	int n_op = 1;  // special operator at beginning
	//
	// dimension some vectors
	vec_double x = vec_double(n_ind);
	vec_a_double ay = vec_a_double(n_dep);
	//
	// independent variables
	x[0] = 1.0;
	vec_a_double ax = cppad_py::independent(x);
	n_var = n_var + n_ind; // one for each indpendent
	n_op = n_op + n_ind;
	//
	// accumulate summation
	a_double ax0 = ax[0];
	a_double csum = a_double(0.0);
	csum = ax0 + ax0 + ax0 + ax0;
	n_var = n_var + 3; // one per + operator
	n_op = n_op + 3;
	//
	// define f(x) = y_0 = csum
	ay[0] = csum;
	d_fun f = d_fun(ax, ay);
	n_op = n_op + 1; // speical operator at end
	//
	// check number of variables and operators
	ok = ok && f.size_var() == n_var;
	ok = ok && f.size_op() == n_op;
	//
	// optimize
	f.optimize();
	//
	// number of variables and operators has decreased by two
	ok = ok && f.size_var() == n_var-2;
	ok = ok && f.size_op() == n_op-2;
	//
	return( ok  );
}
// END SOURCE
// -----------------------------------------------------------------------------
/*
$begin fun_optimize_xam.cpp$$
$spell
	cplusplus
	cppad
	py
	xam
	Jacobian
	Jacobians
$$
$section C++: Optimize an d_fun: Example and Test$$
$srcfile|lib/example/cplusplus/fun_optimize_xam.cpp|0|// BEGIN SOURCE|// END SOURCE|$$
$end
*/
//
