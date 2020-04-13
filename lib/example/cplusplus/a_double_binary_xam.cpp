// -----------------------------------------------------------------------------
//         cppad_py: A C++ Object Library and Python Interface to Cppad
//          Copyright (C) 2017-20 Bradley M. Bell (bradbell@seanet.com)
//              This program is distributed under the terms of the
//              GNU General Public License version 3.0 or later see
//                    https://www.gnu.org/licenses/gpl-3.0.txt
// -----------------------------------------------------------------------------
// a_double binary operations
// -----------------------------------------------------------------------------
// BEGIN SOURCE
# include <cstdio>
# include <cppad/py/cppad_py.hpp>

bool a_double_binary_xam(void) {
	using cppad_py::a_double;
	bool ok      = true;
	a_double a2  = 2.0;
	a_double a3(3.0);
	// -----------------------------------------------------------------------
	a_double a5       = a2 + a3;
	a_double a6       = a2 * a3;
	a_double a1_minus = a2 - a3;
	a_double a23      = a2 / a3;
	//
	ok = ok && a5 == 5.0;
	ok = ok && a6 == 6.0;
	ok = ok && a1_minus == -1.0;
	ok = ok && a23.near_equal( a_double(2.0 / 3.0 ) );
	// -----------------------------------------------------------------------
	a5       = a2 + 3.0;
	a6       = a2 * 3.0;
	a1_minus = a2 - 3.0;
	a23      = a2 / 3.0;
	//
	ok = ok && a5 == 5.0;
	ok = ok && a6 == 6.0;
	ok = ok && a1_minus == -1.0;
	ok = ok && a23.near_equal( a_double(2.0 / 3.0 ) );
	// -----------------------------------------------------------------------
	a_double a8 = a2.pow(a3);
	a_double a9 = a3.pow(2.0);
	ok = ok && a8.near_equal( a_double(8.0) );
	ok = ok && a9.near_equal( a_double(9.0) );
	//
	return( ok );
}
// END SOURCE
//
/*
$begin a_double_binary_xam.cpp$$
$spell
	cplusplus
	cppad
	py
	xam
	Jacobian
	Jacobians
$$
$section C++: a_double Binary Operators With AD Result: Example and Test$$
$srcthisfile|0|// BEGIN SOURCE|// END SOURCE|$$
$end
*/
//
