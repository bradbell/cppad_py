% -----------------------------------------------------------------------------
%         cppad_swig: A C++ Object Library and Swig Interface to Cppad
%          Copyright (C) 2017-17 Bradley M. Bell (bradbell@seanet.com)
%              This program is distributed under the terms of the
%          GNU Affero General Public License version 3.0 or later see
%                     http://www.gnu.org/licenses/agpl.txt
% -----------------------------------------------------------------------------
error_count = 0;
function ok = run_test(name)
	eval( strcat( 'ok = ' , name , '();' ) )
	if ok
		printf( strcat('octave: ', name , ': OK\n') )
	else
		printf( strcat('octave: ', name , ': Error\n') )
		error_count = error_count + 1;
	end
end
fun_list = {
	'a_double_value_xam',
	'a_double_ad_binary_xam',
	'a_double_bool_binary_xam',
	'a_fun_a_fun_xam',
	'vector_ad_xam',
	'vector_double_xam'
}';
for fun = fun_list
	name  = cell2mat(fun);
	run_test(name);
end
%
if error_count > 0
	printf('octave: check_all: error_count = %d\n', error_count)
	exit(1)
end
printf('octave: check_all: OK\n')
exit(0)
