# -----------------------------------------------------------------------------
#         cppad_swig: A C++ Object Library and Swig Interface to Cppad
#          Copyright (C) 2017-17 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#          GNU Affero General Public License version 3.0 or later see
#                     http://www.gnu.org/licenses/agpl.txt
# -----------------------------------------------------------------------------
# $begin omhelp.m4$$
#
# $section m4 Macro That Outputs OMhelp to Display Source Code$$
#
# $head Syntax$$
# $codei%omhelp_(%name%)%$$
#
# $head name_xam$$
# is the name of module object that is tested by this file.
#
# $head omhelp_tag$$
# is the omhelp cross reference tag that will be used for this section is
# $codei%
#	%name%_xam.%ext%
# %$$
# where $icode ext$$ is the file extension used for the
# current language.
#
# $head file_name$$
# is the name of the source code file where the current output is placed.
# This is assumed to be
# $codei%
#	lib/example/%language%.%name%_xam.%ext_%
# %$$
# where $icode language$$ is $code cplusplus$$, $code octave$$,
# $code perl$$, or $code python$$.
#
# $head omhelp_title$$
# is the title of the omhelp section contains the module, $icode name$$
# and the text $code Example and Text$$.
#
# $head Assumption$$
# $list number$$
# The $icode source code$ is surrounded in the following way:
# $codei%
#	%comment% BEGIN SOURCE
#	%source code%
#	%comment% END SOURCE
# %$$
# $lnext
# The $code omhelp_$$ commannd comes after $code END SOURCE$$ above;
# i.e., its output appears below $code END SOURCE$$ in the output file.
# $lend
#
# $end
# -----------------------------------------------------------------------------
# omhelp_other_(comment, omhelp_tag, file_name, omhelp_title)
define(omhelp_other_,
$1 `$'begin $2`$$'
$1 `$'section $4`$$'
$1 `$'srcfile|$3|0|$1 BEGIN SOURCE|$1 END SOURCE|`$$'
$1 `$'end)
# omhelp_cpp_(omhelp_tag, file_name, omhelp_title)
define(omhelp_cpp_,
/*
`$'begin $1`$$'
`$'section $3`$$'
`$'srcfile|$2|0|// BEGIN SOURCE|// END SOURCE|`$$'
`$'end
*/)
# omhelp_any_(comment, omhelp_tag, file_name, title)
define(omhelp_any_,
`ifelse(`$1', //, `omhelp_cpp_($2,$3,$4)', `omhelp_other_(`$1',$2,$3,$4)')'
)
# omhelp_(name_xam)
define(omhelp_, omhelp_any_(
	`c_',dnl
	`$1.ext_',dnl
	`example/language_/$1.ext_',dnl
	`module_($1): Example and Test'dnl
))
# -----------------------------------------------------------------------------
