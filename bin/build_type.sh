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
if [ "$0" != "bin/build_type.sh" ]
then
   echo "bin/build_type.sh: must be executed from its parent directory"
   exit 1
fi
# -----------------------------------------------------------------------------
#
# MSYS
# No symbolic links on MSYS systems
kernel=$(uname -s)
if [[ "$kernel" =~ MSYS.* ]]
then
   echo 'Warning: MSYS does not suppor symbolic links'
   exit 0
fi
#
# build_type
eval $(grep '^build_type *=' bin/get_cppad.sh)
if [ "$build_type" != 'debug' ] && [ "$build_type" != 'release' ]
then
   echo 'build_type.sh: build_type in get_cppad.sh is not debug or release'
   exit 1
fi
echo "build_type=$build_type"
#
# cmake_install_prefix
eval $(grep '^cmake_install_prefix *=' bin/get_cppad.sh)
if ! echo $cmake_install_prefix | grep '^/' > /dev/null
then
   # convert cmake_install_prefix to an absolute path
   cmake_install_prefix="$(pwd)/$cmake_install_prefix"
fi
echo "cmake_install_prefix=$cmake_install_prefix"
#
# cmake_install_prefix: link
# build: link
for dir in "$cmake_install_prefix" build
do
   if [ ! -d $dir.$build_type ]
   then
      mkdir -p $dir.$build_type
   fi
   if [ -e $dir ] || [ -L $dir ]
   then
      if [ ! -L $dir ]
      then
         echo "build_typs.sh: $dir is not a symbolic link"
         exit 1
      fi
      echo_eval rm $dir
   fi
   echo_eval ln -s $dir.$build_type $dir
done
# -----------------------------------------------------------------------------
echo 'build_type.sh: OK'
exit 0
