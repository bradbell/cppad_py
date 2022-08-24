#! /bin/bash -e
# -----------------------------------------------------------------------------
#         cppad_py: A C++ Object Library and Python Interface to Cppad
#          Copyright (C) 2017-22 Bradley M. Bell (bradbell@seanet.com)
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
if [ "$0" != "bin/double2float.sh" ]
then
   echo "bin/double2float.sh: must be executed from its parent directory"
   exit 1
fi
#! /bin/bash -e
git reset --hard
list=`git ls-files '*a_double[^a-z]*'`
for old_name in $list
do
   new_name=`echo $old_name | sed -e 's|a_double\([^a-z]\)|a_float\1|'`
   echo "git mv $old_name $new_name"
   git mv $old_name $new_name
done
cat << EOF > junk.sed
s|a_double_data  |a_float_data   |
s|\\([^a-zA-Z]\\)a_double\\([^a-zA-Z]\\)|\\1a_float\\2|g
s|\\([^a-zA-Z]\\)a_double\$|\\1a_float|g
s|^a_double\\([^a-zA-Z]\\)|a_float\\1|g
s|\\([^a-zA-Z]\\)a_double\\([^a-zA-Z]\\)|\\1a_float\\2|g
s|\\([^a-zA-Z]\\)a_double\$|\\1a_float|g
s|^a_double\\([^a-zA-Z]\\)|a_float\\1|g
EOF
list=`git ls-files`
for file in $list
do
   sed -i $file -f junk.sed
done
