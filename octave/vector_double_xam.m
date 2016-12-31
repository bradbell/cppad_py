
% This file can be automatically generaeted using the following command
% m4 ../octave.m4 ../xam/vector_double_xam.m4 > vector_double_xam.m
% -----------------------------------------------------------------------------
%         cppad_swig: A C++ Object Library and SWIG Interface to CppAD
%          Copyright (C) 2017-17 Bradley M. Bell (bradbell@seanet.com)
%              This program is distributed under the terms of the
%          GNU Affero General Public License version 3.0 or later see
%                     http://www.gnu.org/licenses/agpl.txt
% -----------------------------------------------------------------------------
% std::vector<double>
% -----------------------------------------------------------------------------
function ok = vector_double_xam()
	%
	% load the cppad swig library
	m_cppad
	%
	% initialize return variable
	ok = true;
	n = 4;
	vec = m_cppad.vector_double(n);
	%
	% check size
	ok = ok && vec.size() == n;
	%
	% setting elements
	for i = [ 0 :(n -1) ]
		vec(i) = 2.0 * i;
	end
	% getting elements
	for i = [ 0 :(n -1) ]
		element = vec(i);
		ok = ok && element == 2.0 * i;
	end
	return;
end
