.. _cpp_fun_ctor-name:

!!!!!!!!!!!!
cpp_fun_ctor
!!!!!!!!!!!!

.. raw:: html

   <a href="_sources/cpp_fun_ctor.rst.txt">View page source</a>

.. meta::
   :keywords: cpp_fun_ctor, stop, current, recording, store, function, object

.. index:: cpp_fun_ctor, stop, current, recording, store, function, object

.. _cpp_fun_ctor-title:

Stop Current Recording and Store Function Object
################################################

.. meta::
   :keywords: syntax

.. index:: syntax

.. _cpp_fun_ctor@Syntax:

Syntax
******

.. meta::
   :keywords: d_fun

.. index:: d_fun

.. _cpp_fun_ctor@Syntax@d_fun:

d_fun
=====

| *f* =  ``cppad_py::d_fun`` ( *ax* , *ay* )

.. meta::
   :keywords: a_fun

.. index:: a_fun

.. _cpp_fun_ctor@Syntax@a_fun:

a_fun
=====

| *af* =  ``cppad_py::a_fun`` ( *f* )

.. meta::
   :keywords: ax

.. index:: ax

.. _cpp_fun_ctor@ax:

ax
**
This argument has prototype

| |tab| ``const vec_a_double&`` *ax*

and must be the same as
:ref:`ax<cpp_independent@ax>`
returned by the previous call to ``independent`` ; i.e.,
it must be the independent variable vector.
We use the notation *n* = *ax*\ ``.size`` ()
to denote the number of independent variables.

.. meta::
   :keywords: ay

.. index:: ay

.. _cpp_fun_ctor@ay:

ay
**
This argument has prototype

| |tab| ``const vec_a_double&`` *ax*

It specifies the dependent variables.
We use the notation *m* = *ay*\ ``.size`` ()
to denote the number of dependent variables.

.. meta::
   :keywords: f

.. index:: f

.. _cpp_fun_ctor@f:

f
*
This result has prototype

| |tab| ``cppad_py::d_fun`` *f*

It has a representation for the floating point operations
that mapped the independent variables *ax*
to the dependent variables *ay* .
This object computes function and derivative values using ``double`` .

.. meta::
   :keywords: empty, function

.. index:: empty, function

.. _cpp_fun_ctor@f@Empty Function:

Empty Function
==============
In the case where *ax* and *ay* have size zero,
the function is 'empty' and all its sizes are zero; see
:ref:`cpp_fun_property-name`.

.. meta::
   :keywords: af

.. index:: af

.. _cpp_fun_ctor@af:

af
**
This result has prototype

| |tab| ``cppad_py::a_fun`` *af*

It has a representation of the same function as *f* .
This object computes function and derivative values using ``a_double`` .
Initially, there are not Taylor coefficient stored in *af* ; i.e.,
:ref:`af_size_order()<cpp_fun_property@size_order>` is zero.

.. meta::
   :keywords: example

.. index:: example

.. _cpp_fun_ctor@Example:

Example
*******
All of the examples use these constructors.
