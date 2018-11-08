# ifndef CPPAD_PY_CPPAD_VEC_HPP
# define CPPAD_PY_CPPAD_VEC_HPP
/* ----------------------------------------------------------------------------
          cppad_py: A C++ Object Library and Python Interface to Cppad
           Copyright (C) 2017-18 Bradley M. Bell (bradbell@seanet.com)
               This program is distributed under the terms of the
               GNU General Public License version 3.0 or later see
                     https://www.gnu.org/licenses/gpl-3.0.txt
---------------------------------------------------------------------------- */
# include <cppad/cppad.hpp>
# include <cppad/py/a_double.hpp>

namespace cppad_py {
	//
	// vec2cppad_double
	std::vector< CppAD::AD<double> >
	vec2cppad_double(const std::vector<a_double>& v_in );
	//
	// vec2a_double
	std::vector<a_double>
	vec2a_double(const std::vector< CppAD::AD<double> >& v_in );
	//
}

# endif
