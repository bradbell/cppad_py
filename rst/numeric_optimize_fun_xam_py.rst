.. _numeric_optimize_fun_xam_py-name:

!!!!!!!!!!!!!!!!!!!!!!!!!!!
numeric_optimize_fun_xam_py
!!!!!!!!!!!!!!!!!!!!!!!!!!!

.. raw:: html

   <a href="_sources/numeric_optimize_fun_xam_py.rst.txt">View page source</a>

.. meta::
   :keywords: numeric_optimize_fun_xam_py, example, using, optimize_fun_class, with, scipy, optimization

.. index:: numeric_optimize_fun_xam_py, example, using, optimize_fun_class, with, scipy, optimization

.. _numeric_optimize_fun_xam_py-title:

Example Using optimize_fun_class with Scipy Optimization
########################################################

.. meta::
   :keywords: reference

.. index:: reference

.. _numeric_optimize_fun_xam_py@Reference:

Reference
*********
This problem comes form the
`Interfaces <https://coin-or.github.io/Ipopt/INTERFACES.html>`_
section of the Ipopt documentation.

.. meta::
   :keywords: problem

.. index:: problem

.. _numeric_optimize_fun_xam_py@Problem:

Problem
*******

.. math::

   \begin{array}{cr}
   {\rm minimize}      & x_0 x_3 ( x_0 + x_1 + x_2 ) + x_2   \\
   {\rm subject \; to} &             x_0 x_1 x_2 x_3 \geq 25 \\
                        & x_0^2 + x_1^2 + x_2^2 + x_3^2 = 40  \\
                        &                    1 \leq x \leq 5
   \end{array}

with the starting point :math:`x = (1, 5, 5, 1)`.
The optimal value for :math:`x` is

.. math::

 \newcommand{\W}[1]{{\; #1 \;}}
 (1.00000000 \W{,} 4.74299963 \W{,} 3.82114998 \W{,} 1.37940829)

.. meta::
   :keywords: trust_constr

.. index:: trust_constr

.. _numeric_optimize_fun_xam_py@trust_constr:

trust_constr
************
This is one of the
`scipy.optimize
<https://docs.scipy.org/doc/scipy/reference/optimize.html>`_
methods.

.. meta::
   :keywords: source, code

.. index:: source, code

.. _numeric_optimize_fun_xam_py@Source Code:

Source Code
***********

.. literalinclude:: ../example/python/numeric/optimize_fun_xam.py
   :lines: 61-144
   :language: py
