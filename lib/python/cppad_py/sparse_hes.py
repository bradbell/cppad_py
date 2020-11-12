# -----------------------------------------------------------------------------
#         cppad_py: A C++ Object Library and Python Interface to Cppad
#          Copyright (C) 2017-20 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# -----------------------------------------------------------------------------
# {xsrst_comment_ch #}
#
# {xsrst_begin py_sparse_hes}
#
# .. include:: ../preamble.rst
#
# {xsrst_spell
#   rcv
#   hes
#   cppad
# }
#
# Computing Sparse Hessians
# #########################
#
# Syntax
# ******
#
# | *work* =  ``cppad_py.sparse_hes_work`` ()
# | *n_sweep* = *f*\ ``.sparse_hes`` ( *subset* , *x* , *r* , *pattern* , *work* )
#
# Purpose
# *******
# We use :math:`F : \B{R}^n \rightarrow \B{R}^m` to denote the
# function corresponding to *f* .
# Given a vector :math:`r \in \B{R}^m`, define
#
# .. math::
#
#    H(x) = (r^\R{T} F)^{(2)} ( x )
#
# This routine takes advantage of sparsity when computing elements
# of the Hessian :math:`H(x)`.
#
# f
# *
# This object must have been returned by a previous call to the python
# :ref:`d_fun<py_fun_ctor>` constructor.
# Note that the Taylor coefficients stored in *f* are affected
# by this operation; see
# :ref:`uses_forward<py_sparse_hes.uses_forward>` below.
#
# subset
# ******
# This argument must have be a :ref:`matrix<py_sparse_rcv.matrix>`
# returned by the ``sparse_rcv`` constructor.
# Its row size and column size is *n* ; i.e.,
# *subset*\ ``.nr`` () == *n* and *subset*\ ``.nc`` () == *n* .
# It specifies which elements of the Hessian are computed.
# The input value of its value vector
# *subset*\ ``.val`` () does not matter.
# Upon return it contains the value of the corresponding elements
# of the Jacobian.
# All of the row, column pairs in *subset* must also appear in
# *pattern* ; i.e., they must be possibly non-zero.
#
# x
# *
# This argument is a numpy vector with ``float`` elements
# and size *n* .
# It specifies the point at which to evaluate the Hessian :math:`H(x)`.
#
# r
# *
# This argument is a numpy vector with ``float`` elements
# and size *m* .
# It specifies the multiplier for each component of :math:`F(x)`;
# i.e., :math:`r_i` is the multiplier for :math:`F_i (x)`.
#
# pattern
# *******
# This argument must have be a :ref:`pattern<py_sparse_rc.pattern>`
# returned by the ``sparse_rc`` constructor.
# Its row size and column sizes are *n* ; i.e.,
# *pattern*\ ``.nr`` () == *n* and *pattern*\ ``.nc`` () == *n* .
# It is a sparsity pattern for the Hessian :math:`H(x)`.
# This argument is not used (and need not satisfy any conditions),
# when :ref:`work<py_sparse_hes.work>` is non-empty.
#
# work
# ****
# This argument must have been constructed by the call
#
# | |tab| *work* =  ``cppad_py.sparse_hes_work`` ()
#
# We refer to its initial value,
# and its value after *work*\ ``.clear`` () , as empty.
# If it is empty, information is stored in *work* .
# This can be used to reduce computation when
# a future call is for the same object *f* ,
# and the same subset of the Hessian.
# If either of these values change, use *work*\ ``.clear`` () to
# empty this structure.
#
# n_sweep
# *******
# The return value *n_sweep* has prototype
#
# | |tab| ``int`` *n_sweep*
#
# It is the number of first order forward sweeps
# used to compute the requested Hessian values.
# Each first forward sweep is followed by a second order reverse sweep
# so it is also the number of reverse sweeps.
# This is proportional to the total computational work,
# not counting the zero order forward sweep,
# or combining multiple columns and rows into a single sweep.
#
# Uses Forward
# ************
# After each call to :ref:`py_fun_forward<py_fun_forward>`,
# the object *f* contains the corresponding Taylor coefficients
# for all the variables in the operation sequence..
# After a call to ``sparse_hes``
# the zero order coefficients correspond to
#
# | |tab| *f*\ ``.forward(0`` , *x* )
#
# All the other forward mode coefficients are unspecified.
#
# {xsrst_children
#   example/python/core/sparse_hes_xam.py
# }
# Example
# *******
# :ref:`sparse_hes_xam_py<sparse_hes_xam_py>`
#
# {xsrst_end py_sparse_hes}
# -----------------------------------------------------------------------------
# undocumented fact: pattern.rc (subset.rcv) is vec_int version of
# sparsity pattern (sparse matrix)
import cppad_py
def d_fun_sparse_hes(f, subset, x, r, pattern, work) :
    """
    n_sweep = f.sparse_hes(subset, x, r, pattern, work)
    """
    n       = f.size_domain()
    m       = f.size_range()
    dtype   = float
    syntax  = 'f.sparse_hes(subset, x, r, pattern, work)'
    u       = cppad_py.utility.numpy2vec(x, dtype, n, syntax, 'x')
    v       = cppad_py.utility.numpy2vec(r, dtype, m, syntax, 'r')
    f.sparse_hes(subset.rcv, u, v, pattern.rc, work)
