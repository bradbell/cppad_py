
# This file can be automatically generaeted using the following command
# m4 ../python.m4 ../xam/a_fun_xam.m4 > a_fun_xam.py
# -----------------------------------------------------------------------------
#         cppad_swig: A C++ Object Library and Swig Interface to CppAD
#          Copyright (C) 2017-17 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#          GNU Affero General Public License version 3.0 or later see
#                     http://www.gnu.org/licenses/agpl.txt
# -----------------------------------------------------------------------------
# std::vector<a_double>
# -----------------------------------------------------------------------------
def a_fun_xam() :
	#
	# load the cppad Swig library
	import py_cppad
	#
	# initialize return variable
	ok = True
	n = 2
	m = 1
	#
	# create ax
	x = py_cppad.vector_double(n)
	for i in range( n  ) :
		x[i] = i + 1.0
	ax = py_cppad.independent(x)
	#
	# create af
	ax0 = ax[0]
	ax1 = ax[1]
	ay = py_cppad.vector_ad(1)
	ay[0] = ax0 + ax0 - ax1
	af = py_cppad.a_fun(ax, ay)
	#
	# zero order forward
	x[0] = 3.0
	x[1] = 1.0
	y = af.forward(0, x)
	ok = ok and y[0] == 5.0
	#
	# first order forward
	x[0] = 0.0
	x[1] = 1.0
	y = af.forward(1, x)
	ok = ok and y[0] == -1.0
	#
	return( ok )
#
