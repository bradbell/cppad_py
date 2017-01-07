
% This file can be automatically generated using the following command
% m4 ../octave.m4 ../../xam/a_double_xam.xam > a_double_xam.m
% -----------------------------------------------------------------------------
%         cppad_swig: A C++ Object Library and Swig Interface to Cppad
%          Copyright (C) 2017-17 Bradley M. Bell (bradbell@seanet.com)
%              This program is distributed under the terms of the
%          GNU Affero General Public License version 3.0 or later see
%                     http://www.gnu.org/licenses/agpl.txt
% -----------------------------------------------------------------------------
% a_double
% -----------------------------------------------------------------------------
% BEGIN SOURCE
function ok = a_double_xam()
	%
	% load the Cppad Swig library
	m_cppad
	%
	% initialize return variable
	ok = true;
	two = m_cppad.a_double(2.0);
	three = m_cppad.a_double(3.0);
	%
	five = two + three;
	six = two * three;
	neg_one = two - three;
	two_thirds = two / three;
	%
	ok = ok && five.value() == 5.0;
	ok = ok && six.value() == 6.0;
	ok = ok && neg_one.value() == -1.0;
	ok = ok && 0.5 < two_thirds.value();
	ok = ok && two_thirds.value() < 1.0;
	ok = ok && five < six;
	%
	return;
end
% END SOURCE
%
% $begin a_double_xam.m$$ $newlinech %$$
% $spell
%	cppad
%	xam
% $$
% $code
% $section octave: a_double Example and Test$$
% $verbatim|lib/example/octave/a_double_xam.m|0|% BEGIN SOURCE|% END SOURCE|$$
% $$
% $end

