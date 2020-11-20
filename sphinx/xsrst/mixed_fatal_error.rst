!!!!!!!!!!!!!!!!!
mixed_fatal_error
!!!!!!!!!!!!!!!!!

.. toctree::
   :maxdepth: 1
   :hidden:

   mixed_fatal_error_xam_py

.. include:: ../preamble.rst

.. meta::
   :keywords: mixed_fatal_error, mixed, class, fatal, errors

.. index:: mixed_fatal_error, mixed, class, fatal, errors

.. _mixed_fatal_error:

Mixed Class Fatal Errors
########################
.. contents::
   :local:

.. meta::
   :keywords: syntax

.. index:: syntax

.. _mixed_fatal_error.syntax:

Syntax
******
| *mixed_obj*\ ``.post_fatal_error`` ( *message* )

.. meta::
   :keywords: post_fatal_error

.. index:: post_fatal_error

.. _mixed_fatal_error.post_fatal_error:

post_fatal_error
****************
is a mixed class member function that posts a fatal error.
It's *message* argument is an `str` describing the error.
A call to this function will raise a python ``RuntimeError`` with
the specified message.  It's main purpose is for testing.

.. meta::
   :keywords: example

.. index:: example

.. _mixed_fatal_error.example:

Example
*******
:ref:`mixed_fatal_error_xam_py<mixed_fatal_error_xam_py>`

----

xsrst input file: ``lib/python/cppad_py/mixed.py``
