.. _cpp_fun_optimize-name:

!!!!!!!!!!!!!!!!
cpp_fun_optimize
!!!!!!!!!!!!!!!!

.. raw:: html

   <a href="_sources/cpp_fun_optimize.rst.txt">View page source</a>

.. meta::
   :keywords: cpp_fun_optimize, optimize, an, ad, function

.. index:: cpp_fun_optimize, optimize, an, ad, function

.. _cpp_fun_optimize-title:

Optimize an AD Function
#######################

.. meta::
   :keywords: syntax

.. index:: syntax

.. _cpp_fun_optimize@Syntax:

Syntax
******
*f*\ ``.optimize`` ()

.. meta::
   :keywords: purpose

.. index:: purpose

.. _cpp_fun_optimize@Purpose:

Purpose
*******
This reduces the number of operations
(hence to time and memory) used to compute the function
stored in *f*
On the other hand, the optimization may take a significant amount
of time and memory.

.. meta::
   :keywords: f

.. index:: f

.. _cpp_fun_optimize@f:

f
*
This object is a
:ref:`d_fun<cpp_fun_ctor@Syntax@d_fun>`.
Optimizing this *f* also optimizes the
corresponding :ref:`a_fun<cpp_fun_ctor@Syntax@a_fun>`.

.. meta::
   :keywords: example

.. index:: example

.. _cpp_fun_optimize@Example:

Example
*******
:ref:`fun_optimize_xam_cpp-name`

.. toctree::
   :maxdepth: 1
   :hidden:

   fun_optimize_xam_cpp
