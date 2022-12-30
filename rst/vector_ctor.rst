.. _vector_ctor-name:

!!!!!!!!!!!
vector_ctor
!!!!!!!!!!!

.. raw:: html

   <a href="_sources/vector_ctor.rst.txt">View page source</a>

.. meta::
   :keywords: vector_ctor, cppad, py, vector, constructors

.. index:: vector_ctor, cppad, py, vector, constructors

.. _vector_ctor-title:

Cppad Py Vector Constructors
############################

.. meta::
   :keywords: syntax

.. index:: syntax

.. _vector_ctor@Syntax:

Syntax
******

.. meta::
   :keywords: c++

.. index:: c++

.. _vector_ctor@Syntax@C++:

C++
===
| ``cppad_py::vec_bool``     *bv* ( *n* )
| ``cppad_py::vec_int``      *iv* ( *n* )
| ``cppad_py::vec_double``   *dv* ( *n* )
| ``cppad_py::vec_a_double`` *av* ( *n* )

.. meta::
   :keywords: python

.. index:: python

.. _vector_ctor@Syntax@Python:

Python
======
| *bv* =  ``cppad_py.vec_bool`` ( *n* )
| *iv* =  ``cppad_py.vec_int`` ( *n* )
| *dv* =  ``cppad_py.vec_double`` ( *n* )
| *av* =  ``cppad_py.vec_a_double`` ( *n* )

.. meta::
   :keywords: purpose

.. index:: purpose

.. _vector_ctor@Purpose:

Purpose
*******
Creates a vector with *n* elements.

.. meta::
   :keywords: n

.. index:: n

.. _vector_ctor@n:

n
*
The argument *n* is a non-negative integer with default value zero;
i.e., if it is not present, zero is used.
(It has c++ prototype ``size_t`` *n* .)

.. meta::
   :keywords: vec_bool

.. index:: vec_bool

.. _vector_ctor@vec_bool:

vec_bool
********
This result *bv* is a vector with elements of type ``bool``

.. meta::
   :keywords: vec_int

.. index:: vec_int

.. _vector_ctor@vec_int:

vec_int
*******
This result *bv* is a vector with elements of type ``int``

.. meta::
   :keywords: vec_double

.. index:: vec_double

.. _vector_ctor@vec_double:

vec_double
**********
This result *bv* is a vector with elements of type ``double``

.. meta::
   :keywords: vec_a_double

.. index:: vec_a_double

.. _vector_ctor@vec_a_double:

vec_a_double
************
This result ``av`` is a vector with elements of type
:ref:`a_double-name`.

.. meta::
   :keywords: example

.. index:: example

.. _vector_ctor@Example:

Example
*******
All of the other vector examples use the vector constructors.
