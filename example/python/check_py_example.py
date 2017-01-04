# -----------------------------------------------------------------------------
#         cppad_swig: A C++ Object Library and SWIG Interface to CppAD
#          Copyright (C) 2017-17 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#          GNU Affero General Public License version 3.0 or later see
#                     http://www.gnu.org/licenses/agpl.txt
# -----------------------------------------------------------------------------
# $begin check_py_example.py$$ $newlinech #$$
# $spell
#	py
#	ptr
# $$
#
# $section Python Script That Tests py_example Swig Module$$
#
# $head Load the Module$$
# $srccode%cpp%
import py_example
# %$$
#
# $head Initialize Error Count$$
# $srccode%cpp%
error_count = 0
# %$$
#
# $head factorial_by_val$$
# $srccode%cpp%
if py_example.factorial_by_val(4) == 24 :
	print('py_example.factorial_by_val: OK')
else :
	print('py_example.factorial_by_val: Error')
	error_count = error_count + 1
# %$$
#
# $head message_of_void$$
# $srccode%cpp%
if py_example.message_of_void() == 'OK' :
	print('py_example.message_of_void: OK')
else :
	print('py_example.message_of_void: Error')
	error_count = error_count + 1
# %$$
#
# $head int_class$$
# $srccode%cpp%
obj = py_example.int_class()
py_example.add_by_ptr(3, 4, obj)
if obj.value() == 7 :
	print('py_example.add_by_ptr: OK')
else :
	print('py_example.add_by_ptr: Error')
	error_count = error_count + 1
# %$$
#
# $head int_array_ptr$$
# $srccode%cpp%
n   = 10
array_ptr = py_example.new_int_array_ptr(n)
for i in range(n) :
	py_example.int_array_ptr_setitem(array_ptr, i, 2 * i)
#
if py_example.max_array_by_ptr(n, array_ptr) == 18 :
	print('py_example.max_array_by_ptr: pointer: OK')
else :
	print('py_example.max_array_by_ptr: pointer: Error')
	error_count = error_count + 1
py_example.delete_int_array_ptr(array_ptr)
# %$$
#
# $head int_array_class$$
# $srccode%cpp%
n   = 10
array_obj = py_example.int_array_class(n)
for i in range(n) :
	array_obj[i] = 2 * i
#
if py_example.max_array_by_ptr(n, array_obj) == 18 :
	print('py_example.max_array_by_ptr: class: OK')
else :
	print('py_example.max_array_by_ptr: class: Error')
	error_count = error_count + 1
# %$$
#
# $head vector_double$$
# $srccode%cpp%
n   = 10
vec = py_example.vector_double(n)
for i in range(n) :
	vec[i] = 2.0 * i;
#
if py_example.max_std_vector_double(vec) == 18.0 :
	print('py_example.max_std_vector_double: class: OK')
else :
	print('py_example.max_std_vector_double: class: Error')
	error_count = error_count + 1
# %$$
#
# $head raise_exception$$
# $srccode%cpp%
try :
	py_example.raise_exception('test message')
	message = ''
except :
	message = py_example.raise_exception('')
if message == 'test message' :
	print('py_example.py_example.raise_exception: OK')
else :
	print('py_example.raise_exception.message_of_void: Error')
	error_count = error_count + 1
# %$$
#
# $head normal_class$$
# $srccode%cpp%
two   = py_example.normal_class(2)
three = py_example.normal_class(3)
five  = two + three
ok       = five == py_example.normal_class(5)
ok       = ok and 4 < five.value()  and five.value() < 6
if ok :
	print('py_example.normal_class: OK')
else :
	print('py_example.normal_class: Error')
	error_count = error_count + 1
# %$$
#
# $head double_class$$
# $srccode%cpp%
two   = py_example.double_class(2.0)
three = py_example.double_class(3.0)
five  = two + three
ok       = five == py_example.double_class(5.0)
ok       = ok and 4.5 < five.value()  and five.value() < 5.5
if ok :
	print('py_example.double_class: OK')
else :
	print('py_example.double_class: Error')
	error_count = error_count + 1
# %$$
#
# $head Set Exit Code$$
# $srccode%cpp%
import sys
sys.exit(error_count)
# %$$
#
# $end
