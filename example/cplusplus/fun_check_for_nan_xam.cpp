// -----------------------------------------------------------------------------
//         cppad_py: A C++ Object Library and Python Interface to Cppad
//          Copyright (C) 2017-22 Bradley M. Bell (bradbell@seanet.com)
//              This program is distributed under the terms of the
//              GNU General Public License version 3.0 or later see
//                    https://www.gnu.org/licenses/gpl-3.0.txt
// -----------------------------------------------------------------------------
// d_fun properties
// -----------------------------------------------------------------------------
// BEGIN SOURCE
# include <cstdio>
# include <cppad/py/cppad_py.hpp>
# include <cppad/utility/nan.hpp>

bool fun_check_for_nan_xam(void) {
   using cppad_py::a_double;
   using cppad_py::vec_double;
   using cppad_py::vec_a_double;
   using cppad_py::d_fun;
   //
   // initialize return variable
   bool ok = true;
   // ----------------------------------------------------------------------
   int n_ind = 2; // number of independent variables
   int n_dep = 2; // number of dependent variables
   //
   // dimension some vectors
   vec_double x(n_ind), dx(n_ind), ddx(n_ind);
   vec_double y(n_dep), dy(n_dep), ddy(n_dep);
   vec_a_double ay(n_dep);
   //
   // independent variables
   x[0] = -1.0;
   x[1] = 2.0;
   vec_a_double ax = cppad_py::independent(x);
   //
   // dependent variables
   ay[0] = pow(ax[0], ax[1]);
   ay[1] = pow_int(ax[0], 2);
   //
   // define f(x) = y
   d_fun f(ax, ay);
   //
   // Turn off checking for nan
   bool b = false;
   f.check_for_nan(b);
   //
   // function values are not nan
   y  = f.forward(0, x);
   ok = ok && y[0] == 1.0;   // y[0] = f(x)
   ok = ok && y[1] == 1.0;   // y[1] = f(x)
   //
   // Derivative of pow is nan. This would cause an assert
   // if build_type were debug and check_for_nan were true.
   dx[0] = 1.0;
   dx[1] = 0.0;
   dy    = f.forward(1, dx);
   ok    = ok && CppAD::isnan( dy[0] );
   ok    = ok && dy[1] == -2.0;          // y[1] = f'(x)
   //
   // Second derivative of pow is nan.
   ddx[0] = 0.0;
   ddx[1] = 0.0;
   ddy    = f.forward(2, ddx);
   ok     = ok && CppAD::isnan( ddy[0] );
   ok     = ok && ddy[1] == 1.0;        // ddy[1] = 1/2 * f'(x)
   //
   return( ok  );
}
// END SOURCE
// -----------------------------------------------------------------------------
/*
{xrst_begin fun_check_for_nam_xam}

C++: Check For Nan in Function Result: Example and Test
#######################################################
{xrst_literal
   // BEGIN SOURCE
   // END SOURCE
}
{xrst_end fun_check_for_nam_xam}
*/
//
