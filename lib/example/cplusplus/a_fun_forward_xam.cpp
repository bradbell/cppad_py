// This file can be generated in the lib/xam directory using the command:
// m4 -D Language_=cplusplus a_fun/forward_xam.xam
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
# include <string>
# include <cppad/py/cppad_py.hpp>

bool a_fun_forward_xam(void) {
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
	// number of dependent and independent variables
	int n_dep = 1;
	int n_ind = 2;
	//
	// create the independent variables ax
	vec_double xp = cppad_py::vec_double(n_ind);
	for(int i = 0; i < n_ind ; i++) {
		xp[i] = i + 1.0;
	}
	vec_a_double ax = cppad_py::independent(xp);
	//
	// create dependent varialbes ay with ay0 = ax0 * ax1
	a_double ax0 = ax[0];
	a_double ax1 = ax[1];
	vec_a_double ay = cppad_py::vec_a_double(n_dep);
	ay[0] = ax0 * ax1;
	//
	// define af corresponding to f(x) = x0 * x1
	a_fun af = cppad_py::a_fun(ax, ay);
	//
	// define X(t) = (3 + t, 2 + t)
	// it follows that Y(t) = f(X(t)) = (3 + t) * (2 + t)
	//
	// Y(0) = 6 and p ! = 1
	int p = 0;
	xp[0] = 3.0;
	xp[1] = 2.0;
	vec_double yp = af.forward(p, xp);
	ok = ok && yp[0] == 6.0;
	//
	// first order Taylor coefficients for X(t)
	p = 1;
	xp[0] = 1.0;
	xp[1] = 1.0;
	//
	// first order Taylor coefficient for Y(t)
	// Y'(0) = 3 + 2 = 5 and p ! = 1
	yp = af.forward(p, xp);
	ok = ok && yp[0] == 5.0;
	//
	// second order Taylor coefficients for X(t)
	p = 2;
	xp[0] = 0.0;
	xp[1] = 0.0;
	//
	// second order Taylor coefficient for Y(t)
	// Y''(0) = 2.0 and p ! = 2
	yp = af.forward(p, xp);
	ok = ok && yp[0] == 1.0;
	//
	return( ok );
}
// END SOURCE
//
/*
$begin a_fun_forward_xam.cpp$$
$spell
	cplusplus
	cppad
	py
	xam
	Jacobian
	Jacobians
$$
$section C++: Forward Mode AD: Example and Test$$
$srcfile|lib/example/cplusplus/a_fun_forward_xam.cpp|0|// BEGIN SOURCE|// END SOURCE|$$
$end
*/
//
