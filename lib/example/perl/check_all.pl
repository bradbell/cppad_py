# -----------------------------------------------------------------------------
#         cppad_swig: A C++ Object Library and Swig Interface to Cppad
#          Copyright (C) 2017-17 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# -----------------------------------------------------------------------------
use strict;
use warnings;
use feature 'say';
#
my $error_count = 0;
sub run_test
{	my $name = shift;
	my $ok   = 1;
	my $command = "use $name ; \$ok = $name::$name();";
	#
	eval( $command );die $@ if($@);
	#
	if( $ok )
	{	print "perl: $name: OK\n"; }
	else
	{	print "perl: $name: Error\n";
		$error_count = $error_count + 1;
	}
}
#
my @fun_list = (
	'a_double_cond_assign_xam',
	'a_double_property_xam',
	'a_double_unary_fun_xam',
	'a_double_unary_op_xam',
	'a_double_assign_xam',
	'a_double_ad_binary_xam',
	'a_double_compare_xam',
	'vector_size_xam',
	'vector_set_get_xam',
	'a_fun_property_xam',
	'a_fun_optimize_xam',
	'a_fun_jacobian_xam',
	'a_fun_hessian_xam',
	'a_fun_forward_xam',
	'a_fun_reverse_xam',
	'a_fun_abort_xam',
	'sparse_rc_xam',
	'other_error_message_xam'
);
for( my $i = 0; $i <= $#fun_list; $i++)
{	my $name = $fun_list[$i];
	run_test($name);
}
if( $error_count > 0 )
{	print 'perl: check_all: error_count = ', $error_count, "\n";
	exit 1;
}
print "perl: check_all: OK\n";
exit 0;
