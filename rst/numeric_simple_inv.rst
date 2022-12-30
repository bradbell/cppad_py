.. _numeric_simple_inv-name:

!!!!!!!!!!!!!!!!!!
numeric_simple_inv
!!!!!!!!!!!!!!!!!!

.. raw:: html

   <a href="_sources/numeric_simple_inv.rst.txt">View page source</a>

.. meta::
   :keywords: numeric_simple_inv, an, ad, compatible, matrix, inverse, routine

.. index:: numeric_simple_inv, an, ad, compatible, matrix, inverse, routine

.. _numeric_simple_inv-title:

An AD Compatible Matrix Inverse Routine
#######################################

.. meta::
   :keywords: syntax

.. index:: syntax

.. _numeric_simple_inv@Syntax:

Syntax
******
*Ainv* =  ``simple_inv`` ( *A* )

.. meta::
   :keywords: purpose

.. index:: purpose

.. _numeric_simple_inv@Purpose:

Purpose
*******
This routine can be used with ``ad_double``

.. _numeric_simple_inv@A:

A
*
This must be an invertible square matrix (no singular detection is done).
The type of its elements can be ``float`` or ``a_double`` .

.. meta::
   :keywords: ainv

.. index:: ainv

.. _numeric_simple_inv@Ainv:

Ainv
****
This is the matrix inverse of *A* .

.. meta::
   :keywords: example

.. index:: example

.. _numeric_simple_inv@Example:

Example
*******
:ref:`numeric_simple_inv_xam_py-name`

.. meta::
   :keywords: source, code

.. index:: source, code

.. _numeric_simple_inv@Source Code:

Source Code
***********
When viewing the source code below it is important to know that
optimizes out multiplication by the constant one while recording a function.
It also optimizes out both addition and multiplication by the constant zero.

.. literalinclude:: ../../example/python/numeric/simple_inv.py
   :lines: 6-69
   :language: py

.. toctree::
   :maxdepth: 1
   :hidden:

   numeric_simple_inv_xam_py
