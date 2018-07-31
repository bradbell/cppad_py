# ifndef CPPAD_PY_ERROR_HPP
# define CPPAD_PY_ERROR_HPP
/* ----------------------------------------------------------------------------
          cppad_py: A C++ Object Library and Python Interface to Cppad
           Copyright (C) 2017-18 Bradley M. Bell (bradbell@seanet.com)
               This program is distributed under the terms of the
               GNU General Public License version 3.0 or later see
                     https://www.gnu.org/licenses/gpl-3.0.txt
---------------------------------------------------------------------------- */
# include <exception>
# include <string>
# include <cppad/py/public_lib.hpp>

namespace cppad_py {
	CPPAD_PY_LIB_PUBLIC
	const char* error_message(const char* message);
}

# ifdef NDEBUG
# define CPPAD_PY_ASSERT_UNKNOWN(exp)  // do nothing
# else
# define CPPAD_PY_ASSERT_UNKNOWN(exp) \
{	if( ! ( exp ) ) error_message( #exp " is false in " __FILE__ ); }
# endif

# ifdef NDEBUG
# define CPPAD_PY_ASSERT_KNOWN(exp, msg)  // do nothing
# else
# define CPPAD_PY_ASSERT_KNOWN(exp, msg) \
{	if( ! ( exp ) ) error_message(msg); }
# endif

# endif
