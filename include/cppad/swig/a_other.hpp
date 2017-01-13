# ifndef CPPAD_SWIG_A_OTHER_HPP
# define CPPAD_SWIG_A_OTHER_HPP
/* ----------------------------------------------------------------------------
          cppad_swig: A C++ Object Library and Swig Interface to Cppad
           Copyright (C) 2017-17 Bradley M. Bell (bradbell@seanet.com)
               This program is distributed under the terms of the
           GNU Affero General Public License version 3.0 or later see
                      http://www.gnu.org/licenses/agpl.txt
---------------------------------------------------------------------------- */
# include <exception>
# include <string>

namespace cppad_swig {
	class exception : public std::exception
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
	const char* error_message(const char* message) throw(cppad_swig::exception);
}

# endif
