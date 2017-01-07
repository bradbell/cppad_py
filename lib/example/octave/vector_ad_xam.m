
% This file can be automatically generated using the following command
% m4 ../octave.m4 ../../xam/vector_ad_xam.xam > vector_ad_xam.m
% -----------------------------------------------------------------------------
%         cppad_swig: A C++ Object Library and Swig Interface to Cppad
%          Copyright (C) 2017-17 Bradley M. Bell (bradbell@seanet.com)
%              This program is distributed under the terms of the
%          GNU Affero General Public License version 3.0 or later see
%                     http://www.gnu.org/licenses/agpl.txt
% -----------------------------------------------------------------------------
% std::vector<a_double>
% -----------------------------------------------------------------------------
% BEGIN SOURCE
function ok = vector_ad_xam()
	%
	% load the Cppad Swig library
	m_cppad
	%
	% initialize return variable
	ok = true;
	n = 4;
	a_vec = m_cppad.vector_ad(n);
	%
	% check size
	ok = ok && a_vec.size() == n;
	%
	% setting elements
	for i = [ 0 :(n -1) ]
		ad = m_cppad.a_double(2.0 * i);
		a_vec(i) = ad;
	end
	% getting elements
	for i = [ 0 :(n -1) ]
		a_element = a_vec(i);
		ok = ok && a_element.value() == 2.0 * i;
	end
	return;
end
% END SOURCE
%
% $begin vector_ad_xam.m$$ $newlinech %$$
% $spell
%	cppad
%	xam
% $$
% $code
% $section m_cppad: vector_ad_xam: Example and Test$$
% $verbatim|lib/example/octave/vector_ad_xam.m|0|% BEGIN SOURCE|% END SOURCE|$$
% $$
% $end

