# -----------------------------------------------------------------------------
#         cppad_py: A C++ Object Library and Python Interface to Cppad
#          Copyright (C) 2017-18 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# -----------------------------------------------------------------------------
# error_message
# -----------------------------------------------------------------------------
# BEGIN SOURCE
def error_message_xam() :
	#
	# load the Cppad Py library
	import cppad_py
	#
	# initialize return variable
	ok = True
	# ---------------------------------------------------------------------
	ok = False
	try :
		cppad_py.error_message("test message")
	except : # catch
		stored_message = cppad_py.error_message("")
		ok = (stored_message == "test message")
	#
	return( ok  )
#
# END SOURCE
# -----------------------------------------------------------------------------
# $begin error_message_xam.py$$ $newlinech #$$
# $spell
#	py
#	perl
#	cppad
#	py
#	xam
#	Jacobian
#	Jacobians
# $$
# $section Python: Cppad Py Exception Handling: Example and Test$$
# $srcfile|lib/example/python/error_message_xam.py|0|# BEGIN SOURCE|# END SOURCE|$$
# $end
#
