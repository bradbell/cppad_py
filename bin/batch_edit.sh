#! /bin/bash -e
# -----------------------------------------------------------------------------
#         cppad_swig: A C++ Object Library and SWIG Interface to CppAD
#          Copyright (C) 2017-18 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    http://www.gnu.org/licenses/gpl-3.0.txt
# -----------------------------------------------------------------------------
delete_list='
'
revert_list='
'
move_list='
	include/cppad/swig/cppad_swig.hpp
	lib/cppad_swig.i
'
move_sed='s|cppad_swig|cppad_py|'
#
cat << EOF > junk.sed
s|CPPAD_SWIG|CPPAD_PY|
s|Cppad Swig|Cppad Py|
s|cppad_swig|cppad_py|g
s|A C++ Object Library and Swig|A C++ Object Library and Python|
s|2017-17 Bradley|2017-18 Bradley|
#
# py in spell commands
s|^\\tCppad\$|&\\n\\tPy|
s|^\\tcppad\$|&\\n\\tpy|
s|^#\\tCppad\$|&\\n#\\tPy|
s|^#\\tcppad\$|&\\n#\\tpy|
s|^%\\tcppad\$|&\\n%\\tpy|
s|^\\(.#.\\)\\tcppad\$|&\\n\\1\\tpy|
EOF
# -----------------------------------------------------------------------------
if [ $0 != "bin/batch_edit.sh" ]
then
	echo "bin/batch_edit.sh: must be executed from its parent directory"
	exit 1
fi
# -----------------------------------------------------------------------------
# bash function that echos and executes a command
echo_eval() {
	echo $*
	eval $*
}
# -----------------------------------------------------------------------------
cp bin/batch_edit.sh $HOME/trash/batch_edit.sh
git reset --hard
# ---------------------------------------------------------------------------
list_all=`git ls-files`
for file in $list_all
do
	if [ "$file" != 'bin/batch_edit.sh' ]
	then
		sed -f junk.sed  $file > junk.$$
		if ! diff $file junk.$$ > /dev/null
		then
			echo_eval sed -f junk.sed  -i $file
		fi
	fi
done
if [ -e junk.$$ ]
then
	rm junk.$$
fi
# ----------------------------------------------------------------------------
for old in $move_list
do
	new=`echo $old | sed -e "$move_sed"`
	if [ -e "$new" ]
	then
		rm -r "$new"
	fi
	dir=`echo $new | sed -e 's|/[^/]*$||'`
	if [ "$dir" != "$new" ] && [ ! -e "$dir" ]
	then
		echo_eval mkdir $dir
	fi
	echo_eval git mv $old $new
done
# ----------------------------------------------------------------------------
# files that were hand edited and cached using 'git_new.sh to'
if [ -e new ]
then
	echo_eval git_new.sh from
fi
# ----------------------------------------------------------------------------
for file in $revert_list
do
	echo_eval git checkout $file
done
# ----------------------------------------------------------------------------
for file in $delete_list
do
	echo_eval git rm -f $file
done
# ----------------------------------------------------------------------------
cp $HOME/trash/batch_edit.sh bin/batch_edit.sh
echo "$0: OK"
exit 0


# -----------------------------------------------------------------------------
echo 'bin/batch_edit.sh: OK'
exit 0
