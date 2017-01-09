divert(-1)
# -----------------------------------------------------------------------------
#         cppad_swig: A C++ Object Library and Swig Interface to Cppad
#          Copyright (C) 2017-17 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#          GNU Affero General Public License version 3.0 or later see
#                     http://www.gnu.org/licenses/agpl.txt
# -----------------------------------------------------------------------------
# $begin xam.m4$$ $newlinech #$$
# $spell
#	xam
#	cplusplus
#	perl
#	cppad
# $$
# $section Include File for Library Example Setup$$
#
# $head Syntax$$
# $code include(xam.m4)$$
#
# $head m4 Command$$
# For this documentation, it is assumed that the m4 command is a follows:
# $codei%
#	m4 -I %directory% -D language_=%language% %input_file%
# %$$
#
# $head directory$$
# is the directory where the $code xam.m4$$ file is located; i.e.,
# $code lib/xam/xam.m4$$ relative to the Cppad Swig source directory.
#
# $head language$$
# is one of the available languages; i.e.,
# $code cplusplus$$, $code octave$$, $code perl$$, or $code python$$.
#
# $head input_file$$
# is the input file that can use the $cref lang_m4$$ and $cref omhelp.m4$$
# macros.
#
# $childtable%lib/xam/lang_m4.omh
#	%lib/xam/omhelp.m4
#	%lib/xam/xam_file_name.m4
# %$$
#
# $end
#
include(language_.m4)
include(omhelp.m4)
include(xam_file_name.m4)
# -----------------------------------------------------------------------------
divert(0)dnl trun on output and ignore this end of line
