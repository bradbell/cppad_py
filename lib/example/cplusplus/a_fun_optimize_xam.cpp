// This file can be generated in the lib/xam directory using the command:
// m4 -D Language_=cplusplus a_fun/optimize_xam.xam
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
# include <string>
# include <cppad/py/cppad_py.hpp>

bool a_fun_optimize_xam(void) {
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
	int n_ind = 1; // number of independent variables
	int n_dep = 1; // number of dependent variables
	int n_var = 1; // phantom variable at address 0
	int n_op = 1;  // special operator at beginning
	//
	// dimension some vectors
	vec_double x = cppad_py::vec_double(n_ind);
	vec_a_double ay = cppad_py::vec_a_double(n_dep);
	//
	// independent variables
	x[0] = 1.0;
	vec_a_double ax = cppad_py::independent(x);
	n_var = n_var + n_ind; // one for each indpendent
	n_op = n_op + n_ind;
	//
	// accumulate summation
	a_double ax0 = ax[0];
	a_double csum = cppad_py::a_double(0.0);
	csum = ax0 + ax0 + ax0 + ax0;
	n_var = n_var + 3; // one per + operator
	n_op = n_op + 3;
	//
	// define f(x) = y_0 = csum
	ay[0] = csum;
	a_fun af = cppad_py::a_fun(ax, ay);
	n_op = n_op + 1; // speical operator at end
	//
	// check number of variables and operators
	ok = ok && af.size_var() == n_var;
	ok = ok && af.size_op() == n_op;
	//
	// optimize
	af.optimize();
	//
	// number of variables and operators has decreased by two
	ok = ok && af.size_var() == n_var-2;
	ok = ok && af.size_op() == n_op-2;
	//
	return( ok  );
}
// END SOURCE
// -----------------------------------------------------------------------------
/*
$begin a_fun_optimize_xam.cpp$$
$spell
	cplusplus
	cppad
	py
	xam
	Jacobian
	Jacobians
$$
$section C++: Optimize an a_fun: Example and Test$$
$srcfile|build/lib/example/cplusplus/a_fun_optimize_xam.cpp|0|// BEGIN SOURCE|// END SOURCE|$$
$end
*/
//
