# -----------------------------------------------------------------------------
#         cppad_py: A C++ Object Library and Python Interface to Cppad
#          Copyright (C) 2017-22 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# -----------------------------------------------------------------------------
# initialize cppad_py
# -----------------------------------------------------------------------------
#
# {xrst_begin py_independent}
# {xrst_spell
#     adynamic
#     cppad
#     nd
#     nx
# }
# {xrst_comment_ch #}
#
#
# Declare Independent Variables and Start Recording
# #################################################
#
# Syntax
# ******
#
# | *ax* =  ``cppad_py.independent`` ( *x* )
# | ( *ax* , *adynamic* ) =  ``cppad_py.independent`` ( *x* , *dynamic* )
#
# x
# *
# This argument is a numpy vector with ``float`` elements.
# It specifies the number of independent variables
# and their values during the recording.
# We use *nx* = *x*\ ``.size``
# to denote the number of independent variables.
#
# dynamic
# *******
# This argument is a numpy vector with ``float`` elements.
# It specifies the number of independent dynamic parameters
# and their values during the recording.
# We use *nd* = *dynamic*\ ``.size``
# to denote the number of independent dynamic parameters.
#
# ax
# **
# This result is a numpy vector with ``a_double`` elements.
# This is the vector of independent variables.
# It has size *nx* and for
# *i* = 0 to *n* -1
#
# | |tab| *ax* [ *i* ]. ``value`` () == *x* [ *i* ]
#
# adynamic
# ********
# This result is a numpy vector with ``a_double`` elements.
# This is the vector of independent dynamic parameters.
# It has size *nd* and for
# *i* = 0 to *n* -1
#
# | |tab| *adynamic* [ *i* ]. ``value`` () == *dynamic* [ *i* ]
#
# Purpose
# *******
# This starts a recording of the :ref:`a_double` operations.
# This recording is terminated, and the information is stored,
# by calling the :ref:`d_fun_constructor<py_fun_ctor>`.
# It is terminated, and the information is lost,
# by calling :ref:`abort_recording<py_abort_recording>`.
#
# {xrst_toc_hidden
#  example/python/core/fun_dynamic_xam.py
# }
# Example
# *******
# Most of the python ``d_fun`` examples use this function.
# The :ref:`fun_dynamic_xam_py` uses the syntax that includes
# dynamic parameters.
#
# {xrst_end py_independent}
# -----------------------------------------------------------------------------
# BEGIN_INDEPENDENT_SOURCE
import cppad_py
import numpy
def independent(x, dynamic = None) :
   """
   ax = independent(x)
   creates the indepedent numpy vector ax, with value equal numpy vector x,
   and starts recording a_double operations.
   """
   # convert x -> u
   dtype    = float
   #
   nx = x.size
   if dynamic is None :
      syntax   = 'independent(x)'
      u = cppad_py.utility.numpy2vec(x, dtype, nx, syntax, 'x')
      av = cppad_py.cppad_swig.independent(u)
      ax = cppad_py.utility.vec2numpy(av, av.size());
      return ax
   #
   nd       = dynamic.size
   syntax   = 'independent(x, dynamic)'
   u = cppad_py.utility.numpy2vec(x, dtype, nx, syntax, 'x')
   v = cppad_py.utility.numpy2vec(dynamic, dtype, nd, syntax, 'dynamic')
   a_both   = cppad_py.cppad_swig.independent(u, v)
   ax       = numpy.empty(nx,       dtype=cppad_py.a_double)
   adynamic = numpy.empty(nd, dtype=cppad_py.a_double)
   # use copy constructor so a separate copy is made for numpy arrays
   for i in range(nx) :
      ax[i] = cppad_py.a_double( a_both[i] )
   for i in range(nd) :
      adynamic[i] = cppad_py.a_double( a_both[nx + i] )
   #
   return (ax, adynamic)
# END_INDEPENDENT_SOURCE
