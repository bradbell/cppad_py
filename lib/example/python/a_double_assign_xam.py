# This file can be generated in the lib/xam directory using the command:
# m4 -D `Language_'=python a_double/assign_xam.xam
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
	# load the Cppad Py library
	import cppad_py
	#
	# initialize return variable
	ok = True
	# ---------------------------------------------------------------------
	x = cppad_py.a_double(2.0)
	#
	x = cppad_py.a_double(3.0);
	ok = ok and x.value() == 3.0
	#
	x += cppad_py.a_double(2.0);
	ok = ok and x.value() == 5.0
	#
	x -= cppad_py.a_double(1.0);
	ok = ok and x.value() == 4.0
	#
	x *= cppad_py.a_double(3.0);
	ok = ok and x.value() == 12.0
	#
	x /= cppad_py.a_double(4.0);
	ok = ok and x.value() == 3.0
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
