.. _numeric_runge4_step-name:

!!!!!!!!!!!!!!!!!!!
numeric_runge4_step
!!!!!!!!!!!!!!!!!!!

.. raw:: html

   <a href="_sources/numeric_runge4_step.rst.txt">View page source</a>

.. meta::
   :keywords: numeric_runge4_step, one, fourth, order, runge-kutta, ode, step

.. index:: numeric_runge4_step, one, fourth, order, runge-kutta, ode, step

.. _numeric_runge4_step-title:

One Fourth Order Runge-Kutta ODE Step
#####################################

.. meta::
   :keywords: syntax

.. index:: syntax

.. _numeric_runge4_step@Syntax:

Syntax
******
*yf* =  ``runge4_step`` ( *fun* , *ti* , *yi* , *h* )

.. meta::
   :keywords: purpose

.. index:: purpose

.. _numeric_runge4_step@Purpose:

Purpose
*******
The routine can be used with ``ad_double``
to solve the initial value ODE

.. math::

   y^{(1)} (t)  = f( t , y )

.. meta::
   :keywords: fun

.. index:: fun

.. _numeric_runge4_step@fun:

fun
***
This is a function that evaluates the ordinary differential equation
using the syntax

| |tab| *yp* = *fun*\ ``.f`` ( *t* , *y* )

where *t* is the current time,
*y* is the current value of :math:`y(t)`, and
*yp* is the current derivative :math:`y^{(1)} (t)`.
The type of the elements of *t* and *y*
can be ``float`` or ``ad_double`` .

.. meta::
   :keywords: ti

.. index:: ti

.. _numeric_runge4_step@ti:

ti
**
This is the initial time for the Runge-Kutta step.
It can have type ``float`` or ``a_double`` .

.. meta::
   :keywords: yi

.. index:: yi

.. _numeric_runge4_step@yi:

yi
**
This is the numpy vector containing the
value of :math:`y(t)` at the initial time.
The type of its elements can be ``float`` or ``a_double`` .

.. meta::
   :keywords: h

.. index:: h

.. _numeric_runge4_step@h:

h
*
This is the step size in time; i.e., the time at the end of the step
minus the initial time.
It can have type ``float`` or ``a_double`` .

.. meta::
   :keywords: yf

.. index:: yf

.. _numeric_runge4_step@yf:

yf
**
This is the approximate solution for :math:`y(t)` at the final time
as a numpy vector.
This solution is 4-th order accurate in time :math:`t`; e.g., if
:math:`y(t)` is a polynomial in :math:`t` of order four or lower,
the solution has no truncation error, only round off error.

.. meta::
   :keywords: example

.. index:: example

.. _numeric_runge4_step@Example:

Example
*******
:ref:`numeric_runge4_step_xam_py-name`

.. meta::
   :keywords: source, code

.. index:: source, code

.. _numeric_runge4_step@Source Code:

Source Code
***********

.. literalinclude:: ../../example/python/numeric/runge4_step.py
   :lines: 6-12
   :language: py

.. toctree::
   :maxdepth: 1
   :hidden:

   numeric_runge4_step_xam_py
