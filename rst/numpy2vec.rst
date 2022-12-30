.. _numpy2vec-name:

!!!!!!!!!
numpy2vec
!!!!!!!!!

.. raw:: html

   <a href="_sources/numpy2vec.rst.txt">View page source</a>

.. meta::
   :keywords: numpy2vec, convert, numpy, array, to, cppad_py, vector

.. index:: numpy2vec, convert, numpy, array, to, cppad_py, vector

.. _numpy2vec-title:

Convert a Numpy Array to a cppad_py Vector
##########################################

.. meta::
   :keywords: syntax

.. index:: syntax

.. _numpy2vec@Syntax:

Syntax
******

| *vec* =  ``cppad_py.utility.numpy2vec`` (
| |tab| *array* , *dtype* , *shape* , *context* , *name*
| )

.. meta::
   :keywords: array

.. index:: array

.. _numpy2vec@array:

array
*****
This is either a vector (only one index) or a matrix
(has two indices) that we are converting to a vector.
If this array does not match the conditions below,
an exception is raised with an appropriate error message.

.. meta::
   :keywords: dtype

.. index:: dtype

.. _numpy2vec@dtype:

dtype
*****
This is the expected data type for the elements of the array.
It must be one of the following:
``bool`` , ``int`` , ``float`` or ``cppad_py.a_double`` .

.. meta::
   :keywords: shape

.. index:: shape

.. _numpy2vec@shape:

shape
*****
This either a ``int`` or a tuple of ``int`` with length one or two.
If it is an ``int`` , *array* is expected to be a vector.
If it is a tuple with length one, *array* is expected to be a vector.
Otherwise a matrix is expected.

.. meta::
   :keywords: context

.. index:: context

.. _numpy2vec@context:

context
*******
This is the context that *array* appears in
(often to syntax for some other operation).
It is a ``str`` that is used for error reporting.

.. meta::
   :keywords: name

.. index:: name

.. _numpy2vec@name:

name
****
This is the name used for *array* in *context* .
It is a ``str`` that is used for error reporting.

.. meta::
   :keywords: vec

.. index:: vec

.. _numpy2vec@vec:

vec
***
This is the values of *array*
as a vector is row major order.
It has type ``vec_double`` if *dtype* is ``float`` ,
and ``vec_a_double`` if *dtype* is ``a_double`` .
