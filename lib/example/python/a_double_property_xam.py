# -----------------------------------------------------------------------------
#         cppad_py: A C++ Object Library and Python Interface to Cppad
#          Copyright (C) 2017-20 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# -----------------------------------------------------------------------------
# a_double properties
# -----------------------------------------------------------------------------
# BEGIN SOURCE
def a_double_property_xam() :
	#
	import numpy
	import cppad_py
	#
	# initialize return variable
	ok = True
	# ---------------------------------------------------------------------
	a3 = cppad_py.a_double(3.0)
	#
	ok = ok and a3   == 3.0
	ok = ok and a3.parameter()
	ok = ok and not a3.variable()
	#
	# near_equal
	r3 = a3.sqrt()
	ok = ok and a3.near_equal( r3 * r3) ;
	#
	return( ok )
#
# END SOURCE
#
# $begin a_double_property_xam.py$$ $newlinech #$$
# $spell
#	py
#	perl
#	cppad
#	py
#	xam
#	Jacobian
#	Jacobians
# $$
# $section Python: a_double Properties: Example and Test$$
# $srcthisfile|0|# BEGIN SOURCE|# END SOURCE|$$
# $end
#
