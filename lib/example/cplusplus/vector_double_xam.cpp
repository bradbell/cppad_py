
// This file can be automatically generaeted using the following command
// m4 ../../xam/cplusplus.m4 ../../xam/vector_double_xam.xam > vector_double_xam.cpp
// -----------------------------------------------------------------------------
//         cppad_swig: A C++ Object Library and Swig Interface to Cppad
//          Copyright (C) 2017-17 Bradley M. Bell (bradbell@seanet.com)
//              This program is distributed under the terms of the
//          GNU Affero General Public License version 3.0 or later see
//                     http://www.gnu.org/licenses/agpl.txt
// -----------------------------------------------------------------------------
// std::vector<double>
// -----------------------------------------------------------------------------
// BEGIN SOURCE
# include <cstdio>
# include <cppad/swig/a_double.hpp>
# include <cppad/swig/a_fun.hpp>
# include <cppad/swig/function.hpp>
# include <cppad/swig/typedef.hpp>

bool vector_double_xam(void) {
	using cppad_swig::a_double;
	//
	// initialize return variable
	bool ok = true;
	size_t n = 4;
	cppad_swig::vector_double vec = cppad_swig::vector_double(n);
	//
	// check size
	ok = ok && vec.size() == n;
	//
	// setting elements
	for(size_t i = 0; i < n ; i++) {
		vec[i] = 2.0 * i;
	}
	// getting elements
	for(size_t i = 0; i < n ; i++) {
		double element = vec[i];
		ok = ok && element == 2.0 * i;
	}
	return( ok );
}
// END SOURCE
//
/*
$begin vector_double_xam.cpp$$
$spell
	cplusplus
	cppad
	xam
$$
$section cppad_swig: vector_double_xam: Example and Test$$
$srcfile|lib/example/cplusplus/vector_double_xam.cpp|0|// BEGIN SOURCE|// END SOURCE|$$
$end
*/

