/* -----------------------------------------------------------------------------
           cppad_swig: A C++ Object Library and Swig Interface to Cppad
            Copyright (C) 2017-17 Bradley M. Bell (bradbell@seanet.com)
                This program is distributed under the terms of the
                GNU General Public License version 3.0 or later see
                      https://www.gnu.org/licenses/gpl-3.0.txt
----------------------------------------------------------------------------- */
// BEGIN C++
# include "swig_xam.hpp"
# include <string>
# include <limits>

// factorial_by_value
int factorial_by_value(int n) {
	if (n <= 1) return 1;
	else return n * factorial_by_value(n - 1);
}

// message_of_void
const char* message_of_void(void)
{	return "OK";
}

// add_by_ptr
void add_by_ptr(int x, int y, int* result)
{	*result = x + y;
}

// max_array_by_ptr
int max_array_by_ptr(int n, const int* x)
{	int result = x[0];
	for(int i = 1; i < 10; i++)
		if( x[i] > result )
			result = x[i];
	return result;
}

// max_std_vector_double
double max_std_vector_double(const std::vector<double>& x)
{	double result = - std::numeric_limits<double>::infinity();
	for(size_t i = 0; i < x.size(); i++)
		if( x[i] > result )
			result = x[i];
	return result;
}

// raise_exception
const char* raise_exception(const char* message) throw(const char*)
{	// previous error message
	static std::string previous = "";
	if( message[0] == '\0' )
		return previous.c_str();
	previous = message;
	//
	// raise exception
	throw message;
	//
	// never get to here
	return "";
}
// END C++
/*
$begin swig_xam_function.cpp$$

$section Swig Example: C++ Function Implementation$$

$srcfile%swig_xam/function.cpp%0%// BEGIN C++%// END C++%$$

$end
--------------------------------------------------------------------------
*/
