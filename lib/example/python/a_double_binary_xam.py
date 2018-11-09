# -----------------------------------------------------------------------------
#         cppad_py: A C++ Object Library and Python Interface to Cppad
#          Copyright (C) 2017-18 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# -----------------------------------------------------------------------------
# a_double binary operations
# -----------------------------------------------------------------------------
# BEGIN SOURCE
def a_double_binary_xam() :
	#
	import numpy
	import cppad_py
	ok = True
	a2 = cppad_py.a_double(2.0)
	a3 = cppad_py.a_double(3.0)
	# ---------------------------------------------------------------------
	a5       = a2 + a3
	a6       = a2 * a3
	a1_minus = a2 - a3
	a23 = a2 / a3
	#
	ok = ok and a5 == 5.0
	ok = ok and a6 == 6.0
	ok = ok and a1_minus == -1.0
	ok = ok and a23.near_equal( cppad_py.a_double(2.0 / 3.0) )
	# ---------------------------------------------------------------------
	a5       = a2 + 3.0
	a6       = a2 * 3.0
	a1_minus = a2 - 3.0
	a23 = a2 / 3.0
	#
	ok = ok and a5 == 5.0
	ok = ok and a6 == 6.0
	ok = ok and a1_minus == -1.0
	ok = ok and a23.near_equal( cppad_py.a_double(2.0 / 3.0) )
	#
	return( ok )
#
# END SOURCE
#
# $begin a_double_binary_xam.py$$ $newlinech #$$
# $spell
#	py
#	perl
#	cppad
#	py
#	xam
#	Jacobian
#	Jacobians
# $$
# $section Python: a_double Binary Operators With AD Result: Example and Test$$
# $srcfile|lib/example/python/a_double_binary_xam.py|0|# BEGIN SOURCE|# END SOURCE|$$
# $end
#
