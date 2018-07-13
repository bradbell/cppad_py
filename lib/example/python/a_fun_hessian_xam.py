# -----------------------------------------------------------------------------
#         cppad_py: A C++ Object Library and Python Interface to Cppad
#          Copyright (C) 2017-18 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# -----------------------------------------------------------------------------
# hessian
# -----------------------------------------------------------------------------
# BEGIN SOURCE
def a_fun_hessian_xam() :
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
	x = numpy.zeros(n_ind, dtype=float)
	for i in range( n_ind  ) :
		x[i] = i + 2.0
	#
	ax = cppad_py.independent(x)
	#
	# create dependent variables ay with ay0 = ax_0 * ax_1 * ax_2
	ax_0 = ax[0]
	ax_1 = ax[1]
	ax_2 = ax[2]
	ay   = numpy.zeros(n_dep, dtype=cppad_py.a_double)
	ay[0] = ax_0 * ax_1 * ax_2
	#
	# define af corresponding to f(x) = x_0 * x_1 * x_2
	af = cppad_py.a_fun(ax, ay)
	#
	# g(x) = w_0 * f_0 (x) = f(x)
	w = numpy.zeros(n_dep, dtype=float)
	w[0] = 1.0
	#
	# compute Hessian
	fpp = af.hessian(x, w)
	#
	#          [ 0.0 , x_2 , x_1 ]
	# f''(x) = [ x_2 , 0.0 , x_0 ]
	#          [ x_1 , x_0 , 0.0 ]
	ok = ok and fpp[0, 0] == 0.0
	ok = ok and fpp[0, 1] == x[2]
	ok = ok and fpp[0, 2] == x[1]
	#
	ok = ok and fpp[1, 0] == x[2]
	ok = ok and fpp[1, 1] == 0.0
	ok = ok and fpp[1, 2] == x[0]
	#
	ok = ok and fpp[2, 0] == x[1]
	ok = ok and fpp[2, 1] == x[0]
	ok = ok and fpp[2, 2] == 0.0
	#
	return( ok )
#
# END SOURCE
#
# $begin a_fun_hessian_xam.py$$ $newlinech #$$
# $spell
#	py
#	perl
#	cppad
#	py
#	xam
#	Jacobian
#	Jacobians
# $$
# $section Python: Dense Hessian Using AD: Example and Test$$
# $srcfile|lib/example/python/a_fun_hessian_xam.py|0|# BEGIN SOURCE|# END SOURCE|$$
# $end
#
