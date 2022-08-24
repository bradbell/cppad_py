// -----------------------------------------------------------------------------
//         cppad_py: A C++ Object Library and Python Interface to Cppad
//          Copyright (C) 2017-22 Bradley M. Bell (bradbell@seanet.com)
//              This program is distributed under the terms of the
//              GNU General Public License version 3.0 or later see
//                    https://www.gnu.org/licenses/gpl-3.0.txt
// -----------------------------------------------------------------------------
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
{xrst_begin vector_size_xam_cpp}

{xrst_spell
}
C++: Size of Vectors: Example and Test
######################################
{xrst_literal
   // BEGIN SOURCE
   // END SOURCE
}
{xrst_end vector_size_xam_cpp}
*/
//
