#! /bin/bash -e
# -----------------------------------------------------------------------------
#         cppad_py: A C++ Object Library and Python Interface to Cppad
#          Copyright (C) 2017-20 Bradley M. Bell (bradbell$seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# -----------------------------------------------------------------------------
#
# {xsrst_comment_ch #}
#
# {xsrst_begin get_cppad_sh}
#
# .. include:: ../preamble.rst
#
# {xsrst_spell
#   cppad
#   cxx
#   usr
#   Wno
#   libdir
#   cmake
# }
#
# Get Cppad
# #########
#
# Syntax
# ******
# ``bin/get_cppad.sh``
#
# Top Source Directory
# ********************
# This program must be run from the
# :ref:`top_source_directory<setup_py.download.top_source_directory>`.
#
# Settings
# ********
# If you change any of these settings, you must re-run ``get_cppad.sh`` .
#
# cmake_install_prefix
# ====================
# This prefix is used to install cppad_py. It may be a local directory; e.g.,
# ``build/prefix`` or an absolute path; e.g., ``/usr/local``.
# It may include the shell variable ``$HOME`` but no other variables:
# {xsrst_code sh}
cmake_install_prefix="$HOME/prefix/cppad"
# {xsrst_code}
# If this prefix does no start with ``/``, it is relative to the
# :ref:`top_source_directory<setup_py.download.top_source_directory>`.
# Note that ``$HOME`` starts with ``/``.
#
# cppad_libdir
# ============
# The sub-directory of cmake_install_prefix where libraries are installed.
# (xsrst_code sh)
cppad_libdir='lib64'
# (xsrst_code)
#
# extra_cxx_flags
# ===============
# Extra compiler false used when compiling c++ code not including the
# debugging and optimization flags.
# The ones below are example flags are used by g++:
# {xsrst_code sh}
extra_cxx_flags='-Wall -pedantic-errors -Wno-unused-result -std=c++11'
# {xsrst_code}
#
# build_type
# ==========
# This must be must ``debug`` or ``release`` .
# The debug version has more error messaging while the release
# version runs faster.
# {xsrst_code sh}
build_type='release'
# {xsrst_code}
#
# cmake_install_prefix
# --------------------
# The actual prefix used for the install is
# *cmake_install_prefix* ``.`` *build_type*
# and a soft link is created from *cmake_install_prefix* to this directory.
#
# build
# -----
# This subdirectory ``build.`` *build_type*
# is used to compile and test the software and a soft link is created from
# ``build`` to this subdirectory.
#
# include_mixed
# =============
# This flag is true (false) if we are (are not)
# including the python cppad_mixed interface.
# {xsrst_code sh}
include_mixed='false'
# {xsrst_code}
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
# {xsrst_code sh}
test_cppad='false'
# {xsrst_code}
#
# Caching
# *******
# This script and ``bin/get_cppad_mixed.sh`` cache previous builds so that
# when you re-run the script it does not re-do all the work.
# If you have trouble, try deleting the directory
#
# | |tab| ``build/external``
#
# and re-running this script.
#
# {xsrst_end get_cppad_sh}
# -----------------------------------------------------------------------------
# CppAD version information
remote_repo='https://github.com/coin-or/CppAD.git'
cppad_version='20200210'
hash_code='69d069212c039e1fecc5aba0a7ed2b0b331fe047'
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
# -----------------------------------------------------------------------------
if ! echo $cmake_install_prefix | grep '^/' > /dev/null
then
    # convert cmake_install_prefix to an absolute path
    cmake_install_prefix="$(pwd)/$cmake_install_prefix"
fi
# -----------------------------------------------------------------------------
# create links to proper version of cmake_install_prefix and build
echo_eval bin/build_type.sh
# -----------------------------------------------------------------------------
# change into the build/external
if [ ! -e build/external ]
then
    mkdir build/external
fi
echo_eval cd build/external
# -----------------------------------------------------------------------------
# clone cppad repository directory
if [ ! -e cppad.git ]
then
    echo_eval git clone $remote_repo cppad.git
fi
echo_eval cd cppad.git
git reset --hard
echo_eval git checkout master
echo_eval git pull
echo_eval git checkout --quiet $hash_code
check=`grep '^SET(cppad_version' CMakeLists.txt | \
        sed -e 's|^[^"]*"\([^"]*\)".*|\1|'`
if [ "$check" != "$cppad_version" ]
then
    echo "get_cppad.sh: cppad_version = $cppad_version"
    echo "cppad_version in cppad-$cppad_version.git/CMakeLists.txt = $check"
    exit 1
fi
# -----------------------------------------------------------------------------
# build cppad
# cppad build directory
if [ ! -e build ]
then
    echo_eval mkdir build
fi
echo_eval cd build
if [ -e CMakeCache.txt ]
then
    rm CMakeCache.txt
fi
#
# run cppad cmake command
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
cmake -D CMAKE_VERBOSE_MAKEFILE="$verbose_makefile" \\
    -D cppad_prefix="$cmake_install_prefix"  \\
    -D cmake_install_libdirs="$cppad_libdir"  \\
    -D cppad_cxx_flags="$extra_cxx_flags" \\
    -D cppad_debug_which=$cppad_debug_which \\
    ..
EOF
cmake -D CMAKE_VERBOSE_MAKEFILE="$verbose_makefile" \
    -D cppad_prefix="$cmake_install_prefix"  \
    -D cmake_install_libdirs="$cppad_libdir"  \
    -D cppad_cxx_flags="$extra_cxx_flags" \
    -D cppad_debug_which=$cppad_debug_which \
    ..
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
