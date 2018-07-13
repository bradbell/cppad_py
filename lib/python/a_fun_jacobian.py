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
#	const
#	Jacobian
#	numpy
# $$
#
# $section Jacobian of an AD Function$$
# $spell
#	vec
# $$
#
# $head Syntax$$
# $icode%J% = %af%.jacobian(%x%)%$$
#
# $head af$$
# This object must have been returned by a previous call to the python
# $cref/a_fun/py_a_fun_ctor/$$ constructor.
# Note that its state is changed by this operation.
# The zero order
# $cref/Taylor coefficients/a_fun_forward/Taylor Coefficient/$$ in $icode af$$
# correspond to the value of $icode x$$.
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
	# convert x -> v
	if isinstance(x, cppad_py.vec_double) :
		is_numpy = False
		v        = x
		n        = x.size()
	elif isinstance(x, numpy.ndarray) :
		is_numpy =  True
		if( len( x.shape ) != 1 ) :
			msg = 'independent(x): numpy array x is not a vector'
			raise NotImplementedError(msg)
		n = x.size
		v = cppad_py.vec_double(n)
		for i in range(n) :
			v[i] = x[i]
	else :
		msg = 'af.jacobian(x): x is not a vec_double or numpy vector'
		raise NotImplementedError(msg)
	if n != af.size_domain() :
		msg = 'af.jacobian(x): size of vector x is not equal af.size_domain()'
		raise NotImplementedError(msg)
	#
	# call jacobian
	v =  af.jacobian(v)
	#
	# convert v -> J
	if not is_numpy :
		J = v
	else :
		m = af.size_range()
		J = numpy.zeros((m, n), dtype = float)
		for i in range(m) :
			for j in range(n) :
				# must a copy because av will be deleted at end of independent
				J[i, j] = v[i * n + j]
	return J
