// -----------------------------------------------------------------------------
//         cppad_py: A C++ Object Library and Python Interface to Cppad
//          Copyright (C) 2017-20 Bradley M. Bell (bradbell@seanet.com)
//              This program is distributed under the terms of the
//              GNU General Public License version 3.0 or later see
//                    https://www.gnu.org/licenses/gpl-3.0.txt
// -----------------------------------------------------------------------------
// a_double comparision operators
// -----------------------------------------------------------------------------
// BEGIN SOURCE
# include <cstdio>
# include <cppad/py/cppad_py.hpp>

bool a_double_compare_xam(void) {
    using cppad_py::a_double;
    bool ok = true;
    a_double a2(2.0);
    a_double a3(3.0);
    //------------------------------------------------------------------------
    ok = ok && a2   <  a3;
    ok = ok && a2   <= a3;
    ok = ok && a3 >  a2;
    ok = ok && a3 >= a2;
    ok = ok && a3 != a2;
    ok = ok && a3 == a3;
    //
    ok = ok && ! (a2 >  a3) ;
    ok = ok && ! (a2 >= a3) ;
    ok = ok && ! (a2 == a3) ;
    //------------------------------------------------------------------------
    ok = ok && a2   <  3.0;
    ok = ok && a2   <= 3.0;
    ok = ok && a3 >  2.0;
    ok = ok && a3 >= 2.0;
    ok = ok && a3 != 2.0;
    ok = ok && a3 == 3.0;
    //
    ok = ok && ! (a2 >  3.0) ;
    ok = ok && ! (a2 >= 3.0) ;
    ok = ok && ! (a2 == 3.0) ;
    //
    return( ok );
}
// END SOURCE
//
/*
{xsrst_begin a_double_compare_xam_cpp}

.. include:: ../preamble.rst

{xsrst_spell
}
C++: a_double Comparison Operators: Example and Test
####################################################
{xsrst_file
    // BEGIN SOURCE
    // END SOURCE
}
{xsrst_end a_double_compare_xam_cpp}
*/
//
