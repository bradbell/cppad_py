// -----------------------------------------------------------------------------
//         cppad_py: A C++ Object Library and Python Interface to Cppad
//          Copyright (C) 2017-18 Bradley M. Bell (bradbell@seanet.com)
//              This program is distributed under the terms of the
//              GNU General Public License version 3.0 or later see
//                    https://www.gnu.org/licenses/gpl-3.0.txt
// -----------------------------------------------------------------------------
// a_double assignment
// -----------------------------------------------------------------------------
// BEGIN SOURCE
# include <cstdio>
# include <cppad/py/cppad_py.hpp>

bool a_double_assign_xam(void) {
	using cppad_py::a_double;
	//
	// initialize return variable
	bool ok = true;
	//------------------------------------------------------------------------
	a_double x(2.0);
	//
	x = 3.0;
	ok = ok && x == 3.0;
	//
	x += 2.0;
	ok = ok && x == 5.0;
	//
	x -= 1.0;
	ok = ok && x == 4.0;
	//
	x *= 3.0;
	ok = ok && x == 12.0;
	//
	x /= 4.0;
	ok = ok && x == 3.0;
	//
	return( ok );
}
// END SOURCE
//
/*
$begin a_double_assign_xam.cpp$$
$spell
	cplusplus
	cppad
	py
	xam
	Jacobian
	Jacobians
$$
$section C++: a_double Assignment Operators: Example and Test$$
$srcfile|lib/example/cplusplus/a_double_assign_xam.cpp|0|// BEGIN SOURCE|// END SOURCE|$$
$end
*/
//
