# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileCopyrightText: Bradley M. Bell <bradbell@seanet.com>
# SPDX-FileContributor: 2017-23 Bradley M. Bell
# ----------------------------------------------------------------------------
# for_jac_sparsity, rev_jac_sparsity
# -----------------------------------------------------------------------------
# BEGIN SOURCE
def sparse_jac_xam() :
   #
   import numpy
   import cppad_py
   #
   # initialize return variable
   ok = True
   # ---------------------------------------------------------------------
   # number of dependent and independent variables
   n = 3
   # one
   aone = cppad_py.a_double(1.0)
   #
   # create the independent variables ax
   x = numpy.empty(n, dtype=float)
   for i in range( n  ) :
      x[i] = i + 2.0
   #
   ax = cppad_py.independent(x)
   #
   # create dependent variables ay with ay[i] = (j+1) * ax[j]
   # where i = mod(j + 1, n)
   ay = numpy.empty(n, dtype=cppad_py.a_double)
   for j in range( n  ) :
      i = j+1
      if i >= n  :
         i = i - n
      #
      aj = cppad_py.a_double(j)
      ay_i = (aj + aone) * ax[j]
      ay[i] = ay_i
   #
   #
   # define af corresponding to f(x)
   f  = cppad_py.d_fun(ax, ay)
   #
   # sparsity pattern for identity matrix
   pat_eye = cppad_py.sparse_rc()
   pat_eye.resize(n, n, n)
   for k in range( n ) :
      pat_eye.put(k, k, k)
   #
   #
   # sparsity pattern for the Jacobian
   pat_jac = cppad_py.sparse_rc()
   f.for_jac_sparsity(pat_eye, pat_jac)
   #
   # loop over forward and reverse mode
   for mode in range( 2 ) :
      # compute all possibly non-zero entries in Jacobian
      subset = cppad_py.sparse_rcv()
      subset.pat(pat_jac)
      # work space used to save time for multiple calls
      work = cppad_py.sparse_jac_work()
      if mode == 0  :
         f.sparse_jac_for(subset, x, pat_jac, work)
      #
      if mode == 1  :
         f.sparse_jac_rev(subset, x, pat_jac, work)
      #
      #
      # check result
      ok = ok and n == subset.nnz()
      col_major = subset.col_major()
      row = subset.row()
      col = subset.col()
      val = subset.val()
      for k in range( n ) :
         ell = col_major[k]
         r = row[ell]
         c = col[ell]
         v = val[ell]
         i = c+1
         if i >=  n  :
            i = i - n
         #
         ok = ok and c == k
         ok = ok and r == i
         ok = ok and v == c + 1.0
      #
   #
   #
   return( ok )
#
# END SOURCE
#
#
# {xrst_begin sparse_jac_xam.py}
# {xrst_comment_ch #}
#
# Python: Computing Sparse Jacobians: Example and Test
# ####################################################
# {xrst_literal
#  # BEGIN SOURCE
#  # END SOURCE
# }
# {xrst_end sparse_jac_xam.py}
#
def test_sparse_jac_xam() :
   assert sparse_jac_xam()
