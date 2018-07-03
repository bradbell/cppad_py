# This file can be generated in the lib/xam directory using the command:
# m4 -D `Language_'=python a_fun/cond_assign_xam.xam
# -----------------------------------------------------------------------------
#         cppad_py: A C++ Object Library and Python Interface to Cppad
#          Copyright (C) 2017-18 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# -----------------------------------------------------------------------------
# a_double conditional assignment
# -----------------------------------------------------------------------------
# BEGIN SOURCE
def a_double_cond_assign_xam() :
	#
	# load the Cppad Py library
	import cppad_py
	#
	# initialize return variable
	ok = True
	# ---------------------------------------------------------------------
	n_ind = 4
	n_dep = 1
	#
	# create ax (value of independent variables does not matter)
	x = cppad_py.vec_double(n_ind)
	x[0] = 0.0
	x[1] = 1.0
	x[2] = 2.0
	x[3] = 3.0
	ax = cppad_py.independent(x)
	#
	# arguments to conditional assignment
	left = ax[0]
	right = ax[1]
	if_true = ax[2]
	if_false = ax[3]
	#
	# assignment
	target = cppad_py.a_double()
	target.cond_assign(
		"<",
		left,
		right,
		if_true,
		if_false
	)
	#
	# f(x) = taget
	ay = cppad_py.vec_a_double(n_dep)
	ay[0] = target
	af = cppad_py.a_fun(ax, ay)
	#
	# assignment with different independent variable values
	x[0] = 9.0 # left
	x[1] = 8.0 # right
	x[2] = 7.0 # if_true
	x[3] = 6.0 # if_false
	p = 0
	y = af.forward(p, x)
	ok = ok and y[0] == 6.0
	#
	return( ok  )
#
# END SOURCE
#
# $begin a_double_cond_assign_xam.py$$ $newlinech #$$
# $spell
#	py
#	perl
#	cppad
#	py
#	xam
#	Jacobian
#	Jacobians
# $$
# $section Python: a_double Conditional Assignment: Example and Test$$
# $srcfile|lib/example/python/a_double_cond_assign_xam.py|0|# BEGIN SOURCE|# END SOURCE|$$
# $end
#
