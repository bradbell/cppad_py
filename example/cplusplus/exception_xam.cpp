// SPDX-License-Identifier: GPL-3.0-or-later
// SPDX-FileCopyrightText: Bradley M. Bell <bradbell@seanet.com>
// SPDX-FileContributor: 2017-23 Bradley M. Bell
// ----------------------------------------------------------------------------
// exception
// -----------------------------------------------------------------------------
// BEGIN SOURCE
# include <cstdio>
# include <string>
# include <cppad/py/cppad_py.hpp>

bool exception_xam(void) {
   using std::string;
   //
   // initialize return variable
   bool ok = true;
   //------------------------------------------------------------------------
   ok = false;
   try {
      throw std::runtime_error("test message");
   } catch (std::runtime_error& e) {
      string stored_message = e.what();
      ok = stored_message == "test message";
   }
   return( ok  );
}
// END SOURCE
// -----------------------------------------------------------------------------
/*
{xrst_begin exception_xam.cpp}
{xrst_spell
}

C++: CppAD Py Exception Handling: Example and Test
##################################################
{xrst_literal
   // BEGIN SOURCE
   // END SOURCE
}
{xrst_end exception_xam.cpp}
*/
//
