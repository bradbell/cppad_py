# -----------------------------------------------------------------------------
#         cppad_py: A C++ Object Library and Python Interface to Cppad
#          Copyright (C) 2017-18 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# -----------------------------------------------------------------------------
# a_double unary operators
# -----------------------------------------------------------------------------
# BEGIN SOURCE
def a_double_unary_fun_xam() :
	#
	import numpy
	import cppad_py
	#
	# initialize return variable
	ok = True
	# ---------------------------------------------------------------------
	#
	# fabs
	one = cppad_py.a_double(1.0)
	abs_one = one.fabs()
	ok = ok and abs_one == 1.0
	#
	# pi/4
	pi_4 = one.atan()
	#
	# sqrt(2)
	tmp = cppad_py.a_double(2.0)
	r2 = tmp.sqrt()
	#
	# sin(pi/4)  * sqrt(2) = 1.0;
	tmp = r2 * pi_4.sin()
	ok = ok and tmp.near_equal(one)
	#
	# cos(pi/4)  * sqrt(2) = 1.0;
	tmp = r2 * pi_4.cos()
	ok = ok and tmp.near_equal(one)
	#
	# tan(pi/4)  = 1.0;
	tmp = pi_4.tan()
	ok = ok and tmp.near_equal(one)
	#
	return( ok )
#
# END SOURCE
#
# $begin a_double_unary_fun_xam.py$$ $newlinech #$$
# $spell
#	py
#	perl
#	cppad
#	py
#	xam
#	Jacobian
#	Jacobians
# $$
# $section Python: a_double Unary Functions with AD Result: Example and Test$$
# $srcfile|lib/example/python/a_double_unary_fun_xam.py|0|# BEGIN SOURCE|# END SOURCE|$$
# $end
#
