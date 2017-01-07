
# This file can be automatically generated using the following command
# m4 ../perl.m4 ../../xam/vector_ad_xam.xam > vector_ad_xam.pm
# -----------------------------------------------------------------------------
#         cppad_swig: A C++ Object Library and Swig Interface to Cppad
#          Copyright (C) 2017-17 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#          GNU Affero General Public License version 3.0 or later see
#                     http://www.gnu.org/licenses/agpl.txt
# -----------------------------------------------------------------------------
# std::vector<a_double>
# -----------------------------------------------------------------------------
# BEGIN SOURCE
package vector_ad_xam;
sub vector_ad_xam() {
	# check for standard perl programming conventions
	use strict;
	use warnings;
	#
	# load the Cppad Swig library
	use pm_cppad;
	#
	# initilaize return variable
	my $ok = 1;
	my $n = 4;
	my $a_vec = new pm_cppad::vector_ad(n);
	#
	# check size
	$ok = $ok && $a_vec->size() == n;
	#
	# setting elements
	for(my $i = 0; $i < $n ; $i++) {
		my $ad = new pm_cppad::a_double(2.0 * i);
		$a_vec->set($i, $ad);
	}
	# getting elements
	for(my $i = 0; $i < $n ; $i++) {
		my $a_element = $a_vec->get($i);
		$ok = $ok && $a_element->value() == 2.0 * $i;
	}
	return( $ok );
}
# END SOURCE
#
# $begin vector_ad_xam.pm$$ $newlinech #$$
# $spell
#	py
#	perl
#	cppad
#	xam
# $$
# $section perl: vector_ad Example and Test$$
# $srcfile|lib/example/perl/vector_ad_xam.pm|0|# BEGIN SOURCE|# END SOURCE|$$
# $end

