# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileCopyrightText: Bradley M. Bell <bradbell@seanet.com>
# SPDX-FileContributor: 2017-23 Bradley M. Bell
# ----------------------------------------------------------------------------
# cppad_error
# -----------------------------------------------------------------------------
# BEGIN SOURCE
def cppad_error_xam() :
   #
   import numpy
   import cppad_py
   #
   # initialize return variable
   ok = True
   # ---------------------------------------------------------------------
   # CppAD only detects and reports the error below when NDEBUG is noi defined
   if cppad_py.build_type() == 'release' :
      return ok
   # ---------------------------------------------------------------------
   n_ind = 1 # number of independent variables
   n_dep = 2 # number of dependent variables
   #
   # dimension some vectors
   x  = numpy.empty(n_ind, dtype=float)
   ay = numpy.empty(n_dep, dtype=cppad_py.a_double)
   #
   # independent variables
   x[0]  = 0.0
   ax    = cppad_py.independent(x)
   #
   # dependent variables
   ay[0] = ax[0] ** 2.0
   ay[1] = cppad_py.pow_int(ax[0], 2)
   #
   # define f(x) = y
   f = cppad_py.d_fun(ax, ay)
   #
   # Attempt to use first order before zero order
   try :
      y   = f.forward(1, x)
   except RuntimeError as error :
      message = str(error)
      index   = 0
      index   = message.find('file =', index)
      ok      = ok and 0 < index
      index   = message.find('line =', index)
      ok      = ok and 0 < index
      index   = message.find('exp =', index)
      ok      = ok and 0 < index
      index   = message.find('msg =', index)
      ok      = ok and 0 < index
   #
   return ok
#
# END SOURCE
# -----------------------------------------------------------------------------
#
# {xrst_begin cppad_error_xam}
# {xrst_comment_ch #}
#
# Python: Example CppAD Error Message
# ###################################
# {xrst_literal
#  # BEGIN SOURCE
#  # END SOURCE
# }
# {xrst_end cppad_error_xam}
def test_cppad_error_xam() :
   assert cppad_error_xam()
