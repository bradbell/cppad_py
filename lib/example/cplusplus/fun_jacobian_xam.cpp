// -----------------------------------------------------------------------------
//         cppad_py: A C++ Object Library and Python Interface to Cppad
//          Copyright (C) 2017-18 Bradley M. Bell (bradbell@seanet.com)
//              This program is distributed under the terms of the
//              GNU General Public License version 3.0 or later see
//                    https://www.gnu.org/licenses/gpl-3.0.txt
// -----------------------------------------------------------------------------
// jacobian
// -----------------------------------------------------------------------------
// BEGIN SOURCE
# include <cstdio>
# include <cppad/py/cppad_py.hpp>

bool a_fun_jacobian_xam(void) {
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
	int n_ind = 3;
	//
	// create the independent variables ax
	vec_double x = vec_double(n_ind);
	for(int i = 0; i < n_ind ; i++) {
		x[i] = i + 2.0;
	}
	vec_a_double ax = cppad_py::independent(x);
	//
	// create dependent variables ay with ay0 = ax_0 * ax_1 * ax_2
	a_double ax_0 = ax[0];
	a_double ax_1 = ax[1];
	a_double ax_2 = ax[2];
	vec_a_double ay = vec_a_double(n_dep);
	ay[0] = ax_0 * ax_1 * ax_2;
	//
	// define af corresponding to f(x) = x_0 * x_1 * x_2
	a_fun af = a_fun(ax, ay);
	//
	// compute the Jacobian f'(x) = ( x_1*x_2, x_0*x_2, x_0*x_1 )
	vec_double fp = af.jacobian(x);
	//
	// check Jacobian
	double x_0 = x[0];
	double x_1 = x[1];
	double x_2 = x[2];
	ok = ok && fp[0 * n_ind + 0] == x_1 * x_2 ;
	ok = ok && fp[0 * n_ind + 1] == x_0 * x_2 ;
	ok = ok && fp[0 * n_ind + 2] == x_0 * x_1 ;
	//
	return( ok );
}
// END SOURCE
//
/*
$begin fun_jacobian_xam.cpp$$
$spell
	cplusplus
	cppad
	py
	xam
	Jacobian
	Jacobians
$$
$section C++: Dense Jacobian Using AD: Example and Test$$
$srcfile|lib/example/cplusplus/fun_jacobian_xam.cpp|0|// BEGIN SOURCE|// END SOURCE|$$
$end
*/
//
