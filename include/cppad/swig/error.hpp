# ifndef CPPAD_SWIG_ERROR_HPP
# define CPPAD_SWIG_ERROR_HPP
/* ----------------------------------------------------------------------------
          cppad_swig: A C++ Object Library and Swig Interface to Cppad
           Copyright (C) 2017-17 Bradley M. Bell (bradbell@seanet.com)
               This program is distributed under the terms of the
               GNU General Public License version 3.0 or later see
                     https://www.gnu.org/licenses/gpl-3.0.txt
---------------------------------------------------------------------------- */
# include <exception>
# include <string>
# include <cppad/swig/public_lib.hpp>

namespace cppad_swig {
	class CPPAD_SWIG_LIB_PUBLIC exception : public std::exception
	{	public:
		// message for this exception
		const std::string message_;
		// ctor
		exception(const char* message);
		// dtor
		virtual ~exception() throw();
		// what
		virtual const char* what(void) const throw();
	};
	CPPAD_SWIG_LIB_PUBLIC
	const char* error_message(const char* message) throw(cppad_swig::exception);
}

# ifdef NDEBUG
# define CPPAD_SWIG_ASSERT_UNKNOWN(exp)  // do nothing
# else
# define CPPAD_SWIG_ASSERT_UNKNOWN(exp) \
{	if( ! ( exp ) ) error_message( #exp " is false in " __FILE__ ); }
# endif

# ifdef NDEBUG
# define CPPAD_SWIG_ASSERT_KNOWN(exp, msg)  // do nothing
# else
# define CPPAD_SWIG_ASSERT_KNOWN(exp, msg) \
{	if( ! ( exp ) ) error_message(msg); }
# endif

# endif
