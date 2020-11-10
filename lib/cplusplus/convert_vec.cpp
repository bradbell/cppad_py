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
{xsrst_begin_parent convert_vec}

Convert From Standard Vectors to CppAD Vectors
##############################################

Children
********
{xsrst_child_table
}

{xsrst_end convert_vec}
-------------------------------------------------------------------------------
{xsrst_begin ad_vec_std2cppad}

.. include:: ../preamble.rst

{xsrst_spell
    cppad
}

Convert AD Vector From Standard to CppAD
########################################

Syntax
******

| *v_out* =  ``cppad_py::ad_vec_std2cppad`` ( ``v_in`` )

Prototype
*********
{xsrst_file
    // BEGIN_AD_VEC_STD2CPPAD
    // END_AD_VEC_STD2CPPAD
}

{xsrst_end ad_vec_std2cppad}
-------------------------------------------------------------------------------
*/

// BEGIN_AD_VEC_STD2CPPAD
CppAD::vector< CppAD::AD<double> >
ad_vec_std2cppad(const std::vector<a_double>& v_in )
// END_AD_VEC_STD2CPPAD
{   CppAD::vector< CppAD::AD<double> > v_out( v_in.size() );
    for(size_t i = 0; i < v_in.size(); ++i)
        v_out[i] = *( v_in[i].ptr() );
    return v_out;
}
/*
-------------------------------------------------------------------------------
{xsrst_begin ad_vec_cppad2std}

.. include:: ../preamble.rst

{xsrst_spell
    cppad
}

Convert AD Vector From CppAD to Standard
########################################

Syntax
******

| *v_out* =  ``cppad_py::ad_vec_cppad2std`` ( ``v_in`` )

Prototype
*********
{xsrst_file
    // BEGIN_AD_VEC_CPPAD2STD
    // END_AD_VEC_CPPAD2STD
}

{xsrst_end ad_vec_cppad2std}
-------------------------------------------------------------------------------
*/

// BEGIN_AD_VEC_CPPAD2STD
std::vector<a_double>
ad_vec_cppad2std(const CppAD::vector< CppAD::AD<double> >& v_in )
// END_AD_VEC_CPPAD2STD
{   std::vector<a_double> v_out( v_in.size() );
    for(size_t i = 0; i < v_in.size(); ++i)
        *(v_out[i].ptr()) = v_in[i];
    return v_out;
}
/*
-------------------------------------------------------------------------------
{xsrst_begin d_vec_std2cppad}

.. include:: ../preamble.rst

{xsrst_spell
    cppad
}

Convert double Vector From Standard to CppAD
############################################

Syntax
******

| *v_out* =  ``cppad_py::d_vec_std2cppad`` ( ``v_in`` )

Prototype
*********
{xsrst_file
    // BEGIN_D_VEC_STD2CPPAD
    // END_D_VEC_STD2CPPAD
}

{xsrst_end d_vec_std2cppad}
-------------------------------------------------------------------------------
*/

// BEGIN_D_VEC_STD2CPPAD
CppAD::vector<double>
d_vec_std2cppad(const std::vector<double>& v_in )
// END_D_VEC_STD2CPPAD
{   CppAD::vector<double> v_out( v_in.size() );
    for(size_t i = 0; i < v_in.size(); ++i)
        v_out[i] = v_in[i];
    return v_out;
}
/*
-------------------------------------------------------------------------------
{xsrst_begin d_vec_cppad2std}

.. include:: ../preamble.rst

{xsrst_spell
    cppad
}

Convert double Vector From CppAD to Standard
############################################

Syntax
******

| *v_out* =  ``cppad_py::d_vec_cppad2std`` ( ``v_in`` )

Prototype
*********
{xsrst_file
    // BEGIN_D_VEC_CPPAD2STD
    // END_D_VEC_CPPAD2STD
}

{xsrst_end d_vec_cppad2std}
-------------------------------------------------------------------------------
*/

// BEGIN_D_VEC_CPPAD2STD
std::vector<double>
d_vec_cppad2std(const CppAD::vector<double>& v_in )
// END_D_VEC_CPPAD2STD
{   std::vector<double> v_out( v_in.size() );
    for(size_t i = 0; i < v_in.size(); ++i)
        v_out[i] = v_in[i];
    return v_out;
}

// ----------------------------------------------------------------------------
} // END_CPPAD_PY_NAMESPACE
