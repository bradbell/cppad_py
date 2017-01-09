/* ----------------------------------------------------------------------------
          cppad_swig: A C++ Object Library and Swig Interface to Cppad
           Copyright (C) 2017-17 Bradley M. Bell (bradbell@seanet.com)
               This program is distributed under the terms of the
           GNU Affero General Public License version 3.0 or later see
                      http://www.gnu.org/licenses/agpl.txt
---------------------------------------------------------------------------- */

// system includes
# include <iostream>
# include <cassert>

// external compiled tests
extern bool a_double_a_double_xam(void);
extern bool a_double_value_xam(void);
extern bool a_fun_a_fun_xam(void);
extern bool vector_ad_xam(void);
extern bool vector_double_xam(void);

namespace {
	// function that runs one test
	static size_t Run_ok_count    = 0;
	static size_t Run_error_count = 0;
	bool Run(bool TestOk(void), const char *name)
	{	bool ok = true;
		ok &= TestOk();
		if( ok )
		{	std::cout << "OK:    " << "cplusplus: " << name << std::endl;
			Run_ok_count++;
		}
		else
		{	std::cout << "Error: " << "cplusplus: " << name << std::endl;
			Run_error_count++;
		}
		return ok;
	}
}

// main program that runs all the tests
int main(void)
{	bool ok = true;
	//
	ok &= Run( a_double_a_double_xam,   "a_double_a_double_xam"  );
	ok &= Run( a_double_value_xam,      "a_double_value_xam"     );
	ok &= Run( a_fun_a_fun_xam,         "a_fun_a_fun_xam"        );
	ok &= Run( vector_ad_xam,           "vector_ad_xam"          );
	ok &= Run( vector_double_xam,       "vector_double_xam"      );
	//
	assert( ok || (Run_error_count > 0) );

	// convert int(size_t) to avoid warning on _MSC_VER systems
	if( ok )
		std::cout << "check_all: OK\n";
	else
		std::cout << int(Run_error_count) << " tests failed]\n";

	return static_cast<int>( ! ok );
}

