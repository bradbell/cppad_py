!!!!!!!!!!!!!!!
a_double_binary
!!!!!!!!!!!!!!!

.. toctree::
   :maxdepth: 1
   :hidden:

   a_double_binary_xam_py
   a_double_binary_xam_cpp

.. include:: ../preamble.rst

.. meta::
   :keywords: a_double_binary, a_double, binary, operators, with, an, ad, result

.. index:: a_double_binary, a_double, binary, operators, with, an, ad, result

.. _a_double_binary:

a_double Binary Operators with an AD Result
###########################################
.. contents::
   :local:

.. meta::
   :keywords: syntax

.. index:: syntax

.. _a_double_binary.syntax:

Syntax
******

.. meta::
   :keywords: python

.. index:: python

.. _a_double_binary.syntax.python:

Python
======
| *az* = *ax* *op* *ay*
| *az* = *ax* *op* *y*
| *az* = *x* *op* *ay*

.. meta::
   :keywords: c++

.. index:: c++

.. _a_double_binary.syntax.c++:

C++
===
| *az* = *ax* *op* *ay*
| *az* = *ax* *op* *y*
| *az* = *fun* ( *x* , *ax* )

.. meta::
   :keywords: op

.. index:: op

.. _a_double_binary.op:

op
**
The binary operator *op* is one of the following:
addition ``+`` ,
subtraction ``-`` ,
multiplication ``*`` ,
division ``/`` , or
exponentiation ``**`` .
Note that exponentiation in c++ is special and always has the function syntax;
i.e.,

| *az* = *pow* ( *ax* , *ay* )
| *az* = *pow* ( *ax* , *y* )
| *az* = *pow* ( *x* , *ay* )

.. meta::
   :keywords: fun

.. index:: fun

.. _a_double_binary.fun:

fun
***
This function is one of the following:
``radd`` (right addition) ,
``rsub`` (right subtraction) ,
``rmul`` (right multiplication) ,
``rdiv`` (right division).

.. meta::
   :keywords: ax

.. index:: ax

.. _a_double_binary.ax:

ax
**
This object has c++ prototype

| |tab| ``const a_double&`` *ax*

.. meta::
   :keywords: ay

.. index:: ay

.. _a_double_binary.ay:

ay
**
This object has c++ prototype

| |tab| ``const a_double&`` *ay*

.. meta::
   :keywords: y

.. index:: y

.. _a_double_binary.y:

y
*
This object has c++ prototype

| |tab| ``const double&`` *y*

.. meta::
   :keywords: x

.. index:: x

.. _a_double_binary.x:

x
*
This object has c++ prototype

| |tab| ``const double&`` *x*

.. meta::
   :keywords: az

.. index:: az

.. _a_double_binary.az:

az
**
The result has c++ prototype

| |tab| ``a_double`` *az*

.. meta::
   :keywords: example

.. index:: example

.. _a_double_binary.example:

Example
*******

-  :ref:`a_double_binary_xam_py`
-  :ref:`a_double_binary_xam_cpp`

----

xsrst input file: ``lib/cplusplus/a_double.cpp``
