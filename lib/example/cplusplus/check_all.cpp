/* ----------------------------------------------------------------------------
          cppad_py: A C++ Object Library and Python Interface to Cppad
           Copyright (C) 2017-18 Bradley M. Bell (bradbell@seanet.com)
               This program is distributed under the terms of the
               GNU General Public License version 3.0 or later see
                     https://www.gnu.org/licenses/gpl-3.0.txt
---------------------------------------------------------------------------- */

// system includes
# include <iostream>
# include <cassert>

// external compiled tests
extern bool a_double_cond_assign_xam(void);
extern bool a_double_property_xam(void);
extern bool a_double_unary_fun_xam(void);
extern bool a_double_unary_op_xam(void);
extern bool a_double_assign_xam(void);
extern bool a_double_binary_xam(void);
extern bool a_double_compare_xam(void);
extern bool vector_size_xam(void);
extern bool vector_set_get_xam(void);
extern bool fun_property_xam(void);
extern bool fun_optimize_xam(void);
extern bool fun_jacobian_xam(void);
extern bool fun_hessian_xam(void);
extern bool fun_forward_xam(void);
extern bool fun_reverse_xam(void);
extern bool fun_abort_xam(void);
extern bool sparse_rc_xam(void);
extern bool sparse_rcd_xam(void);
extern bool sparse_jac_pattern_xam(void);
extern bool sparse_hes_pattern_xam(void);
extern bool sparse_jac_xam(void);
extern bool sparse_hes_xam(void);
extern bool error_message_xam(void);

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
	ok &= Run( a_double_cond_assign_xam,  "a_double_cond_assign_xam"  );
	ok &= Run( a_double_property_xam,     "a_double_property_xam"     );
	ok &= Run( a_double_unary_fun_xam,    "a_double_unary_fun_xam"    );
	ok &= Run( a_double_unary_op_xam,     "a_double_unary_op_xam"     );
	ok &= Run( a_double_assign_xam,       "a_double_assign_xam"       );
	ok &= Run( a_double_binary_xam,       "a_double_binary_xam"       );
	ok &= Run( a_double_compare_xam,      "a_double_compare_xam"      );
	ok &= Run( vector_size_xam,           "vector_size_xam"           );
	ok &= Run( vector_set_get_xam,        "vector_set_get_xam"        );
	ok &= Run( fun_property_xam,          "fun_property_xam"          );
	ok &= Run( fun_optimize_xam,          "fun_optimize_xam"        );
	ok &= Run( fun_jacobian_xam,          "fun_jacobian_xam"        );
	ok &= Run( fun_hessian_xam,           "fun_hessian_xam"         );
	ok &= Run( fun_forward_xam,           "fun_forward_xam"         );
	ok &= Run( fun_reverse_xam,           "fun_reverse_xam"         );
	ok &= Run( fun_abort_xam,             "fun_abort_xam"           );
	ok &= Run( sparse_rc_xam,             "sparse_rc_xam" );
	ok &= Run( sparse_rcd_xam,            "sparse_rcd_xam" );
	ok &= Run( sparse_jac_pattern_xam,    "sparse_jac_pattern_xam" );
	ok &= Run( sparse_jac_xam,            "sparse_jac_xam" );
	ok &= Run( sparse_hes_xam,            "sparse_jac_xam" );
	ok &= Run( sparse_hes_pattern_xam,    "sparse_hes_pattern_xam" );
	ok &= Run( error_message_xam,         "error_message_xam" );
	//
	assert( ok || (Run_error_count > 0) );

	// convert int(size_t) to avoid warning on _MSC_VER systems
	if( ok )
		std::cout << "check_all: OK\n";
	else
		std::cout << int(Run_error_count) << " tests failed]\n";

	return static_cast<int>( ! ok );
}
