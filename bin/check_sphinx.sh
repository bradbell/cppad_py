#! /bin/bash -e
# -----------------------------------------------------------------------------
#         cppad_py: A C++ Object Library and Python Interface to Cppad
#          Copyright (C) 2017-20 Bradley M. Bell (bradbell@seanet.com)
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
if [ "$0" != "bin/check_sphinx.sh" ]
then
	echo "bin/check_sphinx.sh: must be executed from its parent directory"
	exit 1
fi
# -----------------------------------------------------------------------------
echo_eval bin/sphinxrst.py sphinx file_list spell_list
echo_eval cd sphinx
file_list=$(ls sphinxrst/*.rst | sed -e 's|^sphinxrst/||' )
for file in $file_list
do
	if [ "$file" != 'sphinxrst_py.rst' ]
	then
		if ! diff sphinxrst/$file test_out/$file
		then
			echo "The output file sphinx/sphinxrst/$file has chaned."
			echo 'If the new file is currect, replace to old check using:'
			echo "    cp sphinx/sphinxrst/$file sphinx/test_out/$file"
			exit 1
		else
			echo "$file: OK"
		fi
	fi
done
# -----------------------------------------------------------------------------
echo "$0: OK"
exit 0
