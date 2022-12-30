.. _numeric_rosen3_step_xam_py-name:

!!!!!!!!!!!!!!!!!!!!!!!!!!
numeric_rosen3_step_xam_py
!!!!!!!!!!!!!!!!!!!!!!!!!!

.. raw:: html

   <a href="_sources/numeric_rosen3_step_xam_py.rst.txt">View page source</a>

.. meta::
   :keywords: numeric_rosen3_step_xam_py, example, computing, derivative, rosenbrock, ode, solution

.. index:: numeric_rosen3_step_xam_py, example, computing, derivative, rosenbrock, ode, solution

.. _numeric_rosen3_step_xam_py-title:

Example Computing Derivative A Rosenbrock Ode Solution
######################################################

.. meta::
   :keywords: y(t,, x)

.. index:: y(t,, x)

.. _numeric_rosen3_step_xam_py@y(t, x):

y(t, x)
*******
The two initial value problems below have the following solution:

.. math::

   y_i (t, x) = ( t^{i+1} / (i+1) ! ) \prod_{j=0}^i x_j

.. meta::
   :keywords: first, ode

.. index:: first, ode

.. _numeric_rosen3_step_xam_py@First ODE:

First ODE
*********

.. math::

   f(t, y, x)  =
   \left\{ \begin{array}{rl}
   x_0               & {\rm if} \; i = 0 \\
   x_i y_{i-1} (t)   & {\rm otherwise}
   \end{array} \right.

with the initial condition :math:`y(0) = 0`

.. meta::
   :keywords: second, ode

.. index:: second, ode

.. _numeric_rosen3_step_xam_py@Second ODE:

Second ODE
**********

.. math::

   f(t, y, x)  = ( t^i / i ! ) \prod_{j=0}^i x_j

with the initial condition :math:`y(0) = 0`

.. meta::
   :keywords: derivative, solution

.. index:: derivative, solution

.. _numeric_rosen3_step_xam_py@Derivative of Solution:

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

.. _numeric_rosen3_step_xam_py@Source Code:

Source Code
***********

.. literalinclude:: ../example/python/numeric/rosen3_step_xam.py
   :lines: 68-204
   :language: py
