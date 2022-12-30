// SPDX-License-Identifier: GPL-3.0-or-later
// SPDX-FileCopyrightText: Bradley M. Bell <bradbell@seanet.com>
// SPDX-FileContributor: 2017-22 Bradley M. Bell
// ----------------------------------------------------------------------------
// forward
// -----------------------------------------------------------------------------
// BEGIN SOURCE
# include <cstdio>
# include <cppad/py/cppad_py.hpp>

bool fun_forward_xam(void) {
   using cppad_py::a_double;
   using cppad_py::vec_double;
   using cppad_py::vec_a_double;
   using cppad_py::d_fun;
   using cppad_py::a_fun;
   //
   // initialize return variable
   bool ok = true;
   // ----------------------------------------------------------------------
   // number of dependent and independent variables
   int n_dep = 1;
   int n_ind = 2;
   //
   // create the independent variables ax
   vec_double xp(n_ind);
   for(int i = 0; i < n_ind ; i++) {
      xp[i] = i + 1.0;
   }
   vec_a_double ax = cppad_py::independent(xp);
   //
   // create dependent varialbes ay with ay0 = ax0 * ax1
   a_double ax0 = ax[0];
   a_double ax1 = ax[1];
   vec_a_double ay(n_dep);
   ay[0] = ax0 * ax1;
   //
   // define af corresponding to f(x) = x0 * x1
   d_fun f(ax, ay);
   ok &= f.size_order() == 0;
   //
   // define X(t) = (3 + t, 2 + t)
   // it follows that Y(t) = f(X(t)) = (3 + t) * (2 + t)
   //
   // Y(0) = 6 and p ! = 1
   int p = 0;
   xp[0] = 3.0;
   xp[1] = 2.0;
   vec_double yp = f.forward(p, xp);
   ok  = ok && yp[0] == 6.0;
   ok &= f.size_order() == 1;
   //
   // first order Taylor coefficients for X(t)
   p = 1;
   xp[0] = 1.0;
   xp[1] = 1.0;
   //
   // first order Taylor coefficient for Y(t)
   // Y'(0) = 3 + 2 = 5 and p ! = 1
   yp = f.forward(p, xp);
   ok = ok && yp[0] == 5.0;
   ok &= f.size_order() == 2;
   //
   // second order Taylor coefficients for X(t)
   p = 2;
   xp[0] = 0.0;
   xp[1] = 0.0;
   //
   // second order Taylor coefficient for Y(t)
   // Y''(0) = 2.0 and p ! = 2
   yp = f.forward(p, xp);
   ok = ok && yp[0] == 1.0;
   ok &= f.size_order() == 3;
   // ----------------------------------------------------------------------
   a_fun af(f);
   ok &= af.size_order() == 0;
   //
   // zero order forward
   vec_a_double axp(n_ind), ayp(n_dep);
   p      = 0;
   axp[0] = 3.0;
   axp[1] = 2.0;
   ayp    = af.forward(p, axp);
   ok     = ok && ayp[0] == 6.0;
   ok    &= af.size_order() == 1;
   //
   return( ok );
}
// END SOURCE
//
/*
{xrst_begin fun_forward_xam_cpp}

C++: Forward Mode AD: Example and Test
######################################
{xrst_literal
   // BEGIN SOURCE
   // END SOURCE
}
{xrst_end fun_forward_xam_cpp}
*/
//
