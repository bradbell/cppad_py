/* -----------------------------------------------------------------------------
           cppad_swig: A C++ Object Library and Swig Interface to Cppad
            Copyright (C) 2017-17 Bradley M. Bell (bradbell@seanet.com)
                This program is distributed under the terms of the
            GNU Affero General Public License version 3.0 or later see
                       http://www.gnu.org/licenses/agpl.txt
----------------------------------------------------------------------------- */
// BEGIN C++
# include <string>
# include <stack>
# include <cppad/swig/other.hpp>
# include <cppad/utility/error_handler.hpp>
# include <cppad/utility/to_string.hpp>

/*
-----------------------------------------------------------------------------
$begin error_message$$
$spell
	vec
	Perl
	cppad
	std
$$

$section Exception Handling$$

$head Syntax$$
$icode%stored_message% = error_message(%input_message%)%$$

$head In Try Block$$
If $icode input_message$$ is $bold not$$ the empty string,
it is stored in $code error_message$$ and an exception is thrown.
This is intended to be done inside a $code try$$ block.

$head exception$$
The type of the exception is $code cppad_swig::exception$$
which is derived from $code std::exception$$.
If the standard exception $code what()$$ is called,
the return value will be the value of $icode input_message$$
when the exception was thrown.

$head In Catch Block$$
If $icode input_message$$ is the empty string,
the most recently stored message in $code error_message$$ is returned.
In addition, the message is deleted from $code error_message$$.
If there are no more messages stored in $code error_message$$,
the empty string is returned.
This is intended to be done inside a $code catch$$ block.

$head Cppad Errors$$
Calls to the Cppad error handler get mapped to a call
to $code error_message$$.

$head Not Thread Safe$$
The message storage is done using static information in
$code error_message$$ and hence is not thread safe.

$children%
	build/lib/example/cplusplus/other_error_message_xam.cpp%
	build/lib/example/octave/other_error_message_xam.m%
	build/lib/example/perl/other_error_message_xam.pm%
	build/lib/example/python/other_error_message_xam.py
%$$
$head Example$$
$cref/C++/other_error_message_xam.cpp/$$,
$cref/Octave/other_error_message_xam.m/$$,
$cref/Perl/other_error_message_xam.pm/$$,
$cref/Python/other_error_message_xam.py/$$.

$end
*/
namespace cppad_swig {
	// -----------------------------------------------------------------------
	// map Cppad error handler to Cppad Swig error handler
	void cppad_error_handler(
		bool known       ,
		int  line        ,
		const char *file ,
		const char *exp  ,
		const char *msg  )
	{	std::string message = "Cppad Error:\n";
		if( known )
			message += msg;
		else
			message += "reason for the error is unknown";
		message += "\nline = ";
		message += CppAD::to_string(line);
		message += "\nfile = ";
		message += file;
		message += "\nsource code = ";
		message += exp;
		//
		error_message(message.c_str());
	}
	CppAD::ErrorHandler cppad_error_mapper(cppad_error_handler);
	// -----------------------------------------------------------------------
	// ctor
	exception::exception(const char* message) : message_(message)
	{ }
	// dtor
	exception::~exception(void) throw()
	{ }
	// what
	const char* exception::what(void) const throw()
	{   return message_.c_str(); }
	// -----------------------------------------------------------------------
	const char*
	error_message(const char* input_message) throw(cppad_swig::exception)
	{	 //
		// message_stack
		static std::stack<std::string> message_stack;
		//
		// return value
		static std::string return_string;
		//
		// input value
		std::string input_string = input_message;
		//
		// push message and raise exception
		if( input_string != "" )
		{	message_stack.push(input_string);
			throw cppad_swig::exception(input_message);
		}
		//
		// pop message
		if( message_stack.size() > 0 )
		{	return_string = message_stack.top();
			message_stack.pop();
		}
		else
			return_string = "";
		return return_string.c_str();
	}
	// -----------------------------------------------------------------------
}
