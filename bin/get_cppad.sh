#! /usr/bin/env bash
# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileCopyrightText: Bradley M. Bell <bradbell@seanet.com>
# SPDX-FileContributor: 2017-23 Bradley M. Bell
# ----------------------------------------------------------------------------
set -e -u
#
# {xrst_begin get_cppad.sh}
# {xrst_comment_ch #}
#
# Get cppad
# #########
#
# Syntax
# ******
# ``bin/get_cppad.sh``
#
# cppad_py.git
# ************
# This program must be run from the :ref:`setup.py@cppad_py.git` directory.
#
# Purpose
# *******
# If you are not using  the python ``cppad_mixed`` module,
# you can use this script install cppad.
#
# Settings
# ********
# This scripts uses the settings in :ref:`install_settings.py-name` .
#
# Caching
# *******
# This script caches previous builds so that
# when you re-run the script it does not re-do all the work.
# If you have trouble, try deleting the directory
#
# | |tab| ``external/cppad.git``
#
# and re-running this script.
#
# Uninstall
# *********
# {xrst_toc_table
#     bin/rm_cppad.sh
# }
#
# {xrst_end get_cppad.sh}
#
# include_mixed, build_type, cmake_install_prefix
eval $(bin/install_settings.py)
# -----------------------------------------------------------------------------
# CppAD version information
# Use same cppad_version and has_code as in cppad_mixed.git/bin/install_cppad.sh
remote_repo='https://github.com/coin-or/CppAD.git'
cppad_version='20210430'
hash_code='241d9e18ecad02082b6cd64bef201be141ff31a9'
# -----------------------------------------------------------------------------
# bash function that echos and executes a command
echo_eval() {
   echo $*
   eval $*
}
# -----------------------------------------------------------------------------
if [ "$0" != "bin/get_cppad.sh" ]
then
   echo "bin/get_cppad.sh: must be executed from its parent directory"
   exit 1
fi
if [ "$include_mixed" == 'true' ]
then
   msg='bin/get_cppad.sh: Must use bin/get_cppad_mixed.sh '
   msg="$msg  when include_mixed is true"
   echo $msg
   exit 1
fi
if [ "$include_mixed" != 'false' ]
then
   echo 'bin/get_cppad.sh: include_mixed is not true or false'
   exit 1
fi
if [ "$build_type" != 'debug' ] && [ "$build_type" != 'release' ]
then
   echo 'get_cppad.sh: build_type is not debug or release'
   exit 1
fi
# -----------------------------------------------------------------------------
#
# libdir
libdir=$(bin/libdir.py)
#
# cmake_install_prefix: link
bin/build_type.sh
# -----------------------------------------------------------------------------
# external
if [ ! -e external ]
then
   mkdir external
fi
echo_eval cd external
#
# external/cppad.git
if [ ! -e cppad.git ]
then
   echo_eval git clone $remote_repo cppad.git
fi
echo_eval cd cppad.git
git reset --hard
echo_eval git checkout master
echo_eval git pull --ff-only
echo_eval git checkout --quiet $hash_code
check=`grep '^SET(cppad_version' CMakeLists.txt | \
      sed -e 's|^[^"]*"\([^"]*\)".*|\1|'`
if [ "$check" != "$cppad_version" ]
then
   echo "get_cppad.sh: cppad_version = $cppad_version"
   echo "cppad_version in cppad-$cppad_version.git/CMakeLists.txt = $check"
   exit 1
fi
#
# external/cppad.git/build/$build_type
if [ ! -e build/$build_type ]
then
   echo_eval mkdir -p build/$build_type
fi
echo_eval cd build/$build_type
if [ -e CMakeCache.txt ]
then
   rm CMakeCache.txt
fi
#
# cmake
if [ "$build_type" == 'debug' ]
then
   cppad_debug_which='debug_all'
elif [ "$build_type" == 'release' ]
then
   cppad_debug_which='debug_none'
else
   echo 'bin/get_cppad.sh: build type is not debug or release'
   exit 1
fi
cat << EOF
cmake -B . -S ../.. \\
   -D CMAKE_VERBOSE_MAKEFILE="$verbose_makefile" \\
   -D cppad_prefix="$cmake_install_prefix"  \\
   -D cmake_install_libdirs="$libdir"  \\
   -D cppad_cxx_flags="$extra_cxx_flags" \\
   -D cppad_debug_which=$cppad_debug_which
EOF
cmake -B . -S ../.. \
   -D CMAKE_VERBOSE_MAKEFILE="$verbose_makefile" \
   -D cppad_prefix="$cmake_install_prefix"  \
   -D cmake_install_libdirs="$libdir"  \
   -D cppad_cxx_flags="$extra_cxx_flags" \
   -D cppad_debug_which=$cppad_debug_which
#
# run check
if [ "$test_cppad" == 'true' ]
then
   make check
fi
#
# install
make install
# -----------------------------------------------------------------------------
echo 'get_cppad.sh: OK'
exit 0
