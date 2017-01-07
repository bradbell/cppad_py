# -----------------------------------------------------------------------------
#         cppad_swig: A C++ Object Library and Swig Interface to Cppad
#          Copyright (C) 2017-17 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#          GNU Affero General Public License version 3.0 or later see
#                     http://www.gnu.org/licenses/agpl.txt
# -----------------------------------------------------------------------------
# $begin omhelp.m4$$ $newlinech #$$
# $spell
#	Omhelp
#	xam
#	cplusplus
#	perl
# $$
#
# $section m4 Macro That Include Omhelp to Display Source Code$$
#
# $head Syntax$$
# $codei%omhelp_(%name_xam%)%$$
#
# $head name_xam$$
# is the name of module object that is tested by this file.
#
# $head omhelp_tag$$
# is the Omhelp cross reference tag that will be used for this section is
# $codei%
#	%name_xam%.%ext%
# %$$
# where $icode ext$$ is the file extension used for the
# current language.
#
# $head file_name$$
# is the name of the source code file where the current output is placed.
# This is assumed to be
# $codei%
#	lib/example/%language%.%name_xam%.%ext%
# %$$
# where $icode language$$ is $code cplusplus$$, $code octave$$,
# $code perl$$, or $code python$$.
#
# $head omhelp_title$$
# is the title of the Omhelp section contains the module, $icode name$$
# and the text $code Example and Text$$.
#
# $head Assumption$$
# $list number$$
# The $icode source code$$ is surrounded in the following way:
# $codei%
#	%comment% BEGIN SOURCE
#	%source code%
#	%comment% END SOURCE
# %$$
# $lnext
# The $code omhelp_$$ command comes after $code END SOURCE$$ above;
# i.e., its output appears below $code END SOURCE$$ in the output file.
# $lend
#
# $end
# -----------------------------------------------------------------------------
# omhelp_other_(omhelp_tag, file_name, omhelp_title)
define(omhelp_other_,
`#' `$'begin $1$$ $newlinech `#$$'
`#' $spell
`#'	py
`#'	perl
`#'	cppad
`#'	xam
`#' $$
`#' $section $3$$
`#' $srcfile|$2|0|`#' BEGIN SOURCE|`#' END SOURCE|$$
`#' $end)
# omhelp_octave_(omhelp_tag, file_name, omhelp_title)
define(omhelp_octave_,
% `$'begin $1$$ $newlinech %$$
% $spell
%	cppad
%	xam
% $$
% $code
% $section $3$$
% $verbatim|$2|0|% BEGIN SOURCE|% END SOURCE|$$
% $$
% $end)
# omhelp_cpp_(omhelp_tag, file_name, omhelp_title)
define(omhelp_cpp_,
/*
`$'begin $1$$
$spell
	cplusplus
	cppad
	xam
$$
$section $3$$
$srcfile|$2|0|// BEGIN SOURCE|// END SOURCE|$$
$end
*/)
# omhelp_any_(omhelp_tag, file_name, omhelp_title)
define(omhelp_any_,
`ifelse(
	language_,
	cplusplus,
	`omhelp_cpp_($1,$2,$3)',
	language_,
	octave,
	`omhelp_octave_($1,$2,$3)',
	`omhelp_other_($1,$2,$3)')'
)
# omhelp_(name_xam)
define(omhelp_, omhelp_any_(
	`$1.ext_',dnl                       omhelp_tag
	`lib/example/language_/$1.ext_',dnl file_name
	`module_: $1: Example and Test'dnl  omhelp_title
))
# -----------------------------------------------------------------------------
