# This file can be automatically generaeted using the following command
# m4 ../python.m4 ../../xam/a_double_xam.xam > a_double_xam.py
# -----------------------------------------------------------------------------
#         cppad_swig: A C++ Object Library and Swig Interface to Cppad
#          Copyright (C) 2017-17 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#          GNU Affero General Public License version 3.0 or later see
#                     http://www.gnu.org/licenses/agpl.txt
# -----------------------------------------------------------------------------
# a_double
# -----------------------------------------------------------------------------
def a_double_xam() :
	#
	# load the Cppad Swig library
	import py_cppad
	#
	# initialize return variable
	ok = True
	two = py_cppad.a_double(2.0)
	three = py_cppad.a_double(3.0)
	#
	five = two + three
	six = two * three
	neg_one = two - three
	two_thirds = two / three
	#
	ok = ok and five.value() == 5.0
	ok = ok and six.value() == 6.0
	ok = ok and neg_one.value() == -1.0
	ok = ok and 0.5 < two_thirds.value()
	ok = ok and two_thirds.value() < 1.0
	ok = ok and five < six
	#
	return( ok )
#
