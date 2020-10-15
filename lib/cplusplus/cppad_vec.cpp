/* -----------------------------------------------------------------------------
           cppad_py: A C++ Object Library and Python Interface to Cppad
            Copyright (C) 2017-20 Bradley M. Bell (bradbell@seanet.com)
                This program is distributed under the terms of the
                GNU General Public License version 3.0 or later see
                      https://www.gnu.org/licenses/gpl-3.0.txt
----------------------------------------------------------------------------- */
# include <cppad/cppad.hpp>
# include <cppad/py/a_double.hpp>
namespace cppad_py { // BEGIN_CPPAD_PY_NAMESPACE
/*
-------------------------------------------------------------------------------
{xsrst_begin vec2cppad_double}

.. include:: ../preamble.rst

{xsrst_spell
    cppad
}

Convert std::vector<a_double> to CppAD::vector< AD<double> >
############################################################

Syntax
******

| *v_out* =  ``cppad_py::vec2cppad_double`` ( ``v_in`` )

Prototype
*********
{xsrst_file
    // BEGIN_VEC2CPPAD_DOUBLE
    // END_VEC2CPPAD_DOUBLE
}

{xsrst_end vec2cppad_double}
-------------------------------------------------------------------------------
*/

// BEGIN_VEC2CPPAD_DOUBLE
CppAD::vector< CppAD::AD<double> >
vec2cppad_double(const std::vector<a_double>& v_in )
// END_VEC2CPPAD_DOUBLE
{   CppAD::vector< CppAD::AD<double> > v_out( v_in.size() );
    for(size_t i = 0; i < v_in.size(); ++i)
        v_out[i] = *( v_in[i].ptr() );
    return v_out;
}
/*
-------------------------------------------------------------------------------
{xsrst_begin vec2a_double}

.. include:: ../preamble.rst

{xsrst_spell
    cppad
}

Convert a CppAD::vector< AD<double> > to std::vector<a_double>
##############################################################

Syntax
******

| *v_out* =  ``cppad_py::vec2a_double`` ( ``v_in`` )

Prototype
*********
{xsrst_file
    // BEGIN_VEC2A_DOUBLE
    // END_VEC2A_DOUBLE
}

{xsrst_end vec2a_double}
-------------------------------------------------------------------------------
*/

// BEGIN_VEC2A_DOUBLE
std::vector<a_double>
vec2a_double(const CppAD::vector< CppAD::AD<double> >& v_in )
// END_VEC2A_DOUBLE
{   std::vector<a_double> v_out( v_in.size() );
    for(size_t i = 0; i < v_in.size(); ++i)
        *(v_out[i].ptr()) = v_in[i];
    return v_out;
}

// ----------------------------------------------------------------------------
} // END_CPPAD_PY_NAMESPACE
