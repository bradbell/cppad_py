# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileCopyrightText: Bradley M. Bell <bradbell@seanet.com>
# SPDX-FileContributor: 2017-23 Bradley M. Bell
# ----------------------------------------------------------------------------
# BEGIN_PYTHON
import numpy
import copy
from cppad_py import a_double
def simple_inv(A) :
   nr, nc = A.shape
   has_a_double = False
   for e in A.flatten() :
      has_a_double = has_a_double or type(e) == a_double
   assert nr == nc
   #
   if has_a_double :
      e_type = a_double
   else :
      e_type = float
   #
   # initialize Tablue = [A | I]
   Tablue = numpy.empty( (nr, 2 * nr), dtype=e_type )
   Tablue[:,0:nr] = A
   for i in range(nr) :
      for j in range(nr) :
         Tablue[i, j]   = e_type( A[i, j] )
         Tablue[i,nr+j] = float(i == j)
   # ------------------------------------------------------------------------
   # Use row reduction to get convert A to an upper traingular matrix
   # with ones along the diagonal
   # ------------------------------------------------------------------------
   # for each column (except the last) of the matrix
   for j in range(nr - 1) :
      # next row is one with maximum absolute element in column j
      if has_a_double :
         i_max = numpy.argmax( numpy.fabs( Tablue[:,j] ) )
      else :
         i_max = numpy.argmax( numpy.abs( Tablue[:,j] ) )
      #
      # swap row j and row i_max
      if i_max != j :
         tmp              = copy.copy( Tablue[j,:] )
         Tablue[j,:]      = Tablue[i_max,:]
         Tablue[i_max,:]  = tmp
      #
      # divide row j by Tablue[j,j]
      Tablue[j,:] = Tablue[j,:] / Tablue[j,j]
      Tablue[j,j] = e_type(1.0)
      #
      # zero out column j in rows after j
      for k in range(nr - j - 1) :
         i = j + k + 1
         Tablue[i,:] = Tablue[i,:] - Tablue[i,j] * Tablue[j,:]
         Tablue[i,j]    = e_type( 0.0 )
   # divide the last row of Tablue by the last pivot element
   Tablue[nr-1,:]     = Tablue[nr-1,:] / Tablue[nr-1,nr-1]
   Tablue[nr-1, nr-1] = e_type( 1.0 )
   # ------------------------------------------------------------------------
   # Use row reduction to get convert upper traingular matrix to the identity
   # ------------------------------------------------------------------------
   for jm in reversed(range(nr - 1) ) :
      j = jm + 1
      # zero out entries in column j and row less than j
      for i in range(j) :
         Tablue[i,:] = Tablue[i,:] - Tablue[i,j] * Tablue[j,:]
         Tablue[i,j] = e_type( 0.0 )
   # -------------------------------------------------------------------------
   Ainv = Tablue[:, nr:]
   return Ainv
# END_PYTHON
#
#
# {xrst_begin numeric_simple_inv}
# {xrst_spell
#     ainv
# }
# {xrst_comment_ch #}
#
#
# An AD Compatible Matrix Inverse Routine
# #######################################
#
# Syntax
# ******
# *Ainv* =  ``simple_inv`` ( *A* )
#
# Purpose
# *******
# This routine can be used with ``ad_double``
#
# A
# *
# This must be an invertible square matrix (no singular detection is done).
# The type of its elements can be ``float`` or ``a_double`` .
#
# Ainv
# ****
# This is the matrix inverse of *A* .
#
# {xrst_toc_hidden
#  example/python/numeric/simple_inv_xam.py
# }
# Example
# *******
# :ref:`numeric_simple_inv_xam.py-name`
#
# Source Code
# ***********
# When viewing the source code below it is important to know that
# optimizes out multiplication by the constant one while recording a function.
# It also optimizes out both addition and multiplication by the constant zero.
# {xrst_literal
#  # BEGIN_PYTHON
#  # END_PYTHON
# }
#
# {xrst_end numeric_simple_inv}
