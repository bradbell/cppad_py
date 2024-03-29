// SPDX-License-Identifier: GPL-3.0-or-later
// SPDX-FileCopyrightText: Bradley M. Bell <bradbell@seanet.com>
// SPDX-FileContributor: 2017-23 Bradley M. Bell
// ----------------------------------------------------------------------------
// a_double binary operations
// -----------------------------------------------------------------------------
// BEGIN SOURCE
# include <cstdio>
# include <cppad/py/cppad_py.hpp>

bool a_double_binary_xam(void) {
   using cppad_py::a_double;
   bool ok      = true;
   a_double a2  = 2.0;
   a_double a3(3.0);
   // -----------------------------------------------------------------------
   // a_double op a_double
   a_double a5       = a2 + a3;
   a_double a6       = a2 * a3;
   a_double a1_minus = a2 - a3;
   a_double a23      = a2 / a3;
   //
   ok = ok && a5 == 5.0;
   ok = ok && a6 == 6.0;
   ok = ok && a1_minus == -1.0;
   ok = ok && a23.near_equal( a_double(2.0 / 3.0 ) );
   // -----------------------------------------------------------------------
   // a_double op double
   a5       = a2 + 3.0;
   a6       = a2 * 3.0;
   a1_minus = a2 - 3.0;
   a23      = a2 / 3.0;
   //
   ok = ok && a5 == 5.0;
   ok = ok && a6 == 6.0;
   ok = ok && a1_minus == -1.0;
   ok = ok && a23.near_equal( a_double(2.0 / 3.0 ) );
   // -----------------------------------------------------------------------
   // double op a_double
   a5           = cppad_py::radd(3.0, a2);
   a6           = cppad_py::rmul(3.0, a2);
   a_double a1  = cppad_py::rsub(3.0,  a2);
   a_double a32 = cppad_py::rdiv(3.0, a2);
   //
   ok = ok && a5 == 5.0;
   ok = ok && a6 == 6.0;
   ok = ok && a1 == 1.0;
   ok = ok && a32.near_equal( a_double(3.0 / 2.0 ) );
   // -----------------------------------------------------------------------
   // pow
   a_double a8 = cppad_py::pow(a2, a3);
   a_double a9 = cppad_py::pow(a3, 2.0);
   a_double a4 = cppad_py::pow(2.0, a2);
   ok = ok && a8.near_equal( a_double(8.0) );
   ok = ok && a9.near_equal( a_double(9.0) );
   ok = ok && a4.near_equal( a_double(4.0) );
   //
   return( ok );
}
// END SOURCE
//
/*
{xrst_begin a_double_binary_xam.cpp}

C++: a_double Binary Operators With AD Result: Example and Test
###############################################################
{xrst_literal
   // BEGIN SOURCE
   // END SOURCE
}
{xrst_end a_double_binary_xam.cpp}
*/
//
