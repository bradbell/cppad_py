# ifndef CPPAD_PY_CONVERT_VEC_HPP
# define CPPAD_PY_CONVERT_VEC_HPP
/* ----------------------------------------------------------------------------
          cppad_py: A C++ Object Library and Python Interface to Cppad
           Copyright (C) 2017-20 Bradley M. Bell (bradbell@seanet.com)
               This program is distributed under the terms of the
               GNU General Public License version 3.0 or later see
                     https://www.gnu.org/licenses/gpl-3.0.txt
---------------------------------------------------------------------------- */
# include <cppad/cppad.hpp>
# include <cppad/py/a_double.hpp>

namespace cppad_py {
    //
    // ad_vec_std2cppad
    CppAD::vector< CppAD::AD<double> >
    ad_vec_std2cppad(const std::vector<a_double>& v_in );
    //
    // ad_vec_cppad2std
    std::vector<a_double>
    ad_vec_cppad2std(const CppAD::vector< CppAD::AD<double> >& v_in );
    //
    // d_vec_std2cppad
    CppAD::vector<double>
    d_vec_std2cppad(const std::vector<double>& v_in );
    //
    // d_vec_cppad2std
    std::vector<double>
    d_vec_cppad2std(const CppAD::vector<double>& v_in );
}

# endif
