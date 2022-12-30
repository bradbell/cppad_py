#! /bin/bash -e
# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileCopyrightText: Bradley M. Bell <bradbell@seanet.com>
# SPDX-FileContributor: 2017-22 Bradley M. Bell
# ----------------------------------------------------------------------------
# bash function that echos and executes a command
echo_eval() {
   echo $*
   eval $*
}
# -----------------------------------------------------------------------------
if [ "$0" != 'bin/check_if_0.sh' ]
then
   echo 'must execut bin/check_if_0.sh from its parent directory'
   exit 1
fi
# -----------------------------------------------------------------------------
list=`git ls-files *.cpp *.hpp`
ok='ye'
for file in $list
do
   if grep '^#[ \t]*if[ \t]*0[ \t]*$' $file > /dev/null
   then
      echo "$file contains '^# if 0'"
      ok='no'
   fi
done
if [ "$ok" == 'no' ]
then
   echo 'check_if_0.sh: Error'
   exit 1
fi
echo 'check_if_0.sh: OK'
exit 0
