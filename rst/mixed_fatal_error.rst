.. _mixed_fatal_error-name:

!!!!!!!!!!!!!!!!!
mixed_fatal_error
!!!!!!!!!!!!!!!!!

.. raw:: html

   <a href="_sources/mixed_fatal_error.rst.txt">View page source</a>

.. meta::
   :keywords: mixed_fatal_error, mixed, class, fatal, errors

.. index:: mixed_fatal_error, mixed, class, fatal, errors

.. _mixed_fatal_error-title:

Mixed Class Fatal Errors
########################

.. meta::
   :keywords: syntax

.. index:: syntax

.. _mixed_fatal_error@Syntax:

Syntax
******
| *mixed_obj*\ ``.post_fatal_error`` ( *message* )

.. meta::
   :keywords: post_fatal_error

.. index:: post_fatal_error

.. _mixed_fatal_error@post_fatal_error:

post_fatal_error
****************
is a mixed class member function that posts a fatal error.
It's *message* argument is an `str` describing the error.
A call to this function will raise a python ``RuntimeError`` with
the specified message.  It's main purpose is for testing.

.. meta::
   :keywords: example

.. index:: example

.. _mixed_fatal_error@Example:

Example
*******
:ref:`mixed_fatal_error_xam_py-name`

.. toctree::
   :maxdepth: 1
   :hidden:

   mixed_fatal_error_xam_py
