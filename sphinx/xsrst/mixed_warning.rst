!!!!!!!!!!!!!
mixed_warning
!!!!!!!!!!!!!

.. toctree::
   :maxdepth: 1
   :hidden:

   mixed_warning_xam_py

.. include:: ../preamble.rst

.. meta::
   :keywords: mixed_warning, mixed, class, warnings

.. index:: mixed_warning, mixed, class, warnings

.. _mixed_warning:

Mixed Class Warnings
####################
.. contents::
   :local:

.. meta::
   :keywords: syntax

.. index:: syntax

.. _mixed_warning.syntax:

Syntax
******
| *warning* ( *message* )
| *mixed_obj*\ ``.post_warning`` ( *message* )

.. meta::
   :keywords: warning

.. index:: warning

.. _mixed_warning.warning:

warning
*******
This is the :ref:`mixed_ctor.warning` argument to the  mixed class
constructor.
It's *message* argument is an `str` describing the warning.

.. meta::
   :keywords: post_warning

.. index:: post_warning

.. _mixed_warning.post_warning:

post_warning
************
is a mixed class member function that posts a warning.
It's *message* argument is an `str` describing the warning.
It's main purpose is for testing.

.. meta::
   :keywords: example

.. index:: example

.. _mixed_warning.example:

Example
*******
:ref:`mixed_warning_xam_py<mixed_warning_xam_py>`

----

xsrst input file: ``lib/python/cppad_py/mixed.py``
