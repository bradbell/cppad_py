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
if [ "$0" != "bin/check_copyright.sh" ]
then
	echo "bin/check_copyright.sh: must be executed from its parent directory"
	exit 1
fi
# -----------------------------------------------------------------------------
if [ ! -e .git ]
then
	echo 'This is not a git repository so cannot check copyright.'
	echo 'check_copyright.sh: skipped'
	exit 0
fi
# -----------------------------------------------------------------------------
list=`git ls-files | sed -e '/^.gitignore$/d'`
ok='yes'
text='Copyright (C) 2017-17 Bradley M. Bell (bradbell@seanet.com)'
for file in $list
do
	if [ -e $file ]
	then
		if ! grep "$text" $file > /dev/null
		then
			ok='no'
			echo "Cannot find copyright message in $file"
		fi
	fi
done
# -----------------------------------------------------------------------------
if [ "$ok" == 'no' ]
then
	echo 'bin/check_copyright.sh: Error'
	exit 1
fi
echo 'bin/check_copyright.sh: OK'
exit 0
