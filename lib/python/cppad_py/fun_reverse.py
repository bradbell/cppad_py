# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileCopyrightText: Bradley M. Bell <bradbell@seanet.com>
# SPDX-FileContributor: 2017-22 Bradley M. Bell
# ----------------------------------------------------------------------------
#
# {xrst_begin py_fun_reverse}
# {xrst_spell
#     xq
#     yq
# }
# {xrst_comment_ch #}
#
#
# Reverse Mode AD
# ###############
#
# Syntax
# ******
# *xq* = *f*\ ``.reverse`` ( *q* , *yq* )
#
# f
# *
# This is either a
# :ref:`d_fun<py_fun_ctor@Syntax@d_fun>` or
# :ref:`a_fun<py_fun_ctor@Syntax@a_fun>` function object
# and is effectively constant; i.e., not changed.
#
# Notation
# ********
#
# f(x)
# ====
# We use the notation :math:`f: \B{R}^n \rightarrow \B{R}^m`
# for the function corresponding to *f* .
# Note that *n* is the size of :ref:`ax<py_fun_ctor@ax>`
# and *m* is the size of :ref:`ay<py_fun_ctor@ay>`
# in to the constructor for *f* .
#
# X(t), S
# =======
# This is the same function as
# :ref:`x(t)<py_fun_forward@X(t)>` in the previous call to
# *f*\ ``.forward`` .
# We use :math:`S \in \B{R}^{n \times q}` to denote the Taylor coefficients
# of :math:`X(t)`.
#
# Y(t), T
# =======
# This is the same function as
# :ref:`y(t)<py_fun_forward@Y(t)>` in the previous call to
# *f*\ ``.forward`` .
# We use :math:`T \in \B{R}^{m \times q}` to denote the Taylor coefficients
# of :math:`Y(t)`.
# We also use the notation :math:`T(S)` to express the fact that
# the Taylor coefficients for :math:`Y(t)` are a function of the
# Taylor coefficients of :math:`X(t)`.
#
# G(T)
# ====
# We use the notation :math:`G : \B{R}^{m \times p} \rightarrow \B{R}`
# for a function that the calling routine chooses.
#
# q
# *
# This argument has type ``int`` and is positive.
# It is the number of the Taylor coefficient (for each variable)
# that we are computing the derivative with respect to.
# It must be greater than zero, and less than or equal
# the number of Taylor coefficient stored in *f* ; i.e.,
# :ref:`f_size_order()<py_fun_property@size_order>`.
#
# yq
# **
# If *f* is a ``d_fun`` ( ``a_fun`` ) object, *yq*
# is a numpy vector with ``float`` ( ``a_double`` ) elements,
# *m* rows and *q* columns.
# For 0 <= *i* < *m* and 0 <= *k* < *q* ,
# *yq* [ *i* , *k* ] is the partial derivative of
# :math:`G(T)` with respect to the *k*-th order Taylor coefficient
# for the *i*-th component function; i.e.,
# the partial derivative of :math:`G(T)` w.r.t. :math:`Y_i^{(k)} (t) / k !`.
#
# xq
# **
# The result is a numpy vector with ``float`` ( ``a_double`` ) elements,
# *n* rows and *q* columns.
# For 0 <= *j* < *n* and 0 <= *k* < *q* ,
# *xq* [ *j* , *k* ] is the partial derivative of
# :math:`G(T(S))` with respect to the *k*-th order Taylor coefficient
# for the *j*-th component function; i.e.,
# the partial derivative of
# :math:`G(T(S))` w.r.t. :math:`S_j^{(k)} (t) / k !`.
#
# {xrst_toc_hidden
#  example/python/core/fun_reverse_xam.py
# }
# Example
# *******
# :ref:`fun_reverse_xam_py-name`
#
# {xrst_end py_fun_reverse}
# -----------------------------------------------------------------------------
import cppad_py
import numpy
# -----------------------------------------------------------------------------
# This function is used by reverse in d_fun class to implement syntax above
def d_fun_reverse(f, q, yq) :
   """
   xq = f.reverse(q, yq)
   given Taylor coefficients for X(t), compute Taylor coefficients for
   Y(t) = f(X(t)).
   """
   #
   n = f.size_domain()
   m = f.size_range()
   #
   # convert yq -> u
   dtype    = float
   shape    = (m, q)
   syntax   = 'f.reverse(q, yq)'
   u = cppad_py.utility.numpy2vec(yq, dtype, shape, syntax, 'yq')
   #
   # call reverse
   v =  f.reverse(q, u)
   #
   # convert v -> xp
   xq = cppad_py.utility.vec2numpy(v, n, q)
   #
   return xq
# -----------------------------------------------------------------------------
# This function is used by reverse in a_fun class to implement syntax above
def a_fun_reverse(af, q, ayq) :
   """
   axq = af.reverse(q, ayq)
   given Taylor coefficients for X(t), compute Taylor coefficients for
   Y(t) = f(X(t)).
   """
   #
   n = af.size_domain()
   m = af.size_range()
   #
   # convert yq -> u
   dtype    = cppad_py.a_double
   shape    = (m, q)
   syntax   = 'af.reverse(q, ayq)'
   au = cppad_py.utility.numpy2vec(ayq, dtype, shape, syntax, 'ayq')
   #
   # call reverse
   av =  af.reverse(q, au)
   #
   # convert v -> xp
   axq = cppad_py.utility.vec2numpy(av, n, q)
   #
   return axq
