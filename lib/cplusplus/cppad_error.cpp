/* -----------------------------------------------------------------------------
           cppad_py: A C++ Object Library and Python Interface to Cppad
         Copyright (C) 2017-22 Bradley M. Bell (bradbell@seanet.com)
            This program is distributed under the terms of the
            GNU General Public License version 3.0 or later see
                      https://www.gnu.org/licenses/gpl-3.0.txt
----------------------------------------------------------------------------- */
# include <stdexcept>
# include <cppad/utility/error_handler.hpp>
# include <cppad/utility/to_string.hpp>

/*
{xrst_begin cppad_error}
{xrst_spell
   cppad
   exp
   msg
   namespace
   runtime
}

Converting CppAD Errors To Python Exceptions
############################################

Code
****
The following CppAD error handler is created
in the empty namespace corresponding to the ``cppad_error.cpp`` file:
{xrst_code cpp}
   CppAD::ErrorHandler cppad_error(handler);
{xrst_code}

handler
*******
The error handler includes the following information in the exception message:

.. csv-table::
   :header: Label, Description
   :widths: 10, 90

   *file* , The name of the CppAD file where the error occurred.
   *line* , The line number in the file where the error occurred.
   *exp*  , The c++ logical expression that should have been true.
   *msg*  , A descriptive error message about the problem.

C++ throw
*********
A ``std::runtime_error`` *cpp_err* is thrown with
*cpp_err*\ ``.what()`` a string containing the information above.

Python raise
************
The swig wrapper for each call to CppAD will catch
the ``std::runtime_error`` and raise a python
``RuntimeError`` *py_err* where ``str``\ ( *py_err* )
is a string containing the information above.

Example
*******
{xrst_toc_list
   example/python/core/cppad_error_xam.py
}


{xrst_end cppad_error}
*/
namespace { // BEGIN_EMPTY_NAMESPACE
   void handler(
      bool known       ,
      int  line        ,
      const char *file ,
      const char *exp  ,
      const char *msg  )
     {  // use the most recent cppad_mixed fatal_error routine
      std::string message;
      //
      message += "\nCppAD: file = ";
      message += file;
      //
      message += "\nline = ";
      message += CppAD::to_string(line);
      //
      message += "\nexp = ";
      message += exp;
      //
      message += "\nmsg = ";
      message += msg;
      //
      std::runtime_error e(message);
      throw(e);
   }
   CppAD::ErrorHandler cppad_error(handler);
} // END_EMPTY_NAMESPACE
