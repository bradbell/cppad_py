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
# include <cstdio>
# include <cppad/py/cppad_py.hpp>

bool a_double_unary_fun_xam(void) {
	using cppad_py::a_double;
	//
	// initialize return variable
	bool ok = true;
	//------------------------------------------------------------------------
	//
	// fabs
	a_double one(1.0);
	a_double abs_one = one.fabs();
	ok = ok && abs_one.value() == 1.0;
	//
	// pi/4
	a_double pi_4 = one.atan();
	//
	// sqrt(2)
	a_double tmp(2.0);
	a_double r2 = tmp.sqrt();
	//
	// sin(pi/4)  * sqrt(2) = 1.0;
	tmp = r2 * pi_4.sin() ;
	ok = ok && tmp.near_equal(one) ;
	//
	// cos(pi/4)  * sqrt(2) = 1.0;
	tmp = r2 * pi_4.cos() ;
	ok = ok && tmp.near_equal(one) ;
	//
	// tan(pi/4)  = 1.0;
	tmp = pi_4.tan() ;
	ok = ok && tmp.near_equal(one) ;
	//
	return( ok );
}
// END SOURCE
//
/*
$begin a_double_unary_fun_xam.cpp$$
$spell
	cplusplus
	cppad
	py
	xam
	Jacobian
	Jacobians
$$
$section C++: a_double Unary Functions with AD Result: Example and Test$$
$srcfile|lib/example/cplusplus/a_double_unary_fun_xam.cpp|0|// BEGIN SOURCE|// END SOURCE|$$
$end
*/
//
