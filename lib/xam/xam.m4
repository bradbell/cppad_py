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
#	dnl
#	newline
# $$
# $section Generating Language Specific Example Files Using M4 Macros$$
#
# $head Syntax$$
# $code include(xam.m4)dnl$$
#
# $head m4 Command$$
# For this documentation, it is assumed that the m4 command is a follows:
# $codei%
#	m4 -I %directory% -D Language_=%language% %xam_file_name%
# %$$
#
# $head directory$$
# is the directory where the $code xam.m4$$ file is located; i.e.,
# $code lib/xam$$ relative to the Cppad Swig source directory.
#
# $head language$$
# is one of the available languages; i.e.,
# $code cplusplus$$, $code octave$$, $code perl$$, or $code python$$.
#
# $head xam_file_name$$
# is the name of one of the *.xam files relative to the $code lib/xam$$
# directory; e.g., $code vector/ad_xam.xam$$.
# This, combined with the language, determines the example / test
# that is being created.
#
# $children%lib/xam/lang_m4.omh
#	%lib/xam/xam_file_name.m4
#	%lib/xam/header.m4
#	%lib/xam/lang_name.m4
#	%lib/xam/omhelp.m4
# %$$
# $head Includes$$
# Including $code xam.m4$$ includes the following macros:
# $list number$$
# $cref lang_m4$$
# $lnext
# $cref lang_name.m4$$
# $lnext
# $cref xam_file_name.m4$$
# $lnext
# $cref header.m4$$
# $lnext
# $cref omhelp.m4$$
# $lend
#
# $head Output$$
# There is no output during the include of $code xam.m4$$.
# To be specific, the output is diverted to $code -1$$ during the
# include of $code xam.m4$$ and restored to $code 0$$ after it.
# The $code dnl$$
# in the $cref/syntax/xam.m4/Syntax/$$ above suppresses the output
# of the newline at the end of the include of $code xam.m4$$.
#
# $end
#
include(Language_.m4)
include(lang_name.m4)
include(header.m4)
include(xam_file_name.m4)
include(omhelp.m4)
# -----------------------------------------------------------------------------
divert(0)dnl trun on output and ignore this end of line
