.. _vector_set_get-name:

!!!!!!!!!!!!!!
vector_set_get
!!!!!!!!!!!!!!

.. raw:: html

   <a href="_sources/vector_set_get.rst.txt">View page source</a>

.. meta::
   :keywords: vector_set_get, setting, getting, vector, elements

.. index:: vector_set_get, setting, getting, vector, elements

.. _vector_set_get-title:

Setting and Getting Vector Elements
###################################

.. meta::
   :keywords: syntax

.. index:: syntax

.. _vector_set_get@Syntax:

Syntax
******

| *u* [ *i* ] = *x*
| *y* = *v* [ *i* ]

.. meta::
   :keywords: element_type

.. index:: element_type

.. _vector_set_get@element_type:

element_type
************
We use *element_type* to denote the type of elements in the
vector. It must be one of the following types:
``bool`` , ``int`` , ``double`` , ``a_double`` .

.. meta::
   :keywords: i

.. index:: i

.. _vector_set_get@i:

i
*
This argument has c++ prototype

| |tab| ``size_t`` *i*

It must be between zero and the size of the vector minus one.

.. meta::
   :keywords: u

.. index:: u

.. _vector_set_get@u:

u
*
The object *u* has c++ prototype

| |tab| ``vec_``\ *element_type*\ ``&`` *u*

.. meta::
   :keywords: x

.. index:: x

.. _vector_set_get@x:

x
*
The argument *x* has c++ prototype

| |tab| ``const`` *element_type*\ ``&`` *x*

.. meta::
   :keywords: v

.. index:: v

.. _vector_set_get@v:

v
*
The object *v* has c++ prototype

| |tab| ``const vec_``\ *element_type*\ ``&`` *v*

.. meta::
   :keywords: y

.. index:: y

.. _vector_set_get@y:

y
*
The result *y* has c++ prototype

| |tab| *element_type* *y*

.. meta::
   :keywords: example

.. index:: example

.. _vector_set_get@Example:

Example
*******
:ref:`c++<vector_set_get_xam_cpp-name>`,
:ref:`python<vector_set_get_xam_py-name>`.

.. toctree::
   :maxdepth: 1
   :hidden:

   vector_set_get_xam_cpp
   vector_set_get_xam_py
