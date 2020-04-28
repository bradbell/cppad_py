// -----------------------------------------------------------------------------
//         cppad_py: A C++ Object Library and Python Interface to Cppad
//          Copyright (C) 2017-20 Bradley M. Bell (bradbell@seanet.com)
//              This program is distributed under the terms of the
//              GNU General Public License version 3.0 or later see
//                    https://www.gnu.org/licenses/gpl-3.0.txt
// -----------------------------------------------------------------------------
// d_fun properties
// -----------------------------------------------------------------------------
// BEGIN SOURCE
# include <cstdio>
# include <cppad/py/cppad_py.hpp>

bool fun_json_xam(void) {
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
// END SOURCE
// --------------------------------------------------------------------------
/*
$begin fun_to_json_xam.cpp$$
$spell
    json
$$
$section C++: to_json: Example and Test$$
$srcthisfile|0|// BEGIN SOURCE|// END SOURCE|$$
$end
*/
