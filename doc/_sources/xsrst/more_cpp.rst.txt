!!!!!!!!
more_cpp
!!!!!!!!

.. include:: ../preamble.rst

.. meta::
   :keywords: more_cpp, steps, to, add, more, c++, functions

.. index:: more_cpp, steps, to, add, more, c++, functions

.. _more_cpp:

Steps To Add More C++ Functions
###############################
.. contents::
   :local:

.. meta::
   :keywords: purpose

.. index:: purpose

.. _more_cpp.purpose:

Purpose
*******
This section outlines the steps for adding more CppAD functionality
to cppad_py.
This is done by example showing how the :ref:`cpp_fun_new_dynamic<cpp_fun_new_dynamic>` was added.
This example case was chosen because it required both changing one
C++ function, :ref:`cpp_independent<cpp_independent>`,
and adding a new C++ function, :ref:`cpp_fun_new_dynamic<cpp_fun_new_dynamic>`.

.. meta::
   :keywords: include, file

.. index:: include, file

.. _more_cpp.include_file:

Include File
************

.. meta::
   :keywords: independent

.. index:: independent

.. _more_cpp.include_file.independent:

independent
===========
The include file ``include/cppad/py/fun.hpp``
was edited to add the following prototype:

.. code-block:: cpp

        CPPAD_PY_LIB_PUBLIC
        std::vector<a_double> independent(
            const std::vector<double>& x, const std::vector<double>& dynamic
        );

The ``independent`` function is not part of the
``d_fun`` or ``a_fun`` class, but
calling it is the first step in creating these objects.
This is why its prototype is in the ``fun.hpp`` file.

.. meta::
   :keywords: new_dynamic

.. index:: new_dynamic

.. _more_cpp.include_file.new_dynamic:

new_dynamic
===========
The include file ``include/cppad/py/fun.hpp``
was edited to add the following member function to ``d_fun`` :

.. code-block:: cpp

        void new_dynamic(const std::vector<double>& dynamic);

The following member function was added to ``a_fun`` :

.. code-block:: cpp

        void new_dynamic(const std::vector<a_double>& adynamic);

.. meta::
   :keywords: documentation

.. index:: documentation

.. _more_cpp.documentation:

Documentation
*************

.. meta::
   :keywords: independent

.. index:: independent

.. _more_cpp.documentation.independent:

independent
===========
The C++ file ``lib/cplusplus/fun.cpp``
was edited to add the following syntax documentation:

| |tab| *a_both* =  ``cppad_py::independent`` ( *x* , *dynamic* )

and the corresponding return value was documented; see
:ref:`a_both<cpp_independent.a_both>`.

.. meta::
   :keywords: new_dynamic

.. index:: new_dynamic

.. _more_cpp.documentation.new_dynamic:

new_dynamic
===========
The :ref:`cpp_fun_new_dynamic<cpp_fun_new_dynamic>` documentation was added.

.. meta::
   :keywords: example

.. index:: example

.. _more_cpp.documentation.example:

Example
=======
The corresponding example file was added to the documentation,
below the :ref:`cpp_independent<cpp_independent>` section, using the OMhelp commands:

| |tab| { ``xsrst_dollar}children%``
| |tab| |tab| ``example/cplusplus/fun_dynamic_xam.cpp``
| |tab| ``%${xsrst_dollar`` }

In addition, a reference to this example was added under the
:ref:`example<cpp_independent.example>` heading in the ``independent``
documentation.

.. meta::
   :keywords: implementation

.. index:: implementation

.. _more_cpp.implementation:

Implementation
**************

.. meta::
   :keywords: independent

.. index:: independent

.. _more_cpp.implementation.independent:

independent
===========
The following function was added to the ``lib/cplusplus/fun.cpp`` file:

.. literalinclude:: ../../lib/cplusplus/fun.cpp
    :lines: 124-145
    :language: cpp

.. meta::
   :keywords: new_dynamic

.. index:: new_dynamic

.. _more_cpp.implementation.new_dynamic:

new_dynamic
===========
The following function
was added to the ``lib/cplusplus/fun.cpp`` file:

.. literalinclude:: ../../lib/cplusplus/fun.cpp
    :lines: 476-492
    :language: cpp

A similar function was added to the ``a_fun`` class.

.. meta::
   :keywords: example

.. index:: example

.. _more_cpp.example:

Example
*******
The file ``example/cplusplus/fun_dynamic_xam.cpp`` was added
with the following contents:
:ref:`fun_dynamic_xam_cpp<fun_dynamic_xam_cpp>`.
In addition, in the file ``example/cplusplus/check_all.cpp`` :

| |tab| ``extern bool fun_optimize_xam(void);``

was added to the external declarations and

| |tab| ``ok &= Run( fun_optimize_xam,          "fun_optimize_xam"        );``

was added to the main program.

.. meta::
   :keywords: testing

.. index:: testing

.. _more_cpp.testing:

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

----

xsrst input file: ``lib/cplusplus/more_cpp.xsrst``
