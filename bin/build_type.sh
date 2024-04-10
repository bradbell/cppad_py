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
# build_type
# symbolic_link
# cmake_install_prefix
eval $(bin/install_settings.py)
#
if [ "$symbolic_link" == 'false' ]
then
   exit 0
fi
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
echo "build_type=$build_type"
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
