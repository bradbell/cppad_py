# -----------------------------------------------------------------------------
#         cppad_py: A C++ Object Library and Python Interface to Cppad
#          Copyright (C) 2017-20 Bradley M. Bell (bradbell@seanet.com)
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
#	adynamic
#	nx
#	nd
# $$
#
# $section Declare Independent Variables and Start Recording$$
#
# $head Syntax$$
# $icode%ax% = cppad_py.independent(%x%)
# %$$
# $codei%(%ax%, %adynamic)% = cppad_py.independent(%x%, %dynamic%)
# %$$
#
# $head x$$
# This argument is a numpy vector with $code float$$ elements.
# It specifies the number of independent variables
# and their values during the recording.
# We use $icode%nx% = %x%.size%$$
# to denote the number of independent variables.
#
# $head dynamic$$
# This argument is a numpy vector with $code float$$ elements.
# It specifies the number of independent dynamic parameters
# and their values during the recording.
# We use $icode%nd% = %dynamic%.size%$$
# to denote the number of independent dynamic parameters.
#
# $head ax$$
# This result is a numpy vector with $code a_double$$ elements.
# This is the vector of independent variables.
# It has size $icode nx$$ and for
# $icode%i% = 0%$$ to $icode%n%-1%$$
# $codei%
#	%ax%[%i%].value() == %x%[%i%]
# %$$
#
# $head adynamic$$
# This result is a numpy vector with $code a_double$$ elements.
# This is the vector of independent dynamic parameters.
# It has size $icode nd$$ and for
# $icode%i% = 0%$$ to $icode%n%-1%$$
# $codei%
#	%adynamic%[%i%].value() == %dynamic%[%i%]
# %$$
#
# $head Purpose$$
# This starts a recording of the $cref a_double$$ operations.
# This recording is terminated, and the information is stored,
# by calling the $cref/d_fun constructor/py_fun_ctor/$$.
# It is terminated, and the information is lost,
# by calling $cref/abort_recording/py_abort_recording/$$.
#
# $children%
#	example/python/core/fun_dynamic_xam.py
# %$$
# $head Example$$
# Most of the python $code d_fun$$ examples use this function.
# The $cref fun_dynamic_xam.py$$ uses the syntax that includes
# dynamic parameters.
#
# $end
# -----------------------------------------------------------------------------
# BEGIN_INDEPENDENT_SOURCE
import cppad_py
import numpy
def independent(x, dynamic = None) :
	"""
	ax = independent(x)
	creates the indepedent numpy vector ax, with value equal numpy vector x,
	and starts recording a_double operations.
	"""
	# convert x -> u
	dtype    = float
	#
	nx = x.size
	if dynamic is None :
		syntax   = 'independent(x)'
		u = cppad_py.utility.numpy2vec(x, dtype, nx, syntax, 'x')
		av = cppad_py.swig.independent(u)
		ax = cppad_py.utility.vec2numpy(av, av.size());
		return ax
	#
	nd       = dynamic.size
	syntax   = 'independent(x, dynamic)'
	u = cppad_py.utility.numpy2vec(x, dtype, nx, syntax, 'x')
	v = cppad_py.utility.numpy2vec(dynamic, dtype, nd, syntax, 'dynamic')
	a_both   = cppad_py.swig.independent(u, v)
	ax       = numpy.empty(nx,       dtype=cppad_py.a_double)
	adynamic = numpy.empty(nd, dtype=cppad_py.a_double)
	# use copy constructor so a separate copy is made for numpy arrays
	for i in range(nx) :
		ax[i] = cppad_py.a_double( a_both[i] )
	for i in range(nd) :
		adynamic[i] = cppad_py.a_double( a_both[nx + i] )
	#
	return (ax, adynamic)
# END_INDEPENDENT_SOURCE
