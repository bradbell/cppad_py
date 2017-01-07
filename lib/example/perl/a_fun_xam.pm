
# This file can be automatically generated using the following command
# m4 ../perl.m4 ../../xam/a_fun_xam.xam > a_fun_xam.pm
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
package a_fun_xam;
sub a_fun_xam() {
	# check for standard perl programming conventions
	use strict;
	use warnings;
	#
	# load the Cppad Swig library
	use pm_cppad;
	#
	# initilaize return variable
	my $ok = 1;
	my $n = 2;
	#
	# create ax
	my $x = new pm_cppad::vector_double(n);
	for(my $i = 0; $i < $n ; $i++) {
		$x->set($i, $i + 1.0);
	}
	my $ax = pm_cppad::independent(x);
	#
	# create af
	my $ax0 = $ax->get(0);
	my $ax1 = $ax->get(1);
	my $ay = new pm_cppad::vector_ad(1);
	$ay->set(0, $ax0 + $ax0 - $ax1);
	my $af = new pm_cppad::a_fun($ax, $ay);
	#
	# zero order forward
	$x->set(0, 3.0);
	$x->set(1, 1.0);
	my $y = $af->forward(0, $x);
	$ok = $ok && $y->get(0) == 5.0;
	#
	# first order forward
	$x->set(0, 0.0);
	$x->set(1, 1.0);
	$y = $af->forward(1, $x);
	$ok = $ok && $y->get(0) == -1.0;
	#
	return( $ok );
}
# END SOURCE
#
# $begin a_fun_xam.pm$$ $newlinech #$$
# $spell
#	py
#	perl
#	cppad
#	xam
# $$
# $section pm_cppad: a_fun_xam: Example and Test$$
# $srcfile|lib/example/perl/a_fun_xam.pm|0|# BEGIN SOURCE|# END SOURCE|$$
# $end

