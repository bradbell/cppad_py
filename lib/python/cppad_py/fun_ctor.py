# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileCopyrightText: Bradley M. Bell <bradbell@seanet.com>
# SPDX-FileContributor: 2017-22 Bradley M. Bell
# ----------------------------------------------------------------------------
#
# {xrst_begin py_fun_ctor}
# {xrst_spell
#     af
#     cppad
# }
# {xrst_comment_ch #}
#
#
# Stop Current Recording and Store Function Object
# ################################################
#
# Syntax
# ******
#
# d_fun
# =====
#
# | *f* =  ``cppad_py.d_fun`` ( *ax* , *ay* )
# | *f* =  ``cppad_py.d_fun`` ()
#
# a_fun
# =====
#
# | *af* =  ``cppad_py.a_fun`` ( *f* )
#
# ax
# **
# This argument must be the same as
# :ref:`ax<py_independent@ax>`
# returned by the previous call to ``independent`` ; i.e.,
# it must be the independent variable vector.
# We use *n*
# to denote the number of independent variables (the size of *ax* ).
#
# ay
# **
# This argument is a numpy array with ``a_double`` elements.
# It specifies the dependent variables.
# We use *m*
# to denote the number of dependent variables (the size of *ay* ).
#
# f
# *
# This result is a function object that
# has a representation for the floating point operations
# that mapped the independent variables *ax*
# to the dependent variables *ay* .
# This object computes function and derivative values using
# ``double``
#
# Empty Function
# ==============
# In the case where *ax* and *ay* are not present
# the function is 'empty' and all its sizes are zero; see
# :ref:`cpp_fun_property-name`.
#
# af
# **
# This result is a function object that
# has a representation for the same function as *f* .
# This object computes function and derivative values using
# ``a_double``
# Initially, there are not Taylor coefficient stored in *af* ; i.e.,
# :ref:`af_size_order()<py_fun_property@size_order>` is zero.
#
# {xrst_toc_hidden
#  example/python/core/a_fun_xam.py
# }
# Example
# *******
# All of the examples use the ``d_fun`` constructor.
# The example :ref:`a_fun_xam_py-name` demonstrates the purpose of
# ``a_fun`` objects.
#
# {xrst_end py_fun_ctor}
# -----------------------------------------------------------------------------
import numpy
import cppad_py
#
# This function is used by __init__ in d_fun class to implement syntax above:
def d_fun_ctor(ax, ay) :
   """
   d_fun(ax, ay)
   Stop recording a_double operations and
   create an AD function object that maps ax -> ay.
   """
   #
   # This case is used to pass the default constructor through swig
   if type(ax) == type(None) or type(ay) == type(None) :
      # python version of defualt consructor does not specify ax or ay
      assert type(ax) == type(None) and type(ay) == type(None)
      ax = numpy.empty(0, dtype = cppad_py.a_double)
      ay = numpy.empty(0, dtype = cppad_py.a_double)
   #
   # convert ax -> au, ay -> av
   dtype    = cppad_py.a_double
   syntax   = 'd_fun(ax, ay)'
   au       = cppad_py.utility.numpy2vec(ax, dtype, ax.size, syntax, 'ax')
   av       = cppad_py.utility.numpy2vec(ay, dtype, ay.size, syntax, 'ay')
   #
   # call d_fun and return result
   return cppad_py.cppad_swig.d_fun(au, av)
