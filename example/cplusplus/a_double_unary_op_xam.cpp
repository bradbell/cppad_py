// SPDX-License-Identifier: GPL-3.0-or-later
// SPDX-FileCopyrightText: Bradley M. Bell <bradbell@seanet.com>
// SPDX-FileContributor: 2017-23 Bradley M. Bell
// ----------------------------------------------------------------------------
// a_double unary operators
// -----------------------------------------------------------------------------
// BEGIN SOURCE
# include <cstdio>
# include <cppad/py/cppad_py.hpp>

bool a_double_unary_op_xam(void) {
   using cppad_py::a_double;
   //
   // initialize return variable
   bool ok = true;
   //------------------------------------------------------------------------
   a_double a2(2.0);
   a_double aplus2 = + a2 ;
   a_double aminus2 = - a2 ;
   //
   ok = ok && aplus2 == 2.0;
   ok = ok && aminus2 == -2.0;
   //
   return( ok );
}
// END SOURCE
//
/*
{xrst_begin a_double_unary_op_xam.cpp}

C++: a_double Unary Plus and Minus: Example and Test
####################################################
{xrst_literal
   // BEGIN SOURCE
   // END SOURCE
}
{xrst_end a_double_unary_op_xam.cpp}
*/
//
