.. _cpp_fun_new_dynamic-name:

!!!!!!!!!!!!!!!!!!!
cpp_fun_new_dynamic
!!!!!!!!!!!!!!!!!!!

.. raw:: html

   <a href="_sources/cpp_fun_new_dynamic.rst.txt">View page source</a>

.. meta::
   :keywords: cpp_fun_new_dynamic, change, the, dynamic, parameters

.. index:: cpp_fun_new_dynamic, change, the, dynamic, parameters

.. _cpp_fun_new_dynamic-title:

Change The Dynamic Parameters
#############################

.. meta::
   :keywords: syntax

.. index:: syntax

.. _cpp_fun_new_dynamic@Syntax:

Syntax
******

| *f*\ ``.new_dynamic`` ( *dynamic* )

.. meta::
   :keywords: f

.. index:: f

.. _cpp_fun_new_dynamic@f:

f
*
This is either a
:ref:`d_fun<cpp_fun_ctor@Syntax@d_fun>` or
:ref:`a_fun<cpp_fun_ctor@Syntax@a_fun>` function object.

.. meta::
   :keywords: dynamic

.. index:: dynamic

.. _cpp_fun_new_dynamic@dynamic:

dynamic
*******
If *f* is a ``d_fun`` or ``a_fun`` ,
this argument has prototype

| |tab| ``const vec_double&`` *dynamic*
| |tab| ``const vec_a_double&`` *dynamic*

and its size must be the same as the size of
:ref:`dynamic<cpp_independent@dynamic>` in the corresponding call to
``independent`` .
It specifies new values for the dynamic parameters in *f* .

.. meta::
   :keywords: size_order

.. index:: size_order

.. _cpp_fun_new_dynamic@size_order:

size_order
**********
After this call
:ref:`f_size_order()<cpp_fun_property@size_order>` is zero.

.. meta::
   :keywords: example

.. index:: example

.. _cpp_fun_new_dynamic@Example:

Example
*******
See :ref:`fun_dynamic_xam_cpp-name`.
