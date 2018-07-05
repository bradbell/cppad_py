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
def a_double_ad_binary_xam() :
	#
	# load the Cppad Py library
	import cppad_py
	#
	# initialize return variable
	ok = True
	# ---------------------------------------------------------------------
	two = cppad_py.a_double(2.0)
	three = cppad_py.a_double(3.0)
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
# END SOURCE
#
# $begin a_double_ad_binary_xam.py$$ $newlinech #$$
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
# $srcfile|lib/example/python/a_double_ad_binary_xam.py|0|# BEGIN SOURCE|# END SOURCE|$$
# $end
#
