// SPDX-License-Identifier: GPL-3.0-or-later
// SPDX-FileCopyrightText: Bradley M. Bell <bradbell@seanet.com>
// SPDX-FileContributor: 2017-23 Bradley M. Bell
// ----------------------------------------------------------------------------
// build_type
// -----------------------------------------------------------------------------
// BEGIN SOURCE
# include <string>
# include <cppad/py/build_type.hpp>
bool build_type_xam(void) {
   // initialize return variable
   bool ok = true;
   //
   // buid_type
   std::string build_type = cppad_py::build_type();
   //
   // ok
   ok &= build_type == "debug" || build_type == "release";
   //
   return( ok  );
}
// END SOURCE
// -----------------------------------------------------------------------------
/*
{xrst_begin build_type_xam.cpp}

C++: CppAD Py build_type: Example and Test
##########################################
{xrst_literal
   // BEGIN SOURCE
   // END SOURCE
}
{xrst_end build_type_xam.cpp}
*/
