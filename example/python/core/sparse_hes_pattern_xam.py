# -----------------------------------------------------------------------------
#         cppad_py: A C++ Object Library and Python Interface to Cppad
#          Copyright (C) 2017-22 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# -----------------------------------------------------------------------------
# for_hes_sparsity, rev_hes_sparsity
# -----------------------------------------------------------------------------
# BEGIN SOURCE
def sparse_hes_pattern_xam() :
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
   # create dependent variables ay with ay[i] = ax[j] * ax[i]
   # where i = mod(j + 1, n)
   ay = numpy.empty(n, dtype=cppad_py.a_double)
   for j in range( n  ) :
      i = j+1
      if i >= n  :
         i = i - n
      #
      ay_i = ax[i] * ax[j]
      ay[i] = ay_i
   #
   #
   # define af corresponding to f(x)
   f  = cppad_py.d_fun(ax, ay)
   #
   # Set select_d (domain) to all true, initial select_r (range) to all false
   select_d = numpy.empty(n, dtype=bool)
   select_r = numpy.empty(n, dtype=bool)
   for i in range( n ) :
      select_d[i] = True
      select_r[i] = False
   #
   #
   # only select component 0 of the range function
   # f_0 (x) = x_0 * x_{n-1}
   select_r[0] = True
   #
   # loop over forward and reverse mode
   for mode in range( 2 ) :
      pat_out = cppad_py.sparse_rc()
      if mode == 0  :
         f.for_hes_sparsity(select_d, select_r, pat_out)
      #
      if mode == 1  :
         f.rev_hes_sparsity(select_d, select_r, pat_out)
      #
      #
      # check that result is sparsity pattern for Hessian of f_0 (x)
      ok = ok and pat_out.nnz() == 2
      row = pat_out.row()
      col = pat_out.col()
      for k in range( 2 ) :
         r = row[k]
         c = col[k]
         if r <= c  :
            ok = ok and r == 0
            ok = ok and c == n-1
         #
         if r >= c  :
            ok = ok and r == n-1
            ok = ok and c == 0
         #
      #
   #
   #
   return( ok )
#
# END SOURCE
#
#
# {xrst_begin sparse_hes_pattern_xam_py}
# {xrst_comment_ch #}
#
# Python: Hessian Sparsity Patterns: Example and Test
# ###################################################
# {xrst_literal
#  # BEGIN SOURCE
#  # END SOURCE
# }
# {xrst_end sparse_hes_pattern_xam_py}
#
