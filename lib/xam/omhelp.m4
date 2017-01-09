# -----------------------------------------------------------------------------
#         cppad_swig: A C++ Object Library and Swig Interface to Cppad
#          Copyright (C) 2017-17 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#          GNU Affero General Public License version 3.0 or later see
#                     http://www.gnu.org/licenses/agpl.txt
# -----------------------------------------------------------------------------
# $begin omhelp.m4$$ $newlinech #$$
# $spell
#	lang
#	Omhelp
#	xam
#	cplusplus
#	perl
# $$
#
# $section m4 Macro That Include Omhelp to Display Source Code$$
#
# $head Syntax$$
# $codei%omhelp_(%name_xam%, %omhelp_title%)%$$
#
# $head name_xam$$
# is the name of module object that is tested by this file.
#
# $head omhelp_title$$
# is the title of this Omhelp section that displays this source code.
#
# $head omhelp_tag$$
# The Omhelp cross reference tag that will be used for this section is
# $codei%
#	%name_xam%.%ext%
# %$$
# where $icode ext$$ is the file extension used for the
# current language.
#
#
# $head Assumption$$
#
# $subhead lang_m4$$
# It is assumed that the macros in $cref lang_m4$$ have been
# set for the $cref/language/xam.m4/language/$$
# that the output corresponds to.
#
# $subhead file_name$$
# The name of the source code file where the current output is placed
# is assumed to be
# $codei%
#	build/lib/example/%language%.%name_xam%.%ext%
# %$$
# where $icode language$$ is $code cplusplus$$, $code octave$$,
# $code perl$$, or $code python$$.
#
# $subhead Formatting$$
# Let $icode source code$$ denote the language specific source code
# and $icode comment$$ denote the commenting characters.
# The input file is assumed to have the following format / order:
# $codei%
#	%comment% BEGIN SOURCE
#	%source code%
#	%comment% END SOURCE
#	omhelp_(%name_xam%, %omhelp_title%)
# %$$
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
% $section $3$$
% $srcfile|$2|0|% BEGIN SOURCE|% END SOURCE|$$
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
# omhelp_(name_xam, omhelp_title)
define(omhelp_, omhelp_any_(
	`$1.ext_',dnl                         omhelp_tag
	`build/lib/example/language_/$1.ext_',dnl file_name
	`$2'dnl                               omhelp_title
))
# -----------------------------------------------------------------------------
