# -----------------------------------------------------------------------------
#         cppad_py: A C++ Object Library and Python Interface to Cppad
#          Copyright (C) 2017-22 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# -----------------------------------------------------------------------------
# BEGIN_PYTHON
import numpy
import cppad_py

class optimize_fun_class :
   def __init__(self, objective_ad, constraint_ad=None) :
      self.objective_ad  = objective_ad
      self.constraint_ad = constraint_ad
   #
   def objective_fun(self, x) :
      # objective as a vector
      y = self.objective_ad.forward(0, x)
      return y[0]
   #
   def objective_grad(self, x) :
      # Jacobian as a matrix
      J = self.objective_ad.jacobian(x)
      # change to a vector
      return J.flatten()
   #
   def objective_hess(self, x) :
      w = numpy.array( [ 1.0 ] )
      H = self.objective_ad.hessian(x, w)
      return H
   #
   def constraint_fun(self, x) :
      return self.constraint_ad.forward(0, x)
   #
   def constraint_jac(self, x) :
      # Jacobian as a matrix
      J = self.constraint_ad.jacobian(x)
      return J
   #
   def constraint_hess(self, x, v) :
      H = self.constraint_ad.hessian(x, v)
      return H
# END_PYTHON
"""
{xrst_begin numeric_optimize_fun_class}
{xrst_spell
   hess
   jac
   rl
}

A Helper Class That Defines Functions Needed for Optimization
#############################################################

Syntax
******
*optimize_fun* =  ``optimize_fun_class`` ( *objective_ad* , *constraint_ad* )

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

objective_ad
************
This is a :ref:`d_fun<py_fun_ctor@Syntax@d_fun>`
representation of the function :math:`f(x)`.

constraint_ad
*************
This is a ``d_fun`` representation of the function :math:`g(x)`.

optimize_fun
************
This class object has the following functions defined:

objective_fun
=============
The syntax

| |tab| *y* = *optimize_fun*\ ``.objective_fun`` ( *x* )

sets :math:`y = f(x)` where
*x* is a numpy vector with length *n*
and *y* is a scalar.

objective_grad
==============
The syntax

| |tab| *z* = *optimize_fun*\ ``.objective_grad`` ( *x* )

sets :math:`z = f^{(1)} (x)` where
*x* and *z* are numpy vectors with length *n* .

objective_hess
==============
The syntax

| |tab| *h* = *optimize_fun*\ ``.objective_hess`` ( *x* )

sets :math:`h = f^{(2)} (x)` where
*x* is a numpy vector with length *n*
and *h* is a numpy *n* by *n*  matrix.

constraint_fun
==============
The syntax

| |tab| *y* = *optimize_fun*\ ``.constraint_fun`` ( *x* )

sets :math:`y = g(x)` where
*x* ( *y* ) is a numpy vector with length
*n* ( *m* ).

constraint_jac
==============
The syntax

| |tab| *J* = *optimize_fun*\ ``.constraint_jac`` ( *x* )

sets :math:`J = g^{(1)} (x)` where
*x* is a numpy vector with length *n*
and *J* is a numpy *m* by *n*  matrix.

constraint_hess
===============
The syntax

| |tab| *H* = *optimize_fun*\ ``.constraint_hess`` ( *x* , *v* )

sets

.. math::

   H = \sum_{i=0}^{m-1} v_k g_i^{(2)} (x)

where *x* is a numpy vector with length *n*
and *H* is a numpy *n* by *n*  matrix.

{xrst_toc_hidden
   example/python/numeric/optimize_fun_xam.py
}
Example
*******
:ref:`numeric_optimize_fun_xam_py`

Source Code
***********
{xrst_literal
   # BEGIN_PYTHON
   # END_PYTHON
}

{xrst_end numeric_optimize_fun_class}
"""
