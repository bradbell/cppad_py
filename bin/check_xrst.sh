#! /bin/bash -e
# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileCopyrightText: Bradley M. Bell <bradbell@seanet.com>
# SPDX-FileContributor: 2017-23 Bradley M. Bell
# ----------------------------------------------------------------------------
# bash function that echos and executes a command
echo_eval() {
   echo $*
   eval $*
}
# -----------------------------------------------------------------------------
if [ "$0" != "bin/check_xrst.sh" ]
then
   echo "bin/check_xrst.sh: must be executed from its parent directory"
   exit 1
fi
test_dir='build/sphinx'
# -----------------------------------------------------------------------------
if [ -e "$test_dir" ]
then
   echo_eval rm -r $test_dir
fi
echo_eval mkdir -p $test_dir
list='
   conf.py
   preamble.rst
   spelling
   keyword
   Makefile
'
for file in $list
do
   cp -r sphinx/$file $test_dir/$file
done
echo "sed -i $test_dir/conf.py -e s|^project *=.*|project = 'xrst'|"
sed -i $test_dir/conf.py -e "s|^project *=.*|project = 'xrst'|"
#
# -----------------------------------------------------------------------------
echo "bin/xrst.py html bin/xrst.py $test_dir spelling keyword"
if ! bin/xrst.py html bin/xrst.py $test_dir spelling  keyword 2> xrst.$$
then
   type_error='error'
else
   type_error='warning'
fi
if [ -s xrst.$$ ]
then
   cat xrst.$$
   rm xrst.$$
   echo "$0: exiting due to $type_error above"
   exit 1
fi
rm xrst.$$
# -----------------------------------------------------------------------------
file_list=$(ls $test_dir/xrst/*.rst | sed -e "s|^$test_dir/xrst/||" )
for file in $file_list
do
   if [ ! -e sphinx/test_out/$file ]
   then
      echo "The output file sphinx/test_out/$file does not exist."
      echo 'Check that the corresponding sections are correct and then:'
      echo "    cp $test_dir/xrst/$file sphinx/test_out/$file"
      exit 1
   elif ! diff sphinx/test_out/$file $test_dir/xrst/$file
   then
      echo "$test_dir/xrst/$file changed; above is output of"
      echo "    diff sphinx/test_out/$file $test_dir/xrst/$file"
      echo 'If the new file is currect, replace old with new using:'
      echo "    cp $test_dir/xrst/$file sphinx/test_out/$file"
      exit 1
   else
      echo "$file: OK"
   fi
done
file_list=$(ls sphinx/test_out/*.rst | sed -e 's|^sphinx/test_out/||' )
for file in $file_list
do
   if [ ! -e $test_dir/xrst/$file ]
   then
      echo "The output file $test_dir/xrst/$file does not nexist."
      echo "Use he following command to remove sphinx/test_out/$file ?"
      echo "    git rm sphinx/test_out/$file"
      exit 1
   fi
done
# -----------------------------------------------------------------------------
echo_eval sphinx-build -b html $test_dir $test_dir/doc
# -----------------------------------------------------------------------------
echo "$0: OK"
exit 0
