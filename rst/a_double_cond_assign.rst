.. _a_double_cond_assign-name:

!!!!!!!!!!!!!!!!!!!!
a_double_cond_assign
!!!!!!!!!!!!!!!!!!!!

.. raw:: html

   <a href="_sources/a_double_cond_assign.rst.txt">View page source</a>

.. meta::
   :keywords: a_double_cond_assign, ad, conditional, assignment

.. index:: a_double_cond_assign, ad, conditional, assignment

.. _a_double_cond_assign-title:

AD Conditional Assignment
#########################

.. meta::
   :keywords: syntax

.. index:: syntax

.. _a_double_cond_assign@Syntax:

Syntax
******
| *target*\ ``.cond_assign`` ( *cop* , *left* , *right* , *if_true* , *if_false* )

.. meta::
   :keywords: purpose

.. index:: purpose

.. _a_double_cond_assign@Purpose:

Purpose
*******
The code

| |tab| ``if`` ( *left* *cop* *right* )
| |tab| |tab| *target* = *if_true*
| |tab| ``else``
| |tab| |tab| *target* = *if_false*

records either the true or false case depending on the value
of *left* and *right* ; see :ref:`cpp_fun_ctor-name`.
If *left* or *right* is a
:ref:`variable<a_double_property@variable>`,
it may be desirable to switch between *if_true* and *if_false*
depending of the value of the independent variable during
calls to order zero :ref:`cpp_fun_forward-name`.
The ``cond_assign`` does this.

.. meta::
   :keywords: target

.. index:: target

.. _a_double_cond_assign@target:

target
******
This object has c++ prototype

| |tab| ``a_double&`` *target*

.. meta::
   :keywords: cop

.. index:: cop

.. _a_double_cond_assign@cop:

cop
***
This argument has c++ prototype

| |tab| ``const char *cop``

The comparison is

| |tab| *left* *cop* *right*

where *cop* is one of the following:

.. csv-table::
   :widths: 10, 10

   *cop* ,
   ``<`` , less than
   ``<=`` , less than or equal
   ``==`` , equal
   ``>=`` , greater than or equal
   ``>`` , greater than

.. meta::
   :keywords: left

.. index:: left

.. _a_double_cond_assign@left:

left
****
This argument has c++ prototype

| |tab| ``const a_double&`` *left*

It specifies the left operand in the comparison.

.. meta::
   :keywords: right

.. index:: right

.. _a_double_cond_assign@right:

right
*****
This argument has c++ prototype

| |tab| ``const a_double&`` *right*

It specifies the right operand in the comparison.

.. meta::
   :keywords: if_true

.. index:: if_true

.. _a_double_cond_assign@if_true:

if_true
*******
This argument has c++ prototype

| |tab| ``const a_double&`` *if_true*

It specifies the value assigned to *ad* if the result
of the comparison is true.

.. meta::
   :keywords: if_false

.. index:: if_false

.. _a_double_cond_assign@if_false:

if_false
********
This argument has c++ prototype

| |tab| ``const a_double&`` *if_false*

It specifies the value assigned to *ad* if the result
of the comparison is false.

.. meta::
   :keywords: example

.. index:: example

.. _a_double_cond_assign@Example:

Example
*******
:ref:`c++<a_double_cond_assign_xam_cpp-name>`,
:ref:`python<a_double_cond_assign_xam_py-name>`.

.. toctree::
   :maxdepth: 1
   :hidden:

   a_double_cond_assign_xam_cpp
   a_double_cond_assign_xam_py
