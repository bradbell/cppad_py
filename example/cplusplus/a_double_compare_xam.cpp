// SPDX-License-Identifier: GPL-3.0-or-later
// SPDX-FileCopyrightText: Bradley M. Bell <bradbell@seanet.com>
// SPDX-FileContributor: 2017-22 Bradley M. Bell
// ----------------------------------------------------------------------------
// a_double comparision operators
// -----------------------------------------------------------------------------
// BEGIN SOURCE
# include <cstdio>
# include <cppad/py/cppad_py.hpp>

bool a_double_compare_xam(void) {
   using cppad_py::a_double;
   bool ok = true;
   a_double a2(2.0);
   a_double a3(3.0);
   //------------------------------------------------------------------------
   ok = ok && a2   <  a3;
   ok = ok && a2   <= a3;
   ok = ok && a3 >  a2;
   ok = ok && a3 >= a2;
   ok = ok && a3 != a2;
   ok = ok && a3 == a3;
   //
   ok = ok && ! (a2 >  a3) ;
   ok = ok && ! (a2 >= a3) ;
   ok = ok && ! (a2 == a3) ;
   //------------------------------------------------------------------------
   ok = ok && a2   <  3.0;
   ok = ok && a2   <= 3.0;
   ok = ok && a3 >  2.0;
   ok = ok && a3 >= 2.0;
   ok = ok && a3 != 2.0;
   ok = ok && a3 == 3.0;
   //
   ok = ok && ! (a2 >  3.0) ;
   ok = ok && ! (a2 >= 3.0) ;
   ok = ok && ! (a2 == 3.0) ;
   //
   return( ok );
}
// END SOURCE
//
/*
{xrst_begin a_double_compare_xam_cpp}

C++: a_double Comparison Operators: Example and Test
####################################################
{xrst_literal
   // BEGIN SOURCE
   // END SOURCE
}
{xrst_end a_double_compare_xam_cpp}
*/
//
