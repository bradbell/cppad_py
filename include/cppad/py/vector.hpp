# ifndef CPPAD_PY_A_VECTOR_HPP
# define CPPAD_PY_A_VECTOR_HPP
/* ----------------------------------------------------------------------------
          cppad_py: A C++ Object Library and Python Interface to Cppad
           Copyright (C) 2017-18 Bradley M. Bell (bradbell@seanet.com)
               This program is distributed under the terms of the
               GNU General Public License version 3.0 or later see
                     https://www.gnu.org/licenses/gpl-3.0.txt
---------------------------------------------------------------------------- */
# include <vector>
# include <cppad/py/a_double.hpp>

namespace cppad_py { // BEGIN_CPPAD_PY_NAMESPACE

typedef std::vector<bool>                 vec_bool;
typedef std::vector<int>                  vec_int;
typedef std::vector<double>               vec_double;
typedef std::vector<cppad_py::a_double> vec_a_double;

} // END_CPPAD_PY_NAMESPACE

# endif
