# -----------------------------------------------------------------------------
#         cppad_py: A C++ Object Library and Python Interface to Cppad
#          Copyright (C) 2017-18 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# -----------------------------------------------------------------------------
# jacobian
# -----------------------------------------------------------------------------
# BEGIN SOURCE
def a_fun_jacobian_xam() :
	#
	import numpy
	import cppad_py
	#
	# initialize return variable
	ok = True
	# ---------------------------------------------------------------------
	# number of dependent and independent variables
	n_dep = 1
	n_ind = 3
	#
	# create the independent variables ax
	x = numpy.empty(n_ind, dtype=float)
	for i in range( n_ind  ) :
		x[i] = i + 2.0
	#
	ax = cppad_py.independent(x)
	#
	# create dependent variables ay with ay0 = ax_0 * ax_1 * ax_2
	ax_0  = ax[0]
	ax_1  = ax[1]
	ax_2  = ax[2]
	ay    = numpy.empty(n_dep, dtype=cppad_py.a_double)
	ay[0] = ax_0 * ax_1 * ax_2
	#
	# define af corresponding to f(x) = x_0 * x_1 * x_2
	af = cppad_py.a_fun(ax, ay)
	#
	# compute the Jacobian f'(x) = ( x_1*x_2, x_0*x_2, x_0*x_1 )
	fp = af.jacobian(x)
	#
	# check Jacobian
	x_0 = x[0]
	x_1 = x[1]
	x_2 = x[2]
	ok = ok and fp[0, 0] == x_1 * x_2
	ok = ok and fp[0, 1] == x_0 * x_2
	ok = ok and fp[0, 2] == x_0 * x_1
	#
	return( ok )
#
# END SOURCE
#
# $begin a_fun_jacobian_xam.py$$ $newlinech #$$
# $spell
#	py
#	perl
#	cppad
#	py
#	xam
#	Jacobian
#	Jacobians
# $$
# $section Python: Dense Jacobian Using AD: Example and Test$$
# $srcfile|lib/example/python/a_fun_jacobian_xam.py|0|# BEGIN SOURCE|# END SOURCE|$$
# $end
#
