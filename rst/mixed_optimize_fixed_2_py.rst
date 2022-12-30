.. _mixed_optimize_fixed_2_py-name:

!!!!!!!!!!!!!!!!!!!!!!!!!
mixed_optimize_fixed_2_py
!!!!!!!!!!!!!!!!!!!!!!!!!

.. raw:: html

   <a href="_sources/mixed_optimize_fixed_2_py.rst.txt">View page source</a>

.. meta::
   :keywords: mixed_optimize_fixed_2_py, the, ipopt, example, problem:, example, test

.. index:: mixed_optimize_fixed_2_py, the, ipopt, example, problem:, example, test

.. _mixed_optimize_fixed_2_py-title:

The Ipopt Example Problem: Example and Test
###########################################

.. meta::
   :keywords: problem

.. index:: problem

.. _mixed_optimize_fixed_2_py@Problem:

Problem
*******
This optimization problem is take from the
`ipopt interfaces <https://coin-or.github.io/Ipopt/INTERFACES.html>`_
documentation.

.. math::
   :nowrap:

   \begin{align*}
   \R{minimize} \;
      & x_0 x_3 ( x_0 + x_1 + x_2) + x_2 & \R{\; w.r.t \;} x \in \B{R}^4
   \\
   \R{subject \; to}  \;
      & 25 \leq  x_0 x_1 x_2 x_3 \\
      & 40 =  x_0^2 + x_1^2 + x_2^2 + x_3^2 \\
      & 1 \leq x \leq 5
   \end{align*}

The starting point for the optimization is :math:`(1,5,5,1)`
and the optimal solution is

.. math::

   ( \; 1.00000000, \; 4.74299963, \; 3.82114998, \; 1.37940829 \; )

.. literalinclude:: ../example/python/mixed/optimize_fixed_2.py
   :lines: 50-95
   :language: py
