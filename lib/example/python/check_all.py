# -----------------------------------------------------------------------------
#         cppad_swig: A C++ Object Library and Swig Interface to Cppad
#          Copyright (C) 2017-17 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#          GNU Affero General Public License version 3.0 or later see
#                     http://www.gnu.org/licenses/agpl.txt
# -----------------------------------------------------------------------------
import sys
import os
# cppad_swig_lib.dll is in .. directory
os.environ['PATH'] = '..;' + os.environ['PATH']
#
error_count = 0
def run_test(name) :
	exec( 'import ' + name )
	exec( 'ok = ' + name + '.' + name + '()' )
	if ok :
		print('python: ' + name + ': OK')
	else :
		print('python: ' + name + ': Error')
		error_count = error_count + 1
#
fun_list = [
	'a_double_cond_assign_xam',
	'a_double_property_xam',
	'a_double_unary_fun_xam',
	'a_double_unary_op_xam',
	'a_double_assign_xam',
	'a_double_ad_binary_xam',
	'a_double_compare_xam',
	'a_vector_size_xam',
	'a_vector_set_get_xam',
	'a_fun_jacobian_xam',
	'a_fun_forward_xam',
	'a_fun_reverse_xam',
	'a_fun_abort_xam',
	'a_other_error_message_xam'
]
for name in fun_list :
	run_test(name)
#
if error_count > 0 :
	print('python: check_all: error_count = ', error_count)
	sys.exit(1)
print('python: check_all: OK')
sys.exit(0)
