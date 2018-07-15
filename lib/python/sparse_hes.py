# -----------------------------------------------------------------------------
#         cppad_py: A C++ Object Library and Python Interface to Cppad
#          Copyright (C) 2017-18 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# -----------------------------------------------------------------------------
# $begin py_sparse_hes$$ $newlinech #$$
# $spell
#	af
#	Jacobian
#	Taylor
#	rcv
#	nr
#	nc
#	const
#	vec
#	rc
#	hes
#	cppad_py
#	numpy
# $$
#
# $section Computing Sparse Hessians$$
#
# $head Syntax$$
# $icode%work% = cppad_py.sparse_hes_work()
# %$$
# $icode%n_sweep% = %af%.sparse_hes(%subset%, %x%, %r%, %pattern%, %work%)
# %$$
#
# $head Purpose$$
# We use $latex F : \B{R}^n \rightarrow \B{R}^m$$ to denote the
# function corresponding to $icode af$$.
# Given a vector $latex r \in \B{R}^m$$, define
# $latex \[
#	H(x) = (r^\R{T} F)^{(2)} ( x )
# \] $$
# This routine takes advantage of sparsity when computing elements
# of the Hessian $latex H(x)$$.
#
# $head af$$
# This object must have been returned by a previous call to the python
# $cref/a_fun/py_a_fun_ctor/$$ constructor.
# Note that the Taylor coefficients stored in $icode af$$ are affected
# by this operation; see
# $cref/uses forward/py_sparse_hes/Uses Forward/$$ below.
#
# $head subset$$
# This argument must have be a $cref/matrix/py_sparse_rcv/matrix/$$
# returned by the $code sparse_rcv$$ constructor.
# Its row size and column size is $icode n$$; i.e.,
# $icode%subset%.nr() == %n%$$ and $icode%subset%.nc() == %n%$$.
# It specifies which elements of the Hessian are computed.
# The input value of its value vector
# $icode%subset%.val()%$$ does not matter.
# Upon return it contains the value of the corresponding elements
# of the Jacobian.
# All of the row, column pairs in $icode subset$$ must also appear in
# $icode pattern$$; i.e., they must be possibly non-zero.
#
# $head x$$
# This argument is a numpy vector with $code float$$ elements
# and size $icode n$$.
# It specifies the point at which to evaluate the Hessian $latex H(x)$$.
#
# $head r$$
# This argument is a numpy vector with $code float$$ elements
# and size $icode m$$.
# It specifies the multiplier for each component of $latex F(x)$$;
# i.e., $latex r_i$$ is the multiplier for $latex F_i (x)$$.
#
# $head pattern$$
# This argument must have be a $cref/pattern/py_sparse_rc/pattern/$$
# returned by the $code sparse_rc$$ constructor.
# Its row size and column sizes are $icode n$$; i.e.,
# $icode%pattern%.nr() == %n%$$ and $icode%pattern%.nc() == %n%$$.
# It is a sparsity pattern for the Hessian $latex H(x)$$.
# This argument is not used (and need not satisfy any conditions),
# when $cref/work/py_sparse_hes/work/$$ is non-empty.
#
# $head work$$
# This argument must have been constructed by the call
# $codei%
#   %work% = cppad_py.sparse_hes_work()
# %$$
# We refer to its initial value,
# and its value after $icode%work%.clear()%$$, as empty.
# If it is empty, information is stored in $icode work$$.
# This can be used to reduce computation when
# a future call is for the same object $icode af$$,
# and the same subset of the Hessian.
# If either of these values change, use $icode%work%.clear()%$$ to
# empty this structure.
#
# $head n_sweep$$
# The return value $icode n_sweep$$ has prototype
# $codei%
#	int %n_sweep%
# %$$
# It is the number of first order forward sweeps
# used to compute the requested Hessian values.
# Each first forward sweep is followed by a second order reverse sweep
# so it is also the number of reverse sweeps.
# This is proportional to the total computational work,
# not counting the zero order forward sweep,
# or combining multiple columns and rows into a single sweep.
#
# $head Uses Forward$$
# After each call to $cref py_a_fun_forward$$,
# the object $icode af$$ contains the corresponding Taylor coefficients
# for all the variables in the operation sequence..
# After a call to $code sparse_hes$$
# the zero order coefficients correspond to
# $codei%
#	%af%.forward(0, %x%)
# %$$
# All the other forward mode coefficients are unspecified.
#
# $children%
#	lib/example/python/sparse_hes_xam.py
# %$$
# $head Example$$
# $cref sparse_hes_xam.py$$
#
# $end
# -----------------------------------------------------------------------------
# undocumented fact: pattern.rc (subset.rcv) is vec_int version of
# sparsity pattern (sparse matrix)
import cppad_py
def a_fun_sparse_hes(af, subset, x, r, pattern, work) :
	"""
	n_sweep = af.sparse_hes(subset, x, r, pattern, work)
	"""
	n       = af.size_domain()
	m       = af.size_range()
	dtype   = float
	syntax  = 'af.sparse_hes(subset, x, r, pattern, work)'
	u       = cppad_py.utility.numpy2vec(x, dtype, n, syntax, 'x')
	v       = cppad_py.utility.numpy2vec(r, dtype, m, syntax, 'r')
	af.sparse_hes(subset.rcv, u, v, pattern.rc, work)
