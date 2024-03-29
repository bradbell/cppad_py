// SPDX-License-Identifier: GPL-3.0-or-later
// SPDX-FileCopyrightText: Bradley M. Bell <bradbell@seanet.com>
// SPDX-FileContributor: 2017-23 Bradley M. Bell
// ----------------------------------------------------------------------------
// a_double unary operators
// -----------------------------------------------------------------------------
// BEGIN SOURCE
# include <cstdio>
# include <cppad/py/cppad_py.hpp>

bool a_double_unary_fun_xam(void) {
   using cppad_py::a_double;
   //
   // initialize return variable
   bool ok = true;
   //------------------------------------------------------------------------
   //
   a_double a1(-1.0);
   a_double abs1 = a1.abs();
   ok  = ok && abs1 == 1.0;
   //
   a1   = 1.0;
   abs1 = a1.fabs();
   ok   = ok && abs1 == 1.0;
   //
   // pi/4
   a_double pi_4 = a1.atan();
   //
   // sqrt(2)
   a_double atmp(2.0);
   a_double r2 = atmp.sqrt();
   //
   // sin(pi/4)  * sqrt(2) = 1.0;
   atmp = r2 * pi_4.sin() ;
   ok = ok && atmp.near_equal(a1) ;
   //
   // cos(pi/4)  * sqrt(2) = 1.0;
   atmp = r2 * pi_4.cos() ;
   ok = ok && atmp.near_equal(a1) ;
   //
   // tan(pi/4)  = 1.0;
   atmp = pi_4.tan() ;
   ok = ok && atmp.near_equal(a1) ;
   //
   // erf(0.5) = 0.5204998778130465
   a_double acheck(0.5204998778130465);
   atmp =  a_double(0.5);
   atmp = atmp.erf();
   ok = ok && atmp.near_equal(acheck);
   //
   return( ok );
}
// END SOURCE
//
/*
{xrst_begin a_double_unary_fun_xam.cpp}

C++: a_double Unary Functions with AD Result: Example and Test
##############################################################
{xrst_literal
   // BEGIN SOURCE
   // END SOURCE
}
{xrst_end a_double_unary_fun_xam.cpp}
*/
//
