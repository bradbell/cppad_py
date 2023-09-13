// SPDX-License-Identifier: GPL-3.0-or-later
// SPDX-FileCopyrightText: Bradley M. Bell <bradbell@seanet.com>
// SPDX-FileContributor: 2017-23 Bradley M. Bell
// ----------------------------------------------------------------------------
// a_double assignment
// -----------------------------------------------------------------------------
// BEGIN SOURCE
# include <cstdio>
# include <cppad/py/cppad_py.hpp>

bool a_double_assign_xam(void) {
   using cppad_py::a_double;
   //
   // initialize return variable
   bool ok = true;
   //------------------------------------------------------------------------
   a_double ax(2.0);
   //
   ax = 3.0;
   ok = ok && ax == 3.0;
   //
   ax += a_double(2.0);
   ok = ok && ax == 5.0;
   //
   ax -= 1.0;
   ok = ok && ax == 4.0;
   //
   ax *= a_double(3.0);
   ok = ok && ax == 12.0;
   //
   ax /= 4.0;
   ok = ok && ax == a_double(3.0);
   //
   return( ok );
}
// END SOURCE
//
/*
{xrst_begin a_double_assign_xam.cpp}

C++: a_double Assignment Operators: Example and Test
####################################################
{xrst_literal
   // BEGIN SOURCE
   // END SOURCE
}
{xrst_end a_double_assign_xam.cpp}
*/
//
