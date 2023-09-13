// SPDX-License-Identifier: GPL-3.0-or-later
// SPDX-FileCopyrightText: Bradley M. Bell <bradbell@seanet.com>
// SPDX-FileContributor: 2017-23 Bradley M. Bell
// ----------------------------------------------------------------------------
// vector size()
// -----------------------------------------------------------------------------
// BEGIN SOURCE
# include <cstdio>
# include <cppad/py/cppad_py.hpp>

bool vector_size_xam(void) {
   using cppad_py::vec_bool;
   using cppad_py::vec_int;
   using cppad_py::vec_double;
   using cppad_py::vec_a_double;
   //
   // initialize return variable
   bool ok = true;
   //------------------------------------------------------------------------
   // create vectors
   vec_bool     bv;
   vec_int      iv(1);
   vec_double   dv(2);
   vec_a_double av(3);
   //
   // check size of vectors
   ok = ok && bv.size() == 0 ;
   ok = ok && iv.size() == 1 ;
   ok = ok && dv.size() == 2 ;
   ok = ok && av.size() == 3 ;
   //
   return( ok );
}
// END SOURCE
//
/*
{xrst_begin vector_size_xam.cpp}

C++: Size of Vectors: Example and Test
######################################
{xrst_literal
   // BEGIN SOURCE
   // END SOURCE
}
{xrst_end vector_size_xam.cpp}
*/
//
