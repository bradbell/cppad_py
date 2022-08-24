// -----------------------------------------------------------------------------
//         cppad_py: A C++ Object Library and Python Interface to Cppad
//          Copyright (C) 2017-22 Bradley M. Bell (bradbell@seanet.com)
//              This program is distributed under the terms of the
//              GNU General Public License version 3.0 or later see
//                    https://www.gnu.org/licenses/gpl-3.0.txt
// -----------------------------------------------------------------------------
// hessian
// -----------------------------------------------------------------------------
// BEGIN SOURCE
# include <cstdio>
# include <cppad/py/cppad_py.hpp>

bool fun_hessian_xam(void) {
   using cppad_py::a_double;
   using cppad_py::vec_double;
   using cppad_py::vec_a_double;
   using cppad_py::d_fun;
   using cppad_py::a_fun;
   //
   // initialize return variable
   bool ok = true;
   // -----------------------------------------------------------------------
   // number of dependent and independent variables
   int n_dep = 1;
   int n_ind = 3;
   //
   // create the independent variables ax
   vec_double x(n_ind);
   for(int i = 0; i < n_ind ; i++) {
      x[i] = i + 2.0;
   }
   vec_a_double ax = cppad_py::independent(x);
   //
   // create dependent variables ay with ay0 = ax_0 * ax_1 * ax_2
   a_double ax_0 = ax[0];
   a_double ax_1 = ax[1];
   a_double ax_2 = ax[2];
   vec_a_double ay(n_dep);
   ay[0] = ax_0 * ax_1 * ax_2;
   //
   // define af corresponding to f(x) = x_0 * x_1 * x_2
   d_fun f(ax, ay);
   //
   // g(x) = w_0 * f_0 (x) = f(x)
   vec_double w(n_dep);
   w[0] = 1.0;
   //
   // compute Hessian
   vec_double fpp = f.hessian(x, w);
   //
   //          [ 0.0 , x_2 , x_1 ]
   // f''(x) = [ x_2 , 0.0 , x_0 ]
   //          [ x_1 , x_0 , 0.0 ]
   ok = ok && fpp[0 * n_ind + 0] == 0.0 ;
   ok = ok && fpp[0 * n_ind + 1] == x[2] ;
   ok = ok && fpp[0 * n_ind + 2] == x[1] ;
   //
   ok = ok && fpp[1 * n_ind + 0] == x[2] ;
   ok = ok && fpp[1 * n_ind + 1] == 0.0 ;
   ok = ok && fpp[1 * n_ind + 2] == x[0] ;
   //
   ok = ok && fpp[2 * n_ind + 0] == x[1] ;
   ok = ok && fpp[2 * n_ind + 1] == x[0] ;
   ok = ok && fpp[2 * n_ind + 2] == 0.0 ;
   // -----------------------------------------------------------------------
   a_fun af(f);
   //
   // compute and check Hessian
   vec_a_double aw(n_dep);
   aw[0] = w[0];
   vec_a_double afpp = af.hessian(ax, aw);
   ok = ok && afpp.size() == fpp.size();
   for(size_t i = 0; i < fpp.size(); ++i)
      ok = ok && afpp[i] == fpp[i];
   //
   return( ok );
}
// END SOURCE
//
/*
{xrst_begin fun_hessian_xam_cpp}

{xrst_spell
}
C++: Dense Hessian Using AD: Example and Test
#############################################
{xrst_literal
   // BEGIN SOURCE
   // END SOURCE
}
{xrst_end fun_hessian_xam_cpp}
*/
//
