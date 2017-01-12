# -----------------------------------------------------------------------------
#         cppad_swig: A C++ Object Library and Swig Interface to Cppad
#          Copyright (C) 2017-17 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#          GNU Affero General Public License version 3.0 or later see
#                     http://www.gnu.org/licenses/agpl.txt
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
