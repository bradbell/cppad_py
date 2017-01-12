#! /bin/bash -e
# -----------------------------------------------------------------------------
#         cppad_swig: A C++ Object Library and SWIG Interface to CppAD
#          Copyright (C) 2017-17 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#          GNU Affero General Public License version 3.0 or later see
#                     http://www.gnu.org/licenses/agpl.txt
# -----------------------------------------------------------------------------
delete_list='
'
revert_list='
'
move_list='
'
move_sed='s|vector|a_vector|'
#
cat << EOF > junk.sed
s|new_var_new_(a_double, *\\([0-9a-z_]*\\), *module_(a_double)|new_var_(a_double, \\1, module_ctor_(a_double)|
s|new_var_new_(vector_double, *\\([0-9a-z_]*\\), *module_(vector_double)|new_var_(vector_double, \\1, module_ctor_(vector_double)|
s|new_var_new_(vector_ad, *\\([0-9a-z_]*\\), *module_(vector_ad)|new_var_(vector_ad, \\1, module_ctor_(vector_ad)|
s|new_var_new_(a_fun, *\\([0-9a-z_]*\\), *module_(a_fun)|new_var_(a_fun, \\1, module_ctor_(a_fun)|
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
