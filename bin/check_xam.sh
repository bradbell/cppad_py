#! /bin/bash -e
# -----------------------------------------------------------------------------
#         cppad_swig: A C++ Object Library and Swig Interface to Cppad
#          Copyright (C) 2017-17 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# -----------------------------------------------------------------------------
# bash function that echos and executes a command
echo_eval() {
	echo $*
	eval $*
}
# -----------------------------------------------------------------------------
if [ "$0" != "bin/check_xam.sh" ]
then
	echo "bin/check_xam.sh: must be executed from its parent directory"
	exit 1
fi
# -----------------------------------------------------------------------------
# list of xam example / test files
xam_file_list=`ls lib/xam/*/*.xam | sed -e 's|lib/xam/||'`
xam_fun_list=`echo $xam_file_list | sed -e 's|/|_|g' -e 's|\.xam||g'`
# -----------------------------------------------------------------------------
check=lib/example/CMakeLists.txt
for file in $xam_file_list
do
	if ! grep $file $check > /dev/null
	then
		echo "check_xam.sh: $file is missing in"
		echo $check
		exit 1
	fi
done
# -----------------------------------------------------------------------------
lang_file_list='
	lib/example/cplusplus/check_all.cpp
	lib/example/octave/check_all.m
	lib/example/perl/check_all.pl
	lib/example/python/check_all.py
'
for lang_file in $lang_file_list
do
	for fun in $xam_fun_list
	do
		if ! grep $fun $lang_file > /dev/null
		then
			echo "check_xam.sh: $fun is missing in"
			echo $lang_file
			exit 1
		fi
	done
done
# -----------------------------------------------------------------------------
echo 'bin/check_xam.sh: OK'
exit 0
