// This file can be generated in the lib/xam directory using the command:
// m4 -D Language_=cplusplus error/message_xam.xam
// -----------------------------------------------------------------------------
//         cppad_py: A C++ Object Library and Python Interface to Cppad
//          Copyright (C) 2017-18 Bradley M. Bell (bradbell@seanet.com)
//              This program is distributed under the terms of the
//              GNU General Public License version 3.0 or later see
//                    https://www.gnu.org/licenses/gpl-3.0.txt
// -----------------------------------------------------------------------------
// error_message
// -----------------------------------------------------------------------------
// BEGIN SOURCE
# include <cstdio>
# include <string>
# include <cppad/py/cppad_py.hpp>

bool error_message_xam(void) {
	using cppad_py::a_double;
	using cppad_py::vec_bool;
	using cppad_py::vec_int;
	using cppad_py::vec_double;
	using cppad_py::vec_a_double;
	using cppad_py::a_fun;
	using cppad_py::sparse_rc;
	using cppad_py::sparse_rcv;
	using cppad_py::sparse_jac_work;
	using cppad_py::sparse_hes_work;
	using std::string;
	//
	// initialize return variable
	bool ok = true;
	//------------------------------------------------------------------------
	ok = false;
	try {
		cppad_py::error_message("test message");
	} catch (...) {
		string stored_message = cppad_py::error_message("");
		ok = stored_message == "test message";
	}
	return( ok  );
}
// END SOURCE
// -----------------------------------------------------------------------------
/*
$begin error_message_xam.cpp$$
$spell
	cplusplus
	cppad
	py
	xam
	Jacobian
	Jacobians
$$
$section C++: Cppad Py Exception Handling: Example and Test$$
$srcfile|build/lib/example/cplusplus/error_message_xam.cpp|0|// BEGIN SOURCE|// END SOURCE|$$
$end
*/
//
