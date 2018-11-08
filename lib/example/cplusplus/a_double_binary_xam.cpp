// -----------------------------------------------------------------------------
//         cppad_py: A C++ Object Library and Python Interface to Cppad
//          Copyright (C) 2017-18 Bradley M. Bell (bradbell@seanet.com)
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
	//
	// initialize return variable
	bool ok = true;
	//------------------------------------------------------------------------
	a_double two(2.0);
	a_double three(3.0);
	//
	a_double five = two + three;
	a_double six = two * three;
	a_double neg_one = two - three;
	a_double two_thirds = two / three;
	//
	ok = ok && five.value() == 5.0;
	ok = ok && six.value() == 6.0;
	ok = ok && neg_one.value() == -1.0;
	ok = ok && 0.5 < two_thirds.value();
	ok = ok && two_thirds.value() < 1.0;
	ok = ok && five < six;
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
$srcfile|lib/example/cplusplus/a_double_binary_xam.cpp|0|// BEGIN SOURCE|// END SOURCE|$$
$end
*/
//
