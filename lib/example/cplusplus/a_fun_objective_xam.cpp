// -----------------------------------------------------------------------------
//         cppad_py: A C++ Object Library and Python Interface to Cppad
//          Copyright (C) 2017-18 Bradley M. Bell (bradbell@seanet.com)
//              This program is distributed under the terms of the
//              GNU General Public License version 3.0 or later see
//                    https://www.gnu.org/licenses/gpl-3.0.txt
// -----------------------------------------------------------------------------
// forward
// -----------------------------------------------------------------------------
// BEGIN SOURCE
# include <cstdio>
# include <cppad/py/cppad_py.hpp>

bool a_fun_objective_xam(void) {
	using cppad_py::a_double;
	using cppad_py::vec_double;
	using cppad_py::vec_a_double;
	using cppad_py::a_fun;
	//
	// initialize return variable
	bool ok = true;
	//------------------------------------------------------------------------
	// number of dependent and independent variables
	int n_dep = 1;
	int n_ind = 2;
	//
	// create the independent variables ax
	vec_double xp = vec_double(n_ind);
	for(int i = 0; i < n_ind ; i++) {
		xp[i] = i + 1.0;
	}
	vec_a_double ax = cppad_py::independent(xp);
	//
	// create dependent varialbes ay with ay0 = ax0 * ax1
	a_double ax0 = ax[0];
	a_double ax1 = ax[1];
	vec_a_double ay = vec_a_double(n_dep);
	ay[0] = ax0 * ax1;
	//
	// define af corresponding to f(x) = x0 * x1
	a_fun af = a_fun(ax, ay);
	//
	// define X(t) = (3 + t, 2 + t)
	// it follows that Y(t) = f(X(t)) = (3 + t) * (2 + t)
	//
	// Y(0) = 6
	xp[0] = 3.0;
	xp[1] = 2.0;
	vec_double yp = af.objective(xp);
	ok = ok && yp[0] == 6.0;
	//
	return( ok );
}
// END SOURCE
//
/*
$begin a_fun_objective_xam.cpp$$
$spell
	cplusplus
	cppad
	py
	xam
	Jacobian
	Jacobians
$$
$section C++: Forward Mode AD: Example and Test$$
$srcfile|lib/example/cplusplus/a_fun_objective_xam.cpp|0|// BEGIN SOURCE|// END SOURCE|$$
$end
*/
//
