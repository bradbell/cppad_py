# -----------------------------------------------------------------------------
#         cppad_py: A C++ Object Library and Python Interface to Cppad
#          Copyright (C) 2017-20 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# -----------------------------------------------------------------------------
# d_fun properties
# -----------------------------------------------------------------------------
# BEGIN SOURCE
def fun_json_xam() :
	#
	import numpy
	import cppad_py
	import re
	#
	# initialize return variable
	ok = True
	# ---------------------------------------------------------------------
	n = 1 # number of independent variables
	m = 2 # number of dependent variables
	#
	# dimension some vectors
	x  = numpy.empty(n, dtype=float)
	ay = numpy.empty(m, dtype=cppad_py.a_double)
	#
	# independent variables
	x[0]  = 1.0
	ax    = cppad_py.independent(x)
	#
	# f(x) = [ x0 + x0, sin(x0) ]
	ay[0] = ax[0] + ax[0]
	ay[1] = ax[0].sin()
	f     = cppad_py.d_fun(ax, ay)
	#
	# check f.to_json
	json     = f.to_json()
	pattern  = r'"op_code" *: *([^,]*),'
	match    = re.search(pattern, json)
	op_code  = int( match.group(1) )
	ok      &= op_code == 1
	pattern  = r'"name" *: *"([^"]*)" *,'
	match    = re.search(pattern, json)
	name     = match.group(1);
	ok      &= name == 'add' or name == 'sub'
	#
	return( ok  )
# END SOURCE
#
# $begin fun_to_json_xam.py$$ $newlinech #$$
# $spell
#     json
# $$
# $section C++: to_json: Example and Test$$
# $srcthisfile|0|# BEGIN SOURCE|# END SOURCE|$$
# $end
