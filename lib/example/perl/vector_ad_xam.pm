# This file can be automatically generaeted using the following command
# m4 ../perl.m4 ../../xam/vector_ad_xam.xam > vector_ad_xam.pl
# -----------------------------------------------------------------------------
#         cppad_swig: A C++ Object Library and Swig Interface to Cppad
#          Copyright (C) 2017-17 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#          GNU Affero General Public License version 3.0 or later see
#                     http://www.gnu.org/licenses/agpl.txt
# -----------------------------------------------------------------------------
# std::vector<a_double>
# -----------------------------------------------------------------------------
package vector_ad_xam;
sub vector_ad_xam() {
	# check for standard perl programming conventions
	use strict;
	use warnings;
	#
	# load the Cppad Swig library
	use pl_cppad;
	#
	# initilaize return variable
	my $ok = 1;
	my $n = 4;
	my $a_vec = new pl_cppad::vector_ad(n);
	#
	# check size
	$ok = $ok && $a_vec->size() == n;
	#
	# setting elements
	for(my $i = 0; $i < $n ; $i++) {
		my $ad = new pl_cppad::a_double(2.0 * i);
		$a_vec->set($i, $ad);
	}
	# getting elements
	for(my $i = 0; $i < $n ; $i++) {
		my $a_element = $a_vec->get($i);
		$ok = $ok && $a_element->value() == 2.0 * $i;
	}
	return( $ok );
}
