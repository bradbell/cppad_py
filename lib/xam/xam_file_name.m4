# -----------------------------------------------------------------------------
#         cppad_swig: A C++ Object Library and Swig Interface to Cppad
#          Copyright (C) 2017-17 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#          GNU Affero General Public License version 3.0 or later see
#                     http://www.gnu.org/licenses/agpl.txt
# -----------------------------------------------------------------------------
# $begin xam_file_name.m4$$ $newlinech #$$
# $spell
#	xam
#	lang
# $$
#
# $section Function and File Naming$$
#
# $head Syntax$$
# $codei%lang_file_name_(%xam_file_name%)
# %$$
# $codei%function_name_(%xam_file_name%)
# %$$
#
# $head xam_file_name$$
# Is the name of an $icode%*%.xam%$$ file relative to the
# $code lib/xam$$ directory.
#
# $head function_name$$
# The output value of $code function_name_$$ has all the forward slash
# $code /$$ characters converted to under bar $code _$$ characters
# and the file extension $code .xam$$ removed.
#
# $head lang_file_name$$
# The output value of $code lang_file_name_$$ has all the forward slash
# $code /$$ characters converted to under bar $code _$$ characters
# and the file extension $code .xam$$ converted to
# $cref/ext_/lang_m4/No Arguments/ext_/$$.
#
# $head Assumptions$$
# It is assumed that the following macro has been set:
# $cref/ext_/lang_m4/No Arguments/ext_/$$.
#
# $end
# -----------------------------------------------------------------------------
define(function_name_,  `patsubst( `patsubst(`$1', /, _)', [.]xam, `')')
define(lang_file_name_, `patsubst( `patsubst(`$1', /, _)', [.]xam, .ext_)')
