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
echo "bin/sphinxrst.py sphinx file_list spell_list"
if ! bin/sphinxrst.py sphinx file_list spell_list 2> sphinxrst.$$
then
	type_error='error'
else
	type_error='warning'
fi
if [ -s sphinxrst.$$ ]
then
	cat sphinxrst.$$
	rm sphinxrst.$$
	echo "$0: exiting due to $type_error above"
	exit 1
fi
rm sphinxrst.$$
#
echo_eval cd sphinx
file_list=$(ls sphinxrst/*.rst | sed -e 's|^sphinxrst/||' )
for file in $file_list
do
	if [ "$file" != 'sphinxrst_py.rst' ]
	then
		if [ ! -e test_out/$file ]
		then
			echo "The output file sphinx/test_out/$file does not exist."
			echo 'Check that the corresponding sections are correct and then:'
			echo "    cp sphinx/sphinxrst/$file sphinx/test_out/$file"
			exit 1
		elif ! diff test_out/$file sphinxrst/$file
		then
			echo "The file sphinx/sphinxrst/$file changed; above is output of"
			echo "	diff test_out/$file sphinxrst/$file"
			echo 'If the new file is currect, replace old with new using:'
			echo "    cp sphinx/sphinxrst/$file sphinx/test_out/$file"
			exit 1
		else
			echo "$file: OK"
		fi
	fi
done
file_list=$(ls test_out/*.rst | sed -e 's|^test_out/||' )
for file in $file_list
do
	if [ ! -e sphinxrst/$file ]
	then
		echo "The output file sphinx/sphinxrst/$file does not nexist."
		echo "Use he following command to remove sphinx/test_out/$file ?"
		echo "	git rm sphinx/test_out/$file"
		exit 1
	fi
done
# -----------------------------------------------------------------------------
echo "$0: OK"
exit 0
