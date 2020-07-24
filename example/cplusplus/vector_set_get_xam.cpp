// -----------------------------------------------------------------------------
//         cppad_py: A C++ Object Library and Python Interface to Cppad
//          Copyright (C) 2017-20 Bradley M. Bell (bradbell@seanet.com)
//              This program is distributed under the terms of the
//              GNU General Public License version 3.0 or later see
//                    https://www.gnu.org/licenses/gpl-3.0.txt
// -----------------------------------------------------------------------------
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
    vec_bool bv = vec_bool(n);
    vec_int iv = vec_int(n);
    vec_double dv(n);
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
{xsrst_begin vector_set_get_xam_cpp}

.. include:: ../preamble.rst

{xsrst_spell
}
C++: Setting and Getting Vector Elements: Example and Test
##########################################################
{xsrst_file
    // BEGIN SOURCE
    // END SOURCE
}
{xsrst_end vector_set_get_xam_cpp}
*/
//
