.. _a_double_binary-name:

!!!!!!!!!!!!!!!
a_double_binary
!!!!!!!!!!!!!!!

.. raw:: html

   <a href="_sources/a_double_binary.rst.txt">View page source</a>

.. meta::
   :keywords: a_double_binary, a_double, binary, operators, with, an, ad, result

.. index:: a_double_binary, a_double, binary, operators, with, an, ad, result

.. _a_double_binary-title:

a_double Binary Operators with an AD Result
###########################################

.. meta::
   :keywords: syntax

.. index:: syntax

.. _a_double_binary@Syntax:

Syntax
******

.. meta::
   :keywords: python

.. index:: python

.. _a_double_binary@Syntax@Python:

Python
======
| *az* = *ax* *op* *ay*
| *az* = *ax* *op* *y*
| *az* = *x* *op* *ay*

.. meta::
   :keywords: c++

.. index:: c++

.. _a_double_binary@Syntax@C++:

C++
===
| *az* = *ax* *op* *ay*
| *az* = *ax* *op* *y*
| *az* = *fun* ( *x* , *ax* )

.. meta::
   :keywords: op

.. index:: op

.. _a_double_binary@op:

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
| *az* = *pow_int* ( *ax* , *i* )

.. meta::
   :keywords: fun

.. index:: fun

.. _a_double_binary@fun:

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

.. _a_double_binary@ax:

ax
**
This object has c++ prototype

| |tab| ``const a_double&`` *ax*

.. meta::
   :keywords: ay

.. index:: ay

.. _a_double_binary@ay:

ay
**
This object has c++ prototype

| |tab| ``const a_double&`` *ay*

.. meta::
   :keywords: y

.. index:: y

.. _a_double_binary@y:

y
*
This object has c++ prototype

| |tab| ``const double&`` *y*

.. meta::
   :keywords: x

.. index:: x

.. _a_double_binary@x:

x
*
This object has c++ prototype

| |tab| ``const double&`` *x*

.. meta::
   :keywords: az

.. index:: az

.. _a_double_binary@az:

az
**
The result has c++ prototype

| |tab| ``a_double`` *az*

.. meta::
   :keywords: pow_int

.. index:: pow_int

.. _a_double_binary@pow_int:

pow_int
*******
Exponentiation by an integer is an even more special case.
Derivatives of the ``pow`` function will return ``nan``
when the argument value is zero; e.g. the derivative of
:math:`\R{pow} (x, 2)` at :math:`x = 0`
( derivatives of the ``pow`` function work fine when :math:`x \ne 0` ).
This is because the derivative of the log function at zero
results in a division by zero.
This ``nan`` can be avoided by using multiplication, instead of logs,
to compute powers when the exponent is an integer.

.. meta::
   :keywords: i

.. index:: i

.. _a_double_binary@pow_int@i:

i
=
The argument to the ``pow_int`` function has c++ prototype

| |tab| ``const int&`` *i*

.. meta::
   :keywords: example

.. index:: example

.. _a_double_binary@Example:

Example
*******

-  :ref:`a_double_binary_xam_py-title`
-  :ref:`a_double_binary_xam_cpp-title`

.. toctree::
   :maxdepth: 1
   :hidden:

   a_double_binary_xam_py
   a_double_binary_xam_cpp
