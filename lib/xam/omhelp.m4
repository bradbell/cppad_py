# -----------------------------------------------------------------------------
#         cppad_py: A C++ Object Library and Python Interface to Cppad
#          Copyright (C) 2017-18 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
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
# $section M4 Macro That Include Omhelp to Display Source Code$$
#
# $head Syntax$$
# $codei%Omhelp_(%FunctionName_%, %Omhelp_title%)%$$
#
# $head FunctionName_$$
# is the name of function corresponding to this output file; see
# $cref/FunctionName_/xam_file_name.m4/FunctionName_/$$.
#
# $head Omhelp_title$$
# is the title of this Omhelp section that displays this source code.
#
# $head Omhelp_tag$$
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
# $subhead lang_file_name$$
# The name of the source code file where the current output is placed
# is assumed to be
# $codei%
#	lib/example/%language%/%lang_file_name%
# %$$
# see $cref/language/xam.m4/language/$$ and
# $cref/lang_file_name/xam_file_name.m4/lang_file_name/$$.
#
# $subhead Formatting$$
# Let $icode source code$$ denote the language specific source code
# and $icode comment$$ denote the commenting characters.
# The input file is assumed to have the following format / order:
# $codei%
#	%comment% BEGIN SOURCE
#	%source code%
#	%comment% END SOURCE
#	Omhelp_(%name_xam%, %Omhelp_title%)
# %$$
#
# $end
# -----------------------------------------------------------------------------
# OmhelpOther_(Omhelp_tag, file_name, Omhelp_title)
define(OmhelpOther_,
`#' `$'begin $1$$ $newlinech `#$$'
`#' $spell
`#'	py
`#'	perl
`#'	cppad
`#'	py
`#'	xam
`#'	Jacobian
`#'	Jacobians
`#' $$
`#' $section $3$$
`#' $srcfile|$2|0|`#' BEGIN SOURCE|`#' END SOURCE|$$
`#' $end)
# OmhelpOctave_(Omhelp_tag, file_name, Omhelp_title)
define(OmhelpOctave_,
% `$'begin $1$$ $newlinech %$$
% $spell
%	cppad
%	py
%	xam
%	Jacobian
%	Jacobians
% $$
% $section $3$$
% $srcfile|$2|0|% BEGIN SOURCE|% END SOURCE|$$
% $end)
# OmhelpCpp_(Omhelp_tag, file_name, Omhelp_title)
define(OmhelpCpp_,
/*
`$'begin $1$$
$spell
	cplusplus
	cppad
	py
	xam
	Jacobian
	Jacobians
$$
$section $3$$
$srcfile|$2|0|// BEGIN SOURCE|// END SOURCE|$$
$end
*/)
# OmhelpAny_(Omhelp_tag, file_name, Omhelp_title)
define(OmhelpAny_,
``ifelse(
	Language_,
	cplusplus,
	`OmhelpCpp_($1,$2,$3)',
	Language_,
	octave,
	`OmhelpOctave_($1,$2,$3)',
	`OmhelpOther_($1,$2,$3)')'')
# Omhelp_(name_xam, Omhelp_title)
define(Omhelp_, OmhelpAny_(
	`$1.Ext_',dnl                         Omhelp_tag
	`lib/example/Language_/$1.Ext_',dnl file_name
	`$2'dnl                               Omhelp_title
))
# -----------------------------------------------------------------------------
