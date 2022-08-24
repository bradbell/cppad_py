# -----------------------------------------------------------------------------
#         cppad_py: A C++ Object Library and Python Interface to Cppad
#          Copyright (C) 2017-22 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# -----------------------------------------------------------------------------
# {xrst_comment_ch #}
#
# {xrst_begin py_fun_hessian}
#
# Hessian of an AD Function
# #########################
#
# Syntax
# ******
# *H* = *f*\ ``.hessian`` ( *x* , *w* )
#
# f
# *
# This is either a
# :ref:`d_fun<py_fun_ctor@syntax@d_fun>` or
# :ref:`a_fun<py_fun_ctor@syntax@a_fun>` function object.
# Upon return, the zero order
# :ref:`taylor_coefficients<py_fun_forward@taylor_coefficient>`
# in *f* correspond to the value of *x* .
# The other Taylor coefficients in *f* are unspecified.
#
# f(x)
# ****
# We use the notation :math:`f: \B{R}^n \rightarrow \B{R}^m`
# for the function corresponding to *f* .
# Note that *n* is the size of :ref:`ax<py_fun_ctor@ax>`
# and *m* is the size of :ref:`ay<py_fun_ctor@ay>`
# in to the constructor for *f* .
#
# g(x)
# ****
# We use the notation :math:`g: \B{R}^n \rightarrow \B{R}`
# for the function defined by
#
# .. math::
#
#    g(x) = \sum_{i=0}^{n-1} w_i f_i (x)
#
# x
# *
# If *f* is a ``d_fun`` or ``a_fun`` ,
# *x* is a numpy vector with ``float`` ( ``a_double`` ) elements
# and size *n* .
# It specifies the argument value at we are computing the Hessian
# :math:`g^{(2)}(x)`.
#
# w
# *
# If *f* is a ``d_fun`` or ``a_fun`` ,
# *w* is a numpy vector with ``float`` ( ``a_double`` ) elements
# and size *m* .
# It specifies the vector *w* in the definition of :math:`g(x)` above.
#
# H
# *
# The result is a numpy matrix with ``float`` ( ``a_double`` ) elements,
# *n* rows and ``n`` columns.
# For *i* between zero and *n* -1
# and *j* between zero and *n* -1 ,
#
# .. math::
#
#    H [ i, j ] = \frac{ \partial^2 g }{ \partial x_i \partial x_j } (x)
#
# {xrst_toc_hidden
#  example/python/core/fun_hessian_xam.py
# }
# Example
# *******
# :ref:`fun_hessian_xam_py`
#
# {xrst_end py_fun_hessian}
# -----------------------------------------------------------------------------
import cppad_py
import numpy
# -----------------------------------------------------------------------------
# This function is used by hessian in d_fun class to implement syntax above
def d_fun_hessian(f, x, w) :
   """
   H = f.hessian(x, w)
   computes Hessian of a function corresponding a sum of the components of f
   """
   #
   n = f.size_domain()
   m = f.size_range()
   #
   # convert x -> u, w -> v
   dtype    = float
   syntax   = 'f.hessian(x, w)'
   u = cppad_py.utility.numpy2vec(x, dtype, n, syntax, 'x')
   v = cppad_py.utility.numpy2vec(w, dtype, m, syntax, 'w')
   #
   # call hessian
   z =  f.hessian(u, v)
   #
   H = cppad_py.utility.vec2numpy(z, n, n)
   #
   return H
# -----------------------------------------------------------------------------
# This function is used by hessian in d_fun class to implement syntax above
def a_fun_hessian(af, ax, aw) :
   """
   aH = af.hessian(ax, aw)
   computes Hessian of a function corresponding a sum of the components of af
   """
   #
   n = af.size_domain()
   m = af.size_range()
   #
   # convert x -> u, w -> v
   dtype    = cppad_py.a_double
   syntax   = 'f.hessian(x, w)'
   au = cppad_py.utility.numpy2vec(ax, dtype, n, syntax, 'ax')
   av = cppad_py.utility.numpy2vec(aw, dtype, m, syntax, 'aw')
   #
   # call hessian
   az =  af.hessian(au, av)
   #
   aH = cppad_py.utility.vec2numpy(az, n, n)
   #
   return aH
