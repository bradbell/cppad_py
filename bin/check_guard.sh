#! /usr/bin/env bash
# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileCopyrightText: Bradley M. Bell <bradbell@seanet.com>
# SPDX-FileContributor: 2017-23 Bradley M. Bell
# ----------------------------------------------------------------------------
set -e -u
# ----------------------------------------------------------------------------
if [ ! -e 'bin/check_guard.sh' ]
then
   echo 'bin/check_guard.sh: must be executed from its parent directory'
   exit 1
fi
if [ "$#" != 0 ]
then
   echo 'bin/check_guard.sh: does not expect any arguments'
   exit 1
fi
# ---------------------------------------------------------------------------
#
# different, file_name
list=$(git ls-files *.hpp)
different='no'
for file_name in $list
do
   #
   # short_name
   short_name=$(echo $file_name | sed -e 's|^include/||')
   if [ "$file_name" == "$short_name" ]
   then
      echo 'bin/check_guard.sh: include file name does not start with include/'
      echo $file_name
      exit 1
   fi
   #
   # macro_name
   macro_name=$(\
      sed -n -e '/^# *ifndef *CPPAD_PY_[0-9A-Z_]*_HPP[ \t]*$/p' $file_name | \
      sed -e 's|^# *ifndef *||' -e 's|[ \t]*$||'
   )
   #
   # check
   check=$(echo $short_name | tr [a-zA-Z/.] [A-Za-z__])
   #
   if [ "$macro_name" == '' ]
   then
      echo "$file_name: Cannot find  ^# *ifndef *CPPAD_PY_[0-9A-Z_]*_HPP[ \t]*"
      different='yes'
   elif [ "$macro_name" != "$check" ]
   then
      echo
      echo "file_name  = $file_name"
      echo "macro_name = $macro_name"
      different='yes'
   fi
done
#
if [ $different = 'yes' ]
then
   echo
   echo 'bin/check_guard.sh: See include guard errors above'
   exit 1
fi
echo 'bin/check_guard.sh: OK'
exit 0
