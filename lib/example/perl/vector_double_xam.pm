
# This file can be automatically generaeted using the following command
# m4 ../perl.m4 ../../xam/vector_double_xam.xam > vector_double_xam.pm
# -----------------------------------------------------------------------------
#         cppad_swig: A C++ Object Library and Swig Interface to Cppad
#          Copyright (C) 2017-17 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#          GNU Affero General Public License version 3.0 or later see
#                     http://www.gnu.org/licenses/agpl.txt
# -----------------------------------------------------------------------------
# std::vector<double>
# -----------------------------------------------------------------------------
# BEGIN SOURCE
package vector_double_xam;
sub vector_double_xam() {
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
	my $vec = new pm_cppad::vector_double(n);
	#
	# check size
	$ok = $ok && $vec->size() == n;
	#
	# setting elements
	for(my $i = 0; $i < $n ; $i++) {
		$vec->set($i, 2.0 * $i);
	}
	# getting elements
	for(my $i = 0; $i < $n ; $i++) {
		my $element = $vec->get($i);
		$ok = $ok && $element == 2.0 * $i;
	}
	return( $ok );
}
# END SOURCE
#
# $begin vector_double_xam.pm$$ $newlinech #$$
# $spell
#	py
#	perl
#	cppad
#	xam
# $$
# $section pm_cppad: vector_double_xam: Example and Test$$
# $srcfile|lib/example/perl/vector_double_xam.pm|0|# BEGIN SOURCE|# END SOURCE|$$
# $end

