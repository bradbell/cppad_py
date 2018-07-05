// -----------------------------------------------------------------------------
//         cppad_py: A C++ Object Library and Python Interface to Cppad
//          Copyright (C) 2017-18 Bradley M. Bell (bradbell@seanet.com)
//              This program is distributed under the terms of the
//              GNU General Public License version 3.0 or later see
//                    https://www.gnu.org/licenses/gpl-3.0.txt
// -----------------------------------------------------------------------------
// a_double comparision operators
// -----------------------------------------------------------------------------
// BEGIN SOURCE
# include <cstdio>
# include <cppad/py/cppad_py.hpp>

bool a_double_compare_xam(void) {
	using cppad_py::a_double;
	//
	// initialize return variable
	bool ok = true;
	//------------------------------------------------------------------------
	a_double two = a_double(2.0);
	a_double three = a_double(3.0);
	//
	ok = ok && two   <  three;
	ok = ok && two   <= three;
	ok = ok && three >  two;
	ok = ok && three >= two;
	ok = ok && three != two;
	ok = ok && three == three;
	//
	ok = ok && ! (two >  three) ;
	ok = ok && ! (two >= three) ;
	ok = ok && ! (two == three) ;
	//
	return( ok );
}
// END SOURCE
//
/*
$begin a_double_compare_xam.cpp$$
$spell
	cplusplus
	cppad
	py
	xam
	Jacobian
	Jacobians
$$
$section C++: a_double Comparison Operators: Example and Test$$
$srcfile|lib/example/cplusplus/a_double_compare_xam.cpp|0|// BEGIN SOURCE|// END SOURCE|$$
$end
*/
//
