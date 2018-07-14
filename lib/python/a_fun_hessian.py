# -----------------------------------------------------------------------------
#         cppad_py: A C++ Object Library and Python Interface to Cppad
#          Copyright (C) 2017-18 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# -----------------------------------------------------------------------------
# $begin py_a_fun_hessian$$ $newlinech #$$
# $spell
#	vec
#	af
#	Taylor
#	const
#	numpy
# $$
#
# $section Hessian of an AD Function$$
#
# $head Syntax$$
# $icode%H% = %af%.hessian(%x%, %w%)%$$
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
# Note that $icode n$$ is the size of $cref/ax/cpp_a_fun_ctor/ax/$$
# and $icode m$$ is the size of $cref/ay/cpp_a_fun_ctor/ay/$$
# in to the constructor for $icode af$$.
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
#	lib/example/python/a_fun_hessian_xam.py
# %$$
# $head Example$$
# $cref a_fun_hessian_xam.py$$
#
#
# $end
# -----------------------------------------------------------------------------
import cppad_py
import numpy
#
# This function is used by hessian in a_fun class to implement syntax above
def a_fun_hessian(af, x, w) :
	"""
	H = af.hessian(x)
	computes Hessian of a function corresponding a sum of the components of af
	"""
	from cppad_py import vec_double as vec_double
	# convert x -> u, w -> v
	if isinstance(x, vec_double) and isinstance(w, vec_double) :
		is_numpy = False
		u        = x
		v        = w
		n        = x.size()
		m        = w.size()
	elif isinstance(x, numpy.ndarray) and isinstance(w, numpy.ndarray) :
		is_numpy =  True
		if( len( x.shape ) != 1 ) or len( w.shape ) != 1 :
			msg = 'af.hessian(x): numpy array x is not a vector'
			raise NotImplementedError(msg)
		n = x.size
		u = cppad_py.vec_double(n)
		for i in range(n) :
			u[i] = x[i]
		m = w.size
		v = cppad_py.vec_double(m)
		for i in range(m) :
			v[i] = w[i]
	else :
		msg = 'af.hessian(x, w): arguments not both vec_double or numpy vectors'
		raise NotImplementedError(msg)
	if n != af.size_domain() :
		msg = 'af.hessian(x, w): size of vector x is not equal af.size_domain()'
		raise NotImplementedError(msg)
	if m != af.size_range() :
		msg = 'af.hessian(x, w): size of vector w is not equal af.size_range()'
		raise NotImplementedError(msg)
	#
	# call hessian
	z =  af.hessian(u, v)
	#
	# convert v -> J
	if not is_numpy :
		H = z
	else :
		H = numpy.zeros((n, n), dtype = float)
		for i in range(n) :
			for j in range(n) :
				# must a copy because av will be deleted
				H[i, j] = z[i * n + j]
	return H
