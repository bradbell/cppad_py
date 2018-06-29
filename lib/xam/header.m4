# -----------------------------------------------------------------------------
#         cppad_py: A C++ Object Library and Python Interface to Cppad
#          Copyright (C) 2017-18 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# -----------------------------------------------------------------------------
# $begin header.m4$$ $newlinech #$$
# $spell
#	xam
# $$
#
# $section Comment Showing How to Generate This Output$$
#
# $head Syntax$$
# $codei%Header_(%xam_file_name%)%$$
#
# $head xam_file_name$$
# Is the name of the $icode%*%.xam%$$ file, relative to the
# $code lib/xam$$ directory, that this output corresponds to.
#
# $head Assumptions$$
# It is assumed that the following macros have been set:
# $cref/C_/lang_m4/No Arguments/C_/$$,
# $cref/Language_/xam.m4/language/$$.
#
# $end
# -----------------------------------------------------------------------------
define(Header_,dnl
`C_' This file can be generated in the lib/xam directory using the command:
`C_' m4 -D ``Language_''=Language_ $1)
