// This file can be automatically generaeted using the following command
// m4 ../../xam/cplusplus.m4 ../../xam/vector_ad_xam.xam > vector_ad_xam.cpp
// -----------------------------------------------------------------------------
//         cppad_swig: A C++ Object Library and Swig Interface to Cppad
//          Copyright (C) 2017-17 Bradley M. Bell (bradbell@seanet.com)
//              This program is distributed under the terms of the
//          GNU Affero General Public License version 3.0 or later see
//                     http://www.gnu.org/licenses/agpl.txt
// -----------------------------------------------------------------------------
// std::vector<a_double>
// -----------------------------------------------------------------------------
# include <cstdio>
# include <cppad/swig/a_double.hpp>
# include <cppad/swig/a_fun.hpp>
# include <cppad/swig/function.hpp>
# include <cppad/swig/typedef.hpp>

bool vector_ad_xam(void) {
	using cppad_swig::a_double;
	//
	// initialize return variable
	bool ok = true;
	size_t n = 4;
	cppad_swig::vector_ad a_vec = cppad_swig::vector_ad(n);
	//
	// check size
	ok = ok && a_vec.size() == n;
	//
	// setting elements
	for(size_t i = 0; i < n ; i++) {
		cppad_swig::a_double ad = cppad_swig::a_double(2.0 * i);
		a_vec[i] = ad;
	}
	// getting elements
	for(size_t i = 0; i < n ; i++) {
		cppad_swig::a_double a_element = a_vec[i];
		ok = ok && a_element.value() == 2.0 * i;
	}
	return( ok );
}
