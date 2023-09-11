#! /usr/bin/env bash
# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileCopyrightText: Bradley M. Bell <bradbell@seanet.com>
# SPDX-FileContributor: 2017-23 Bradley M. Bell
# ----------------------------------------------------------------------------
set -e -u
# -----------------------------------------------------------------------------
# bash function that echos and executes a command
echo_eval() {
   echo $*
   eval $*
}
# -----------------------------------------------------------------------------
if [ "$0" != "bin/rm_cppad.sh" ] || [ "$#" != 0 ]
then
   echo "bin/rm_cppad.sh: must be executed from its parent directory"
   exit 1
fi
# -----------------------------------------------------------------------------
# build_dir
eval $(grep '^cmake_install_prefix *=' bin/get_cppad.sh)
build_dir="external/cppad.git/build/$build_type"
if [ ! -f "$build_dir/install_manifest.txt" ]
then
   echo "rm_cppad.sh: $build_dir/install_manifest.txt does not exist"
   echo 'It should have been created by get_cppad.sh during install of cppad.'
   exit 1
fi
#
# uninstall
echo_eval cd $build_dir
echo_eval make uninstall
#
echo 'rm_cppad.sh: OK'
exit 1
