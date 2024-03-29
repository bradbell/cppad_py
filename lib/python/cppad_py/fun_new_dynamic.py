# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileCopyrightText: Bradley M. Bell <bradbell@seanet.com>
# SPDX-FileContributor: 2017-23 Bradley M. Bell
# ----------------------------------------------------------------------------
#
# {xrst_begin py_fun_new_dynamic}
# {xrst_comment_ch #}
#
# New Dynamic Parameters
# ######################
#
# Syntax
# ******
# *f*\ ``.new_dynamic`` ( *dynamic* )
#
# f
# *
# This is either a
# :ref:`d_fun<py_fun_ctor@Syntax@d_fun>` or
# :ref:`a_fun<py_fun_ctor@Syntax@a_fun>`.
# The independent :ref:`dynamic<py_independent@dynamic>` parameters
# are changed to have the specified values.
# The other dynamic parameters are then computed.
#
# dynamic
# *******
# If *f* is a ``d_fun`` ( ``a_fun`` ) object,
# *dynamic* is a numpy vector with ``float`` ( ``a_double`` )
# elements and its size must be the same as the size of
# :ref:`dynamic<py_independent@dynamic>` in the corresponding call to
# ``independent`` .
# It specifies new values for the dynamic parameters in *f* .
#
# size_order
# ==========
# After this call,
# :ref:`f_size_order()<py_fun_property@size_order>` is zero.
#
# Example
# *******
# See :ref:`fun_dynamic_xam.py-name`
#
# {xrst_end py_fun_new_dynamic}
# -----------------------------------------------------------------------------
import cppad_py
import numpy
# ----------------------------------------------------------------------------
# This function is used by d_fun class to implement syntax above
def d_fun_new_dynamic(f, dynamic) :
   """
   f.new_dynamic(dynamic)
   Set the independent dynamic parameters and compute the others.
   """
   #
   # convert x -> u
   dtype    = float
   syntax   = 'f.dynamic(p, dynamic)'
   n        = dynamic.size
   u        = cppad_py.utility.numpy2vec(dynamic, dtype, n, syntax, 'xp')
   f.new_dynamic(u)
# ----------------------------------------------------------------------------
# This function is used by a_fun class to implement syntax above
def a_fun_new_dynamic(af, adynamic) :
   """
   af.new_dynamic(adynamic)
   Set the independent dynamic parameters and compute the others.
   """
   #
   # convert x -> u
   dtype    = cppad_py.a_double
   syntax   = 'af.dynamic(adynamic)'
   n        = adynamic.size
   au       = cppad_py.utility.numpy2vec(adynamic, dtype, n, syntax, 'dynamic')
   af.new_dynamic(au)
