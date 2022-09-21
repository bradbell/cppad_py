# -----------------------------------------------------------------------------
#         cppad_py: A C++ Object Library and Python Interface to Cppad
#          Copyright (C) 2017-22 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# -----------------------------------------------------------------------------
#
# {xrst_begin py_fun_forward}
# {xrst_comment_ch #}
#
# {xrst_spell
#  xp
#  yp
#  xp
# }
#
# Forward Mode AD
# ###############
#
# Syntax
# ******
# *yp* = *f*\ ``.forward`` ( *p* , *xp* )
#
# Taylor Coefficient
# ******************
# For a function :math:`g(t)` of a scalar argument :math:`t \in \B{R}`,
# the *p*-th order Taylor coefficient is its
# ``p`` -th order derivative divided by *p* factorial
# and evaluated at :math:`t = 0`; i.e.,
#
# .. math::
#
#    g^{(p)} (0) /  p !
#
# f
# *
# This is either a
# :ref:`d_fun<py_fun_ctor@Syntax@d_fun>` or
# :ref:`a_fun<py_fun_ctor@Syntax@a_fun>` function object.
# Note that its state is changed by this operation because
# all the Taylor coefficient that it calculates for every
# variable in recording are stored.
# See more discussion of this fact under the heading
# :ref:`p<py_fun_forward@p>` below.
#
# f(x)
# ****
# We use the notation :math:`f: \B{R}^n \rightarrow \B{R}^m`
# for the function corresponding to *f* .
# Note that *n* is the size of :ref:`ax<py_fun_ctor@ax>`
# and *m* is the size of :ref:`ay<py_fun_ctor@ay>`
# in to the constructor for *f* .
#
# X(t)
# ****
# We use the notation :math:`X : \B{R} \rightarrow \B{R}^n`
# for a function that the calling routine chooses.
#
# Y(t)
# ****
# We define the function :math:`Y : \B{R} \rightarrow \B{R}^n`
# by :math:`Y(t) = f(X(t))`.
#
# p
# *
# This argument has type ``int`` and is non-negative.
# Its value is the order of the Taylor coefficient being calculated.
# If there was no call to ``forward`` for this *f* ,
# the value of *p* must be zero.
# Otherwise, it must be between zero and one greater that its
# value for the previous call using this *f* .
# After this call, the Taylor coefficients for orders zero though *p* ,
# and for every variable in the recording, will be stored in *f* .
#
# size_order
# ==========
# After this call,
# :ref:`f_size_order()<py_fun_property@size_order>` is *p* +1 .
#
# xp
# **
# If *f* is a ``d_fun`` ( ``a_fun`` ) object, *xp*
# is a numpy vector with ``float`` ( ``a_double`` ) elements
# and size *n* .
# It specifies the *p*-th order Taylor coefficients for *X(t* ) .
#
# yp
# **
# The result is a numpy vector with ``float`` ( ``a_double`` ) elements
# and size *m* .
# It is the *p*-th order Taylor coefficients for :math:`Y(t)`.
#
# {xrst_toc_hidden
#  example/python/core/fun_forward_xam.py
# }
# Example
# *******
# :ref:`fun_forward_xam_py`
#
# {xrst_end py_fun_forward}
# -----------------------------------------------------------------------------
import cppad_py
import numpy
# ----------------------------------------------------------------------------
# This function is used by forward in d_fun class to implement syntax above
def d_fun_forward(f, p, xp) :
   """
   yp = f.forward(p, xp)
   given Taylor coefficients for X(t), compute Taylor coefficients for
   Y(t) = f(X(t)).
   """
   #
   n = f.size_domain()
   m = f.size_range()
   #
   # convert x -> u
   dtype    = float
   syntax   = 'f.forward(p, xp)'
   u = cppad_py.utility.numpy2vec(xp, dtype, n, syntax, 'xp')
   #
   # call forward
   v =  f.forward(p, u)
   #
   # convert v -> yp
   yp = cppad_py.utility.vec2numpy(v, m)
   #
   return yp
# ----------------------------------------------------------------------------
# This function is used by forward in a_fun class to implement syntax above
def a_fun_forward(af, p, axp) :
   """
   ayp = af.forward(p, axp)
   given Taylor coefficients for X(t), compute Taylor coefficients for
   Y(t) = f(X(t)).
   """
   #
   n = af.size_domain()
   m = af.size_range()
   #
   # convert x -> u
   dtype    = cppad_py.a_double
   syntax   = 'af.forward(p, axp)'
   au = cppad_py.utility.numpy2vec(axp, dtype, n, syntax, 'axp')
   #
   # call forward
   av =  af.forward(p, au)
   #
   # convert av -> ayp
   ayp = cppad_py.utility.vec2numpy(av, m)
   #
   return ayp
