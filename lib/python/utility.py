# -----------------------------------------------------------------------------
#         cppad_py: A C++ Object Library and Python Interface to Cppad
#          Copyright (C) 2017-18 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# -----------------------------------------------------------------------------
# $begin numpy2vec$$ $newlinech #$$
# $spell
#	Numpy
#	cppad_py
#	vec
#	dtype
#	tuple
#	str
# $$
#
# $section Convert a Numpy Array to a cppad_py Vector$$
#
# $head Syntax$$
# $icode%vec% = cppad_py.numpy2vec(
#	%array%, %dtype%, %shape%, %syntax%, %name%
# )%$$
#
# $head array$$
# This is the array that we are converting to a vector.
# If this array does not match the conditions below,
# an exception is raised with an appropriate error message.
#
# $head dtype$$
# This is the expected data type for the elements of the array.
# It must be either $code float$$ or $code cppad_py.a_double$$.
#
# $head shape$$
# This either a $code int$$ or a tuple of $code int$$ with length one or two.
#
# $head syntax$$
# This is the syntax that $icode array$$ appears in.
# It is a $code str$$ that is used for error reporting.
#
# $head name$$
# This is the name used for $icode array$$ in $icode syntax$$.
# It is a $code str$$ that is used for error reporting.
#
# $head vec$$
# This is the values of $icode array$$
# as a vector is row major order.
# It has type $code vec_double$$ if $icode dtype$$ is $code float$$,
# and $code vec_a_double$$ if $icode dtype$$ is $code a_double$$.
#
# $end
# -----------------------------------------------------------------------------
def numpy2vec(array, dtype, shape, syntax, name) :
	import numpy
	import cppad_py
	assert dtype == float or dtype == cppad_py.a_double
	if isinstance(shape, int) :
		shape = (shape, )
	assert len(shape) == 1 or len(shape) == 2
	#
	if not isinstance(array, numpy.ndarray) :
		msg = syntax + ': ' + name + ' is not an numpy.ndarray'
		raise NotImplementedError(msg)
	if not array.dtype == dtype :
		msg = syntax + ': ' + name + '.dtype is not ' + str(dtype)
		raise NotImplementedError(msg)
	#
	if not len(array.shape) == len(shape) :
		msg = syntax + ': len(' + name + '.shape) is not ' + str(len(shape))
	#
	nr = shape[0]
	if array.shape[0] != nr :
		msg = syntax + ': ' + name + '.shape[0] is not ' + str(nr)
	#
	if len(shape) == 1 :
		if dtype == float :
			vec = cppad_py.vec_double(nr)
		else :
			vec = cppad_py.vec_a_double(nr)
		#
		for i in range(nr) :
			vec[i] = array[i]
	else :
		nc = shape[1]
		if array.shape[1] != nc :
			msg = syntax + ': ' + name + '.shape[1] is not ' + str(nc)
		#
		if dtype == float :
			vec = cppad_py.vec_double(nr * nc)
		else :
			vec = cppad_py.vec_a_double(nr * nc)
		#
		for i in range(nr) :
			for j in range(nc):
				vec[i * nc + j] = array[i, j]
	#
	return vec
