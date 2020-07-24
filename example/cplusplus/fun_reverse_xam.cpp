// -----------------------------------------------------------------------------
//         cppad_py: A C++ Object Library and Python Interface to Cppad
//          Copyright (C) 2017-20 Bradley M. Bell (bradbell@seanet.com)
//              This program is distributed under the terms of the
//              GNU General Public License version 3.0 or later see
//                    https://www.gnu.org/licenses/gpl-3.0.txt
// -----------------------------------------------------------------------------
// reverse
// -----------------------------------------------------------------------------
// BEGIN SOURCE
# include <cstdio>
# include <cppad/py/cppad_py.hpp>

bool fun_reverse_xam(void) {
    using cppad_py::a_double;
    using cppad_py::vec_double;
    using cppad_py::vec_a_double;
    using cppad_py::d_fun;
    using cppad_py::a_fun;
    //
    // initialize return variable
    bool ok = true;
    //------------------------------------------------------------------------
    // number of dependent and independent variables
    int n_dep = 1;
    int n_ind = 3;
    //
    // create the independent variables ax
    vec_double xp(n_ind);
    for(int i = 0; i < n_ind ; i++) {
        xp[i] = i;
    }
    vec_a_double ax = cppad_py::independent(xp);
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
    // -----------------------------------------------------------------------
    // define          X(t) = (x_0 + t, x_1 + t, x_2 + t)
    // it follows that Y(t) = f(X(t)) = (x_0 + t) * (x_1 + t) * (x_2 + t)
    // and that       Y'(0) = x_1 * x_2 + x_0 * x_2 + x_0 * x_1
    // -----------------------------------------------------------------------
    // zero order forward mode
    int p = 0;
    xp[0] = 2.0;
    xp[1] = 3.0;
    xp[2] = 4.0;
    vec_double yp = f.forward(p, xp);
    ok = ok && yp[0] == 24.0;
    // -----------------------------------------------------------------------
    // first order reverse (derivative of zero order forward)
    // define G( Y ) = y_0 = x_0 * x_1 * x_2
    int q = 1;
    vec_double yq1 = vec_double(n_dep);
    yq1[0] = 1.0;
    vec_double xq1 = f.reverse(q, yq1);
    // partial G w.r.t x_0
    ok = ok && xq1[0] == 3.0 * 4.0 ;
    // partial G w.r.t x_1
    ok = ok && xq1[1] == 2.0 * 4.0 ;
    // partial G w.r.t x_2
    ok = ok && xq1[2] == 2.0 * 3.0 ;
    // -----------------------------------------------------------------------
    // first order forward mode
    p = 1;
    xp[0] = 1.0;
    xp[1] = 1.0;
    xp[2] = 1.0;
    yp = f.forward(p, xp);
    ok = ok && yp[0] == 3.0*4.0 + 2.0*4.0 + 2.0*3.0;
    // -----------------------------------------------------------------------
    // second order reverse (derivative of first order forward)
    // define G( y_0^0 , y_0^1 ) = y_0^1
    // = x_1^0 * x_2^0  +  x_0^0 * x_2^0  +  x_0^0  *  x_1^0
    q = 2;
    vec_double yq2 = vec_double(n_dep * q);
    yq2[0 * q + 0] = 0.0; // partial of G w.r.t y_0^0
    yq2[0 * q + 1] = 1.0; // partial of G w.r.t y_0^1
    vec_double xq2 = f.reverse(q, yq2);
    // partial G w.r.t x_0^0
    ok = ok && xq2[0 * q + 0] == 3.0 + 4.0;
    // partial G w.r.t x_1^0
    ok = ok && xq2[1 * q + 0] == 2.0 + 4.0;
    // partial G w.r.t x_2^0
    ok = ok && xq2[2 * q + 0] == 2.0 + 3.0;
    // -----------------------------------------------------------------------
    a_fun af(f);
    ok &= af.size_order() == 0;
    //
    // zero order forward
    vec_a_double axp(n_ind), ayp(n_dep);
    p      = 0;
    axp[0] = 2.0;
    axp[1] = 3.0;
    axp[2] = 4.0;
    ayp    = af.forward(p, axp);
    ok     = ok && ayp[0] == 24.0;
    ok    &= af.size_order() == 1;
    //
    // first order reverse
    q = 1;
    vec_a_double ayq1 = vec_a_double(n_dep);
    ayq1[0]           = 1.0;
    vec_a_double axq1 = af.reverse(q, ayq1);
    // partial G w.r.t x_0
    ok = ok && axq1[0] == 3.0 * 4.0;
    // partial G w.r.t x_1
    ok = ok && axq1[1] == 2.0 * 4.0;
    // partial G w.r.t x_2
    ok = ok && axq1[2] == 2.0 * 3.0;
    //
    return( ok );
}
// END SOURCE
//
/*
{xsrst_begin fun_reverse_xam_cpp}

.. include:: ../preamble.rst

{xsrst_spell
}
C++: Reverse Mode AD: Example and Test
######################################
{xsrst_file
    // BEGIN SOURCE
    // END SOURCE
}
{xsrst_end fun_reverse_xam_cpp}
*/
//
