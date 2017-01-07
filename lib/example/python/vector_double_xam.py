
# This file can be automatically generated using the following command
# m4 ../python.m4 ../../xam/vector_double_xam.xam > vector_double_xam.py
# -----------------------------------------------------------------------------
#         cppad_swig: A C++ Object Library and Swig Interface to Cppad
#          Copyright (C) 2017-17 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#          GNU Affero General Public License version 3.0 or later see
#                     http://www.gnu.org/licenses/agpl.txt
# -----------------------------------------------------------------------------
# std::vector<double>
# -----------------------------------------------------------------------------
# BEGIN SOURCE
def vector_double_xam() :
	#
	# load the Cppad Swig library
	import py_cppad
	#
	# initialize return variable
	ok = True
	n = 4
	vec = py_cppad.vector_double(n)
	#
	# check size
	ok = ok and vec.size() == n
	#
	# setting elements
	for i in range( n  ) :
		vec[i] = 2.0 * i
	#
	# getting elements
	for i in range( n  ) :
		element = vec[i]
		ok = ok and element == 2.0 * i
	#
	return( ok )
#
# END SOURCE
#
# $begin vector_double_xam.py$$ $newlinech #$$
# $spell
#	py
#	perl
#	cppad
#	xam
# $$
# $section python: vector_double Example and Test$$
# $srcfile|lib/example/python/vector_double_xam.py|0|# BEGIN SOURCE|# END SOURCE|$$
# $end

