
// This file can be automatically generated using the following command
// m4 ../../xam/cplusplus.m4 ../../xam/a_fun_xam.xam > a_fun_xam.cpp
// -----------------------------------------------------------------------------
//         cppad_swig: A C++ Object Library and Swig Interface to Cppad
//          Copyright (C) 2017-17 Bradley M. Bell (bradbell@seanet.com)
//              This program is distributed under the terms of the
//          GNU Affero General Public License version 3.0 or later see
//                     http://www.gnu.org/licenses/agpl.txt
// -----------------------------------------------------------------------------
// std::vector<a_double>
// -----------------------------------------------------------------------------
// BEGIN SOURCE
# include <cstdio>
# include <cppad/swig/a_double.hpp>
# include <cppad/swig/a_fun.hpp>
# include <cppad/swig/function.hpp>
# include <cppad/swig/typedef.hpp>

bool a_fun_xam(void) {
	using cppad_swig::a_double;
	//
	// initialize return variable
	bool ok = true;
	size_t n = 2;
	//
	// create ax
	cppad_swig::vector_double x = cppad_swig::vector_double(n);
	for(size_t i = 0; i < n ; i++) {
		x[i] = i + 1.0;
	}
	cppad_swig::vector_ad ax = cppad_swig::independent(x);
	//
	// create af
	a_double ax0 = ax[0];
	a_double ax1 = ax[1];
	cppad_swig::vector_ad ay = cppad_swig::vector_ad(1);
	ay[0] = ax0 + ax0 - ax1;
	cppad_swig::a_fun af = cppad_swig::a_fun(ax, ay);
	//
	// zero order forward
	x[0] = 3.0;
	x[1] = 1.0;
	cppad_swig::vector_double y = af.forward(0, x);
	ok = ok && y[0] == 5.0;
	//
	// first order forward
	x[0] = 0.0;
	x[1] = 1.0;
	y = af.forward(1, x);
	ok = ok && y[0] == -1.0;
	//
	return( ok );
}
// END SOURCE
//
/*
$begin a_fun_xam.cpp$$
$spell
	cplusplus
	cppad
	xam
$$
$section cplusplus: a_fun Example and Test$$
$srcfile|lib/example/cplusplus/a_fun_xam.cpp|0|// BEGIN SOURCE|// END SOURCE|$$
$end
*/

