.. _cpp_check_for_nan-name:

!!!!!!!!!!!!!!!!!
cpp_check_for_nan
!!!!!!!!!!!!!!!!!

.. raw:: html

   <a href="_sources/cpp_check_for_nan.rst.txt">View page source</a>

.. meta::
   :keywords: cpp_check_for_nan, check, for, nan, in, function, or, derivative, results

.. index:: cpp_check_for_nan, check, for, nan, in, function, or, derivative, results

.. _cpp_check_for_nan-title:

Check For Nan In Function or Derivative Results
###############################################

.. meta::
   :keywords: syntax

.. index:: syntax

.. _cpp_check_for_nan@Syntax:

Syntax
******

| *f*\ ``.check_for_nan``\ ( *b* )

.. meta::
   :keywords: f

.. index:: f

.. _cpp_check_for_nan@f:

f
*
is a
:ref:`d_fun<cpp_fun_ctor@Syntax@d_fun>` function object.

.. meta::
   :keywords: b

.. index:: b

.. _cpp_check_for_nan@b:

b
*
This argument has prototype

| |tab| ``int`` *b*

If *b* is true and
:ref:`get_cppad_sh@Settings@build_type` is ``debug`` ,
*f* will generate an assert when ``nan`` occurs in its function
or derivative values.
Otherwise, it will just pass back the ``nan`` values.

.. meta::
   :keywords: example

.. index:: example

.. _cpp_check_for_nan@Example:

Example
*******

-  :ref:`fun_check_for_nam_xam-title`

.. toctree::
   :maxdepth: 1
   :hidden:

   fun_check_for_nam_xam
