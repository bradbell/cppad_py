# -----------------------------------------------------------------------------
#         cppad_py: A C++ Object Library and Python Interface to Cppad
#          Copyright (C) 2017-20 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# -----------------------------------------------------------------------------
# $begin py_fun_jacobian$$ $newlinech #$$
# $spell
#	vec
#	Taylor
#	Jacobian
#	numpy
# $$
#
# $section Jacobian of an AD Function$$
#
# $head Syntax$$
# $icode%J% = %f%.jacobian(%x%)%$$
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
# $head x$$
# If $icode f$$ is a $code d_fun$$ or $code a_fun$$,
# $icode x$$ is a numpy vector with $code float$$ ($code a_double$$) elements
# and size $icode n$$.
# It specifies the argument value at we are computing the Jacobian
# $latex f'(x)$$.
#
# $head J$$
# The result is a numpy matrix with $code float$$ ($code a_double$$) elements,
# $icode m$$ rows, and $code n$$ columns.
# For $icode i$$ between zero and $icode%m%-1%$$
# and $icode j$$ between zero and $icode%n%-1%$$,
# $latex \[
#	J [ i,  j ] = \frac{ \partial f_i }{ \partial x_j } (x)
# \] $$
#
# $children%
#	example/python/core/fun_jacobian_xam.py
# %$$
# $head Example$$
# $cref fun_jacobian_xam.py$$
#
# $end
# -----------------------------------------------------------------------------
import cppad_py
import numpy
# ----------------------------------------------------------------------------
# This function is used by jacobian in d_fun class to implement syntax above
def d_fun_jacobian(f, x) :
	"""
	J = f.jacobian(x)
	computes the Jacobian of the function corresponding to f
	"""
	#
	n = f.size_domain()
	m = f.size_range()
	#
	# convert x -> u
	dtype    = float
	syntax   = 'f.jacobian(x)'
	u = cppad_py.utility.numpy2vec(x, dtype, n, syntax, 'x')
	#
	# call jacobian
	v =  f.jacobian(u)
	#
	# convert v -> J
	J = cppad_py.utility.vec2numpy(v, m, n)
	#
	return J
# ----------------------------------------------------------------------------
# This function is used by jacobian in a_fun class to implement syntax above
def a_fun_jacobian(af, ax) :
	"""
	aJ = af.jacobian(ax)
	computes the Jacobian of the function corresponding to af
	"""
	#
	n = af.size_domain()
	m = af.size_range()
	#
	# convert x -> u
	dtype    = cppad_py.a_double
	syntax   = 'af.jacobian(ax)'
	au = cppad_py.utility.numpy2vec(ax, dtype, n, syntax, 'ax')
	#
	# call jacobian
	av =  af.jacobian(au)
	#
	# convert v -> J
	aJ = cppad_py.utility.vec2numpy(av, m, n)
	#
	return aJ
