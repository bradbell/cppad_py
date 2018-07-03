// This file can be generated in the lib/xam directory using the command:
// m4 -D Language_=cplusplus a_double/unary_op_xam.xam
// -----------------------------------------------------------------------------
//         cppad_py: A C++ Object Library and Python Interface to Cppad
//          Copyright (C) 2017-18 Bradley M. Bell (bradbell@seanet.com)
//              This program is distributed under the terms of the
//              GNU General Public License version 3.0 or later see
//                    https://www.gnu.org/licenses/gpl-3.0.txt
// -----------------------------------------------------------------------------
// a_double unary operators
// -----------------------------------------------------------------------------
// BEGIN SOURCE
// This test fails in Octave and so is skipped by make check_lib_octave
# include <cstdio>
# include <cppad/py/cppad_py.hpp>

bool a_double_unary_op_xam(void) {
	using cppad_py::a_double;
	//
	// initialize return variable
	bool ok = true;
	//------------------------------------------------------------------------
	a_double two = cppad_py::a_double(2.0);
	a_double plus_two = + two ;
	a_double minus_two = - two ;
	//
	ok = ok && plus_two.value() == 2.0;
	ok = ok && minus_two.value() == -2.0;
	//
	return( ok );
}
// END SOURCE
//
/*
$begin a_double_unary_op_xam.cpp$$
$spell
	cplusplus
	cppad
	py
	xam
	Jacobian
	Jacobians
$$
$section C++: a_double Unary Plus and Minus: Example and Test$$
$srcfile|lib/example/cplusplus/a_double_unary_op_xam.cpp|0|// BEGIN SOURCE|// END SOURCE|$$
$end
*/
//
