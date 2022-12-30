.. _more_cpp-name:

!!!!!!!!
more_cpp
!!!!!!!!

.. raw:: html

   <a href="_sources/more_cpp.rst.txt">View page source</a>

.. meta::
   :keywords: more_cpp, steps, to, add, more, c++, functions

.. index:: more_cpp, steps, to, add, more, c++, functions

.. _more_cpp-title:

Steps To Add More C++ Functions
###############################

.. meta::
   :keywords: purpose

.. index:: purpose

.. _more_cpp@Purpose:

Purpose
*******
This section outlines the steps for adding more CppAD functionality
to cppad_py.
This is done by example showing how the :ref:`cpp_fun_new_dynamic-name` was added.
This example case was chosen because it required both changing one
C++ function, :ref:`cpp_independent-name`,
and adding a new C++ function, :ref:`cpp_fun_new_dynamic-name`.

.. meta::
   :keywords: include, file

.. index:: include, file

.. _more_cpp@Include File:

Include File
************

.. meta::
   :keywords: independent

.. index:: independent

.. _more_cpp@Include File@independent:

independent
===========
The include file ``include/cppad/py/fun.hpp``
was edited to add the following prototype:

.. literalinclude:: ../lib/cplusplus/more_cpp.xrst
   :lines: 39-42
   :language: cpp

The ``independent`` function is not part of the
``d_fun`` or ``a_fun`` class, but
calling it is the first step in creating these objects.
This is why its prototype is in the ``fun.hpp`` file.

.. meta::
   :keywords: new_dynamic

.. index:: new_dynamic

.. _more_cpp@Include File@new_dynamic:

new_dynamic
===========
The include file ``include/cppad/py/fun.hpp``
was edited to add the following member function to ``d_fun`` :

.. literalinclude:: ../lib/cplusplus/more_cpp.xrst
   :lines: 54-54
   :language: cpp

The following member function was added to ``a_fun`` :

.. literalinclude:: ../lib/cplusplus/more_cpp.xrst
   :lines: 58-58
   :language: cpp

.. meta::
   :keywords: documentation

.. index:: documentation

.. _more_cpp@Documentation:

Documentation
*************

.. meta::
   :keywords: independent

.. index:: independent

.. _more_cpp@Documentation@independent:

independent
===========
The C++ file ``lib/cplusplus/fun.cpp``
was edited to add the following syntax documentation:

| |tab| *a_both* =  ``cppad_py::independent`` ( *x* , *dynamic* )

and the corresponding return value was documented; see
:ref:`a_both<cpp_independent@a_both>`.

.. meta::
   :keywords: new_dynamic

.. index:: new_dynamic

.. _more_cpp@Documentation@new_dynamic:

new_dynamic
===========
The :ref:`cpp_fun_new_dynamic-name` documentation was added.

.. meta::
   :keywords: example

.. index:: example

.. _more_cpp@Documentation@Example:

Example
=======
The corresponding example file was added to the documentation,
below the :ref:`cpp_independent-name` section, using the OMhelp commands:

| |tab| { ``xrst_dollar}children%``
| |tab| |tab| ``example/cplusplus/fun_dynamic_xam.cpp``
| |tab| ``%${xrst_dollar`` }

In addition, a reference to this example was added under the
:ref:`example<cpp_independent@Example>` heading in the ``independent``
documentation.

.. meta::
   :keywords: implementation

.. index:: implementation

.. _more_cpp@Implementation:

Implementation
**************

.. meta::
   :keywords: independent

.. index:: independent

.. _more_cpp@Implementation@independent:

independent
===========
The following function was added to the ``lib/cplusplus/fun.cpp`` file:

.. literalinclude:: ../lib/cplusplus/fun.cpp
   :lines: 119-140
   :language: cpp

.. meta::
   :keywords: new_dynamic

.. index:: new_dynamic

.. _more_cpp@Implementation@new_dynamic:

new_dynamic
===========
The following function
was added to the ``lib/cplusplus/fun.cpp`` file:

.. literalinclude:: ../lib/cplusplus/fun.cpp
   :lines: 464-480
   :language: cpp

A similar function was added to the ``a_fun`` class.

.. meta::
   :keywords: example

.. index:: example

.. _more_cpp@Example:

Example
*******
The file ``example/cplusplus/fun_dynamic_xam.cpp`` was added
with the following contents:
:ref:`fun_dynamic_xam_cpp-name`.
In addition, in the file ``example/cplusplus/check_all.cpp`` :

| |tab| ``extern bool fun_optimize_xam(void);``

was added to the external declarations and

| |tab| ``ok &= Run( fun_optimize_xam,          "fun_optimize_xam"        );``

was added to the main program.

.. meta::
   :keywords: testing

.. index:: testing

.. _more_cpp@Testing:

Testing
*******
You must do a git add for all of the new files before running
``bin/check_all.sh`` .
After all the C++ changes above were implemented,
``bin/check_all.sh`` was run and the changes were made
until the warnings and errors were fixed.
The command

| |tab| ``grep 'fun_dynamic_xam' check_all.log``

was used to make sure that the new C++ example / test was run.
Note that if a particular step in ``bin/check_all.sh`` is failing,
you can just re-run that step to see if a particular fix works.
Once the C++ tests were working, the changes where checked into using
``git`` .
