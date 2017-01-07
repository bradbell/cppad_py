
% This file can be automatically generaeted using the following command
% m4 ../octave.m4 ../../xam/a_fun_xam.xam > a_fun_xam.m
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
function ok = a_fun_xam()
	%
	% load the Cppad Swig library
	m_cppad
	%
	% initialize return variable
	ok = true;
	n = 2;
	%
	% create ax
	x = m_cppad.vector_double(n);
	for i = [ 0 :(n -1) ]
		x(i) = i + 1.0;
	end
	ax = m_cppad.independent(x);
	%
	% create af
	ax0 = ax(0);
	ax1 = ax(1);
	ay = m_cppad.vector_ad(1);
	ay(0) = ax0 + ax0 - ax1;
	af = m_cppad.a_fun(ax, ay);
	%
	% zero order forward
	x(0) = 3.0;
	x(1) = 1.0;
	y = af.forward(0, x);
	ok = ok && y(0) == 5.0;
	%
	% first order forward
	x(0) = 0.0;
	x(1) = 1.0;
	y = af.forward(1, x);
	ok = ok && y(0) == -1.0;
	%
	return;
end
% END SOURCE
%
% $begin a_fun.m$$
% $section m_cppad.a_fun: Example and Test$$
% $srcfile|example/octave/a_fun.m|0|% BEGIN SOURCE|% END SOURCE|$$
% $end

