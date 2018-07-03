// This file can be generated in the lib/xam directory using the command:
// m4 -D Language_=cplusplus vector/size.xam
// -----------------------------------------------------------------------------
//         cppad_py: A C++ Object Library and Python Interface to Cppad
//          Copyright (C) 2017-18 Bradley M. Bell (bradbell@seanet.com)
//              This program is distributed under the terms of the
//              GNU General Public License version 3.0 or later see
//                    https://www.gnu.org/licenses/gpl-3.0.txt
// -----------------------------------------------------------------------------
// vector size()
// -----------------------------------------------------------------------------
// BEGIN SOURCE
# include <cstdio>
# include <string>
# include <cppad/py/cppad_py.hpp>

bool vector_size_xam(void) {
	using cppad_py::a_double;
	using cppad_py::vec_bool;
	using cppad_py::vec_int;
	using cppad_py::vec_double;
	using cppad_py::vec_a_double;
	using std::string;
	//
	// initialize return variable
	bool ok = true;
	//------------------------------------------------------------------------
	// create vectors
	vec_bool bv = cppad_py::vec_bool();
	vec_int iv = cppad_py::vec_int(1);
	vec_double dv = cppad_py::vec_double(2);
	vec_a_double av = cppad_py::vec_a_double(3);
	//
	// check size of vectors
	ok = ok && bv.size() == 0 ;
	ok = ok && iv.size() == 1 ;
	ok = ok && dv.size() == 2 ;
	ok = ok && av.size() == 3 ;
	//
	return( ok );
}
// END SOURCE
//
/*
$begin vector_size_xam.cpp$$
$spell
	cplusplus
	cppad
	py
	xam
	Jacobian
	Jacobians
$$
$section C++: Size of Vectors: Example and Test$$
$srcfile|lib/example/cplusplus/vector_size_xam.cpp|0|// BEGIN SOURCE|// END SOURCE|$$
$end
*/
//
