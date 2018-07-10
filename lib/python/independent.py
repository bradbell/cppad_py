# -----------------------------------------------------------------------------
#         cppad_py: A C++ Object Library and Python Interface to Cppad
#          Copyright (C) 2017-18 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# -----------------------------------------------------------------------------
# initialize cppad_py
# -----------------------------------------------------------------------------
# $begin py_independent$$ $newlinech #$$
# $spell
#	numpy
#	cppad_py
# $$
#
# $section Declare Independent Variables and Start Recording$$
#
# $head Syntax$$
# $icode%ax% = cppad_py.independent(%x%)%$$
#
# $head x$$
# This argument is a numpy vector will elements that
# correspond to c++ $code double$$.
# Its specifies the number of independent variables
# and their values during the recording.
# We use $icode%n% = %x%.size%$$
# to denote the number of independent variables.
#
# $head ax$$
# The result is a numpy vector will elements that
# correspond to c++ $code a_double$$.
# This is the vector of independent variables.
# It has size $icode n$$ and for
# $icode%i% = 0%$$ to $icode%n%-1%$$
# $codei%
#	%ax%[%i%].value() == %x%[%i%]
# %$$
#
# $head Purpose$$
# This starts a recording of the $cref a_double$$ operations.
# This recording is terminated, and the information is stored,
# by calling the $cref/a_fun constructor/a_fun_ctor/$$.
# It is terminated, and the information is lost,
# by calling $cref abort_recording$$.
#
# $head Example$$
# All of the python $code a_fun$$ examples use this function.
#
# $end
import cppad_py
import numpy

def independent(x) :
	import cppad_py
	"""
	ax = independent(x)
	creates the indepedent numpy vector ax, with value equal numpy vector x,
	and starts recording a_double operations.
	"""
	# convert x -> v
	if isinstance(x, cppad_py.vec_double) :
		is_numpy = False
		v        = x
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
		msg = 'independent(x): x is not a vec_double or numpy vector'
		raise NotImplementedError(msg)
	#
	# call independent
	av =  cppad_py.cppad_py_swig.independent(v)
	#
	# convert av -> ax
	if not is_numpy :
		ax = av
	else :
		ax = numpy.zeros(n, dtype = cppad_py.a_double)
		for i in range(n) :
			# must make a copy because av will be deleted at end of independent
			ax[i] = cppad_py.a_double( av[i] )
	#
	return ax
