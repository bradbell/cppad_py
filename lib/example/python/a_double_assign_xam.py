# -----------------------------------------------------------------------------
#         cppad_py: A C++ Object Library and Python Interface to Cppad
#          Copyright (C) 2017-18 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# -----------------------------------------------------------------------------
# a_double assignment
# -----------------------------------------------------------------------------
# BEGIN SOURCE
def a_double_assign_xam() :
	#
	import numpy
	import cppad_py
	#
	# initialize return variable
	ok = True
	# ---------------------------------------------------------------------
	x = cppad_py.a_double(2.0)
	#
	x = cppad_py.a_double(3.0);
	ok = ok and x == 3.0
	#
	x += cppad_py.a_double(2.0);
	ok = ok and x == 5.0
	#
	x -= cppad_py.a_double(1.0);
	ok = ok and x == 4.0
	#
	x *= cppad_py.a_double(3.0);
	ok = ok and x == 12.0
	#
	x /= cppad_py.a_double(4.0);
	ok = ok and x == 3.0
	#
	return( ok )
#
# END SOURCE
#
# $begin a_double_assign_xam.py$$ $newlinech #$$
# $spell
#	py
#	perl
#	cppad
#	py
#	xam
#	Jacobian
#	Jacobians
# $$
# $section Python: a_double Assignment Operators: Example and Test$$
# $srcfile|lib/example/python/a_double_assign_xam.py|0|# BEGIN SOURCE|# END SOURCE|$$
# $end
#
