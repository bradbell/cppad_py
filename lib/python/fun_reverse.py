# -----------------------------------------------------------------------------
#         cppad_py: A C++ Object Library and Python Interface to Cppad
#          Copyright (C) 2017-18 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# -----------------------------------------------------------------------------
# $begin py_d_fun_reverse$$ $newlinech #$$
# $spell
#	vec
#	xq
#	Taylor
#	yq
#	numpy
# $$
#
# $section Reverse Mode AD$$
#
# $head Syntax$$
# $icode%xq% = %f%.reverse(%q%, %yq%)%$$
#
# $head f$$
# This object must have been returned by a previous call to the python
# $cref/d_fun/py_d_fun_ctor/$$ constructor.
# Note that it is effectively constant; i.e., not changed.
#
# $head Notation$$
#
# $subhead f(x)$$
# We use the notation $latex f: \B{R}^n \rightarrow \B{R}^m$$
# for the function corresponding to $icode f$$.
# Note that $icode n$$ is the size of $cref/ax/py_d_fun_ctor/ax/$$
# and $icode m$$ is the size of $cref/ay/py_d_fun_ctor/ay/$$
# in to the constructor for $icode f$$.
#
# $subhead X(t), S$$
# This is the same function as
# $cref/X(t)/py_d_fun_forward/X(t)/$$ in the previous call to
# $icode%f%.forward%$$.
# We use $latex S \in \B{R}^{n \times q}$$ to denote the Taylor coefficients
# of $latex X(t)$$.
#
# $subhead Y(t), T$$
# This is the same function as
# $cref/Y(t)/py_d_fun_forward/Y(t)/$$ in the previous call to
# $icode%f%.forward%$$.
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
# the number of Taylor coefficient stored in $icode f$$; i.e.,
# $cref/f.size_order()/py_d_fun_property/size_order/$$.
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
#	lib/example/python/fun_reverse_xam.py
# %$$
# $head Example$$
# $cref fun_reverse_xam.py$$
#
# $end
# -----------------------------------------------------------------------------
import cppad_py
import numpy
#
# This function is used by reverse in d_fun class to implement syntax above
def d_fun_reverse(f, q, yq) :
	"""
	xq = f.reverse(q, yq)
	given Taylor coefficients for X(t), compute Taylor coefficients for
	Y(t) = f(X(t)).
	"""
	#
	n = f.size_domain()
	m = f.size_range()
	#
	# convert yq -> u
	dtype    = float
	shape    = (m, q)
	syntax   = 'f.reverse(q, yq)'
	u = cppad_py.utility.numpy2vec(yq, dtype, shape, syntax, 'yq')
	#
	# call reverse
	v =  f.reverse(q, u)
	#
	# convert v -> xp
	xq = cppad_py.utility.vec2numpy(v, n, q)
	#
	return xq
