# -----------------------------------------------------------------------------
#         cppad_py: A C++ Object Library and Python Interface to Cppad
#          Copyright (C) 2017-18 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# -----------------------------------------------------------------------------
# $begin py_a_fun_jacobian$$ $newlinech #$$
# $spell
#	vec
#	af
#	Taylor
#	Jacobian
#	numpy
# $$
#
# $section Jacobian of an AD Function$$
#
# $head Syntax$$
# $icode%J% = %af%.jacobian(%x%)%$$
#
# $head af$$
# This object must have been returned by a previous call to the python
# $cref/a_fun/py_a_fun_ctor/$$ constructor.
# Note that its state is changed by this operation.
# The zero order
# $cref/Taylor coefficients/py_a_fun_forward/Taylor Coefficient/$$
# in $icode af$$ correspond to the value of $icode x$$.
# The other Taylor coefficients in $icode af$$ are unspecified.
#
# $head f(x)$$
# We use the notation $latex f: \B{R}^n \rightarrow \B{R}^m$$
# for the function corresponding to $icode af$$.
# Note that $icode n$$ is the size of $cref/ax/py_a_fun_ctor/ax/$$
# and $icode m$$ is the size of $cref/ay/py_a_fun_ctor/ay/$$
# in to the constructor for $icode af$$.
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
#	lib/example/python/a_fun_jacobian_xam.py
# %$$
# $head Example$$
# $cref a_fun_jacobian_xam.py$$
#
# $end
# -----------------------------------------------------------------------------
import cppad_py
import numpy
#
# This function is used by jacobian in a_fun class to implement syntax above
def a_fun_jacobian(af, x) :
	"""
	J = af.jacobian(x)
	computes the Jacobian of the function corresponding to af
	"""
	#
	n = af.size_domain()
	m = af.size_range()
	#
	# convert x -> u
	if isinstance(x, cppad_py.vec_double) :
		is_numpy = False
		u        = x
		assert x.size() == n
	else :
		is_numpy = True
		dtype    = float
		syntax   = 'af.jacobian(x)'
		u = cppad_py.utility.numpy2vec(x, dtype, n, syntax, 'x')
	# call jacobian
	v =  af.jacobian(u)
	#
	# convert v -> J
	if not is_numpy :
		J = v
	else :
		J = cppad_py.utility.vec2numpy(v, m, n)
	#
	return J
