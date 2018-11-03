# -----------------------------------------------------------------------------
#         cppad_py: A C++ Object Library and Python Interface to Cppad
#          Copyright (C) 2017-18 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# -----------------------------------------------------------------------------
# $begin py_a_fun_objective$$ $newlinech #$$
# $spell
#	vec
#	af
#	Taylor
#	Objective
#	numpy
# $$
#
# $section Objective of an AD Function$$
#
# $head Syntax$$
# $icode%J% = %af%.objective(%x%)%$$
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
# It specifies the argument value at we are computing the Objective
# $latex f(x)$$.
#
# $head O$$
# The result is a numpy matrix with $code float$$ elements,
# $icode m$$ rows.
#
# $children%
#	lib/example/python/a_fun_objective_xam.py
# %$$
# $head Example$$
# $cref a_fun_objective_xam.py$$
#
# $end
# -----------------------------------------------------------------------------
import cppad_py
import numpy
#
# This function is used by jacobian in a_fun class to implement syntax above
def a_fun_objective(af, x) :
	"""
	J = af.objective(x)
	computes the Objective of the function corresponding to af
	"""
	#
	n = af.size_domain()
	m = af.size_range()
	#
	# convert x -> u
	dtype    = float
	syntax   = 'af.objective(x)'
	u = cppad_py.utility.numpy2vec(x, dtype, n, syntax, 'x')
	#
	# call jacobian
	v =  af.objective(u)
	#
	# convert v -> J
	O = cppad_py.utility.vec2numpy(v, m)
	#
	return O
