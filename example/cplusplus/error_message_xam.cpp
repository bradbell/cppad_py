// -----------------------------------------------------------------------------
//         cppad_py: A C++ Object Library and Python Interface to Cppad
//          Copyright (C) 2017-20 Bradley M. Bell (bradbell@seanet.com)
//              This program is distributed under the terms of the
//              GNU General Public License version 3.0 or later see
//                    https://www.gnu.org/licenses/gpl-3.0.txt
// -----------------------------------------------------------------------------
// error_message
// -----------------------------------------------------------------------------
// BEGIN SOURCE
# include <cstdio>
# include <string>
# include <cppad/py/cppad_py.hpp>

bool error_message_xam(void) {
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
{xsrst_begin error_message_xam_cpp}

.. include:: ../preamble.rst

{xsrst_spell
    cppad
}
C++: Cppad Py Exception Handling: Example and Test
##################################################
{xsrst_file
    // BEGIN SOURCE
    // END SOURCE
}
{xsrst_end error_message_xam_cpp}
*/
//
