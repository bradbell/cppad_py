# -----------------------------------------------------------------------------
#         cppad_py: A C++ Object Library and Python Interface to Cppad
#          Copyright (C) 2017-18 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# -----------------------------------------------------------------------------
# forward
# -----------------------------------------------------------------------------
# BEGIN SOURCE
def a_fun_forward_xam() :
	#
	import numpy
	import cppad_py
	#
	# initialize return variable
	ok = True
	# ---------------------------------------------------------------------
	# number of dependent and independent variables
	n_dep = 1
	n_ind = 2
	#
	# create the independent variables ax
	xp = numpy.zeros(n_ind, dtype=float)
	for i in range( n_ind  ) :
		xp[i] = i + 1.0
	#
	ax = cppad_py.independent(xp)
	#
	# create dependent varialbes ay with ay0 = ax0 * ax1
	ax0    = ax[0]
	ax1    = ax[1]
	ay    = numpy.zeros(n_dep, dtype=cppad_py.a_double)
	ay[0] = ax0 * ax1
	#
	# define af corresponding to f(x) = x0 * x1
	af = cppad_py.a_fun(ax, ay)
	#
	# define X(t) = (3 + t, 2 + t)
	# it follows that Y(t) = f(X(t)) = (3 + t) * (2 + t)
	#
	# Y(0) = 6 and p ! = 1
	p     = 0
	xp[0] = 3.0
	xp[1] = 2.0
	yp = af.forward(p, xp)
	ok = ok and yp[0] == 6.0
	#
	# first order Taylor coefficients for X(t)
	p     = 1
	xp[0] = 1.0
	xp[1] = 1.0
	#
	# first order Taylor coefficient for Y(t)
	# Y'(0) = 3 + 2 = 5 and p ! = 1
	yp = af.forward(p, xp)
	ok = ok and yp[0] == 5.0
	#
	# second order Taylor coefficients for X(t)
	p     = 2
	xp[0] = 0.0
	xp[1] = 0.0
	#
	# second order Taylor coefficient for Y(t)
	# Y''(0) = 2.0 and p ! = 2
	yp = af.forward(p, xp)
	ok = ok and yp[0] == 1.0
	#
	return( ok )
#
# END SOURCE
#
# $begin a_fun_forward_xam.py$$ $newlinech #$$
# $spell
#	py
#	perl
#	cppad
#	py
#	xam
#	Jacobian
#	Jacobians
# $$
# $section Python: Forward Mode AD: Example and Test$$
# $srcfile|lib/example/python/a_fun_forward_xam.py|0|# BEGIN SOURCE|# END SOURCE|$$
# $end
#
