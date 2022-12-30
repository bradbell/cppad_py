.. _py_fun_check_for_nan-name:

!!!!!!!!!!!!!!!!!!!!
py_fun_check_for_nan
!!!!!!!!!!!!!!!!!!!!

.. raw:: html

   <a href="_sources/py_fun_check_for_nan.rst.txt">View page source</a>

.. meta::
   :keywords: py_fun_check_for_nan, check, for, nan, in, function, object

.. index:: py_fun_check_for_nan, check, for, nan, in, function, object

.. _py_fun_check_for_nan-title:

Check for Nan in a Function Object
##################################

.. meta::
   :keywords: syntax

.. index:: syntax

.. _py_fun_check_for_nan@Syntax:

Syntax
******

| *f*\ ``.check_for_nan`` ( *b* )

.. meta::
   :keywords: f

.. index:: f

.. _py_fun_check_for_nan@f:

f
*
This is a
:ref:`d_fun<py_fun_ctor@Syntax@d_fun>` or
:ref:`a_fun<py_fun_ctor@Syntax@a_fun>` function object.

.. meta::
   :keywords: b

.. index:: b

.. _py_fun_check_for_nan@b:

b
*
The argument *b* is a ``bool`` .
If *b* is true and
:ref:`get_cppad_sh@Settings@build_type` is ``debug`` ,
*f* will generate an assert when ``nan`` occurs
in its function or derivative values.
Otherwise, it will just pass back the ``nan`` values.

.. meta::
   :keywords: example

.. index:: example

.. _py_fun_check_for_nan@Example:

Example
*******

-  :ref:`check_for_nan_xam_py-title`

.. toctree::
   :maxdepth: 1
   :hidden:

   check_for_nan_xam_py
