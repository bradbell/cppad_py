// SPDX-License-Identifier: GPL-3.0-or-later
// SPDX-FileCopyrightText: Bradley M. Bell <bradbell@seanet.com>
// SPDX-FileContributor: 2017-23 Bradley M. Bell
// ----------------------------------------------------------------------------
// a_double properties
// -----------------------------------------------------------------------------
// BEGIN SOURCE
# include <cstdio>
# include <cppad/py/cppad_py.hpp>

bool a_double_property_xam(void) {
   using cppad_py::a_double;
   //
   // initialize return variable
   bool ok = true;
   //------------------------------------------------------------------------
   a_double a3(3.0);
   //
   ok = ok && a3   == 3.0;
   ok = ok && a3.parameter();
   ok = ok && ! a3.variable();
   //
   // near_equal
   a_double r3 = a3.sqrt() ;
   ok = ok && a3.near_equal( r3 * r3) ;;
   //
   // var2par
   a_double p3 = a3.var2par();
   ok &= p3.value() == 3.0;
   //
   return( ok );
}
// END SOURCE
//
/*
{xrst_begin a_double_property_xam.cpp}

C++: a_double Properties: Example and Test
##########################################
{xrst_literal
   // BEGIN SOURCE
   // END SOURCE
}
{xrst_end a_double_property_xam.cpp}
*/
//
