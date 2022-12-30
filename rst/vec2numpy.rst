.. _vec2numpy-name:

!!!!!!!!!
vec2numpy
!!!!!!!!!

.. raw:: html

   <a href="_sources/vec2numpy.rst.txt">View page source</a>

.. meta::
   :keywords: vec2numpy, convert, cppad_py, vector, to, numpy, array

.. index:: vec2numpy, convert, cppad_py, vector, to, numpy, array

.. _vec2numpy-title:

Convert a cppad_py Vector to a Numpy Array
##########################################

.. meta::
   :keywords: syntax

.. index:: syntax

.. _vec2numpy@Syntax:

Syntax
******

| *array* =  ``cppad_py.utility.vec2numpy`` ( *vec* , *nr* )
| *array* =  ``cppad_py.utility.vec2numpy`` ( *vec* , *nr* , *nc* )

.. meta::
   :keywords: vec

.. index:: vec

.. _vec2numpy@vec:

vec
***
This must have one of the following types:
``cppad_py.vec_int`` ,
``cppad_py.vec_double`` ,
``vec_py.vec_a_double`` .
with size equal to *nr* ``*`` *nc* .

.. meta::
   :keywords: nr

.. index:: nr

.. _vec2numpy@nr:

nr
**
This is an ``int`` equal to the number of rows in the array.
If the argument *nc* is not present, the array is a vector; i.e.,
``len`` ( *array*\ ``.shape ) == 1`` .

.. meta::
   :keywords: nc

.. index:: nc

.. _vec2numpy@nc:

nc
**
If this argument is present,
it is an ``int`` equal to the number of columns in the array.
In this case the array is a matrix; i.e.,
``len`` ( *array*\ ``.shape ) == 2`` .

.. meta::
   :keywords: array

.. index:: array

.. _vec2numpy@array:

array
*****
This is the array corresponding to *vec* in row major order.
Note that this array can be used after the vector *vec* drops
out of scope (is deleted).
