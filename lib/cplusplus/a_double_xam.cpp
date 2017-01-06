// This file can be automatically generaeted using the following command
// m4 ../cpp.m4 ../xam/a_double_xam.m4 > a_double_xam.cpp
// -----------------------------------------------------------------------------
//         cppad_swig: A C++ Object Library and Swig Interface to Cppad
//          Copyright (C) 2017-17 Bradley M. Bell (bradbell@seanet.com)
//              This program is distributed under the terms of the
//          GNU Affero General Public License version 3.0 or later see
//                     http://www.gnu.org/licenses/agpl.txt
// -----------------------------------------------------------------------------
// a_double
// -----------------------------------------------------------------------------
# include <cstdio>
# include <cppad/swig/a_double.hpp>
# include <cppad/swig/a_fun.hpp>
# include <cppad/swig/function.hpp>
# include <cppad/swig/typedef.hpp>

bool a_double_xam(void) {
	using cppad_swig::a_double;
	//
	// initialize return variable
	bool ok = true;
	a_double two = cppad_swig::a_double(2.0);
	a_double three = cppad_swig::a_double(3.0);
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
