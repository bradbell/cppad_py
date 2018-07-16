# -----------------------------------------------------------------------------
#         cppad_py: A C++ Object Library and Python Interface to Cppad
#          Copyright (C) 2017-18 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# -----------------------------------------------------------------------------
# $begin py_a_fun_ctor$$ $newlinech #$$
# $spell
#	vec
#	af
#	const
#	cppad_py
#	numpy
# $$
#
# $section Stop Current Recording and Store in an a_fun Object$$
#
# $head Syntax$$
# $icode%af% = cppad_py.a_fun(%ax%, %ay%)%$$
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
# $head af$$
# The result is a $code cppad_py.a_fun$$ object.
# It has a representation for the $cref a_double$$ operations
# that mapped the independent variables to the dependent variables.
# These operations define the function that can be differentiated.
#
# $head Example$$
# All of the $code a_fun$$ examples use an $code a_fun$$ constructor.
#
# $end
# -----------------------------------------------------------------------------
import numpy
import cppad_py
#
# This function is used by __init__ in a_fun class to implement syntax above:
def a_fun_ctor(ax, ay) :
	"""
	a_fun(ax, ay)
	Stop recording a_double operations and
	create an AD function object that maps ax -> ay.
	"""
	# convert ax -> au, ay -> av
	dtype    = cppad_py.a_double
	syntax   = 'a_fun(ax, ay)'
	au       = cppad_py.utility.numpy2vec(ax, dtype, ax.size, syntax, 'ax')
	av       = cppad_py.utility.numpy2vec(ay, dtype, ay.size, syntax, 'ay')
	#
	# call a_fun and return result
	return cppad_py.cppad_py_swig.a_fun(au, av)
