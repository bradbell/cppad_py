.. _numeric_rosen3_step-name:

!!!!!!!!!!!!!!!!!!!
numeric_rosen3_step
!!!!!!!!!!!!!!!!!!!

.. raw:: html

   <a href="_sources/numeric_rosen3_step.rst.txt">View page source</a>

.. meta::
   :keywords: numeric_rosen3_step, one, third, order, rosenbrock, ode, step

.. index:: numeric_rosen3_step, one, third, order, rosenbrock, ode, step

.. _numeric_rosen3_step-title:

One Third Order Rosenbrock ODE Step
###################################

.. meta::
   :keywords: syntax

.. index:: syntax

.. _numeric_rosen3_step@Syntax:

Syntax
******

| *yf* =  ``rosen3_step`` ( *fun* , *ti* , *yi* , *h* )
| *ok* =  ``check_rosen3_step`` ( *fun* , *ti* , *yi* , *h* )

.. meta::
   :keywords: purpose

.. index:: purpose

.. _numeric_rosen3_step@Purpose:

Purpose
*******
The routine ``rosen3_step`` can be used with
``ad_double`` to solve an initial value ODE

.. math::

   y^{(1)} (t)  = f( t , y )

.. meta::
   :keywords: reference

.. index:: reference

.. _numeric_rosen3_step@Reference:

Reference
*********
The formulas in this method are taken from page 100 of the following
reference (except that 98/108 was correct to 97/108):
Shampine, L.F.,
*Implementation of Rosenbrock Methods* ,
ACM Transactions on Mathematical Software, Vol. 8, No. 2, June 1982.

.. meta::
   :keywords: fun

.. index:: fun

.. _numeric_rosen3_step@fun:

fun
***
This is a function that evaluates the ordinary differential equation,
and its partial derivatives,

.. meta::
   :keywords: t

.. index:: t

.. _numeric_rosen3_step@fun@t:

t
=
The argument *t* below is the current time.
It can be a ``float`` or ``a_double`` .

.. meta::
   :keywords: y

.. index:: y

.. _numeric_rosen3_step@fun@y:

y
=
The argument *y* below is the current value of :math:`y(t)`.
The type of the elements of *y*
can be ``float`` or ``ad_double`` .

.. meta::
   :keywords: f

.. index:: f

.. _numeric_rosen3_step@fun@f:

f
=
The syntax

| |tab| *yp* = *fun*\ ``.f`` ( *t* , *y* )

sets *yp* to the value of :math:`f(t, y)`.

.. meta::
   :keywords: f_t

.. index:: f_t

.. _numeric_rosen3_step@fun@f_t:

f_t
===
The syntax

| |tab| *yp_t* = *fun*\ ``.f_t`` ( *t* , *y* )

set *yp_t* to the value of :math:`\partial_t f(t, y)`.

.. meta::
   :keywords: f_y

.. index:: f_y

.. _numeric_rosen3_step@fun@f_y:

f_y
===
The syntax

| |tab| *yp_y* = *fun*\ ``.f_y`` ( *t* , *y* )

sets *yp_y* to the value of :math:`\partial_y f(t, y)`.

.. meta::
   :keywords: ti

.. index:: ti

.. _numeric_rosen3_step@ti:

ti
**
This is the initial time for the Rosenbrock step.
It can have type ``float`` or ``a_double`` .
(For ``check_rosen3_step`` only ``float`` is allowed.)

.. meta::
   :keywords: yi

.. index:: yi

.. _numeric_rosen3_step@yi:

yi
**
This is the numpy vector containing the
value of :math:`y(t)` at the initial time.
The type of its elements can be ``float`` or ``a_double`` .
(For ``check_rosen3_step`` only ``float`` is allowed.)

.. meta::
   :keywords: h

.. index:: h

.. _numeric_rosen3_step@h:

h
*
This is the step size in time; i.e., the time at the end of the step
minus the initial time.
It can have type ``float`` or ``a_double`` .
(This is not used by ``check_rosen3_step`` .)

.. meta::
   :keywords: yf

.. index:: yf

.. _numeric_rosen3_step@yf:

yf
**
This is the approximate solution for :math:`y(t)` at the final time
as a numpy vector.
This solution is 3-th order accurate in time :math:`t`; e.g., if
:math:`y(t)` is a polynomial in :math:`t` of order three or lower,
the solution has no truncation error, only round off error.

.. meta::
   :keywords: ok

.. index:: ok

.. _numeric_rosen3_step@ok:

ok
**
This is true if the function *fun*\ ``.f`` *t* , *y* )
and the partials *fun*\ ``.f_t`` ( *t* , *y* ) ,
*fun*\ ``.f_y`` ( *t* , *y* ) agree.
Otherwise AD has detected an error in these functions.

.. meta::
   :keywords: example

.. index:: example

.. _numeric_rosen3_step@Example:

Example
*******
:ref:`numeric_rosen3_step_xam_py-name`

.. meta::
   :keywords: source, code

.. index:: source, code

.. _numeric_rosen3_step@Source Code:

Source Code
***********

.. meta::
   :keywords: rosen3_step

.. index:: rosen3_step

.. _numeric_rosen3_step@Source Code@rosen3_step:

rosen3_step
===========

.. literalinclude:: ../../example/python/numeric/rosen3_step.py
   :lines: 6-53
   :language: py

.. meta::
   :keywords: check_rosen3_step

.. index:: check_rosen3_step

.. _numeric_rosen3_step@Source Code@check_rosen3_step:

check_rosen3_step
=================

.. literalinclude:: ../../example/python/numeric/rosen3_step.py
   :lines: 56-102
   :language: py

.. toctree::
   :maxdepth: 1
   :hidden:

   numeric_rosen3_step_xam_py
