
% This file can be automatically generaeted using the following command
% m4 ../octave.m4 ../xam/vector_ad_xam.m4 > vector_ad_xam.m
% -----------------------------------------------------------------------------
%         cppad_swig: A C++ Object Library and SWIG Interface to CppAD
%          Copyright (C) 2017-17 Bradley M. Bell (bradbell@seanet.com)
%              This program is distributed under the terms of the
%          GNU Affero General Public License version 3.0 or later see
%                     http://www.gnu.org/licenses/agpl.txt
% -----------------------------------------------------------------------------
% std::vector<a_double>
% -----------------------------------------------------------------------------
function ok = vector_ad_xam()
	%
	% load the cppad swig library
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
