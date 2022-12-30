.. _cppad_error-name:

!!!!!!!!!!!
cppad_error
!!!!!!!!!!!

.. raw:: html

   <a href="_sources/cppad_error.rst.txt">View page source</a>

.. meta::
   :keywords: cppad_error, converting, cppad, errors, to, python, exceptions

.. index:: cppad_error, converting, cppad, errors, to, python, exceptions

.. _cppad_error-title:

Converting CppAD Errors To Python Exceptions
############################################

.. meta::
   :keywords: code

.. index:: code

.. _cppad_error@Code:

Code
****
The following CppAD error handler is created
in the empty namespace corresponding to the ``cppad_error.cpp`` file:

.. literalinclude:: ../lib/cplusplus/cppad_error.cpp
   :lines: 27-27
   :language: cpp

.. meta::
   :keywords: handler

.. index:: handler

.. _cppad_error@handler:

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

.. meta::
   :keywords: c++, throw

.. index:: c++, throw

.. _cppad_error@C++ throw:

C++ throw
*********
A ``std::runtime_error`` *cpp_err* is thrown with
*cpp_err*\ ``.what()`` a string containing the information above.

.. meta::
   :keywords: python, raise

.. index:: python, raise

.. _cppad_error@Python raise:

Python raise
************
The swig wrapper for each call to CppAD will catch
the ``std::runtime_error`` and raise a python
``RuntimeError`` *py_err* where ``str``\ ( *py_err* )
is a string containing the information above.

.. meta::
   :keywords: example

.. index:: example

.. _cppad_error@Example:

Example
*******

-  :ref:`cppad_error_xam-title`

.. toctree::
   :maxdepth: 1
   :hidden:

   cppad_error_xam
