# This file can be generated in the lib/xam directory using the command:
# m4 -D `Language_'=python a_double/unary_op_xam.xam
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
def a_double_unary_op_xam() :
	#
	# load the Cppad Py library
	import cppad_py
	#
	# initialize return variable
	ok = True
	# ---------------------------------------------------------------------
	two = cppad_py.a_double(2.0)
	plus_two = + two
	minus_two = - two
	#
	ok = ok and plus_two.value() == 2.0
	ok = ok and minus_two.value() == -2.0
	#
	return( ok )
#
# END SOURCE
#
# $begin a_double_unary_op_xam.py$$ $newlinech #$$
# $spell
#	py
#	perl
#	cppad
#	py
#	xam
#	Jacobian
#	Jacobians
# $$
# $section Python: a_double Unary Plus and Minus: Example and Test$$
# $srcfile|lib/example/python/a_double_unary_op_xam.py|0|# BEGIN SOURCE|# END SOURCE|$$
# $end
#
