# -----------------------------------------------------------------------------
#         cppad_py: A C++ Object Library and Python Interface to Cppad
#          Copyright (C) 2017-20 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# -----------------------------------------------------------------------------
# $begin py_fun_ctor$$ $newlinech #$$
# $spell
#	cppad_py
#	numpy
#	af
#	Taylor
# $$
#
# $section Stop Current Recording and Store Function Object$$
#
# $head Syntax$$
#
# $subhead d_fun$$
# $icode%f% = cppad_py.d_fun(%ax%, %ay%)
# %$$
#
# $subhead a_fun$$
# $icode%af% = cppad_py.a_fun(%f%)
# %$$
#
# $head ax$$
# This argument must be the same as
# $cref/ax/py_independent/ax/$$
# returned by the previous call to $code independent$$; i.e.,
# it must be the independent variable vector.
# We use $icode%n%$$
# to denote the number of independent variables (the size of $icode ax$$).
#
# $head ay$$
# This argument is a numpy array with $code a_double$$ elements.
# It specifies the dependent variables.
# We use $icode m$$
# to denote the number of dependent variables (the size of $icode ay$$).
#
# $head f$$
# This result is a function object that
# has a representation for the floating point operations
# that mapped the independent variables to the dependent variables.
# This object computes function and derivative values using
# $code double$$
#
# $head af$$
# This result is a function object that
# has a representation for the same function as $icode f$$.
# This object computes function and derivative values using
# $code a_double$$
# Initially, there are not Taylor coefficient stored in $icode af$$; i.e.,
# $cref/af.size_order()/py_fun_property/size_order/$$ is zero.
#
# $children%
#	example/python/a_fun_xam.py
# %$$
# $head Example$$
# All of the examples use the $code d_fun$$ constructor.
# The example $cref a_fun_xam.py$$ demonstrates the purpose of
# $code a_fun$$ objects.
#
# $end
# -----------------------------------------------------------------------------
import numpy
import cppad_py
#
# This function is used by __init__ in d_fun class to implement syntax above:
def d_fun_ctor(ax, ay) :
	"""
	d_fun(ax, ay)
	Stop recording a_double operations and
	create an AD function object that maps ax -> ay.
	"""
	# convert ax -> au, ay -> av
	dtype    = cppad_py.a_double
	syntax   = 'd_fun(ax, ay)'
	au       = cppad_py.utility.numpy2vec(ax, dtype, ax.size, syntax, 'ax')
	av       = cppad_py.utility.numpy2vec(ay, dtype, ay.size, syntax, 'ay')
	#
	# call d_fun and return result
	return cppad_py.swig.d_fun(au, av)
