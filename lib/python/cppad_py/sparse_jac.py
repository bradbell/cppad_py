# -----------------------------------------------------------------------------
#         cppad_py: A C++ Object Library and Python Interface to Cppad
#          Copyright (C) 2017-22 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# -----------------------------------------------------------------------------
#
# {xrst_begin py_sparse_jac}
# {xrst_comment_ch #}
#
# {xrst_spell
#  rcv
#  cppad
# }
#
# Computing Sparse Jacobians
# ##########################
#
# Syntax
# ******
#
# | *work* =  ``cppad_py.sparse_jac_work`` ()
# | *n_sweep* = *f*\ ``.sparse_jac_for`` ( *subset* , *x* , *pattern* , *work* )
# | *n_sweep* = *f*\ ``.sparse_jac_rev`` ( *subset* , *x* , *pattern* , *work* )
#
# Purpose
# *******
# We use :math:`F : \B{R}^n \rightarrow \B{R}^m` to denote the
# function corresponding to *f* .
# The syntax above takes advantage of sparsity when computing the Jacobian
#
# .. math::
#
#    J(x) = F^{(1)} (x)
#
# In the sparse case, this should be faster and take less memory than
# :ref:`py_fun_jacobian`.
# We use the notation :math:`J_{i,j} (x)` to denote the partial of
# :math:`F_i (x)` with respect to :math:`x_j`.
#
# sparse_jac_for
# **************
# This function uses first order forward mode sweeps :ref:`py_fun_forward`
# to compute multiple columns of the Jacobian at the same time.
#
# sparse_jac_rev
# **************
# This function uses first order reverse mode sweeps :ref:`py_fun_reverse`
# to compute multiple rows of the Jacobian at the same time.
#
# f
# *
# This object must have been returned by a previous call to the python
# :ref:`d_fun<py_fun_ctor>` constructor.
# Note that the Taylor coefficients stored in *f* are affected
# by this operation; see
# :ref:`uses_forward<py_sparse_jac@Uses Forward>` below.
#
# subset
# ******
# This argument must have be a :ref:`matrix<py_sparse_rcv@matrix>`
# returned by the ``sparse_rcv`` constructor.
# Its row size is *subset*\ ``.nr`` () == *m* ,
# and its column size is *subset*\ ``.nc`` () == *n* .
# It specifies which elements of the Jacobian are computed.
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
# It specifies the point at which to evaluate the Jacobian :math:`J(x)`.
#
# pattern
# *******
# This argument must have be a :ref:`pattern<py_sparse_rc@pattern>`
# returned by the ``sparse_rc`` constructor.
# Its row size is *pattern*\ ``.nr`` () == *m* ,
# and its column size is *pattern*\ ``.nc`` () == *n* .
# It is a sparsity pattern for the Jacobian :math:`J(x)`.
# This argument is not used (and need not satisfy any conditions),
# when :ref:`work<py_sparse_jac@work>` is non-empty.
#
# work
# ****
# This argument must have been constructed by the call
#
# | |tab| *work* =  ``cppad_py.sparse_jac_work`` ()
#
# We refer to its initial value,
# and its value after *work*\ ``.clear`` () , as empty.
# If it is empty, information is stored in *work* .
# This can be used to reduce computation when
# a future call is for the same object *f* ,
# the same member function ``sparse_jac_for`` or ``sparse_jac_rev`` ,
# and the same subset of the Jacobian.
# If any of these values change, use *work*\ ``.clear`` () to
# empty this structure.
#
# n_sweep
# *******
# This return value is and ``int`` .
# If ``sparse_jac_for`` ( ``sparse_jac_rev`` ) is used,
# *n_sweep* is the number of first order forward (reverse) sweeps
# used to compute the requested Jacobian values.
# This is proportional to the total computational work,
# not counting the zero order forward sweep,
# or combining multiple columns (rows) into a single sweep.
#
# Uses Forward
# ************
# After each call to :ref:`py_fun_forward`,
# the object *f* contains the corresponding Taylor coefficients
# for all the variables in the operation sequence..
# After a call to ``sparse_jac_forward`` or ``sparse_jac_rev`` ,
# the zero order coefficients correspond to
#
# | |tab| *f*\ ``.forward(0`` , *x* )
#
# All the other forward mode coefficients are unspecified.
#
# {xrst_toc_hidden
#  example/python/core/sparse_jac_xam.py
# }
# Example
# *******
# :ref:`sparse_jac_xam_py`
#
# {xrst_end py_sparse_jac}
# -----------------------------------------------------------------------------
# undocumented fact: pattern.rc (subset.rcv) is vec_int version of
# sparsity pattern (sparse matrix)
import cppad_py
def d_fun_sparse_jac_for(f, subset, x, pattern, work) :
   """
   n_sweep = f.sparse_jac_for(subset, x, pattern, work)
   """
   n       = f.size_domain()
   m       = f.size_range()
   dtype   = float
   syntax  = 'f.sparse_jac_for(subset, x, pattern, work)'
   u       = cppad_py.utility.numpy2vec(x, dtype, n, syntax, 'x')
   f.sparse_jac_for(subset.rcv, u, pattern.rc, work)
#
def d_fun_sparse_jac_rev(f, subset, x, pattern, work) :
   """
   n_sweep = f.sparse_jac_rev(subset, x, pattern, work)
   """
   n       = f.size_domain()
   m       = f.size_range()
   dtype   = float
   syntax  = 'f.sparse_jac_rev(subset, x, pattern, work)'
   u       = cppad_py.utility.numpy2vec(x, dtype, n, syntax, 'x')
   f.sparse_jac_rev(subset.rcv, u, pattern.rc, work)
