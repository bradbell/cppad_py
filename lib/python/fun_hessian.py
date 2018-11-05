# -----------------------------------------------------------------------------
#         cppad_py: A C++ Object Library and Python Interface to Cppad
#          Copyright (C) 2017-18 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# -----------------------------------------------------------------------------
# $begin py_d_fun_hessian$$ $newlinech #$$
# $spell
#	vec
#	Taylor
#	const
#	numpy
# $$
#
# $section Hessian of an AD Function$$
#
# $head Syntax$$
# $icode%H% = %f%.hessian(%x%, %w%)%$$
#
# $head f$$
# This object must have been returned by a previous call to the python
# $cref/d_fun/py_d_fun_ctor/$$ constructor.
# Note that its state is changed by this operation.
# The zero order
# $cref/Taylor coefficients/py_d_fun_forward/Taylor Coefficient/$$
# in $icode f$$ correspond to the value of $icode x$$.
# The other Taylor coefficients in $icode f$$ are unspecified.
#
# $head f(x)$$
# We use the notation $latex f: \B{R}^n \rightarrow \B{R}^m$$
# for the function corresponding to $icode f$$.
# Note that $icode n$$ is the size of $cref/ax/py_d_fun_ctor/ax/$$
# and $icode m$$ is the size of $cref/ay/py_d_fun_ctor/ay/$$
# in to the constructor for $icode f$$.
#
# $head g(x)$$
# We use the notation $latex g: \B{R}^n \rightarrow \B{R}$$
# for the function defined by
# $latex \[
#	g(x) = \sum_{i=0}^{n-1} w_i f_i (x)
# \] $$
#
# $head x$$
# This argument is a numpy vector with $code float$$ elements
# and size $icode n$$.
# It specifies the argument value at we are computing the Hessian
# $latex g^{(2)}(x)$$.
#
# $head w$$
# This argument is a numpy vector with $code float$$ elements
# and size $icode m$$.
# It specifies the vector $icode w$$ in the definition of $latex g(x)$$ above.
#
# $head H$$
# The result is a numpy matrix with $code float$$ elements,
# $icode n$$ rows and $code n$$ columns.
# For $icode i$$ between zero and $icode%n%-1%$$
# and $icode j$$ between zero and $icode%n%-1%$$,
# $latex \[
#	H [ i, j ] = \frac{ \partial^2 g }{ \partial x_i \partial x_j } (x)
# \] $$
#
#
# $children%
#	lib/example/python/fun_hessian_xam.py
# %$$
# $head Example$$
# $cref fun_hessian_xam.py$$
#
#
# $end
# -----------------------------------------------------------------------------
import cppad_py
import numpy
#
# This function is used by hessian in d_fun class to implement syntax above
def d_fun_hessian(f, x, w) :
	"""
	H = f.hessian(x, w)
	computes Hessian of a function corresponding a sum of the components of af
	"""
	from cppad_py import vec_double as vec_double
	#
	n = f.size_domain()
	m = f.size_range()
	#
	# convert x -> u, w -> v
	dtype    = float
	syntax   = 'f.hessian(x, w)'
	u = cppad_py.utility.numpy2vec(x, dtype, n, syntax, 'x')
	v = cppad_py.utility.numpy2vec(w, dtype, m, syntax, 'w')
	#
	# call hessian
	z =  f.hessian(u, v)
	#
	H = cppad_py.utility.vec2numpy(z, n, n)
	#
	return H
