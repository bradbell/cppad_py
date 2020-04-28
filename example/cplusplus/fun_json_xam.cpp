// -----------------------------------------------------------------------------
//         cppad_py: A C++ Object Library and Python Interface to Cppad
//          Copyright (C) 2017-20 Bradley M. Bell (bradbell@seanet.com)
//              This program is distributed under the terms of the
//              GNU General Public License version 3.0 or later see
//                    https://www.gnu.org/licenses/gpl-3.0.txt
// -----------------------------------------------------------------------------
// d_fun properties
// -----------------------------------------------------------------------------
# include <limits>
# include <cmath>
# include <cppad/py/cppad_py.hpp>

// ==========================================================================
namespace { // begin empty namespace
// ==========================================================================

// BEGIN_TO_JSON_XAM
bool to_json_xam(void) {
	using cppad_py::a_double;
	using cppad_py::vec_double;
	using cppad_py::vec_a_double;
	using cppad_py::d_fun;
	using cppad_py::a_fun;
	//
	// initialize return variable
	bool ok = true;
	// ----------------------------------------------------------------------
	int n = 1; // number of independent variables
	int m = 2; // number of dependent variables
	//
	// dimension some vectors
	vec_double x(n);
	vec_a_double ay(m);
	//
	// independent variables
	x[0]            = 1.0;
	vec_a_double ax = cppad_py::independent(x);
	//
	// f(x) = [ x0 + x0, sin(x0) ]
	ay[0] = ax[0] + ax[0];
	ay[1] = ax[0].sin();
	d_fun f(ax, ay);
	//
	std::string json = f.to_json();
	size_t pos       = json.find("\"op_code\"");
	size_t start     = json.find(":", pos) + 1;
	size_t end       = json.find(",", pos);
	int op_code      = std::atoi( json.substr(start, end - start).c_str() );
	ok              &= op_code == 1;
	pos              = json.find("\"name\"", pos);
	start            = json.find(":", pos);
	start            = json.find("\"", start + 1) + 1;
	end              = json.find("\"", start + 1);
	std::string name = json.substr(start, end - start);
	ok              &= name == "add" || name == "sin";
    //
	return( ok  );
}
// END_TO_JSON_XAM
/*
$begin fun_to_json_xam.cpp$$
$spell
    json
$$
$section C++: to_json: Example and Test$$
$srcthisfile|0|// BEGIN_TO_JSON_XAM|// END_TO_JSON_XAM|$$
$end
-----------------------------------------------------------------------------
*/
// BEGIN_FROM_JSON_XAM
bool from_json_xam(void) {
	using cppad_py::a_double;
	using cppad_py::vec_double;
	using cppad_py::vec_a_double;
	using cppad_py::d_fun;
	using cppad_py::a_fun;
	//
	// initialize return variable
	bool ok = true;
	// ----------------------------------------------------------------------
	// AD graph repersentation of f(x) = sin(x) / cos(x)
	//
	// node_1 : x[0]
	// node_2 : sin( x[0] )
	// node_3 : cos( x[0] )
	// node_4 : sin( x[0] ) / cos( x[0] )
	// y[0]   = sin( x[0] ) / cos( x[0] )
	// use single quote to avodi having to escape double quote
	std::string json =
		"{\n"
		"	'function_name' : 'tangent function',\n"
		"	'op_define_vec' : [ 3, [\n"
		"		{ 'op_code':1, 'name':'sin', 'n_arg':1 } ,\n"
		"		{ 'op_code':2, 'name':'cos', 'n_arg':1 } ,\n"
		"		{ 'op_code':3, 'name':'div', 'n_arg':2 } ]\n"
		"	],\n"
		"	'n_dynamic_ind'  : 0,\n"
		"	'n_variable_ind' : 1,\n"
		"	'constant_vec'   : [ 0, [ ] ],\n"
		"	'op_usage_vec'   : [ 3, [\n"
		"		[ 1, 1 ]   ,\n"  // node_2: sin(x[0])
		"		[ 2, 1 ]   ,\n"  // node_3: cos(x[0])
		"		[ 3, 2, 3] ]\n"  // node_4: sin(x[0]) / cos(x[0])
		"	],\n"
		"	'dependent_vec' : [ 1, [4] ]\n"
		"}\n";
	// convert the single quote to double quote
	for(size_t i = 0; i < json.size(); ++i)
		if( json[i] == '\'' )
			json[i] = '"';
	//
	// convert json to a fucntion object
	vec_a_double ax(0), ay(0); // construct an empty function
	d_fun f(ax, ay);
	f.from_json(json);
	//
	// compute y = f(x)
	vec_double x(1), y(1);
	x[0]  = 1.0;
	y     = f.forward(0, x);
	//
	// check the function value
	double eps99     = std::numeric_limits<double>::epsilon();
	double check     = std::tan(x[0]);
	double rel_error = y[0] / check - 1.0;
	ok              &= std::fabs( rel_error ) < eps99;
    //
	return ok;
}
// END_FROM_JSON_XAM
// --------------------------------------------------------------------------
/*
$begin fun_from_json_xam.cpp$$
$spell
    json
$$
$section C++: to_json: Example and Test$$
$srcthisfile|0|// BEGIN_FROM_JSON_XAM|// END_FROM_JSON_XAM|$$
$end
*/
// ==========================================================================
} // end empty namespace
// ==========================================================================

bool fun_json_xam(void)
{	bool ok = true;
	ok     &= to_json_xam();
	ok     &= from_json_xam();
	return ok;
}
