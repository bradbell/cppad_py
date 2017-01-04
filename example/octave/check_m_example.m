% -----------------------------------------------------------------------------
%         cppad_swig: A C++ Object Library and SWIG Interface to CppAD
%          Copyright (C) 2017-17 Bradley M. Bell (bradbell@seanet.com)
%              This program is distributed under the terms of the
%          GNU Affero General Public License version 3.0 or later see
%                     http://www.gnu.org/licenses/agpl.txt
% -----------------------------------------------------------------------------
% $begin check_m_example.m$$ $newlinech %$$
% $spell
%	ptr
% #$$
%
% $section Octave Script That Tests m_example Swig Module$$
%
% $head Load the Module$$
% $srccode#cpp#
m_example
% #$$
%
% $head Initialize Error Count$$
% $srccode#cpp#
error_count = 0;
% #$$
%
% $head factorial_by_val$$
% $srccode#cpp#
if (m_example.factorial_by_val(4) == 24)
	printf('m_example.factorial_by_val: OK\n')
else
	printf('m_example.factorial_by_val: Error\n')
	error_count = error_count + 1;
end
% #$$
%
% $head message_of_void$$
% $srccode#cpp#
if (m_example.message_of_void() == 'OK' )
	printf('m_example.message_of_void: OK\n')
else
	printf('m_example.message_of_void: Error\n')
	error_count = error_count + 1;
end
% #$$
%
% $head int_class$$
% $srccode#cpp#
obj = m_example.int_class();
m_example.add_by_ptr(3, 4, obj)
if( obj.value() == 7 )
	printf('m_example.add_by_ptr: OK\n')
else
	printf('m_example.add_by_ptr: Error\n')
	error_count = error_count + 1;
end
% #$$
%
% $head int_array_ptr$$
% $srccode#cpp#
n   = 10;
array_ptr = m_example.new_int_array_ptr(n);
for i = 0 : (n-1)
	m_example.int_array_ptr_setitem(array_ptr, i, 2 * i);
endfor
if( m_example.max_array_by_ptr(n, array_ptr) == 18 )
	printf('m_example.max_array_by_ptr: pointer:  OK\n')
else
	printf('m_example.max_array_by_ptr: pointer:  Error\n')
	error_count = error_count + 1;
end
m_example.delete_int_array_ptr(array_ptr);
% #$$
%
% $head int_array_class$$
% $srccode#cpp#
n   = 10;
array_obj = m_example.int_array_class(n);
for i = 0 : (n-1)
	array_obj(i) = 2 * i;
endfor
if( m_example.max_array_by_ptr(n, array_obj) == 18 )
	printf('m_example.max_array_by_ptr: class:  OK\n')
else
	printf('m_example.max_array_by_ptr: class:  Error\n')
	error_count = error_count + 1;
end
% #$$
%
% $head raise_exception$$
% $srccode#cpp#
try
	m_example.raise_exception('test message');
	message = '';
catch
	message = m_example.raise_exception('');
end_try_catch
if( message == 'test message' )
	printf('m_example.m_example.raise_exception: OK\n')
else
	printf('m_example.raise_exception.message_of_void: Error\n')
	error_count = error_count + 1
end
% #$$
%
% $head normal_class$$
% $srccode#cpp#
two   = m_example.normal_class(2);
three = m_example.normal_class(3);
five  = two + three;
ok       = five == m_example.normal_class(5);
ok       = ok & (4 < five.value() ) & (five.value() < 6);
if( ok )
	printf('m_example.normal_class: OK\n')
else
	printf('m_example.normal_class: Error\n')
	error_count = error_count + 1
end
% #$$
%
% $head double_class$$
% $srccode#cpp#
two   = m_example.double_class(2.0);
three = m_example.double_class(3.0);
five  = two + three;
ok       = five == m_example.double_class(5.0);
ok       = ok & (4.5 < five.value() ) & (five.value() < 5.5);
if( ok )
	printf('m_example.double_class: OK\n')
else
	printf('m_example.double_class: Error\n')
	error_count = error_count + 1
end
% #$$
%
% $head Set Exit Code$$
% $srccode#cpp#
exit(error_count)
% #$$
%
% $end
