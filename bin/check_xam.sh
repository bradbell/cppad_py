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
list=`ls lib/xam/*.xam | sed -e 's|^lib/xam/||' -e 's|\.xam$||'`
ok='yes'
declare -A ext
ext['octave']='m'
ext['perl']='pm'
ext['python']='py'
ext['cplusplus']='cpp'
for lang in cplusplus octave perl python
do
	for name in $list
	do
		file_name="$name.${ext[${lang}]}"
		for check in $lang.omh CMakeLists.txt
		do
			if ! grep "$file_name" "lib/example/$lang/$check" > /dev/null
			then
				if [ "$ok" == 'yes' ]
				then
					echo '----------------------------------------------------'
				fi
				ok='no'
				echo "lib/example/$lang/$check is missing"
				echo "$file_name"
			fi
		done
	done
done
if [ "$ok" != 'yes' ]
then
	echo 'bin/check_xam.sh: see errors above'
	exit 1
fi
# -----------------------------------------------------------------------------
echo 'bin/check_xam.sh: OK'
exit 0
