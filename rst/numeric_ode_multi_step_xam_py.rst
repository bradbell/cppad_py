.. _numeric_ode_multi_step_xam_py-name:

!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
numeric_ode_multi_step_xam_py
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

.. raw:: html

   <a href="_sources/numeric_ode_multi_step_xam_py.rst.txt">View page source</a>

.. meta::
   :keywords: numeric_ode_multi_step_xam_py, example, computing, derivative, runge-kutta, ode, solution

.. index:: numeric_ode_multi_step_xam_py, example, computing, derivative, runge-kutta, ode, solution

.. _numeric_ode_multi_step_xam_py-title:

Example Computing Derivative A Runge-Kutta Ode Solution
#######################################################

.. meta::
   :keywords: ode

.. index:: ode

.. _numeric_ode_multi_step_xam_py@ODE:

ODE
***

.. math::

   \partial_t y_i (t, x) =  f(t, y, x) \left\{ \begin{array}{rl}
        x_0               & {\rm if} \; i = 0 \\
        x_i y_{i-1} (t)   & {\rm otherwise}
   \end{array} \right.

with the initial condition :math:`y(0) = 0`

.. meta::
   :keywords: solution

.. index:: solution

.. _numeric_ode_multi_step_xam_py@Solution:

Solution
********
This is a special case for which we know the solution

.. math::

   y_i (t, x) = \left\{ \begin{array}{rl}
        t  x_0                            & {\rm if} \; i = 0 \\
        ( t^i / (i+1) ! ) \prod_{j=0}^i x_j   & {\rm otherwise}
   \end{array} \right.

.. meta::
   :keywords: derivative, solution

.. index:: derivative, solution

.. _numeric_ode_multi_step_xam_py@Derivative of Solution:

Derivative of Solution
**********************
For this special case, the partial derivative of the solution with respect
to the j-th component of the vector :math:`x` is

.. math::

   \partial_{x(j)} y_i (t, x) =  \left\{ \begin{array}{rl}
        y_i (t, x) / x_j      & {\rm if} \; j \leq i \\
        0                     & {\rm otherwise}
   \end{array} \right.

.. meta::
   :keywords: source, code

.. index:: source, code

.. _numeric_ode_multi_step_xam_py@Source Code:

Source Code
***********

.. literalinclude:: ../../example/python/numeric/ode_multi_step_xam.py
   :lines: 62-139
   :language: py
