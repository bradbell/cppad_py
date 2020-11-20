!!!!!!!!!!!!!!!!!!!!
py_fun_check_for_nan
!!!!!!!!!!!!!!!!!!!!

.. toctree::
   :maxdepth: 1
   :hidden:

   check_for_nan_xam_py

.. include:: ../preamble.rst

.. meta::
   :keywords: py_fun_check_for_nan, check, for, nan, in, function, object

.. index:: py_fun_check_for_nan, check, for, nan, in, function, object

.. _py_fun_check_for_nan:

Check for Nan in a Function Object
##################################
.. contents::
   :local:

.. meta::
   :keywords: syntax

.. index:: syntax

.. _py_fun_check_for_nan.syntax:

Syntax
******

| *f*\ ``.check_for_nan`` ( *b* )

.. meta::
   :keywords: f

.. index:: f

.. _py_fun_check_for_nan.f:

f
*
This is a
:ref:`d_fun<py_fun_ctor.syntax.d_fun>` or
:ref:`a_fun<py_fun_ctor.syntax.a_fun>` function object.

.. meta::
   :keywords: b

.. index:: b

.. _py_fun_check_for_nan.b:

b
*
The argument *b* is a ``bool`` .
If *b* is true and
:ref:`get_cppad_sh.settings.build_type` is ``debug`` ,
*f* will generate an assert when ``nan`` occurs
in its function or derivative values.
Otherwise, it will just pass back the ``nan`` values.

.. meta::
   :keywords: example

.. index:: example

.. _py_fun_check_for_nan.example:

Example
*******

-  :ref:`check_for_nan_xam_py`

----

xsrst input file: ``lib/python/cppad_py/fun_check_for_nan.xsrst``
