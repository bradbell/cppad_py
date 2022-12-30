# ifndef CPPAD_PY_A_VECTOR_HPP
# define CPPAD_PY_A_VECTOR_HPP
// SPDX-License-Identifier: GPL-3.0-or-later
// SPDX-FileCopyrightText: Bradley M. Bell <bradbell@seanet.com>
// SPDX-FileContributor: 2017-22 Bradley M. Bell
// ----------------------------------------------------------------------------
# include <vector>
# include <cppad/py/a_double.hpp>

namespace cppad_py { // BEGIN_CPPAD_PY_NAMESPACE

typedef std::vector<bool>                 vec_bool;
typedef std::vector<int>                  vec_int;
typedef std::vector<double>               vec_double;
typedef std::vector<cppad_py::a_double>   vec_a_double;

} // END_CPPAD_PY_NAMESPACE

# endif
