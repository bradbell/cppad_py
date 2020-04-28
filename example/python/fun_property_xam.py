# -----------------------------------------------------------------------------
#         cppad_py: A C++ Object Library and Python Interface to Cppad
#          Copyright (C) 2017-20 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# -----------------------------------------------------------------------------
# d_fun properties
# -----------------------------------------------------------------------------
# BEGIN SOURCE
def fun_property_xam() :
	#
	import numpy
	import cppad_py
	#
	# initialize return variable
	ok = True
	# ---------------------------------------------------------------------
	n_ind = 1 # number of independent variables
	n_dep = 2 # number of dependent variables
	n_var = 1 # phantom variable at address 0
	n_op  = 1 # special operator at beginning
	#
	# dimension some vectors
	# x  = numpy.empty(n_ind, dtype=float)
	x  = numpy.empty(n_ind, dtype=float)
	ay = numpy.empty(n_dep, dtype=cppad_py.a_double)
	#
	# independent variables
	x[0]  = 1.0
	ax    = cppad_py.independent(x)
	n_var = n_var + n_ind # one for each indpendent
	n_op  = n_op + n_ind
	#
	# first dependent variable
	ay[0] = ax[0] + ax[0]
	n_var = n_var + 1 # one variable and operator
	n_op  = n_op + 1
	#
	# second dependent variable
	ax0   = ax[0]
	ay[1] = ax0.sin()
	n_var = n_var + 2 # two varialbes, one operator
	n_op  = n_op + 1
	#
	# define f(x) = y
	f  = cppad_py.d_fun(ax, ay)
	n_op = n_op + 1 # speical operator at end
	#
	# check af properties except f.to_json
	ok = ok and f.size_domain() == n_ind
	ok = ok and f.size_range()  == n_dep
	ok = ok and f.size_var()    == n_var
	ok = ok and f.size_op()     == n_op
	ok = ok and f.size_order()  == 0
	#
	# compute zero order Taylor coefficients
	y  = f.forward(0, x)
	ok = ok and f.size_order() == 1
	# ---------------------------------------------------------------------
	af = cppad_py.a_fun(f)
	#
	# check af properties
	ok = ok and af.size_domain() == n_ind
	ok = ok and af.size_range()  == n_dep
	ok = ok and af.size_var()    == n_var
	ok = ok and af.size_op()     == n_op
	ok = ok and af.size_order()  == 0
	# ---------------------------------------------------------------------
	# The empty function
	f = cppad_py.d_fun()
	ok = ok and f.size_domain() == 0
	ok = ok and f.size_range()  == 0
	ok = ok and f.size_var()    == 0
	ok = ok and f.size_op()     == 0
	ok = ok and f.size_order()  == 0
	#
	return( ok  )
#
# END SOURCE
# -----------------------------------------------------------------------------
# $begin fun_property_xam.py$$ $newlinech #$$
# $spell
#	py
#	perl
#	cppad
#	py
#	xam
#	Jacobian
#	Jacobians
# $$
# $section Python: d_fun Properties: Example and Test$$
# $srcthisfile|0|# BEGIN SOURCE|# END SOURCE|$$
# $end
#
