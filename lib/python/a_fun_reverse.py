# -----------------------------------------------------------------------------
#         cppad_py: A C++ Object Library and Python Interface to Cppad
#          Copyright (C) 2017-18 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# -----------------------------------------------------------------------------
# $begin py_a_fun_reverse$$ $newlinech #$$
# $spell
#	vec
#	af
#	xq
#	Taylor
#	yq
#	numpy
# $$
#
# $section Reverse Mode AD$$
#
# $head Syntax$$
# $icode%xq% = %af%.reverse(%q%, %yq%)%$$
#
# $head af$$
# This object must have been returned by a previous call to the python
# $cref/a_fun/py_a_fun_ctor/$$ constructor.
# Note that it is effectively constant; i.e., not changed.
#
# $head Notation$$
#
# $subhead f(x)$$
# We use the notation $latex f: \B{R}^n \rightarrow \B{R}^m$$
# for the function corresponding to $icode af$$.
# Note that $icode n$$ is the size of $cref/ax/py_a_fun_ctor/ax/$$
# and $icode m$$ is the size of $cref/ay/py_a_fun_ctor/ay/$$
# in to the constructor for $icode af$$.
#
# $subhead X(t), S$$
# This is the same function as
# $cref/X(t)/py_a_fun_forward/X(t)/$$ in the previous call to
# $icode%af%.forward%$$.
# We use $latex S \in \B{R}^{n \times q}$$ to denote the Taylor coefficients
# of $latex X(t)$$.
#
# $subhead Y(t), T$$
# This is the same function as
# $cref/Y(t)/py_a_fun_forward/Y(t)/$$ in the previous call to
# $icode%af%.forward%$$.
# We use $latex T \in \B{R}^{m \times q}$$ to denote the Taylor coefficients
# of $latex Y(t)$$.
# We also use the notation $latex T(S)$$ to express the fact that
# the Taylor coefficients for $latex Y(t)$$ are a function of the
# Taylor coefficients of $latex X(t)$$.
#
# $subhead G(T)$$
# We use the notation $latex G : \B{R}^{m \times p} \rightarrow \B{R}$$
# for a function that the calling routine chooses.
#
# $head q$$
# This argument has type $code int$$ and is positive.
# It is the number of the Taylor coefficient (for each variable)
# that we are computing the derivative with respect to.
# It must be greater than zero, and less than or equal
# the number of Taylor coefficient stored in $icode af$$; i.e.,
# $cref/af.size_order()/py_a_fun_property/size_order/$$.
#
# $head yq$$
# This argument is a numpy matrix with $code float$$ elements,
# $icode m$$ rows and $icode q$$ columns.
# For $icode%0% <= %i% < %m%$$ and $icode%0% <= %k% < %q%$$,
# $icode%yq%[ %i%, %k% ]%$$ is the partial derivative of
# $latex G(T)$$ with respect to the $th k$$ order Taylor coefficient
# for the $th i$$ component function; i.e.,
# the partial derivative of $latex G(T)$$ w.r.t. $latex Y_i^{(k)} (t) / k !$$.
#
# $head xq$$
# The result is a numpy matrix with $code float$$ elements,
# $icode n$$ rows and $icode q$$ columns.
# For $icode%0% <= %j% < %n%$$ and $icode%0% <= %k% < %q%$$,
# $icode%yq%[ %j%, %k% ]%$$ is the partial derivative of
# $latex G(T(S))$$ with respect to the $th k$$ order Taylor coefficient
# for the $th j$$ component function; i.e.,
# the partial derivative of
# $latex G(T(S))$$ w.r.t. $latex S_j^{(k)} (t) / k !$$.
#
# $children%
#	lib/example/python/a_fun_reverse_xam.py
# %$$
# $head Example$$
# $cref a_fun_reverse_xam.py$$
#
# $end
# -----------------------------------------------------------------------------
import cppad_py
import numpy
#
# This function is used by reverse in a_fun class to implement syntax above
def a_fun_reverse(af, q, yq) :
	"""
	xq = af.reverse(q, yq)
	given Taylor coefficients for X(t), compute Taylor coefficients for
	Y(t) = f(X(t)).
	"""
	#
	n = af.size_domain()
	m = af.size_range()
	#
	# convert yq -> u
	if isinstance(yq, cppad_py.vec_double) :
		is_numpy = False
		u        = yq
		mq       = yq.size()
	else :
		is_numpy =  True
		dtype    = float
		shape    = (m, q)
		syntax   = 'af.reverse(q, yq)'
		u        = cppad_py.numpy2vec(yq, dtype, shape, syntax, 'yq')
	#
	# call reverse
	v =  af.reverse(q, u)
	#
	# convert v -> xq
	if not is_numpy :
		xq = v
	else :
		n  = af.size_domain()
		xq = numpy.empty((n, q), dtype = float)
		for j in range(n) :
			for k in range(q) :
				# do not need a copy because float is not mutable
				xq[j, k] = v[j * q + k]
	return xq
