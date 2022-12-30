.. _py_independent-name:

!!!!!!!!!!!!!!
py_independent
!!!!!!!!!!!!!!

.. raw:: html

   <a href="_sources/py_independent.rst.txt">View page source</a>

.. meta::
   :keywords: py_independent, declare, independent, variables, start, recording

.. index:: py_independent, declare, independent, variables, start, recording

.. _py_independent-title:

Declare Independent Variables and Start Recording
#################################################

.. meta::
   :keywords: syntax

.. index:: syntax

.. _py_independent@Syntax:

Syntax
******

| *ax* =  ``cppad_py.independent`` ( *x* )
| ( *ax* , *adynamic* ) =  ``cppad_py.independent`` ( *x* , *dynamic* )

.. meta::
   :keywords: x

.. index:: x

.. _py_independent@x:

x
*
This argument is a numpy vector with ``float`` elements.
It specifies the number of independent variables
and their values during the recording.
We use *nx* = *x*\ ``.size``
to denote the number of independent variables.

.. meta::
   :keywords: dynamic

.. index:: dynamic

.. _py_independent@dynamic:

dynamic
*******
This argument is a numpy vector with ``float`` elements.
It specifies the number of independent dynamic parameters
and their values during the recording.
We use *nd* = *dynamic*\ ``.size``
to denote the number of independent dynamic parameters.

.. meta::
   :keywords: ax

.. index:: ax

.. _py_independent@ax:

ax
**
This result is a numpy vector with ``a_double`` elements.
This is the vector of independent variables.
It has size *nx* and for
*i* = 0 to *n* -1

| |tab| *ax* [ *i* ]. ``value`` () == *x* [ *i* ]

.. meta::
   :keywords: adynamic

.. index:: adynamic

.. _py_independent@adynamic:

adynamic
********
This result is a numpy vector with ``a_double`` elements.
This is the vector of independent dynamic parameters.
It has size *nd* and for
*i* = 0 to *n* -1

| |tab| *adynamic* [ *i* ]. ``value`` () == *dynamic* [ *i* ]

.. meta::
   :keywords: purpose

.. index:: purpose

.. _py_independent@Purpose:

Purpose
*******
This starts a recording of the :ref:`a_double-name` operations.
This recording is terminated, and the information is stored,
by calling the :ref:`d_fun_constructor<py_fun_ctor-name>`.
It is terminated, and the information is lost,
by calling :ref:`abort_recording<py_abort_recording-name>`.

.. meta::
   :keywords: example

.. index:: example

.. _py_independent@Example:

Example
*******
Most of the python ``d_fun`` examples use this function.
The :ref:`fun_dynamic_xam_py-name` uses the syntax that includes
dynamic parameters.

.. toctree::
   :maxdepth: 1
   :hidden:

   fun_dynamic_xam_py
