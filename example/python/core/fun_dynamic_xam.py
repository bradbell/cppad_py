# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileCopyrightText: Bradley M. Bell <bradbell@seanet.com>
# SPDX-FileContributor: 2017-22 Bradley M. Bell
# ----------------------------------------------------------------------------
# fun_dynamid
# -----------------------------------------------------------------------------
# BEGIN SOURCE
import numpy
import cppad_py
def fun_dynamic_xam() :
   ok  = True
   nx  = 2
   nd  = 2
   #
   # value of independent variables during recording
   x = numpy.empty(nx, dtype=float)
   x[0] = 1.0
   x[1] = 2.0
   #
   # value of independent dynamic parameters during recording
   dynamic = numpy.empty(nd, dtype=float)
   dynamic[0] = 3.0
   dynamic[1] = 4.0
   #
   # start recording
   (ax, adynamic) = cppad_py.independent(x, dynamic)
   #
   # create another dynamic paramerer
   adyn  = adynamic[0] + adynamic[1]
   #
   # create another variable
   avar  = ax[0] + ax[1] + adyn
   #
   # create f(x) = x[0] + x[1] + dynamic[0] + dynamic[1]
   ay    = numpy.empty(1, dtype=cppad_py.a_double)
   ay[0] = avar
   f     = cppad_py.d_fun(ax, ay)
   #
   # check some properties of f
   ok = ok and f.size_domain() == nx
   ok = ok and f.size_order()  == 0
   #
   # zero order forward mode using same values as during the recording
   y  = f.forward(0, x)
   ok = ok and y[0] == (x[0] + x[1] + dynamic[0] + dynamic[1])
   #
   #  zero order forward mode using different value for dynamic parameters
   dynamic[0] = dynamic[0] + 1.0
   dynamic[1] = dynamic[1] + 1.0
   f.new_dynamic(dynamic)
   y   = f.forward(0, x)
   ok  = ok and y[0] == (x[0] + x[1] + dynamic[0] + dynamic[1])
   #
   return ok
# END SOURCE
# -----------------------------------------------------------------------------
#
# {xrst_begin fun_dynamic_xam_py}
# {xrst_comment_ch #}
#
# Python: Using Dynamic Parameters: Example and Test
# ##################################################
# {xrst_literal
#  # BEGIN SOURCE
#  # END SOURCE
# }
# {xrst_end fun_dynamic_xam_py}
