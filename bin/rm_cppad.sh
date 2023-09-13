#! /usr/bin/env bash
# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileCopyrightText: Bradley M. Bell <bradbell@seanet.com>
# SPDX-FileContributor: 2017-23 Bradley M. Bell
# ----------------------------------------------------------------------------
#
# {xrst_begin rm_cppad.sh}
# {xrst_spell
#     uninstall
#     cppad
#     rm
#     cmake
# }
# {xrst_comment_ch #}
#
# Uninstall get_cppad.sh
# ######################
#
# Syntax
# ******
# | |tab| ``bin/rm_cppad.sh``
#
# Purpose
# *******
# This will remove any files that were installed by :ref:`get_cppad.sh-name` .
# This assumes that the values of
# :ref:`get_cppad.sh@Settings@cmake_install_prefix` and
# :ref:`get_cppad.sh@Settings@build_type` have not changed.
#
# If there is a ``cppad_py`` python package installed below
# *cmake_install_prefix*, it  will also be remove.
#
# {xrst_end rm_cppad.sh}
# ----------------------------------------------------------------------------
# bash function that echos and executes a command
echo_eval() {
	echo $*
	eval $*
}
# -----------------------------------------------------------------------------
set -e -u
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
# build_type
eval $(grep '^build_type *=' bin/get_cppad.sh)
#
# build_dir
build_dir="external/cppad.git/build/$build_type"
#
# uninstall
pushd $build_dir
make uninstall
popd
#
# cppad_py python package files
list=$(find -L $cmake_install_prefix -regex '.*/cppad_py[^/]*.egg')
if [ "$list" != '' ]
then
   for file in $list
   do
      echo_eval rm -r $file
   done
fi
list=$(find -L $cmake_install_prefix -regex '.*/site-packages/cppad_py')
if [ "$list" != '' ]
then
   for dir in $list
   do
      echo_eval rm -r $dir
   done
fi
#
if [ ! -L $cmake_install_prefix ]
then
   echo "Remove empty directories below $cmake_install_prefix"
   find $cmake_install_prefix -type d -empty -delete
   if [ ! -d $cmake_install_prefix ]
   then
      mkdir $cmake_install_prefix
   fi
else
   echo "Remove empty directories below $cmake_install_prefix.$build_type"
   find $cmake_install_prefix.$build_type -type d -empty -delete
   if [ ! -d $cmake_install_prefix.$build_type ]
   then
      mkdir $cmake_install_prefix.$build_type
   fi
fi
#
echo 'rm_cppad.sh: OK'
exit 0
