#! /usr/bin/env bash
# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileCopyrightText: Bradley M. Bell <bradbell@seanet.com>
# SPDX-FileContributor: 2017-23 Bradley M. Bell
# ----------------------------------------------------------------------------
#
# {xrst_begin rm_cppad_mixed.sh}
# {xrst_spell
#     uninstall
#     cppad
#     rm
#     cmake
# }
# {xrst_comment_ch #}
#
# Uninstall get_cppad_mixed.sh
# ############################
#
# Syntax
# ******
# | |tab| ``bin/rm_cppad_mixed.sh``
#
# Purpose
# *******
# This will remove any files that were installed by
# :ref:`get_cppad_mixed_sh-name` .
# This assumes that the values of
# :ref:`get_cppad_sh@Settings@cmake_install_prefix` and
# :ref:`get_cppad_sh@Settings@build_type` have not changed.
#
# If there is a ``cppad_py`` python package installed below
# *cmake_install_prefix*, it  will also be remove.
#
# {xrst_end rm_cppad_mixed.sh}
# ----------------------------------------------------------------------------
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
cd 'external/cppad_mixed.git'
bin/example_remove.sh
#
echo 'rm_cppad_mixed.sh: OK'
exit 0
