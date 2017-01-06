#! /bin/bash -e
# -----------------------------------------------------------------------------
#         cppad_swig: A C++ Object Library and Swig Interface to Cppad
#          Copyright (C) 2017-17 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#          GNU Affero General Public License version 3.0 or later see
#                     http://www.gnu.org/licenses/agpl.txt
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
cd lib/xam
list=`ls *.xam | sed -e 's|\.xam$||'`
ok='yes'
declare -A ext
ext['octave']='m'
ext['perl']='pm'
ext['python']='py'
ext['cplusplus']='cpp'
for name in $list
do
	for lang in cplusplus octave perl python
	do
		lang_file="example/$lang/$name.${ext[${lang}]}"
		if [ ! -e "../$lang_file" ]
		then
			touch ../$lang_file
		fi
		m4 $lang.m4 $name.xam > check_swig_xam.$$
		if diff ../$lang_file check_swig_xam.$$ > /dev/null
		then
			rm check_swig_xam.$$
		else
			if [ "$ok" == 'yes' ]
			then
				echo '---------------------------------------------------------'
			fi
			mv check_swig_xam.$$ ../$lang_file
			echo "lib/$lang_file changed."
			ok='no'
		fi
	done
done
if [ "$ok" != 'yes' ]
then
	echo 'check_swig_xam.sh: changed some language specific files'
	exit 1
fi
# -----------------------------------------------------------------------------
echo 'bin/check_xam.sh: OK'
exit 0
