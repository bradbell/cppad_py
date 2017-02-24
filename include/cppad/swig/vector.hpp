# ifndef CPPAD_SWIG_A_VECTOR_HPP
# define CPPAD_SWIG_A_VECTOR_HPP
/* ----------------------------------------------------------------------------
          cppad_swig: A C++ Object Library and Swig Interface to Cppad
           Copyright (C) 2017-17 Bradley M. Bell (bradbell@seanet.com)
               This program is distributed under the terms of the
               GNU General Public License version 3.0 or later see
                     https://www.gnu.org/licenses/gpl-3.0.txt
---------------------------------------------------------------------------- */
# include <vector>
# include <cppad/swig/a_double.hpp>

namespace cppad_swig { // BEGIN_CPPAD_SWIG_NAMESPACE

typedef std::vector<bool>                 vec_bool;
typedef std::vector<int>                  vec_int;
typedef std::vector<double>               vec_double;
typedef std::vector<cppad_swig::a_double> vec_a_double;

} // END_CPPAD_SWIG_NAMESPACE

# endif
