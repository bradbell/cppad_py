# -----------------------------------------------------------------------------
#         cppad_py: A C++ Object Library and Python Interface to Cppad
#          Copyright (C) 2017-18 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# -----------------------------------------------------------------------------
# $begin py_a_fun_forward$$ $newlinech #$$
# $spell
#	vec
#	af
#	xp
#	Taylor
#	yp
#	xp
#	numpy
# $$
#
# $section Forward Mode AD$$
#
# $head Syntax$$
# $icode%yp% = %af%.forward(%p%, %xp%)%$$
#
# $head Taylor Coefficient$$
# For a function $latex g(t)$$ of a scalar argument $latex t \in \B{R}$$,
# the $th p$$ order Taylor coefficient is its
# $code p$$-th order derivative divided by $icode p$$ factorial
# and evaluated at $latex t = 0$$; i.e.,
# $latex \[
#	g^{(p)} (0) /  p !
# \]$$
#
# $head af$$
# This object must have been returned by a previous call to the python
# $cref/a_fun/py_a_fun_ctor/$$ constructor.
# Note that its state is changed by this operation because
# all the Taylor coefficient that it calculates for every
# variable in recording are stored.
# See more discussion of this fact under the heading
# $cref/p/py_a_fun_forward/p/$$ below.
#
# $head f(x)$$
# We use the notation $latex f: \B{R}^n \rightarrow \B{R}^m$$
# for the function corresponding to $icode af$$.
# Note that $icode n$$ is the size of $cref/ax/cpp_a_fun_ctor/ax/$$
# and $icode m$$ is the size of $cref/ay/cpp_a_fun_ctor/ay/$$
# in to the constructor for $icode af$$.
#
# $head X(t)$$
# We use the notation $latex X : \B{R} \rightarrow \B{R}^n$$
# for a function that the calling routine chooses.
#
# $head Y(t)$$
# We define the function $latex Y : \B{R} \rightarrow \B{R}^n$$
# by $latex Y(t) = f(X(t))$$.
#
# $head p$$
# This argument has type $code int$$ and is non-negative.
# Its value is the order of the Taylor coefficient being calculated.
# If there was no call to $code forward$$ for this $icode af$$,
# the value of $icode p$$ must be zero.
# Otherwise, it must be between zero and one greater that its
# value for the previous call using this $icode af$$.
# After this call, the Taylor coefficients for orders zero though $icode p$$,
# and for every variable in the recording, will be stored in $icode af$$.
#
# $subhead size_order$$
# After this call,
# $cref/af.size_order()/py_a_fun_property/size_order/$$ is $icode%p%+1%$$.
#
# $head xp$$
# This argument is a numpy vector with $code float$$ elements
# and size $icode n$$.
# It specifies the $th p$$ order Taylor coefficients for $icode X(t)$$.
#
# $head yp$$
# The result is a numpy vector with $code float$$ elements
# and size $icode m$$.
# It is the $th p$$ order Taylor coefficients for $latex Y(t)$$.
#
# $children%
#	lib/example/python/a_fun_forward_xam.py
# %$$
# $head Example$$
# $cref a_fun_forward_xam.py$$
#
#
# $end
# -----------------------------------------------------------------------------
import cppad_py
import numpy
#
# This function is used by forward in a_fun class to implement syntax above
def a_fun_forward(af, p, xp) :
	"""
	yp = af.forward(p, xp)
	given Taylor coefficients for X(t), compute Taylor coefficients for
	Y(t) = f(X(t)).
	"""
	#
	n = af.size_domain()
	m = af.size_range()
	#
	# convert x -> u
	if isinstance(xp, cppad_py.vec_double) :
		is_numpy = False
		u        = xp
		assert xp.size() == n
	else :
		is_numpy =  True
		dtype    = float
		syntax   = 'af.forward(p, xp)'
		u        = cppad_py.numpy2vec(xp, dtype, n, syntax, 'xp')
	#
	# call forward
	v =  af.forward(p, u)
	#
	# convert v -> yp
	if not is_numpy :
		yp = v
	else :
		m  = af.size_range()
		yp = numpy.empty(m, dtype = float)
		for i in range(m) :
			# do not need a copy because float is not mutable
			yp[i] = v[i]
	return yp
