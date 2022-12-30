// SPDX-License-Identifier: GPL-3.0-or-later
// SPDX-FileCopyrightText: Bradley M. Bell <bradbell@seanet.com>
// SPDX-FileContributor: 2017-22 Bradley M. Bell
// ----------------------------------------------------------------------------
// std::vector<double>
// -----------------------------------------------------------------------------
// BEGIN SOURCE
# include <cstdio>
# include <cppad/py/cppad_py.hpp>

bool vector_set_get_xam(void) {
   using cppad_py::a_double;
   using cppad_py::vec_bool;
   using cppad_py::vec_int;
   using cppad_py::vec_double;
   using cppad_py::vec_a_double;
   //
   // initialize return variable
   bool ok = true;
   //------------------------------------------------------------------------
   int n = 4;
   vec_bool     bv(n);
   vec_int      iv(n);
   vec_double   dv(n);
   vec_a_double av(n);
   //
   // setting elements
   for(int i = 0; i < n ; i++) {
      bv[i] = i > n / 2;
      iv[i] = 2 * i;
      dv[i] = 3.0 * i;
      av[i] = 4.0 * i;
   }
   //
   for(int i = 0; i < n ; i++) {
      bool be = bv[i];
      ok = ok && be == (i > n / 2) ;
      //
      int ie = iv[i];
      ok = ok && ie == 2 * i ;
      //
      double de = dv[i];
      ok = ok && de == 3.0 * i ;
      //
      a_double ae = av[i];
      ok = ok && ae == 4.0 * i ;
   }
   //
   return( ok );
}
// END SOURCE
//
/*
{xrst_begin vector_set_get_xam_cpp}

C++: Setting and Getting Vector Elements: Example and Test
##########################################################
{xrst_literal
   // BEGIN SOURCE
   // END SOURCE
}
{xrst_end vector_set_get_xam_cpp}
*/
//
