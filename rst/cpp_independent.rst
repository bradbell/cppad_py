.. _cpp_independent-name:

!!!!!!!!!!!!!!!
cpp_independent
!!!!!!!!!!!!!!!

.. raw:: html

   <a href="_sources/cpp_independent.rst.txt">View page source</a>

.. meta::
   :keywords: cpp_independent, declare, independent, variables, start, recording

.. index:: cpp_independent, declare, independent, variables, start, recording

.. _cpp_independent-title:

Declare Independent Variables and Start Recording
#################################################

.. meta::
   :keywords: syntax

.. index:: syntax

.. _cpp_independent@Syntax:

Syntax
******

| *ax* =  ``cppad_py::independent`` ( *x* )
| *a_both* =  ``cppad_py::independent`` ( *x* , *dynamic* )

.. meta::
   :keywords: purpose

.. index:: purpose

.. _cpp_independent@Purpose:

Purpose
*******
This starts recording :ref:`a_double-name` operations.
This recording is terminated, and the information is stored,
by calling the :ref:`d_fun_constructor<cpp_fun_ctor-name>`.
It can be terminated, and the information is lost,
by calling :ref:`abort_recording<cpp_abort_recording-name>`.

.. meta::
   :keywords: x

.. index:: x

.. _cpp_independent@x:

x
*
This argument has prototype

| |tab| ``const vec_double&`` *x*

Its specifies the number of independent variables
and their values during the recording.
We use the notation *nx* = *x*\ ``.size`` ()
to denote the number of independent variables.

.. meta::
   :keywords: dynamic

.. index:: dynamic

.. _cpp_independent@dynamic:

dynamic
*******
This argument has prototype

| |tab| ``const vec_double&`` *dynamic*

Its specifies the number of independent dynamic parameters
and their values during the recording.
We use the notation *nd* = *dynamic*\ ``.size`` ()
to denote the number of independent variables.

.. meta::
   :keywords: ax

.. index:: ax

.. _cpp_independent@ax:

ax
**
This result has prototype

| |tab| ``vec_a_double&`` *ax*

and is the vector of independent variables.
It has size *nx* and for
*i* = 0 to *n* -1

| |tab| *ax* [ *i* ] == *x* [ *i* ]

.. meta::
   :keywords: a_both

.. index:: a_both

.. _cpp_independent@a_both:

a_both
******
this result has prototype

| |tab| ``vec_a_double&`` *a_both*

and is the vector of both the independent variables
and independent dynamic parameters.
It has size *nx* + *nd* .
For *i* = 0 to *nx* -1

| |tab| *a_both* [ *i* ] == *x* [ *i* ]

is the *i*-th independent variable.
For *i* = 0 to *nd* -1

| |tab| *a_both* [ *nx* + *i* ] == *dynamic* [ *i* ]

is the *i*-th independent dynamic parameter.

.. meta::
   :keywords: example

.. index:: example

.. _cpp_independent@Example:

Example
*******
Most of the c++ ``d_fun`` examples use the *ax*
return syntax.
The :ref:`fun_dynamic_xam_cpp-name` example uses the *a_both*
return syntax.

.. toctree::
   :maxdepth: 1
   :hidden:

   fun_dynamic_xam_cpp
