# ifndef CPPAD_PY_ERROR_HPP
# define CPPAD_PY_ERROR_HPP
/* ----------------------------------------------------------------------------
          cppad_py: A C++ Object Library and Python Interface to Cppad
           Copyright (C) 2017-20 Bradley M. Bell (bradbell@seanet.com)
               This program is distributed under the terms of the
               GNU General Public License version 3.0 or later see
                     https://www.gnu.org/licenses/gpl-3.0.txt
---------------------------------------------------------------------------- */
# include <exception>
# include <string>
# include <cppad/py/public_lib.hpp>
/*
-----------------------------------------------------------------------------
{xsrst_begin error_message}

.. include:: ../preamble.rst

Exception Handling
##################

C++ Exceptions
==============
The type of the exception is ``std::runtime_error``
which is derived from ``std::exception`` .
If the standard exception member function ``what()`` is called,
the return value is a message describing the error.

Python Exceptions
=================
The type of the exception is ``RuntimeError``.
If ``err`` is the exception, ``str(err)`` is
a message describing the error.


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

# ifdef NDEBUG
# define CPPAD_PY_ASSERT_UNKNOWN(exp)  // do nothing
# else
# define CPPAD_PY_ASSERT_UNKNOWN(exp) \
{   if( ! ( exp ) ) throw std::runtime_error( #exp " is false in " __FILE__ ); }
# endif

# ifdef NDEBUG
# define CPPAD_PY_ASSERT_KNOWN(exp, msg)  // do nothing
# else
# define CPPAD_PY_ASSERT_KNOWN(exp, msg) \
{   if( ! ( exp ) ) throw std::runtime_error(msg); }
# endif

# endif
