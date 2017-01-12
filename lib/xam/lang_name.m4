# -----------------------------------------------------------------------------
#         cppad_swig: A C++ Object Library and Swig Interface to Cppad
#          Copyright (C) 2017-17 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#          GNU Affero General Public License version 3.0 or later see
#                     http://www.gnu.org/licenses/agpl.txt
# -----------------------------------------------------------------------------
# $begin lang_name.m4$$ $newlinech #$$
# $spell
#	Lang
#	cplusplus
#	perl
# $$
# $section Language Name$$
#
# $head Syntax$$
# $code LangName_$$
#
# $head Result$$
# The result is the name for this language as follows:
# $table
# $icode language$$ $cnext $icode Name$$     $rnext
# $code cplusplus$$ $cnext $code C++$$       $rnext
# $code octave$$    $cnext $code Octave$$    $rnext
# $code perl$$      $cnext $code Perl$$      $rnext
# $code python$$    $cnext $code Python$$
# $tend
#
# $head Assumption$$
# The $cref/Language_/xam.m4/language/$$ macro has been set to one
# of the $icode language$$ values above.
#
# $end
define(LangName_,
`ifelse(
	Language_,
	cplusplus,
	C++,
	Language_,
	octave,
	Octave,
	Language_,
	perl,
	Perl,
	Language_,
	python,
	Python,
	`Error: invalid value for Language_')'dnl
)
