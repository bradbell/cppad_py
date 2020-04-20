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

bool fun_property_xam(void) {
	using cppad_py::a_double;
	using cppad_py::vec_double;
	using cppad_py::vec_a_double;
	using cppad_py::d_fun;
	using cppad_py::a_fun;
	//
	// initialize return variable
	bool ok = true;
	// ----------------------------------------------------------------------
	int n_ind = 1; // number of independent variables
	int n_dep = 2; // number of dependent variables
	int n_var = 1; // phantom variable at address 0
	int n_op  = 1; // special operator at beginning
	//
	// dimension some vectors
	vec_double x(n_ind);
	vec_a_double ay(n_dep);
	//
	// independent variables
	x[0]            = 1.0;
	vec_a_double ax = cppad_py::independent(x);
	n_var           = n_var + n_ind; // one for each indpendent
	n_op            = n_op + n_ind;
	//
	// first dependent variable
	ay[0] = ax[0] + ax[0];
	n_var = n_var + 1; // one variable and operator
	n_op = n_op + 1;
	//
	// second dependent variable
	a_double ax0 = ax[0];
	ay[1]        = ax0.sin();
	n_var        = n_var + 2; // two varialbes, one operator
	n_op         = n_op + 1;
	//
	// define f(x) = y
	d_fun f(ax, ay);
	n_op     = n_op + 1; // speical operator at end
	//
	// check f properties
	ok = ok && f.size_domain() == n_ind;
	ok = ok && f.size_range()  == n_dep;
	ok = ok && f.size_var()    == n_var;
	ok = ok && f.size_op()     == n_op;
	ok = ok && f.size_order()  == 0;
	//
	// compute zero order Taylor coefficients
	vec_double y  = f.forward(0, x);
	ok = ok && f.size_order() == 1;
	//
	// create an a_fun object
	a_fun af(f);
	//
	// ----------------------------------------------------------------------
	// check af properties
	ok = ok && af.size_domain() == n_ind;
	ok = ok && af.size_range()  == n_dep;
	ok = ok && af.size_var()    == n_var;
	ok = ok && af.size_op()     == n_op;
	ok = ok && af.size_order()  == 0;
	//
	return( ok  );
}
// END SOURCE
// -----------------------------------------------------------------------------
/*
$begin fun_property_xam.cpp$$
$spell
	cplusplus
	cppad
	py
	xam
	Jacobian
	Jacobians
$$
$section C++: d_fun Properties: Example and Test$$
$srcthisfile|0|// BEGIN SOURCE|// END SOURCE|$$
$end
*/
//
