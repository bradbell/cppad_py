.. _a_double_unary_fun-name:

!!!!!!!!!!!!!!!!!!
a_double_unary_fun
!!!!!!!!!!!!!!!!!!

.. raw:: html

   <a href="_sources/a_double_unary_fun.rst.txt">View page source</a>

.. meta::
   :keywords: a_double_unary_fun, unary, functions, with, ad, result

.. index:: a_double_unary_fun, unary, functions, with, ad, result

.. _a_double_unary_fun-title:

Unary Functions with AD Result
##############################

.. meta::
   :keywords: syntax

.. index:: syntax

.. _a_double_unary_fun@Syntax:

Syntax
******

.. meta::
   :keywords: c++

.. index:: c++

.. _a_double_unary_fun@Syntax@C++:

C++
===
*ay* = *ax* . *fun* ()

.. meta::
   :keywords: python

.. index:: python

.. _a_double_unary_fun@Syntax@Python:

Python
======
| *ay* = *ax* . *fun* ()
| *ay* = ``numpy.``\ *fun* ( *ax* )

.. meta::
   :keywords: ax

.. index:: ax

.. _a_double_unary_fun@ax:

ax
**
This object has prototype

| |tab| ``const a_double&`` *ax*

This is the argument for the function evaluation.

.. meta::
   :keywords: fun

.. index:: fun

.. _a_double_unary_fun@fun:

fun
***
This specifies which function is being evaluated and is one
of  following value:
``abs`` ,
``acos`` ,
``asin`` ,
``atan`` ,
``cos`` ,
``cosh`` ,
``erf`` ,
``exp`` ,
``fabs`` ,
``log`` ,
``sin`` ,
``sinh`` ,
``sqrt`` ,
``tan`` ,
``tanh`` .
The ``numpy`` version of the python syntax does not work with the ``abs``
function.
2DO: Add the C++11 functions
asinh, acosh, atanh, expm1, and log1p to this list.

.. meta::
   :keywords: ay

.. index:: ay

.. _a_double_unary_fun@ay:

ay
**
The result object has c++ prototype

| |tab| ``a_double`` *ay*

and is the value of the function *fun* evaluated at the argument *ax*; i.e.,

| |tab| *ay* = *fun* ( *ax* )

.. meta::
   :keywords: example

.. index:: example

.. _a_double_unary_fun@Example:

Example
*******
:ref:`c++<a_double_unary_fun_xam_cpp-name>`,
:ref:`python<a_double_unary_fun_xam_py-name>`.

.. toctree::
   :maxdepth: 1
   :hidden:

   a_double_unary_fun_xam_cpp
   a_double_unary_fun_xam_py
