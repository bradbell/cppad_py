/* -----------------------------------------------------------------------------
           cppad_swig: A C++ Object Library and Swig Interface to Cppad
            Copyright (C) 2017-17 Bradley M. Bell (bradbell@seanet.com)
                This program is distributed under the terms of the
            GNU Affero General Public License version 3.0 or later see
                       http://www.gnu.org/licenses/agpl.txt
----------------------------------------------------------------------------- */
// BEGIN C++
# include <cppad/swig/a_other.hpp>
# include <string>

/*
-----------------------------------------------------------------------------
$begin error_msg$$
$spell
	Perl
	cppad
	std
$$

$section Exception Handling$$

$head Syntax$$
$icode%stored_message% = error_msg(%message%)%$$

$head In Try Block$$
If $icode message$$ is $bold not$$ the empty string,
it is stored in $code error_msg$$ and an exception is thrown.
This is intended to be done inside a $code try$$ block.

$head exception$$
The type of the exception is $code cppad_swig::exception$$
which is derived from $code std::exception$$.
If the standard exception $code what()$$ is called,
the return value will be the stored message.

$head In Catch Block$$
If $icode message$$ is the empty string,
the currently stored message is returned.
This is intended to be done inside a $code catch$$ block.

$head Not Thread Safe$$
The message storage is done using a static variable in
$code error_msg$$ and hence is not thread safe.

$children%
	build/lib/example/cplusplus/a_other_error_msg_xam.cpp%
	build/lib/example/octave/a_other_error_msg_xam.m%
	build/lib/example/perl/a_other_error_msg_xam.pm%
	build/lib/example/python/a_other_error_msg_xam.py
%$$
$head Example$$
$cref/C++/a_other_error_msg_xam.cpp/$$,
$cref/Octave/a_other_error_msg_xam.m/$$,
$cref/Perl/a_other_error_msg_xam.pm/$$,
$cref/Python/a_other_error_msg_xam.py/$$.

$end
*/
namespace cppad_swig {
	const char* exception::what(void) const throw()
	{	return error_msg(""); }
	const char* error_msg(const char* message) throw(cppad_swig::exception)
	{	// previous error message
		static std::string previous = "";
		if( message[0] == '\0' )
			return previous.c_str();
		previous = message;
		//
		// raise exception
		throw cppad_swig::exception();
		//
		// never get to here
		return "";
	}
}
