# -----------------------------------------------------------------------------
#         cppad_swig: A C++ Object Library and Swig Interface to Cppad
#          Copyright (C) 2017-17 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#          GNU Affero General Public License version 3.0 or later see
#                     http://www.gnu.org/licenses/agpl.txt
# -----------------------------------------------------------------------------
# $begin header$$
# $spell
# $$
#
# $section Comment Shwoing How to Generate This Output$$
#
# $head Syntax$$
# $codei%header_(%xam_file_name%)
#
# $head xam_file_name$$
# Is the name of the $icode%*%.xam%$$ file, relative to the
# $code lib/xam$$ directory, that this output corresponds to.
#
# $head Assumptions$$
# It is assumed that the following macros have been set:
# $cref/c_/lang_m4/No Arguments/c_/$$,
# $cref/language_/xam.m4/No Arguments/language_/$$.
#
# $end
# -----------------------------------------------------------------------------
define(header_,dnl
`c_' This file can be generated in the lib/xam directory using the command:
`c_' m4 -D ``language_''=language_ $1)
