# -----------------------------------------------------------------------------
#         cppad_py: A C++ Object Library and Python Interface to Cppad
#          Copyright (C) 2017-20 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# -----------------------------------------------------------------------------
# $begin py_fun_hessian$$ $newlinech #$$
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
# This is either a
# $cref/d_fun/py_fun_ctor/Syntax/d_fun/$$ or
# $cref/a_fun/py_fun_ctor/Syntax/a_fun/$$ function object.
# Upon return, the zero order
# $cref/Taylor coefficients/py_fun_forward/Taylor Coefficient/$$
# in $icode f$$ correspond to the value of $icode x$$.
# The other Taylor coefficients in $icode f$$ are unspecified.
#
# $head f(x)$$
# We use the notation $latex f: \B{R}^n \rightarrow \B{R}^m$$
# for the function corresponding to $icode f$$.
# Note that $icode n$$ is the size of $cref/ax/py_fun_ctor/ax/$$
# and $icode m$$ is the size of $cref/ay/py_fun_ctor/ay/$$
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
# If $icode f$$ is a $code d_fun$$ or $code a_fun$$,
# $icode x$$ is a numpy vector with $code float$$ ($code a_double$$) elements
# and size $icode n$$.
# It specifies the argument value at we are computing the Hessian
# $latex g^{(2)}(x)$$.
#
# $head w$$
# If $icode f$$ is a $code d_fun$$ or $code a_fun$$,
# $icode w$$ is a numpy vector with $code float$$ ($code a_double$$) elements
# and size $icode m$$.
# It specifies the vector $icode w$$ in the definition of $latex g(x)$$ above.
#
# $head H$$
# The result is a numpy matrix with $code float$$ ($code a_double$$) elements,
# $icode n$$ rows and $code n$$ columns.
# For $icode i$$ between zero and $icode%n%-1%$$
# and $icode j$$ between zero and $icode%n%-1%$$,
# $latex \[
#	H [ i, j ] = \frac{ \partial^2 g }{ \partial x_i \partial x_j } (x)
# \] $$
#
# $children%
#	example/python/fun_hessian_xam.py
# %$$
# $head Example$$
# $cref fun_hessian_xam.py$$
#
#
# $end
# -----------------------------------------------------------------------------
import cppad_py
import numpy
# -----------------------------------------------------------------------------
# This function is used by hessian in d_fun class to implement syntax above
def d_fun_hessian(f, x, w) :
	"""
	H = f.hessian(x, w)
	computes Hessian of a function corresponding a sum of the components of f
	"""
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
# -----------------------------------------------------------------------------
# This function is used by hessian in d_fun class to implement syntax above
def a_fun_hessian(af, ax, aw) :
	"""
	aH = af.hessian(ax, aw)
	computes Hessian of a function corresponding a sum of the components of af
	"""
	#
	n = af.size_domain()
	m = af.size_range()
	#
	# convert x -> u, w -> v
	dtype    = cppad_py.a_double
	syntax   = 'f.hessian(x, w)'
	au = cppad_py.utility.numpy2vec(ax, dtype, n, syntax, 'ax')
	av = cppad_py.utility.numpy2vec(aw, dtype, m, syntax, 'aw')
	#
	# call hessian
	az =  af.hessian(au, av)
	#
	aH = cppad_py.utility.vec2numpy(az, n, n)
	#
	return aH
