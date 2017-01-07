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
# $$
# $section Include File for Library Example Setup$$
#
# $head Syntax$$
# $code include(xam.m4)$$
#
# $head language_$$
# It is assumed that the macro $code language_$$ has been defined to
# be one of the available languages; i.e.,
# $code cplusplus$$, $code octave$$, $code perl$$, or $code python$$.
#
# $head Directory$$
# The include command above must be executed in the $code lib/xam$$
# directory.
#
# $childtable%lib/xam/lang_m4.omh
#	%lib/xam/omhelp.m4
# %$$
#
# $end
#
include(language_.m4)
include(omhelp.m4)
# -----------------------------------------------------------------------------
divert(0)dnl trun on output and ignore this end of line
