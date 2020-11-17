!!!!!!!!!!!!!!!!
mixed2sparse_rcv
!!!!!!!!!!!!!!!!

.. include:: ../preamble.rst

.. meta::
   :keywords: mixed2sparse_rcv, convert, sparse, matrix, from, cppad_mixed, to, cppad_py

.. index:: mixed2sparse_rcv, convert, sparse, matrix, from, cppad_mixed, to, cppad_py

.. _mixed2sparse_rcv:

Convert Sparse Matrix from cppad_mixed to cppad_py
##################################################
.. contents::
   :local:

.. meta::
   :keywords: syntax

.. index:: syntax

.. _mixed2sparse_rcv.syntax:

Syntax
******

| *sparse_out* = ``cppad_py::mixed2sparse_rcv`` ( *sparse_in* )

.. meta::
   :keywords: prototype

.. index:: prototype

.. _mixed2sparse_rcv.prototype:

Prototype
*********

.. literalinclude:: ../../lib/cplusplus/cpp_convert.cpp
    :lines: 208-209
    :language: cpp

.. meta::
   :keywords: restriction

.. index:: restriction

.. _mixed2sparse_rcv.restriction:

Restriction
***********
This routine is only available when
:ref:`include_mixed <get_cppad_sh.settings.include_mixed>` is true.

----

xsrst input file: ``lib/cplusplus/cpp_convert.cpp``
