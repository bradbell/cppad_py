.. _vector_size-name:

!!!!!!!!!!!
vector_size
!!!!!!!!!!!

.. raw:: html

   <a href="_sources/vector_size.rst.txt">View page source</a>

.. meta::
   :keywords: vector_size, size, vector

.. index:: vector_size, size, vector

.. _vector_size-title:

Size of a Vector
################

.. meta::
   :keywords: syntax

.. index:: syntax

.. _vector_size@Syntax:

Syntax
******
*n* = *v*\ ``.size`` ()

.. meta::
   :keywords: v

.. index:: v

.. _vector_size@v:

v
*
The object *v* has one of the following prototypes:

| |tab| ``const vec_bool&`` *v*
| |tab| ``const vec_int&`` *v*
| |tab| ``const vec_double&`` *v*
| |tab| ``const vec_a_double&`` *v*

.. meta::
   :keywords: n

.. index:: n

.. _vector_size@n:

n
*
The result has c++ prototype

| |tab| ``size_t`` *n*

i.e., it is a positive integer.
Its value is the number of elements in the vector *v* .

.. meta::
   :keywords: example

.. index:: example

.. _vector_size@Example:

Example
*******
:ref:`c++<vector_size_xam_cpp-name>`,
:ref:`python<vector_size_xam_py-name>`.

.. toctree::
   :maxdepth: 1
   :hidden:

   vector_size_xam_cpp
   vector_size_xam_py
