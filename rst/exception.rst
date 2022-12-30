.. _exception-name:

!!!!!!!!!
exception
!!!!!!!!!

.. raw:: html

   <a href="_sources/exception.rst.txt">View page source</a>

.. meta::
   :keywords: exception, exception, handling

.. index:: exception, exception, handling

.. _exception-title:

Exception Handling
##################

.. meta::
   :keywords: c++, exceptions

.. index:: c++, exceptions

.. _exception@C++ Exceptions:

C++ Exceptions
==============
The type of the exception is ``std::runtime_error``
which is derived from ``std::exception`` .
If the standard exception member function ``what()`` is called,
the return value is a message describing the error.

.. meta::
   :keywords: python, exceptions

.. index:: python, exceptions

.. _exception@Python Exceptions:

Python Exceptions
=================
The type of the exception is ``RuntimeError``.
If *err* is the exception, ``str`` (*err*) is
a message describing the error.

.. meta::
   :keywords: example

.. index:: example

.. _exception@Python Exceptions@Example:

Example
*******
:ref:`c++<exception_xam_cpp-name>`,
:ref:`python<exception_xam_py-name>`.

.. toctree::
   :maxdepth: 1
   :hidden:

   exception_xam_cpp
   exception_xam_py
