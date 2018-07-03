// This file can be generated in the lib/xam directory using the command:
// m4 -D Language_=cplusplus vector/set_get_xam.xam
// -----------------------------------------------------------------------------
//         cppad_py: A C++ Object Library and Python Interface to Cppad
//          Copyright (C) 2017-18 Bradley M. Bell (bradbell@seanet.com)
//              This program is distributed under the terms of the
//              GNU General Public License version 3.0 or later see
//                    https://www.gnu.org/licenses/gpl-3.0.txt
// -----------------------------------------------------------------------------
// std::vector<double>
// -----------------------------------------------------------------------------
// BEGIN SOURCE
# include <cstdio>
# include <string>
# include <cppad/py/cppad_py.hpp>

bool vector_set_get_xam(void) {
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
	int n = 4;
	vec_bool bv = cppad_py::vec_bool(n);
	vec_int iv = cppad_py::vec_int(n);
	vec_double dv = cppad_py::vec_double(n);
	vec_a_double av = cppad_py::vec_a_double(n);
	//
	// setting elements
	for(int i = 0; i < n ; i++) {
		bv[i] = i > n / 2;
		iv[i] = 2 * i;
		dv[i] = 3.0 * i;
		av[i] = cppad_py::a_double(4.0 * i);
	}
	//
	for(int i = 0; i < n ; i++) {
		bool be = bv[i];
		ok = ok && be == (i > n / 2) ;
		//
		int ie = iv[i];
		ok = ok && ie == 2 * i ;
		//
		double de = dv[i];
		ok = ok && de == 3.0 * i ;
		//
		a_double ae = av[i];
		ok = ok && ae.value() == 4.0 * i ;
	}
	//
	return( ok );
}
// END SOURCE
//
/*
$begin vector_set_get_xam.cpp$$
$spell
	cplusplus
	cppad
	py
	xam
	Jacobian
	Jacobians
$$
$section C++: Setting and Getting Vector Elements: Example and Test$$
$srcfile|build/lib/example/cplusplus/vector_set_get_xam.cpp|0|// BEGIN SOURCE|// END SOURCE|$$
$end
*/
//
