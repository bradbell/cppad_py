# -----------------------------------------------------------------------------
#         cppad_py: A C++ Object Library and Python Interface to Cppad
#          Copyright (C) 2017-20 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# -----------------------------------------------------------------------------
# $begin py_hes_sparsity$$ $newlinech #$$
# $spell
#	hes
#	const
#	vec
#	bool
#	rc
#	numpy
# $$
#
# $section Hessian Sparsity Patterns$$
#
# $head Syntax$$
# $icode%f%.for_hes_sparsity(%select_domain%, %select_range%, %pattern_out%)
# %$$
# $icode%f%.rev_hes_sparsity(%select_domain%, %select_range%, %pattern_out%)%$$
#
# $head Purpose$$
# We use $latex F : \B{R}^n \rightarrow \B{R}^m$$ to denote the
# function corresponding to the operation sequence stored in $icode f$$.
# Fix a diagonal matrix $latex D \in \B{R}^{n \times n}$$, fix a vector
# $latex r \in \B{R}^m$$, and define
# $latex \[
#	H(x) = D (r^\R{T} F)^{(2)} ( x ) D
# \] $$
# Given a sparsity pattern for $latex D$$ and $latex r$$,
# these routines compute a sparsity pattern for $latex H(x)$$.
#
# $head x$$
# Note that a sparsity pattern for $latex H(x)$$ corresponds to the
# operation sequence stored in $icode f$$ and does not depend on
# the argument $icode x$$.
#
# $head f$$
# This object must have been returned by a previous call to the python
# $cref/d_fun/py_fun_ctor/$$ constructor.
#
# $head select_domain$$
# The argument is a numpy vector with $code bool$$ elements.
# It has size $icode n$$ and is a sparsity pattern for the diagonal of
# $latex D$$; i.e., $icode%select_domain%[%j%]%$$ is true if and only if
# $latex D_{j,j}$$ is possibly non-zero.
#
# $head select_range$$
# The argument is a numpy vector with $code bool$$ elements.
# It has size $icode m$$ and is a sparsity pattern for the vector
# $latex r$$; i.e., $icode%select_range%[%i%]%$$ is true if and only if
# $latex r_i$$ is possibly non-zero.
#
# $head pattern_out$$
# This argument must have be a $cref/pattern/py_sparse_rc/pattern/$$
# returned by the $code sparse_rc$$ constructor.
# This input value of $icode pattern_out$$ does not matter.
# Upon return $icode pattern_out$$ is a sparsity pattern for
# $latex H(x)$$.
#
# $head Sparsity for Component Wise Hessian$$
# Suppose that $latex D$$ is the identity matrix,
# and only the $th i$$ component of $icode r$$ is possibly non-zero.
# In this case, $icode pattern_out$$ is a sparsity pattern for
# $latex F_i^{(2)} ( x )$$.
#
# $children%
#	example/python/core/sparse_hes_pattern_xam.py
# %$$
# $head Example$$
# $cref/Python/sparse_hes_pattern_xam.py/$$
#
# $end
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
