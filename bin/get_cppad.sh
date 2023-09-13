#! /usr/bin/env bash
# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileCopyrightText: Bradley M. Bell <bradbell@seanet.com>
# SPDX-FileContributor: 2017-23 Bradley M. Bell
# ----------------------------------------------------------------------------
set -e -u
# {xrst_begin get_cppad.sh}
# {xrst_spell
#     caching
#     cmake
#     cppad
#     cxx
#     usr
#     wno
#     makefile
#     rm
#     uninstall
# }
# {xrst_comment_ch #}
#
#
# Get or Remove Cppad
# ###################
#
# Syntax
# ******
# | |tab| ``bin/get_cppad.sh``
# | |tab| ``bin/rm_cppad.sh``
#
# Top Source Directory
# ********************
# This program must be run from the
# :ref:`top_source_directory<setup_py@Download@Top Source Directory>`.
#
# Settings
# ********
# If you change any of these settings, you must re-run ``get_cppad.sh``
# (or ``get_cppad_mixed.sh`` if *include_mixed* is true ).
#
# cmake_install_prefix
# ====================
# This prefix is used to install cppad_py.
# {xrst_code sh}
cmake_install_prefix="$HOME/prefix/cppad_py"
# {xrst_code}
#
# #.  If this prefix starts with ''/'' ,
#     it is an absolute path; e.g., ``/usr/local``.
# #.  If it does not start with ``/`` , it is relative to the
#     :ref:`top_source_directory<setup_py@Download@Top Source Directory>`.
# #.  It may include the shell variable ``$HOME`` but no other variables;
#     e.g; ``$HOME/prefix`` .
#     Note that ``$HOME`` starts with ``/`` .
# #.  The case where the prefix ends with ``/.local`` is a special case
#     (because it is used by ``pip install --user`` *package* ).
#
# extra_cxx_flags
# ===============
# Extra compiler flags used when compiling c++ code not including the
# debugging and optimization flags.
# The ones below are example flags are used by g++:
# {xrst_code sh}
extra_cxx_flags='-Wall -pedantic-errors -Wno-unused-result -std=c++11'
# {xrst_code}
#
# build_type
# ==========
# This must be must ``debug`` or ``release`` .
# The debug version has more error messaging while the release
# version runs faster.
# {xrst_code sh}
build_type='release'
# {xrst_code}
#
# cmake_install_prefix
# --------------------
# If *cmake_install_prefix* ends with ``/.local`` ,
# it is the actual install prefix.
# Otherwise, the actual prefix used for the install is
#
# | |tab| *cmake_install_prefix.build_type*
#
# and a soft link is created from *cmake_install_prefix* to this directory.
#
# build
# -----
# The subdirectory
#
# | |tab| ``build.``\ *build_type*
#
# is used to compile and test the software and a soft link is created from
# ``build`` to this subdirectory.
#
# include_mixed
# =============
# This flag is true (false) if we are (are not)
# including the python cppad_mixed interface.
# {xrst_code sh}
include_mixed='false'
# {xrst_code}
# If it is true, the install script ``bin/get_cppad_mixed.sh``
# should be used to install Cppad together with the all the other cppad_mixed
# requirements.
# Otherwise, ``bin/get_cppad.sh`` should be used to install Cppad.
#
# test_cppad
# ==========
# This must be must ``true`` or ``false`` .
# Cppad has a huge test suite and this can take a significant amount of time,
# but it may be useful if you have problems.
# {xrst_code sh}
test_cppad='false'
# {xrst_code}
#
# verbose_makefile
# ================
# This flag is true (false) a verbose version of the build description
# will (will not) be printed.
# {xrst_code sh}
verbose_makefile='false'
# {xrst_code}
#
# Caching
# *******
# This script and ``bin/get_cppad_mixed.sh`` cache previous builds so that
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
# cmake_install_prefix
if ! echo $cmake_install_prefix | grep '^/' > /dev/null
then
   # convert cmake_install_prefix to an absolute path
   cmake_install_prefix="$(pwd)/$cmake_install_prefix"
fi
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
