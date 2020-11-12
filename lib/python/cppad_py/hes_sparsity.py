# -----------------------------------------------------------------------------
#         cppad_py: A C++ Object Library and Python Interface to Cppad
#          Copyright (C) 2017-20 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# -----------------------------------------------------------------------------
# {xsrst_comment_ch #}
#
# {xsrst_begin py_hes_sparsity}
#
# .. include:: ../preamble.rst
#
# {xsrst_spell
#   hes
#   bool
# }
#
# Hessian Sparsity Patterns
# #########################
#
# Syntax
# ******
#
# | *f*\ ``.for_hes_sparsity`` ( *select_domain* , *select_range* , *pattern_out* )
#
# *f*\ ``.rev_hes_sparsity`` ( *select_domain* , *select_range* , *pattern_out* )
#
# Purpose
# *******
# We use :math:`F : \B{R}^n \rightarrow \B{R}^m` to denote the
# function corresponding to the operation sequence stored in *f* .
# Fix a diagonal matrix :math:`D \in \B{R}^{n \times n}`, fix a vector
# :math:`r \in \B{R}^m`, and define
#
# .. math::
#
#    H(x) = D (r^\R{T} F)^{(2)} ( x ) D
#
# Given a sparsity pattern for :math:`D` and :math:`r`,
# these routines compute a sparsity pattern for :math:`H(x)`.
#
# x
# *
# Note that a sparsity pattern for :math:`H(x)` corresponds to the
# operation sequence stored in *f* and does not depend on
# the argument *x* .
#
# f
# *
# This object must have been returned by a previous call to the python
# :ref:`d_fun<py_fun_ctor>` constructor.
#
# select_domain
# *************
# The argument is a numpy vector with ``bool`` elements.
# It has size *n* and is a sparsity pattern for the diagonal of
# :math:`D`; i.e., *select_domain* [ *j* ] is true if and only if
# :math:`D_{j,j}` is possibly non-zero.
#
# select_range
# ************
# The argument is a numpy vector with ``bool`` elements.
# It has size *m* and is a sparsity pattern for the vector
# :math:`r`; i.e., *select_range* [ *i* ] is true if and only if
# :math:`r_i` is possibly non-zero.
#
# pattern_out
# ***********
# This argument must have be a :ref:`pattern<py_sparse_rc.pattern>`
# returned by the ``sparse_rc`` constructor.
# This input value of *pattern_out* does not matter.
# Upon return *pattern_out* is a sparsity pattern for
# :math:`H(x)`.
#
# Sparsity for Component Wise Hessian
# ***********************************
# Suppose that :math:`D` is the identity matrix,
# and only the *i*-th component of *r* is possibly non-zero.
# In this case, *pattern_out* is a sparsity pattern for
# :math:`F_i^{(2)} ( x )`.
#
# {xsrst_children
#   example/python/core/sparse_hes_pattern_xam.py
# }
# Example
# *******
# :ref:`python<sparse_hes_pattern_xam_py>`
#
# {xsrst_end py_hes_sparsity}
# -----------------------------------------------------------------------------
# undocumented fact: pattern.rc is vec_int version of sparsity pattern
from cppad_py.utility import numpy2vec
def d_fun_for_hes_sparsity(f, select_domain, select_range, pattern_out) :
    """
    f.for_hes_sparsity(select_domain, select_range, pattern_out)
    """
    n      = f.size_domain()
    m      = f.size_range()
    dtype  = bool
    syntax = 'f.for_hes_sparsity(select_domain, select_range, pattern_out)'
    u      = numpy2vec(select_domain, dtype, n, syntax, 'select_domain')
    v      = numpy2vec(select_range,  dtype, m, syntax, 'select_range')
    f.for_hes_sparsity(u, v, pattern_out.rc)
#
def d_fun_rev_hes_sparsity(f, select_domain, select_range, pattern_out) :
    """
    f.rev_hes_sparsity(select_domain, select_range, pattern_out)
    """
    n      = f.size_domain()
    m      = f.size_range()
    dtype  = bool
    syntax = 'f.rev_hes_sparsity(select_domain, select_range, pattern_out)'
    u      = numpy2vec(select_domain, dtype, n, syntax, 'select_domain')
    v      = numpy2vec(select_range,  dtype, m, syntax, 'select_range')
    f.rev_hes_sparsity(u, v, pattern_out.rc)
