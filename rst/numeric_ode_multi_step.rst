.. _numeric_ode_multi_step-name:

!!!!!!!!!!!!!!!!!!!!!!
numeric_ode_multi_step
!!!!!!!!!!!!!!!!!!!!!!

.. raw:: html

   <a href="_sources/numeric_ode_multi_step.rst.txt">View page source</a>

.. meta::
   :keywords: numeric_ode_multi_step, multiple, ode, steps

.. index:: numeric_ode_multi_step, multiple, ode, steps

.. _numeric_ode_multi_step-title:

Multiple Ode Steps
##################

.. meta::
   :keywords: syntax

.. index:: syntax

.. _numeric_ode_multi_step@Syntax:

Syntax
******
*y_all* =  ``ode_multi_step`` ( *one_step* , *f* , *t_all* , *y_init* )

.. meta::
   :keywords: purpose

.. index:: purpose

.. _numeric_ode_multi_step@Purpose:

Purpose
*******
The routine can be used with ``ad_double`` to solve an initial
value ODE

.. math::

   y^{(1)} (t) = f( t , y )

.. meta::
   :keywords: one_step

.. index:: one_step

.. _numeric_ode_multi_step@one_step:

one_step
********
This routine executes one step of an ODE approximation method with the
following syntax:

| |tab| *y1* = *one_step* ( *f* , *t0* , *y0* , *t_step* )

The elements of *y0* and the scalars above can be
``float`` or ``a_double`` .

.. meta::
   :keywords: t0

.. index:: t0

.. _numeric_ode_multi_step@one_step@t0:

t0
==
is the initial time value for the step.

.. meta::
   :keywords: y0

.. index:: y0

.. _numeric_ode_multi_step@one_step@y0:

y0
==
is the initial value of :math:`y(t)` for the step.

.. meta::
   :keywords: t_step

.. index:: t_step

.. _numeric_ode_multi_step@one_step@t_step:

t_step
======
is the is the size of the step (in time).

.. meta::
   :keywords: y1

.. index:: y1

.. _numeric_ode_multi_step@one_step@y1:

y1
==
is the approximation for the ODE solution at time *t0* + *t_step* .

.. meta::
   :keywords: fun

.. index:: fun

.. _numeric_ode_multi_step@fun:

fun
***

.. meta::
   :keywords: fun.set_t_all_index(index)

.. index:: fun.set_t_all_index(index)

.. _numeric_ode_multi_step@fun@fun.set_t_all_index(index):

fun.set_t_all_index(index)
==========================
Often, we use interpolation with knots to define :math:`f(t, y)`.
It is one of the subtitle issues of AD that even though values are the
same, derivatives might not be the same; e.g.,
piecewise linear interpolation.
We must break the integration of the ODE at each of the knot
so we can use a method that assumes :math:`f(t, y)` is smooth.
Also so that AD can be used to compute derivatives of our solutions.
The function ``set_t_all_index``
informs *fun* that we are currently integrating the time interval

| |tab| [ *t_all* [ *index* ] , *t_all* [ *index* +1] ]

so that it know which smooth function to represent
even if :math:`t` is at a knot and it matters if it is the interval
to the left or right of the knot.
The function ``set_t_all_index`` is called at the start
of each integration interval and before any of the other
*fun* member functions.

.. meta::
   :keywords: fun.f(t,, y)

.. index:: fun.f(t,, y)

.. _numeric_ode_multi_step@fun@fun.f(t, y):

fun.f(t, y)
===========
This call evaluates the function that defines the ODE

.. math::

   y^{(1)} (t) = f [ t , y(t) ]

.. meta::
   :keywords: one_step

.. index:: one_step

.. _numeric_ode_multi_step@fun@one_step:

one_step
========
The routine *one_step* may put extra requirements on *fun* .

.. meta::
   :keywords: t_all

.. index:: t_all

.. _numeric_ode_multi_step@t_all:

t_all
*****
This is a numpy vector of time values at which the solution is calculated.
The type of its elements can be ``float`` or ``ad_double`` .
It must be either monotone increasing or decreasing.

.. meta::
   :keywords: y_init

.. index:: y_init

.. _numeric_ode_multi_step@y_init:

y_init
******
This is the value of :math:`y(t)` at the initial time
*t_all* [ 0 ] as a numpy vector.
The type of its elements can be ``float`` or ``ad_double`` .

.. meta::
   :keywords: y_all

.. index:: y_all

.. _numeric_ode_multi_step@y_all:

y_all
*****
This is the approximate solution for :math:`y(t)` at all of the
times specified by *t_all* as a numpy array.
The value *y_all* [ *i* , *j* ] is the value of the j-th
component of :math:`y(t)` at time *t_all* [ *i* ] .

.. meta::
   :keywords: example

.. index:: example

.. _numeric_ode_multi_step@Example:

Example
*******
:ref:`numeric_ode_multi_step_xam_py-name`

.. meta::
   :keywords: source, code

.. index:: source, code

.. _numeric_ode_multi_step@Source Code:

Source Code
***********

.. literalinclude:: ../example/python/numeric/ode_multi_step.py
   :lines: 6-24
   :language: py

.. toctree::
   :maxdepth: 1
   :hidden:

   numeric_ode_multi_step_xam_py
