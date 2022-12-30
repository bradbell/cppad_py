.. _a_double_ctor-name:

!!!!!!!!!!!!!
a_double_ctor
!!!!!!!!!!!!!

.. raw:: html

   <a href="_sources/a_double_ctor.rst.txt">View page source</a>

.. meta::
   :keywords: a_double_ctor, the, a_double, constructor

.. index:: a_double_ctor, the, a_double, constructor

.. _a_double_ctor-title:

The a_double Constructor
########################

.. meta::
   :keywords: syntax

.. index:: syntax

.. _a_double_ctor@Syntax:

Syntax
******

.. meta::
   :keywords: c++

.. index:: c++

.. _a_double_ctor@Syntax@C++:

C++
===
| ``cppad_py::a_double`` *ad* ()
| ``cppad_py::a_double`` *ad* ( *d* )
| ``cppad_py::a_double`` *ad* ( *a_other* )

.. meta::
   :keywords: python

.. index:: python

.. _a_double_ctor@Syntax@Python:

Python
======
| *ad* =  ``cppad_py.a_double`` ()
| *ad* =  ``cppad_py.a_double`` ( *d* )
| *ad* =  ``cppad_py.a_double`` ( *a_other* )

.. meta::
   :keywords: purpose

.. index:: purpose

.. _a_double_ctor@Purpose:

Purpose
*******
Creates a ``cppad_py::a_double`` object that can be use
to track floating point operations and perform algorithmic differentiation.

.. meta::
   :keywords: d

.. index:: d

.. _a_double_ctor@d:

d
*
This argument has c++ prototype

| |tab| ``const double&`` *d*

The resulting *ad* variable represents
a constant function equal to *d* .

.. meta::
   :keywords: a_other

.. index:: a_other

.. _a_double_ctor@a_other:

a_other
*******
This argument has c++ prototype

| |tab| ``const a_double&`` *a_other*

The resulting *ad* variable is the same function
of the independent variables as *a_other* .

.. meta::
   :keywords: ad

.. index:: ad

.. _a_double_ctor@ad:

ad
**
is the ``a_double`` object that is constructed.

.. meta::
   :keywords: example

.. index:: example

.. _a_double_ctor@Example:

Example
*******
All of the other ``a_double`` examples use an ``a_double``
constructor.
