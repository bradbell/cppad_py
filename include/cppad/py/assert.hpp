# ifndef CPPAD_PY_ASSERT_HPP
# define CPPAD_PY_ASSERT_HPP
// SPDX-License-Identifier: GPL-3.0-or-later
// SPDX-FileCopyrightText: Bradley M. Bell <bradbell@seanet.com>
// SPDX-FileContributor: 2017-23 Bradley M. Bell
// ----------------------------------------------------------------------------
# include <exception>
# include <string>
# include <cppad/py/public_lib.hpp>
/*
-----------------------------------------------------------------------------
{xrst_begin exception}
{xrst_spell
   runtime
}

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
If *err* is the exception, ``str`` (*err*) is
a message describing the error.


{xrst_toc_hidden
   example/cplusplus/exception_xam.cpp
   example/python/core/exception_xam.py
}
Example
*******
:ref:`c++<exception_xam.cpp-name>`,
:ref:`python<exception_xam.py-name>`.

{xrst_end exception}
*/

# define CPPAD_PY_ASSERT_UNKNOWN(exp) \
{  if( ! ( exp ) ) throw std::runtime_error( #exp " is false in " __FILE__ ); }

# define CPPAD_PY_ASSERT_KNOWN(exp, msg) \
{  if( ! ( exp ) ) throw std::runtime_error(msg); }

# endif
