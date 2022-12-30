.. _numeric_optimize_fun_class-name:

!!!!!!!!!!!!!!!!!!!!!!!!!!
numeric_optimize_fun_class
!!!!!!!!!!!!!!!!!!!!!!!!!!

.. raw:: html

   <a href="_sources/numeric_optimize_fun_class.rst.txt">View page source</a>

.. meta::
   :keywords: numeric_optimize_fun_class, helper, class, that, defines, functions, needed, for, optimization

.. index:: numeric_optimize_fun_class, helper, class, that, defines, functions, needed, for, optimization

.. _numeric_optimize_fun_class-title:

A Helper Class That Defines Functions Needed for Optimization
#############################################################

.. meta::
   :keywords: syntax

.. index:: syntax

.. _numeric_optimize_fun_class@Syntax:

Syntax
******
*optimize_fun* =  ``optimize_fun_class`` ( *objective_ad* , *constraint_ad* )

.. meta::
   :keywords: purpose

.. index:: purpose

.. _numeric_optimize_fun_class@Purpose:

Purpose
*******
This class is an aid solving optimization problems of the form

.. math::

   \begin{array}{rl}
   {\rm minimize}       & f(x) \; {\rm w.r.t} \; x \\
   {\rm subject \; to}  & a \leq g(x) \leq b \\
   \end{array}

where :math:`x` is a vector,
:math:`f(x)` is a scalar, and
:math:`a, g(x), b` are all vectors with the same length.
We use :math:`n`, :math:`m` for the length of the vectors
:math:`x` and :math:`g(x)` respectively.

.. meta::
   :keywords: objective_ad

.. index:: objective_ad

.. _numeric_optimize_fun_class@objective_ad:

objective_ad
************
This is a :ref:`d_fun<py_fun_ctor@Syntax@d_fun>`
representation of the function :math:`f(x)`.

.. meta::
   :keywords: constraint_ad

.. index:: constraint_ad

.. _numeric_optimize_fun_class@constraint_ad:

constraint_ad
*************
This is a ``d_fun`` representation of the function :math:`g(x)`.

.. meta::
   :keywords: optimize_fun

.. index:: optimize_fun

.. _numeric_optimize_fun_class@optimize_fun:

optimize_fun
************
This class object has the following functions defined:

.. meta::
   :keywords: objective_fun

.. index:: objective_fun

.. _numeric_optimize_fun_class@optimize_fun@objective_fun:

objective_fun
=============
The syntax

| |tab| *y* = *optimize_fun*\ ``.objective_fun`` ( *x* )

sets :math:`y = f(x)` where
*x* is a numpy vector with length *n*
and *y* is a scalar.

.. meta::
   :keywords: objective_grad

.. index:: objective_grad

.. _numeric_optimize_fun_class@optimize_fun@objective_grad:

objective_grad
==============
The syntax

| |tab| *z* = *optimize_fun*\ ``.objective_grad`` ( *x* )

sets :math:`z = f^{(1)} (x)` where
*x* and *z* are numpy vectors with length *n* .

.. meta::
   :keywords: objective_hess

.. index:: objective_hess

.. _numeric_optimize_fun_class@optimize_fun@objective_hess:

objective_hess
==============
The syntax

| |tab| *h* = *optimize_fun*\ ``.objective_hess`` ( *x* )

sets :math:`h = f^{(2)} (x)` where
*x* is a numpy vector with length *n*
and *h* is a numpy *n* by *n*  matrix.

.. meta::
   :keywords: constraint_fun

.. index:: constraint_fun

.. _numeric_optimize_fun_class@optimize_fun@constraint_fun:

constraint_fun
==============
The syntax

| |tab| *y* = *optimize_fun*\ ``.constraint_fun`` ( *x* )

sets :math:`y = g(x)` where
*x* ( *y* ) is a numpy vector with length
*n* ( *m* ).

.. meta::
   :keywords: constraint_jac

.. index:: constraint_jac

.. _numeric_optimize_fun_class@optimize_fun@constraint_jac:

constraint_jac
==============
The syntax

| |tab| *J* = *optimize_fun*\ ``.constraint_jac`` ( *x* )

sets :math:`J = g^{(1)} (x)` where
*x* is a numpy vector with length *n*
and *J* is a numpy *m* by *n*  matrix.

.. meta::
   :keywords: constraint_hess

.. index:: constraint_hess

.. _numeric_optimize_fun_class@optimize_fun@constraint_hess:

constraint_hess
===============
The syntax

| |tab| *H* = *optimize_fun*\ ``.constraint_hess`` ( *x* , *v* )

sets

.. math::

   H = \sum_{i=0}^{m-1} v_k g_i^{(2)} (x)

where *x* is a numpy vector with length *n*
and *H* is a numpy *n* by *n*  matrix.

.. meta::
   :keywords: example

.. index:: example

.. _numeric_optimize_fun_class@Example:

Example
*******
:ref:`numeric_optimize_fun_xam_py-name`

.. meta::
   :keywords: source, code

.. index:: source, code

.. _numeric_optimize_fun_class@Source Code:

Source Code
***********

.. literalinclude:: ../../example/python/numeric/optimize_fun_class.py
   :lines: 6-40
   :language: py

.. toctree::
   :maxdepth: 1
   :hidden:

   numeric_optimize_fun_xam_py
