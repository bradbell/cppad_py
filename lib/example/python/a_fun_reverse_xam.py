# This file can be generated in the lib/xam directory using the command:
# m4 -D `Language_'=python a_fun/reverse_xam.xam
# -----------------------------------------------------------------------------
#         cppad_py: A C++ Object Library and Python Interface to Cppad
#          Copyright (C) 2017-18 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# -----------------------------------------------------------------------------
# reverse
# -----------------------------------------------------------------------------
# BEGIN SOURCE
def a_fun_reverse_xam() :
	#
	# load the Cppad Py library
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
	xp = cppad_py.vec_double(n_ind)
	for i in range( n_ind  ) :
		xp[i] = i
	#
	ax = cppad_py.independent(xp)
	#
	# create dependent variables ay with ay0 = ax_0 * ax_1 * ax_2
	ax_0 = ax[0]
	ax_1 = ax[1]
	ax_2 = ax[2]
	ay = cppad_py.vec_a_double(n_dep)
	ay[0] = ax_0 * ax_1 * ax_2
	#
	# define af corresponding to f(x) = x_0 * x_1 * x_2
	af = cppad_py.a_fun(ax, ay)
	# -----------------------------------------------------------------------
	# define          X(t) = (x_0 + t, x_1 + t, x_2 + t)
	# it follows that Y(t) = f(X(t)) = (x_0 + t) * (x_1 + t) * (x_2 + t)
	# and that       Y'(0) = x_1 * x_2 + x_0 * x_2 + x_0 * x_1
	# -----------------------------------------------------------------------
	# zero order forward mode
	p = 0
	xp[0] = 2.0
	xp[1] = 3.0
	xp[2] = 4.0
	yp = af.forward(p, xp)
	ok = ok and yp[0] == 24.0
	# -----------------------------------------------------------------------
	# first order reverse (derivative of zero order forward)
	# define G( Y ) = y_0 = x_0 * x_1 * x_2
	q = 1
	yq1 = cppad_py.vec_double(n_dep)
	yq1[0] = 1.0
	xq1 = af.reverse(q, yq1)
	# partial G w.r.t x_0
	ok = ok and xq1[0] == 3.0 * 4.0
	# partial G w.r.t x_1
	ok = ok and xq1[1] == 2.0 * 4.0
	# partial G w.r.t x_2
	ok = ok and xq1[2] == 2.0 * 3.0
	# -----------------------------------------------------------------------
	# first order forward mode
	p = 1
	xp[0] = 1.0
	xp[1] = 1.0
	xp[2] = 1.0
	yp = af.forward(p, xp)
	ok = ok and yp[0] == 3.0*4.0 + 2.0*4.0 + 2.0*3.0
	# -----------------------------------------------------------------------
	# second order reverse (derivative of first order forward)
	# define G( y_0^0 , y_0^1 ) = y_0^1
	# = x_1^0 * x_2^0  +  x_0^0 * x_2^0  +  x_0^0  *  x_1^0
	q = 2
	yq2 = cppad_py.vec_double(n_dep * q)
	yq2[0 * q + 0] = 0.0 # partial of G w.r.t y_0^0
	yq2[0 * q + 1] = 1.0 # partial of G w.r.t y_0^1
	xq2 = af.reverse(q, yq2)
	# partial G w.r.t x_0^0
	ok = ok and xq2[0 * q + 0] == 3.0 + 4.0
	# partial G w.r.t x_1^0
	ok = ok and xq2[1 * q + 0] == 2.0 + 4.0
	# partial G w.r.t x_2^0
	ok = ok and xq2[2 * q + 0] == 2.0 + 3.0
	# -----------------------------------------------------------------------
	#
	return( ok )
#
# END SOURCE
#
# $begin a_fun_reverse_xam.py$$ $newlinech #$$
# $spell
#	py
#	perl
#	cppad
#	py
#	xam
#	Jacobian
#	Jacobians
# $$
# $section Python: Reverse Mode AD: Example and Test$$
# $srcfile|build/lib/example/python/a_fun_reverse_xam.py|0|# BEGIN SOURCE|# END SOURCE|$$
# $end
#
