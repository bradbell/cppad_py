# -----------------------------------------------------------------------------
#         cppad_py: A C++ Object Library and Python Interface to Cppad
#          Copyright (C) 2017-20 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# -----------------------------------------------------------------------------
# {xsrst_comment_ch #}
#
# {xsrst_begin py_sparse_rc}
#
# .. include:: ../preamble.rst
#
# {xsrst_spell
#   nnz
#   resize
#   cppad
# }
#
# Sparsity Patterns
# #################
#
# Syntax
# ******
#
# | *pattern* =  ``cppad_py.sparse_rc`` ()
# | *pattern* . ``resize`` ( *nr* , *nc* , *nnz* )
# | *nr* = *pattern* . ``nr`` ()
# | *nc* = *pattern* . ``nc`` ()
# | *nnz* = *pattern* . ``nnz`` ()
# | *pattern* . ``put`` ( *k* , *r* , *c* )
# | *row* = *pattern* . ``row`` ()
# | *col* = *pattern* . ``col`` ()
# | *row_major* = *pattern* . ``row_major`` ()
# | *col_major* = *pattern* . ``col_major`` ()
#
# pattern
# *******
# This result is used to hold a sparsity pattern for a matrix.
# It is constant
# except during the ``resize`` and ``put`` operations.
#
# nr
# **
# This argument is a non-negative ``int``
# and is the number of rows in the sparsity pattern.
# The function ``nr()`` returns the value of
# *nr* in the previous ``resize`` operation.
#
# nc
# **
# This argument is a non-negative ``int``
# and is the number of columns in the sparsity pattern.
# The function ``nc()`` returns the value of
# *nc* in the previous ``resize`` operation.
#
# nnz
# ***
# This argument is a non-negative ``int``
# and is the number of possibly non-zero
# index pairs in the sparsity pattern.
# The function ``nnz()`` returns the value of
# *nnz* in the previous ``resize`` operation.
#
# resize
# ******
# The current sparsity pattern is lost and a new one is started
# with the specified parameters.
# After each ``resize`` , the elements in the *row*
# and *col* vectors should be assigned using ``put`` .
#
# put
# ***
# This function sets the values
#
# | |tab| *row* [ *k* ] = *r*
# | |tab| *col* [ *k* ] = *c*
#
# (The name ``set`` is used by Cppad, but not used here,
# because ``set`` it is a built-in name in Python.)
#
# k
# =
# This argument is a non-negative ``int``
# and must be less than *nnz* .
#
# r
# =
# This argument is a non-negative ``int``
# and must be less than *nr* .
# It specifies the value assigned to *row* [ *k* ] .
#
# c
# =
# This argument is a non-negative ``int``
# and must be less than *nc* .
# It specifies the value assigned to *col* [ *k* ] .
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
# {xsrst_children
#   example/python/core/sparse_rc_xam.py
# }
# Example
# *******
# :ref:`sparse_rc_xam_py<sparse_rc_xam_py>`
#
# {xsrst_end py_sparse_rc}
# -----------------------------------------------------------------------------
import cppad_py
import numpy
class sparse_rc :
    """Python interface to CppAD::sparse_rc"""
    #
    def __init__(self) :
        self.rc = cppad_py.swig.sparse_rc()
    #
    # resize
    def resize(self, nr, nc, nnz) :
        self.rc.resize(nr, nc, nnz)
    #
    # nr
    def nr(self) :
        return self.rc.nr()
    #
    # nc
    def nc(self) :
        return self.rc.nc()
    #
    # nnz
    def nnz(self) :
        return self.rc.nnz()
    #
    # put
    def put(self, k, r, c) :
        self.rc.put(k, r, c)
    #
    # row
    def row(self) :
        vec   = self.rc.row()
        assert vec.size() == self.rc.nnz()
        array = cppad_py.utility.vec2numpy(vec, vec.size() )
        return array
    #
    # col
    def col(self) :
        vec   = self.rc.col()
        assert vec.size() == self.rc.nnz()
        array = cppad_py.utility.vec2numpy(vec, vec.size() )
        return array
    #
    # row_major
    def row_major(self) :
        vec   = self.rc.row_major()
        assert vec.size() == self.rc.nnz()
        array = cppad_py.utility.vec2numpy(vec, vec.size() )
        return array
    #
    # col_major
    def col_major(self) :
        vec   = self.rc.col_major()
        assert vec.size() == self.rc.nnz()
        array = cppad_py.utility.vec2numpy(vec, vec.size() )
        return array
