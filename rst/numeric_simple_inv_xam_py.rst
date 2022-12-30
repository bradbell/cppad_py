.. _numeric_simple_inv_xam_py-name:

!!!!!!!!!!!!!!!!!!!!!!!!!
numeric_simple_inv_xam_py
!!!!!!!!!!!!!!!!!!!!!!!!!

.. raw:: html

   <a href="_sources/numeric_simple_inv_xam_py.rst.txt">View page source</a>

.. meta::
   :keywords: numeric_simple_inv_xam_py, example, computing, derivatives, matrix, inversion

.. index:: numeric_simple_inv_xam_py, example, computing, derivatives, matrix, inversion

.. _numeric_simple_inv_xam_py-title:

Example Computing Derivatives of Matrix Inversion
#################################################

.. meta::
   :keywords: problem

.. index:: problem

.. _numeric_simple_inv_xam_py@Problem:

Problem
*******
We define

.. math::

   A(x) = \left( \begin{array}{cc}
   x_0 & x_1 \\
   x_2 & x_3
   \end{array} \right)

It follows that

.. math::

   A^{-1}(x) =
   \frac{1}{x_3 * x_0 - x_1 * x_2}
   \left( \begin{array}{cc}
   x_3 & - x_1 \\
   - x_2 & x_0
   \end{array} \right)

We define

.. math::

   f(x) = (x_3 * x_0 - x_1 * x_2) [
   A_{0,0}^{-1} (x),
   A_{0,1}^{-1} (x),
   A_{1,0}^{-1} (x),
   A_{1,1}^{-1} (x)
   ]
   = [ x_3, -x_1, -x_2, x_0]

The following example below check the derivative of :math:`f(x)`

.. meta::
   :keywords: source, code

.. index:: source, code

.. _numeric_simple_inv_xam_py@Source Code:

Source Code
***********

.. literalinclude:: ../example/python/numeric/simple_inv_xam.py
   :lines: 60-92
   :language: py
