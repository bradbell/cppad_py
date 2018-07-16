# -----------------------------------------------------------------------------
#         cppad_py: A C++ Object Library and Python Interface to Cppad
#          Copyright (C) 2017-18 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# -----------------------------------------------------------------------------
# optimize
# -----------------------------------------------------------------------------
# BEGIN SOURCE
def a_fun_optimize_xam() :
	#
	import numpy
	import cppad_py
	#
	# initialize return variable
	ok = True
	# ---------------------------------------------------------------------
	n_ind = 1 # number of independent variables
	n_dep = 1 # number of dependent variables
	n_var = 1 # phantom variable at address 0
	n_op  = 1 # special operator at beginning
	#
	# dimension some vectors
	x  = numpy.empty(n_ind, dtype=float)
	ay = numpy.empty(n_dep, dtype=cppad_py.a_double)
	#
	# independent variables
	x[0]  = 1.0
	ax    = cppad_py.independent(x)
	n_var = n_var + n_ind # one for each indpendent
	n_op  = n_op + n_ind
	#
	# accumulate summation
	ax0   = ax[0]
	csum  = cppad_py.a_double(0.0)
	csum  = ax0 + ax0 + ax0 + ax0
	n_var = n_var + 3 # one per + operator
	n_op  = n_op + 3
	#
	# define f(x) = y_0 = csum
	ay[0] = csum
	af    = cppad_py.a_fun(ax, ay)
	n_op  = n_op + 1 # speical operator at end
	#
	# check number of variables and operators
	ok = ok and af.size_var() == n_var
	ok = ok and af.size_op() == n_op
	#
	# optimize
	af.optimize()
	#
	# number of variables and operators has decreased by two
	ok = ok and af.size_var() == n_var-2
	ok = ok and af.size_op() == n_op-2
	#
	return( ok  )
#
# END SOURCE
# -----------------------------------------------------------------------------
# $begin a_fun_optimize_xam.py$$ $newlinech #$$
# $spell
#	py
#	perl
#	cppad
#	py
#	xam
#	Jacobian
#	Jacobians
# $$
# $section Python: Optimize an a_fun: Example and Test$$
# $srcfile|lib/example/python/a_fun_optimize_xam.py|0|# BEGIN SOURCE|# END SOURCE|$$
# $end
#
