.. _py_fun_new_dynamic-name:

!!!!!!!!!!!!!!!!!!
py_fun_new_dynamic
!!!!!!!!!!!!!!!!!!

.. raw:: html

   <a href="_sources/py_fun_new_dynamic.rst.txt">View page source</a>

.. meta::
   :keywords: py_fun_new_dynamic, new, dynamic, parameters

.. index:: py_fun_new_dynamic, new, dynamic, parameters

.. _py_fun_new_dynamic-title:

New Dynamic Parameters
######################

.. meta::
   :keywords: syntax

.. index:: syntax

.. _py_fun_new_dynamic@Syntax:

Syntax
******
*f*\ ``.new_dynamic`` ( *dynamic* )

.. meta::
   :keywords: f

.. index:: f

.. _py_fun_new_dynamic@f:

f
*
This is either a
:ref:`d_fun<py_fun_ctor@Syntax@d_fun>` or
:ref:`a_fun<py_fun_ctor@Syntax@a_fun>`.
The independent :ref:`dynamic<py_independent@dynamic>` parameters
are changed to have the specified values.
The other dynamic parameters are then computed.

.. meta::
   :keywords: dynamic

.. index:: dynamic

.. _py_fun_new_dynamic@dynamic:

dynamic
*******
If *f* is a ``d_fun`` ( ``a_fun`` ) object,
*dynamic* is a numpy vector with ``float`` ( ``a_double`` )
elements and its size must be the same as the size of
:ref:`dynamic<py_independent@dynamic>` in the corresponding call to
``independent`` .
It specifies new values for the dynamic parameters in *f* .

.. meta::
   :keywords: size_order

.. index:: size_order

.. _py_fun_new_dynamic@dynamic@size_order:

size_order
==========
After this call,
:ref:`f_size_order()<py_fun_property@size_order>` is zero.

.. meta::
   :keywords: example

.. index:: example

.. _py_fun_new_dynamic@Example:

Example
*******
See :ref:`fun_dynamic_xam_py-name`
