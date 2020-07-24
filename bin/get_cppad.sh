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
#   yyyymmdd
#   cxx
#   messaging
#   usr
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
# Each time it is run it removes the old ``build`` directory and
# starts over.
#
# Settings
# ********
# If you change any of these settings, you must re-run ``get_cppad.sh`` .
#
# cppad_prefix
# ============
# This prefix is used to install CppAD may be a local director; e.g.,
# ``build/prefix`` or an absolute path; e.g., ``/usr/local`` ,
# it may include the shell variable ``$HOME`` but no variables:
# {xsrst_code sh}
cppad_prefix="$HOME/prefix/cppad"
# {xsrst_code}
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
# If you used the ``debug`` build type you may get the following warning
# from the compiler (because the optimization is totally turned off):
#
# | |tab| ``warning _FORTIFY_SOURCE requires compiling with optimization``
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
# This procedure cashes previous builds so that when you re-run
# this script it does not re-do all the work.
# If you have trouble, try deleting the directory
#
# | |tab| ``build/cppad`` - *yyyymmdd* . ``git``
#
# and re-running this script.
#
# {xsrst_end get_cppad_sh}
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
# -----------------------------------------------------------------------------
# CppAD version information
remote_repo='https://github.com/coin-or/CppAD.git'
cppad_version='20200210'
hash_code='69d069212c039e1fecc5aba0a7ed2b0b331fe047'
# -----------------------------------------------------------------------------
# convert cppad_prefix relative to absolute paths
if ! echo $cppad_prefix | grep '^/' > /dev/null
then
    cppad_prefix="$(pwd)/$cppad_prefix"
fi
# -----------------------------------------------------------------------------
# cppad_py build directory
if [ -e 'build' ]
then
    echo_eval rm -rf build
fi
echo_eval mkdir build
echo_eval cd build
#
# cppad repository directory
echo_eval git clone $remote_repo cppad-$cppad_version.git
echo_eval cd cppad-$cppad_version.git
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
# cppad build directory
if [ ! -e build ]
then
    echo_eval mkdir build
fi
echo_eval cd build
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
    -D cppad_prefix="$cppad_prefix"  \\
    -D cppad_cxx_flags="$extra_cxx_flags" \\
    -D cppad_debug_which=$cppad_debug_which \\
    ..
EOF
cmake -D CMAKE_VERBOSE_MAKEFILE="$verbose_makefile" \
    -D cppad_prefix="$cppad_prefix"  \
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
