# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileCopyrightText: Bradley M. Bell <bradbell@seanet.com>
# SPDX-FileContributor: 2017-23 Bradley M. Bell
# ----------------------------------------------------------------------------
#
# {xrst_begin py_sparse_rcv}
# {xrst_spell
#     col
#     nnz
#     ot
#     val
# }
# {xrst_comment_ch #}
#
#
# Sparse Matrices
# ###############
#
# Syntax
# ******
#
# | *matrix* =  ``cppad_py.sparse_rcv()``
# | *matrix*.pat ( *pattern* )
# | *nr* = *matrix*\ ``.nr()``
# | *nc* = *matrix*\ ``.nc()``
# | *nnz* =  *matrix*\ ``.nnz()``
# | *matrix*\ ``.put`` ( *k* , *v* )
# | *row* = *matrix*\ ``.row()``
# | *col* = *matrix*\ ``.col()``
# | *val* = *matrix*\ ``.val()``
# | *row_major* = *matrix*\ ``.row_major()``
# | *col_major* = *matrix*\ ``.col_major()``
#
# matrix
# ******
# This result is used ot hold a sparse matrix.
# It has zero row *nr*, zero columns *nc*, and zero non-zero values *nnz*
# when it is first created.
# It is constant except for the ``pat`` and ``put`` operations.
#
# pat
# ***
# This changes the sparsity pattern for the matrix to *pattern*.
# The argument *pattern* is a ``cppad_py.sparse_rc`` object,
# it is not changed, and it specifies *nr*, *nc*, *nnz*, *row*, and *col*.
# The values in the *val* vector are unspecified after this operation.
# The ``put`` operation can be used to set these values.
#
# nr
# **
# This return value is an ``int``
# and is the number of rows in the matrix.
#
# nc
# **
# This return value is an ``int``
# and is the number of columns in the matrix.
#
# nnz
# ***
# This return value is an ``int``
# and is the number of possibly non-zero values in the matrix.
#
# put
# ***
# This function sets the value
#
# | |tab| *val* [ *k* ] = *v*
#
# (The name ``set`` is used by CppAD, but not used here,
# because ``set`` it is a built-in name in Python.)
#
# k
# =
# This is a non-negative ``int`` and must be less than *nnz* .
#
# v
# =
# This argument has type ``float`` and
# specifies the value assigned to *val* [ *k* ] .
#
# row
# ***
# This result is a numpy vector with ``int`` elements
# and its size is *nnz* .
# For *k* = 0, ... , *nnz* -1 ,
# *row* [ *k* ] is the row index for the *k*-th possibly non-zero
# entry in the matrix.
#
# col
# ***
# This result is a numpy vector with ``int`` elements
# and its size is *nnz* .
# For *k* = 0, ... , *nnz* -1 ,
# *col* [ *k* ] is the column index for the *k*-th possibly non-zero
# entry in the matrix.
#
# val
# ***
# This result is a numpy vector with ``float`` elements
# and its size is *nnz* .
# For *k* = 0, ... , *nnz* -1 ,
# *val* [ *k* ] is the value of the *k*-th possibly non-zero
# entry in the matrix (the value may be zero).
#
# row_major
# *********
# This result is a numpy vector with ``int`` elements
# and its size *nnz* .
# It sorts the sparsity pattern in row-major order.
# To be specific,
#
# | |tab| *col* [ *row_major* [ *k* ] ] <= *col* [ *row_major* [ *k* +1] ]
#
# and if *col* [ *row_major* [ *k* ] ] == *col* [ *row_major* [ *k* +1] ] ,
#
# | |tab| *row* [ *row_major* [ *k* ] ] < *row* [ *row_major* [ *k* +1] ]
#
# This routine generates an assert if there are two entries with the same
# row and column values (if ``NDEBUG`` is not defined).
#
# col_major
# *********
# This result is a numpy vector with ``int`` elements
# and its size *nnz* .
# It sorts the sparsity pattern in column-major order.
# To be specific,
#
# | |tab| *row* [ *col_major* [ *k* ] ] <= *row* [ *col_major* [ *k* +1] ]
#
# and if *row* [ *col_major* [ *k* ] ] == *row* [ *col_major* [ *k* +1] ] ,
#
# | |tab| *col* [ *col_major* [ *k* ] ] < *col* [ *col_major* [ *k* +1] ]
#
# This routine generates an assert if there are two entries with the same
# row and column values (if ``NDEBUG`` is not defined).
#
# {xrst_toc_hidden
#  example/python/core/sparse_rcv_xam.py
# }
# Example
# *******
# :ref:`sparse_rcv_xam.py-name`
#
# {xrst_end py_sparse_rcv}
# -----------------------------------------------------------------------------
import cppad_py
import numpy
class sparse_rcv :
   """Python interface to CppAD::sparse_rc"""
   #
   def __init__(self) :
      pattern  = cppad_py.cppad_swig.sparse_rc()
      self.rcv = cppad_py.cppad_swig.sparse_rcv( pattern )
   #
   # pat
   def pat(self, pattern) :
      # use undocumented fact that pattern.rc is vec_int version of sparsity
      self.rcv = cppad_py.cppad_swig.sparse_rcv(pattern.rc)
   #
   # nr
   def nr(self) :
      return self.rcv.nr()
   #
   # nc
   def nc(self) :
      return self.rcv.nc()
   #
   # nnz
   def nnz(self) :
      return self.rcv.nnz()
   #
   # put
   def put(self, k, v) :
      self.rcv.put(k, v)
   #
   # row
   def row(self) :
      vec   = self.rcv.row()
      assert vec.size() == self.rcv.nnz()
      array = cppad_py.utility.vec2numpy(vec, vec.size() )
      return array
   #
   # col
   def col(self) :
      vec   = self.rcv.col()
      assert vec.size() == self.rcv.nnz()
      array = cppad_py.utility.vec2numpy(vec, vec.size() )
      return array
   #
   # val
   def val(self) :
      vec   = self.rcv.val()
      assert vec.size() == self.rcv.nnz()
      array = cppad_py.utility.vec2numpy(vec, vec.size() )
      return array
   #
   # row_major
   def row_major(self) :
      vec   = self.rcv.row_major()
      assert vec.size() == self.rcv.nnz()
      array = cppad_py.utility.vec2numpy(vec, vec.size() )
      return array
   #
   # col_major
   def col_major(self) :
      vec   = self.rcv.col_major()
      assert vec.size() == self.rcv.nnz()
      array = cppad_py.utility.vec2numpy(vec, vec.size() )
      return array
