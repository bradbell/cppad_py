.. _mixed2sparse_rcv-name:

!!!!!!!!!!!!!!!!
mixed2sparse_rcv
!!!!!!!!!!!!!!!!

.. raw:: html

   <a href="_sources/mixed2sparse_rcv.rst.txt">View page source</a>

.. meta::
   :keywords: mixed2sparse_rcv, convert, sparse, matrix, from, cppad_mixed, to, cppad_py

.. index:: mixed2sparse_rcv, convert, sparse, matrix, from, cppad_mixed, to, cppad_py

.. _mixed2sparse_rcv-title:

Convert Sparse Matrix from cppad_mixed to cppad_py
##################################################

.. meta::
   :keywords: syntax

.. index:: syntax

.. _mixed2sparse_rcv@Syntax:

Syntax
******

| *sparse_out* = ``cppad_py::mixed2sparse_rcv`` ( *sparse_in* )

.. meta::
   :keywords: prototype

.. index:: prototype

.. _mixed2sparse_rcv@Prototype:

Prototype
*********

.. literalinclude:: ../lib/cplusplus/cpp_convert.cpp
   :lines: 195-196
   :language: cpp

.. meta::
   :keywords: restriction

.. index:: restriction

.. _mixed2sparse_rcv@Restriction:

Restriction
***********
This routine is only available when
:ref:`include_mixed <get_cppad_sh@Settings@include_mixed>` is true.
