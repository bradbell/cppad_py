#! /bin/bash -e
# -----------------------------------------------------------------------------
#         cppad_swig: A C++ Object Library and SWIG Interface to CppAD
#          Copyright (C) 2017-17 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#          GNU Affero General Public License version 3.0 or later see
#                     http://www.gnu.org/licenses/agpl.txt
# -----------------------------------------------------------------------------
revert_list='
'
move_list='
'
move_sed='s|/local/|/core/|'
#
cat << EOF > junk.sed
s|[Ss][Ww][Ii][Gg]|Swig|g
s|cppad_Swig|cppad_swig|g
s|Swig_FOUND|SWIG_FOUND|g
s|FIND_PACKAGE(Swig)|FIND_PACKAGE(SWIG)|g
s|Swig/|swig/|g
s|\$code Swig\$\\\$|Swig|g
s|SwigPYTHON|SWIGPYTHON|g
s|SwigOCTAVE|SWIGOCTAVE|g
s|SwigPERL|SWIGPERL|g
s|UseSwig|UseSWIG|g
s|^# *ifdef Swig|# ifdef SWIG|
#
s|\\([a-z][a-z][a-z]*\\)_Swig|\\1_swig|g
s|Swig_\\([a-z][a-z][a-z]*\\)|swig_\\1|g
s|\\([A-Z][A-Z][A-Z]*\\)_Swig|\\1_SWIG|g
s|Swig_\\([A-Z][A-Z][A-Z]*\\)|SWIG_\\1|g
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
cp $HOME/trash/batch_edit.sh bin/batch_edit.sh
echo "$0: OK"
exit 0


# -----------------------------------------------------------------------------
echo 'bin/batch_edit.sh: OK'
exit 0