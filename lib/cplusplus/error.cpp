/* -----------------------------------------------------------------------------
           cppad_py: A C++ Object Library and Python Interface to Cppad
            Copyright (C) 2017-20 Bradley M. Bell (bradbell@seanet.com)
                This program is distributed under the terms of the
                GNU General Public License version 3.0 or later see
                      https://www.gnu.org/licenses/gpl-3.0.txt
----------------------------------------------------------------------------- */
// BEGIN C++
# include <string>
# include <stack>
# include <cppad/py/error.hpp>
# include <cppad/utility/error_handler.hpp>
# include <cppad/utility/to_string.hpp>

/*
-----------------------------------------------------------------------------
{xsrst_begin error_message}

.. include:: ../preamble.rst

{xsrst_spell
    cppad
}

Exception Handling
##################

Syntax
******
*stored_message* =  ``error_message`` ( *input_message* )

In Try Block
************
If *input_message* is **not** the empty string,
it is stored in ``error_message`` and an exception is thrown.
This is intended to be done inside a ``try`` block.

exception
=========
The type of the exception is ``std::runtime_error``
which is derived from ``std::exception`` .
If the standard exception ``what()`` is called,
the return value will be the value of *input_message*
when the exception was thrown.

In Catch Block
**************
If *input_message* is the empty string,
the most recently stored message in ``error_message`` is returned.
In addition, the message is deleted from ``error_message`` .
If there are no more messages stored in ``error_message`` ,
the empty string is returned.
This is intended to be done inside a ``catch`` block.

Cppad Errors
************
Calls to the Cppad error handler get mapped to a call
to ``error_message`` .

Not Thread Safe
***************
The message storage is done using static information in
``error_message`` and hence is not thread safe.

{xsrst_children
    example/cplusplus/error_message_xam.cpp
    example/python/core/error_message_xam.py
}
Example
*******
:ref:`c++<error_message_xam_cpp>`,
:ref:`python<error_message_xam_py>`.

{xsrst_end error_message}
*/
namespace cppad_py {
    // -----------------------------------------------------------------------
    // map Cppad error handler to Cppad Py error handler
    void cppad_error_handler(
        bool known       ,
        int  line        ,
        const char *file ,
        const char *exp  ,
        const char *msg  )
    {   std::string message = "Cppad Error:\n";
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
    const char* error_message(const char* input_message)
    {   //
        // message_stack
        static std::stack<std::string> message_stack;
        //
        // return value
        static std::string return_string;
        //
        // input value
        std::string input_string = input_message;
        //
        // Check for a throw
        if( input_string != "" )
        {   // push message and raise exception
            message_stack.push(input_string);
            throw std::runtime_error( input_string );
        }
        //
        if( message_stack.size() > 0 )
        {   // pop message
            return_string = message_stack.top();
            message_stack.pop();
        }
        else
            return_string = "";
        return return_string.c_str();
    }
    // -----------------------------------------------------------------------
}
