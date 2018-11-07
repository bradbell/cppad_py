# -----------------------------------------------------------------------------
#         cppad_py: A C++ Object Library and Python Interface to Cppad
#          Copyright (C) 2017-18 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# -----------------------------------------------------------------------------
# $begin py_fun_forward$$ $newlinech #$$
# $spell
#	vec
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
# $icode%yp% = %f%.forward(%p%, %xp%)%$$
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
# $head f$$
# This is either a
# $cref/d_fun/py_fun_ctor/Syntax/d_fun/$$ or
# $cref/a_fun/py_fun_ctor/Syntax/a_fun/$$ function object.
# Note that its state is changed by this operation because
# all the Taylor coefficient that it calculates for every
# variable in recording are stored.
# See more discussion of this fact under the heading
# $cref/p/py_fun_forward/p/$$ below.
#
# $head f(x)$$
# We use the notation $latex f: \B{R}^n \rightarrow \B{R}^m$$
# for the function corresponding to $icode f$$.
# Note that $icode n$$ is the size of $cref/ax/py_fun_ctor/ax/$$
# and $icode m$$ is the size of $cref/ay/py_fun_ctor/ay/$$
# in to the constructor for $icode f$$.
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
# If there was no call to $code forward$$ for this $icode f$$,
# the value of $icode p$$ must be zero.
# Otherwise, it must be between zero and one greater that its
# value for the previous call using this $icode f$$.
# After this call, the Taylor coefficients for orders zero though $icode p$$,
# and for every variable in the recording, will be stored in $icode f$$.
#
# $subhead size_order$$
# After this call,
# $cref/f.size_order()/py_fun_property/size_order/$$ is $icode%p%+1%$$.
#
# $head xp$$
# If $icode f$$ is a $code d_fun$$ ($code a_fun$$) object, $icode xp$$
# is a numpy vector with $code float$$ ($code a_double$$) elements
# and size $icode n$$.
# It specifies the $th p$$ order Taylor coefficients for $icode X(t)$$.
#
# $head yp$$
# The result is a numpy vector with $code float$$ ($code a_double$$) elements
# and size $icode m$$.
# It is the $th p$$ order Taylor coefficients for $latex Y(t)$$.
#
# $children%
#	lib/example/python/fun_forward_xam.py
# %$$
# $head Example$$
# $cref fun_forward_xam.py$$
#
# $end
# -----------------------------------------------------------------------------
import cppad_py
import numpy
# ----------------------------------------------------------------------------
# This function is used by forward in d_fun class to implement syntax above
def d_fun_forward(f, p, xp) :
	"""
	yp = f.forward(p, xp)
	given Taylor coefficients for X(t), compute Taylor coefficients for
	Y(t) = f(X(t)).
	"""
	#
	n = f.size_domain()
	m = f.size_range()
	#
	# convert x -> u
	dtype    = float
	syntax   = 'f.forward(p, xp)'
	u = cppad_py.utility.numpy2vec(xp, dtype, n, syntax, 'xp')
	#
	# call forward
	v =  f.forward(p, u)
	#
	# convert v -> yp
	yp = cppad_py.utility.vec2numpy(v, m)
	#
	return yp
# ----------------------------------------------------------------------------
# This function is used by forward in a_fun class to implement syntax above
def a_fun_forward(af, p, axp) :
	"""
	ayp = af.forward(p, axp)
	given Taylor coefficients for X(t), compute Taylor coefficients for
	Y(t) = f(X(t)).
	"""
	#
	n = af.size_domain()
	m = af.size_range()
	#
	# convert x -> u
	dtype    = cppad_py.a_double
	syntax   = 'af.forward(p, axp)'
	au = cppad_py.utility.numpy2vec(axp, dtype, n, syntax, 'axp')
	#
	# call forward
	av =  af.forward(p, au)
	#
	# convert av -> ayp
	ayp = cppad_py.utility.vec2numpy(av, m)
	#
	return ayp
