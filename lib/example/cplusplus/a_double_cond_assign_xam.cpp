// -----------------------------------------------------------------------------
//         cppad_py: A C++ Object Library and Python Interface to Cppad
//          Copyright (C) 2017-18 Bradley M. Bell (bradbell@seanet.com)
//              This program is distributed under the terms of the
//              GNU General Public License version 3.0 or later see
//                    https://www.gnu.org/licenses/gpl-3.0.txt
// -----------------------------------------------------------------------------
// a_double conditional assignment
// -----------------------------------------------------------------------------
// BEGIN SOURCE
# include <cstdio>
# include <cppad/py/cppad_py.hpp>

bool a_double_cond_assign_xam(void) {
	using cppad_py::a_double;
	using cppad_py::vec_double;
	using cppad_py::vec_a_double;
	using cppad_py::d_fun;
	//
	// initialize return variable
	bool ok = true;
	//------------------------------------------------------------------------
	int n_ind = 4;
	int n_dep = 1;
	//
	// create ax (value of independent variables does not matter)
	vec_double x(n_ind);
	x[0] = 0.0;
	x[1] = 1.0;
	x[2] = 2.0;
	x[3] = 3.0;
	vec_a_double ax = cppad_py::independent(x);
	//
	// arguments to conditional assignment
	a_double left = ax[0];
	a_double right = ax[1];
	a_double if_true = ax[2];
	a_double if_false = ax[3];
	//
	// assignment
	a_double target;
	target.cond_assign(
		"<",
		left,
		right,
		if_true,
		if_false
	);
	//
	// f(x) = taget
	vec_a_double ay(n_dep);
	ay[0] = target;
	d_fun f(ax, ay);
	//
	// assignment with different independent variable values
	x[0] = 9.0; // left
	x[1] = 8.0; // right
	x[2] = 7.0; // if_true
	x[3] = 6.0; // if_false
	int p = 0;
	vec_double y = f.forward(p, x);
	ok = ok && y[0] == 6.0;
	//
	return( ok  );
}
// END SOURCE
//
/*
$begin a_double_cond_assign_xam.cpp$$
$spell
	cplusplus
	cppad
	py
	xam
	Jacobian
	Jacobians
$$
$section C++: a_double Conditional Assignment: Example and Test$$
$srcfile|lib/example/cplusplus/a_double_cond_assign_xam.cpp|0|// BEGIN SOURCE|// END SOURCE|$$
$end
*/
//
