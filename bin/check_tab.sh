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
if [ "$0" != 'bin/check_tab.sh' ]
then
   echo 'must execut bin/check_tab.sh from its parent directory'
   exit 1
fi
# -----------------------------------------------------------------------------
list=`git ls-files | sed -e '/^sphinx\/Makefile$/d'`
ok='yes'
for file in $list
do
   if grep $'\t' $file > /dev/null
   then
      echo "$file has a tabs"
      ok='no'
   fi
done
if [ "$ok" == 'no' ]
then
   echo 'check_tab.sh: Error'
   exit 1
fi
echo 'check_tab.sh: OK'
exit 0
