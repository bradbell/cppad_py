% -----------------------------------------------------------------------------
%         cppad_swig: A C++ Object Library and Swig Interface to Cppad
%          Copyright (C) 2017-17 Bradley M. Bell (bradbell@seanet.com)
%              This program is distributed under the terms of the
%          GNU Affero General Public License version 3.0 or later see
%                     http://www.gnu.org/licenses/agpl.txt
% -----------------------------------------------------------------------------
% $begin check_swig_xam.m$$ $newlinech %$$
% $spell
%	xam
%	std
%	ptr
% #$$
%
% $section Octave Script That Tests m_swig_xam$$
%
% $head Load the Module$$
% $srccode#cpp#
m_swig_xam
% #$$
%
% $head Initialize Error Count$$
% $srccode#cpp#
error_count = 0;
% #$$
%
% $head factorial_by_value$$
% $srccode#cpp#
if (m_swig_xam.factorial_by_value(4) == 24)
	printf('m_swig_xam.factorial_by_value: OK\n')
else
	printf('m_swig_xam.factorial_by_value: Error\n')
	error_count = error_count + 1;
end
% #$$
% see C++ $cref/factorial_by_value/swig_xam_function/factorial_by_value/$$.
%
% $head message_of_void$$
% $srccode#cpp#
if (m_swig_xam.message_of_void() == 'OK' )
	printf('m_swig_xam.message_of_void: OK\n')
else
	printf('m_swig_xam.message_of_void: Error\n')
	error_count = error_count + 1;
end
% #$$
% see C++ $cref/message_of_void/swig_xam_function/message_of_void/$$.
%
% $head int_class$$
% $srccode#cpp#
obj = m_swig_xam.int_class();
m_swig_xam.add_by_ptr(3, 4, obj)
if( obj.value() == 7 )
	printf('m_swig_xam.add_by_ptr: OK\n')
else
	printf('m_swig_xam.add_by_ptr: Error\n')
	error_count = error_count + 1;
end
% #$$
% see Swig $cref/int_class/swig_xam.i/int_class/$$ and
% C++ $cref/add_by_ptr/swig_xam_function/add_by_ptr/$$.
%
% $head int_array_ptr$$
% $srccode#cpp#
n   = 10;
array_ptr = m_swig_xam.new_int_array_ptr(n);
for i = 0 : (n-1)
	m_swig_xam.int_array_ptr_setitem(array_ptr, i, 2 * i);
end
if( m_swig_xam.max_array_by_ptr(n, array_ptr) == 18 )
	printf('m_swig_xam.max_array_by_ptr: pointer:  OK\n')
else
	printf('m_swig_xam.max_array_by_ptr: pointer:  Error\n')
	error_count = error_count + 1;
end
m_swig_xam.delete_int_array_ptr(array_ptr);
% #$$
% see Swig $cref/int_array_ptr/swig_xam.i/int_array_ptr/$$ and
% C++ $cref/max_array_by_ptr/swig_xam_function/max_array_by_ptr/$$.
%
% $head int_array_class$$
% $srccode#cpp#
n   = 10;
array_obj = m_swig_xam.int_array_class(n);
for i = 0 : (n-1)
	array_obj(i) = 2 * i;
end
if( m_swig_xam.max_array_by_ptr(n, array_obj) == 18 )
	printf('m_swig_xam.max_array_by_ptr: class:  OK\n')
else
	printf('m_swig_xam.max_array_by_ptr: class:  Error\n')
	error_count = error_count + 1;
end
% #$$
% see Swig $cref/int_array_class/swig_xam.i/int_array_class/$$ and
% C++ $cref/max_array_by_ptr/swig_xam_function/max_array_by_ptr/$$.
%
% $head vector_double$$
% $srccode%cpp%
n   = 10;
vec = m_swig_xam.vector_double(n);
for i = [ 0 : (n-1) ]
	vec(i) = 2.0 * i;
end
if( m_swig_xam.max_std_vector_double(vec) == 18.0 )
	printf('m_swig_xam.max_std_vector_double: class: OK\n')
else
	printf('m_swig_xam.max_std_vector_double: class: Error\n')
	error_count = error_count + 1;
end
% %$$
% see Swig $cref/vector_double/swig_xam.i/vector_double/$$ and
% C++ $cref/max_std_vector_double/swig_xam_function/max_std_vector_double/$$.
%
% $head raise_exception$$
% $srccode#cpp#
try
	m_swig_xam.raise_exception('test message');
	message = '';
catch
	message = m_swig_xam.raise_exception('');
end
if( message == 'test message' )
	printf('m_swig_xam.raise_exception: OK\n')
else
	printf('m_swig_xam.raise_exception.message_of_void: Error\n')
	error_count = error_count + 1
end
% #$$
% see C++ $cref/raise_exception/swig_xam_function/raise_exception/$$.
%
% $head normal_class$$
% $srccode#cpp#
two   = m_swig_xam.normal_class(2);
three = m_swig_xam.normal_class(3);
five  = two + three;
ok       = five == m_swig_xam.normal_class(5);
ok       = ok & (4 < five.value() ) & (five.value() < 6);
if( ok )
	printf('m_swig_xam.normal_class: OK\n')
else
	printf('m_swig_xam.normal_class: Error\n')
	error_count = error_count + 1
end
% #$$
% see C++ $cref example_normal_class$$.
%
% $head double_class$$
% $srccode#cpp#
two   = m_swig_xam.double_class(2.0);
three = m_swig_xam.double_class(3.0);
five  = two + three;
ok       = five == m_swig_xam.double_class(5.0);
ok       = ok & (4.5 < five.value() ) & (five.value() < 5.5);
if( ok )
	printf('m_swig_xam.double_class: OK\n')
else
	printf('m_swig_xam.double_class: Error\n')
	error_count = error_count + 1
end
% #$$
% see Swig $cref/double_class/swig_xam.i/double_class/$$.
%
% $head Set Exit Code$$
% $srccode#cpp#
exit(error_count)
% #$$
%
% $end
