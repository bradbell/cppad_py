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
for lang in cplusplus octave perl python
do
cat << EOF > temp.1.$$
This file was automatically created by bin/check_xam.sh
-------------------------------------------------------------------------------
          cppad_swig: A C++ Object Library and Swig Interface to Cppad
           Copyright (C) 2017-17 Bradley M. Bell (bradbell@seanet.com)
               This program is distributed under the terms of the
           GNU Affero General Public License version 3.0 or later see
                      http://www.gnu.org/licenses/agpl.txt
-------------------------------------------------------------------------------
EOF
	echo "\$begin lib_example_$lang\$\$"          >> temp.1.$$
	echo "\$spell $lang \$\$"                     >> temp.1.$$
	echo "\$section $lang Examples and Tests\$\$" >> temp.1.$$
	first='yes'
	for name in $list
	do
		lang_file="example/$lang/$name.${ext[${lang}]}"
		if [ "$first" == 'yes' ]
		then
			echo "\$childtable%lib/$lang_file" >> temp.1.$$
			first='no'
		else
			echo "	%lib/$lang_file" >> temp.1.$$
		fi
		if [ ! -e "../$lang_file" ]
		then
			touch ../$lang_file
		fi
		m4 -D "language_=$lang" $name.xam > temp.2.$$
		if diff ../$lang_file temp.2.$$ > /dev/null
		then
			rm temp.2.$$
		else
			if [ "$ok" == 'yes' ]
			then
				echo '---------------------------------------------------------'
			fi
			mv temp.2.$$ ../$lang_file
			echo "lib/$lang_file changed."
			ok='no'
		fi
	done
	#
	echo '%$$'  >> temp.1.$$
	echo '$end' >> temp.1.$$
	#
	if diff temp.1.$$ ../example/$lang/$lang.omh > /dev/null
	then
		rm temp.1.$$
	else
		mv temp.1.$$ ../example/$lang/$lang.omh
		echo "lib/example/$lang.omh changed."
		ok='no'
	fi
done
if [ "$ok" != 'yes' ]
then
	echo 'check_xam.sh: changed some language specific files'
	exit 1
fi
# -----------------------------------------------------------------------------
echo 'bin/check_xam.sh: OK'
exit 0
