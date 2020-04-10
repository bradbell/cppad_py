// -----------------------------------------------------------------------------
//         cppad_py: A C++ Object Library and Python Interface to Cppad
//          Copyright (C) 2017-20 Bradley M. Bell (bradbell@seanet.com)
//              This program is distributed under the terms of the
//              GNU General Public License version 3.0 or later see
//                    https://www.gnu.org/licenses/gpl-3.0.txt
// -----------------------------------------------------------------------------
// fun_dynamid
// -----------------------------------------------------------------------------
// BEGIN SOURCE
# include <cstdio>
# include <cppad/py/cppad_py.hpp>

bool fun_dynamic_xam(void) {
	using cppad_py::a_double;
	using cppad_py::vec_double;
	using cppad_py::vec_a_double;
	using cppad_py::d_fun;
	//
	// initialize return variable
	bool ok = true;
	//------------------------------------------------------------------------
	int nx = 2;
	int nd = 2;
	//
	// value of independent variables during recording
	vec_double x(nx);
	for(int i = 0; i < nx ; i++) {
		x[i] = i + 1.0;
	}
	//
	// value of independent dynamic parameters during recording
	vec_double dynamic(nd);
	for(int i = 0; i < nd ; i++) {
		dynamic[i] = i + x[nx-1] + 1.0;
	}
	vec_a_double a_both = cppad_py::independent(x, dynamic);
	//
	// extract vector of independent variables and dynamic parameters
	vec_a_double ax(nx), adynamic(nd);
	for(int i = 0; i < nx ; i++) {
		ax[i] = a_both[i];
	}
	for(int i = 0; i < nd ; i++) {
		adynamic[i] = a_both[nx + i];
	}
	//
	// create another dynamic paramerer
	a_double adyn  = adynamic[0] + adynamic[1];
	//
	// create another variable
	a_double avar  = ax[0] + ax[1] + adyn;
	//
	// create f(x) = x[0] + x[1] + dynamic[0] + dynamic[1]
	vec_a_double ay(1);
	ay[0] = avar;
	d_fun f(ax, ay);
	//
	// check some properties of f
	ok &= f.size_domain() == nx;
	ok &= f.size_order()  == 0;
	//
	// zero order forward mode using same values as during the recording
	vec_double y(1);
	y   = f.forward(0, x);
	ok &= y[0] == (x[0] + x[1] + dynamic[0] + dynamic[1]);
	//
	// zero order forward mode using different value for dynamic parameters
	dynamic[0] = dynamic[0] + 1.0;
	dynamic[1] = dynamic[1] + 1.0;
	f.new_dynamic(dynamic);
	y   = f.forward(0, x);
	ok &= y[0] == (x[0] + x[1] + dynamic[0] + dynamic[1]);
	//
	return( ok );
}
// END SOURCE
//
/*
$begin fun_dynamic_xam.cpp$$
$spell
$$
$section C++: Using Dynamic Parameters: Example and Test$$
$srcthisfile|0|// BEGIN SOURCE|// END SOURCE|$$
$end
*/
//
