# -----------------------------------------------------------------------------
#         cppad_py: A C++ Object Library and Python Interface to Cppad
#          Copyright (C) 2017-22 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# -----------------------------------------------------------------------------
# sparse_rcv
# -----------------------------------------------------------------------------
# BEGIN SOURCE
def sparse_rcv_xam() :
   #
   import numpy
   import cppad_py
   #
   # initialize return variable
   ok = True
   # ---------------------------------------------------------------------
   # create an empty matrix
   matrix = cppad_py.sparse_rcv()
   ok     = ok and matrix.nr()  == 0
   ok     = ok and matrix.nc()  == 0
   ok     = ok and matrix.nnz() == 0
   #
   # create sparsity pattern for n by n identity matrix
   pattern = cppad_py.sparse_rc()
   n = 5
   pattern.resize(n, n, n)
   for k in range( n ) :
      pattern.put(k, k, k)
   #
   # create n by n sparse representation of identity matrix
   matrix.pat(pattern)
   for k in range( n ) :
      matrix.put(k, 1.0)
   #
   # row, column indices
   row = matrix.row()
   col = matrix.col()
   val = matrix.val()
   #
   # check results
   for k in range( n ) :
      ok = ok and row[k] == k
      ok = ok and col[k] == k
      ok = ok and val[k] == 1.0
   #
   # For this case, row_major and col_major order are same as original order
   row_major = matrix.row_major()
   col_major = matrix.col_major()
   for k in range( n ) :
      ok = ok and row_major[k] == k
      ok = ok and col_major[k] == k
   #
   #
   return( ok )
#
# END SOURCE
#
#
# {xrst_begin sparse_rcv_xam_py}
# {xrst_comment_ch #}
#
# Python: Sparsity Patterns: Example and Test
# ###########################################
# {xrst_literal
#  # BEGIN SOURCE
#  # END SOURCE
# }
# {xrst_end sparse_rcv_xam_py}
#
