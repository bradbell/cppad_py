# -----------------------------------------------------------------------------
#         cppad_py: A C++ Object Library and Python Interface to Cppad
#          Copyright (C) 2017-22 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# -----------------------------------------------------------------------------
# sparse_hes
# -----------------------------------------------------------------------------
# BEGIN SOURCE
def sparse_hes_xam() :
   #
   import numpy
   import cppad_py
   #
   # initialize return variable
   ok = True
   # ---------------------------------------------------------------------
   # number of dependent and independent variables
   n = 3
   #
   # create the independent variables ax
   x = numpy.empty(n, dtype=float)
   for i in range( n  ) :
      x[i] = i + 2.0
   #
   ax = cppad_py.independent(x)
   #
   # ay[i] = j * ax[j] * ax[i]
   # where i = mod(j + 1, n)
   ay = numpy.empty(n, dtype=cppad_py.a_double)
   for j in range( n  ) :
      i = j+1
      if i >= n  :
         i = i - n
      #
      aj = cppad_py.a_double(j)
      ax_j = ax[j]
      ax_i = ax[i]
      ay[i] = aj * ax_j * ax_i
   #
   #
   # define af corresponding to f(x)
   f  = cppad_py.d_fun(ax, ay)
   #
   # Set select_d (domain) to all true,
   # initial select_r (range) to all false
   # initialize r to all zeros
   select_d = numpy.empty(n, dtype=bool)
   select_r = numpy.empty(n, dtype=bool)
   r = numpy.empty(n, dtype=float)
   for i in range( n ) :
      select_d[i] = True
      select_r[i] = False
      r[i] = 0.0
   #
   #
   # only select component n-1 of the range function
   # f_0 (x) = (n-1) * x_{n-1} * x_0
   select_r[0] = True
   r[0] = 1.0
   #
   # sparisty pattern for Hessian
   pattern = cppad_py.sparse_rc()
   f.for_hes_sparsity(select_d, select_r, pattern)
   #
   # compute all possibly non-zero entries in Hessian
   # (should only compute lower triangle becuase matrix is symmetric)
   subset = cppad_py.sparse_rcv()
   subset.pat(pattern)
   #
   # work space used to save time for multiple calls
   work = cppad_py.sparse_hes_work()
   #
   f.sparse_hes(subset, x, r, pattern, work)
   #
   # check that result is sparsity pattern for Hessian of f_0 (x)
   ok = ok and subset.nnz() == 2
   row = subset.row()
   col = subset.col()
   val = subset.val()
   for k in range( 2 ) :
      i = row[k]
      j = col[k]
      v = val[k]
      if i <= j  :
         ok = ok and i == 0
         ok = ok and j == n-1
      #
      if i >= j  :
         ok = ok and i == n-1
         ok = ok and j == 0
      #
      ok = ok and v == n-1
   #
   #
   return( ok )
#
# END SOURCE
#
#
# {xrst_begin sparse_hes_xam_py}
# {xrst_comment_ch #}
#
# {xrst_spell
# }
# Python: Hessian Sparsity Patterns: Example and Test
# ###################################################
# {xrst_literal
#  # BEGIN SOURCE
#  # END SOURCE
# }
# {xrst_end sparse_hes_xam_py}
#
