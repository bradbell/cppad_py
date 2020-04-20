// -----------------------------------------------------------------------------
//         cppad_py: A C++ Object Library and Python Interface to Cppad
//          Copyright (C) 2017-20 Bradley M. Bell (bradbell@seanet.com)
//              This program is distributed under the terms of the
//              GNU General Public License version 3.0 or later see
//                    https://www.gnu.org/licenses/gpl-3.0.txt
// -----------------------------------------------------------------------------
// abort_recording
// -----------------------------------------------------------------------------
// BEGIN SOURCE
# include <cstdio>
# include <cppad/py/cppad_py.hpp>

bool fun_abort_xam(void) {
	using cppad_py::a_double;
	using cppad_py::vec_double;
	using cppad_py::vec_a_double;
	using cppad_py::d_fun;
	//
	// initialize return variable
	bool ok = true;
	//------------------------------------------------------------------------
	int n_ind = 2;
	//
	// create ax
	vec_double x(n_ind);
	for(int i = 0; i < n_ind ; i++) {
		x[i] = i + 1.0;
	}
	vec_a_double ax = cppad_py::independent(x);
	//
	// preform some a_double operations
	a_double ax0 = ax[0];
	a_double ax1 = ax[1];
	a_double ay = ax0 + ax1;
	//
	// check that ay is a variable; its value depends on the value of ax
	ok = ok && ay.variable();
	//
	// abort this recording
	cppad_py::abort_recording();
	//
	// check that ay is now a parameter, no longer a variable.
	ok = ok && ay.parameter();
	//
	// since it is a parameter, we can retrieve its value
	double y = ay.value();
	//
	// its value should be x0 + x1
	ok = ok && y  == x[0] + x[1];
	//
	// an abort when not recording has no effect
	cppad_py::abort_recording();
	//
	return( ok );
}
// END SOURCE
//
/*
$begin fun_abort_xam.cpp$$
$spell
	cplusplus
	cppad
	py
	xam
	Jacobian
	Jacobians
$$
$section C++: Abort Recording a_double Operations: Example and Test$$
$srcthisfile|0|// BEGIN SOURCE|// END SOURCE|$$
$end
*/
//
