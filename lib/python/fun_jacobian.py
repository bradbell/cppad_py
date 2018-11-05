# -----------------------------------------------------------------------------
#         cppad_py: A C++ Object Library and Python Interface to Cppad
#          Copyright (C) 2017-18 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# -----------------------------------------------------------------------------
# $begin py_d_fun_jacobian$$ $newlinech #$$
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
# $head x$$
# This argument is a numpy vector with $code float$$ elements
# and size $icode n$$.
# It specifies the argument value at we are computing the Jacobian
# $latex f'(x)$$.
#
# $head J$$
# The result is a numpy matrix with $code float$$ elements,
# $icode m$$ rows, and $code n$$ columns.
# For $icode i$$ between zero and $icode%m%-1%$$
# and $icode j$$ between zero and $icode%n%-1%$$,
# $latex \[
#	J [ i,  j ] = \frac{ \partial f_i }{ \partial x_j } (x)
# \] $$
#
# $children%
#	lib/example/python/fun_jacobian_xam.py
# %$$
# $head Example$$
# $cref fun_jacobian_xam.py$$
#
# $end
# -----------------------------------------------------------------------------
import cppad_py
import numpy
#
# This function is used by jacobian in d_fun class to implement syntax above
def d_fun_jacobian(f, x) :
	"""
	J = f.jacobian(x)
	computes the Jacobian of the function corresponding to af
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
