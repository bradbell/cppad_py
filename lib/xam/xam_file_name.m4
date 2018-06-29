# -----------------------------------------------------------------------------
#         cppad_py: A C++ Object Library and Python Interface to Cppad
#          Copyright (C) 2017-18 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
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
# $codei%LangFileName_(%xam_file_name%)
# %$$
# $codei%FunctionName__(%xam_file_name%)
# %$$
#
# $head xam_file_name$$
# Is the name of an $icode%*%.xam%$$ file relative to the
# $code lib/xam$$ directory.
#
# $head FunctionName_$$
# The output value of $code FunctionName__$$ has all the forward slash
# $code /$$ characters converted to under bar $code _$$ characters
# and the file extension $code .xam$$ removed.
#
# $head lang_file_name$$
# The output value of $code LangFileName_$$ has all the forward slash
# $code /$$ characters converted to under bar $code _$$ characters
# and the file extension $code .xam$$ converted to
# $cref/Ext_/lang_m4/No Arguments/Ext_/$$.
#
# $head Assumptions$$
# It is assumed that the following macro has been set:
# $cref/Ext_/lang_m4/No Arguments/Ext_/$$.
#
# $end
# -----------------------------------------------------------------------------
define(FunctionName__,  `patsubst( `patsubst(`$1', /, _)', [.]xam, `')')
define(LangFileName_, `patsubst( `patsubst(`$1', /, _)', [.]xam, .Ext_)')
