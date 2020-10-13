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
# {xsrst_begin get_cppad_mixed_sh}
#
# .. include:: ../preamble.rst
#
# Get cppad_mixed
# ###############
#
# Syntax
# ******
# ``bin/get_cppad_mixed.sh``
#
# Top Source Directory
# ********************
# This program must be run from the
# :ref:`top_source_directory<setup_py.download.top_source_directory>`.
#
# Purpose
# *******
# If you are going to use the python ``cppad_mixed`` module,
# you will need to run this script to install the corresponding
# C++ module. This script includes the installation of cppad so it is not
# necessary to also run :ref:`get_cppad.sh<get_cppad.sh>`.
#
# Settings
# ********
# This scripts uses the
# :ref:`get_cppad.sh settings<get_cppad_sh.settings>` for
# *cppad_prefix* , *extra_cxx_flags*, and *build_type* .
#
# {xsrst_end get_cppad_mixed_sh}
# ---------------------------------------------------------------------------
# CppAD mixed version information
web_page='https://github.com/bradbell/cppad_mixed.git'
hash_key='c48f69eb78a5e9483d5bee3dc5477a6cdb902f18'
version='20201010'
# --------------------------------------------------------------------------
name='bin/get_cppad_mixed.sh'
if [ $0 != $name ]
then
    echo "$name: must be executed from its parent directory"
    exit 1
fi
# -----------------------------------------------------------------------------
# bash function that echos and executes a command
echo_eval() {
    echo $*
    eval $*
}
# --------------------------------------------------------------------------
# build_type
cmd=`grep '^build_type=' bin/get_cppad.sh`
eval $cmd
#
# extra_cxx_flags
cmd=`grep '^extra_cxx_flags=' bin/get_cppad.sh`
eval $cmd
#
# cppad_prefix
cmd=`grep '^cppad_prefix=' bin/get_cppad.sh`
eval $cmd
#
# include_mixed
cmd=`grep '^include_mixed=' bin/get_cppad.sh`
eval $cmd
if [ "$include_mixed" == 'false' ]
then
    echo "$name: Must use bin/get_cppad.sh when include_mixed is false"
    exit 1
fi
if [ "$include_mixed" != 'true' ]
then
    echo "$name: include_mixed is not true or false in bin/get_cppad.sh."
    exit 1
fi
# ---------------------------------------------------------------------------
echo_eval bin/build_type.sh
# ---------------------------------------------------------------------------
# cd into build/external
if [ ! -e build/external ]
then
    mkdir build/external
fi
echo_eval cd build/external
# --------------------------------------------------------------------------
# clone cppad_mixed.git
if [ ! -e cppad_mixed.git ]
then
    echo_eval git clone $web_page cppad_mixed.git
fi
cd cppad_mixed.git
git reset --hard
echo_eval git checkout master
echo_eval git pull
echo_eval git checkout --quiet $hash_key
check=`grep '^SET(cppad_mixed_version' CMakeLists.txt | \
    sed -e 's|^[^"]*"\([^"]*\).*|\1|'`
if [ "$version" != "$check" ]
then
    echo 'install_cppad_mixed.sh: version number does not agree with hash_key'
    exit 1
fi
if [ "$build_type" == 'release' ]
then
    optmize='yes'
else
    optmize='no'
fi
# install options
sed -i bin/run_cmake.sh \
    -e "s|^verbose_makefile=.*|verbose_makefile='no'|" \
    -e "s|^build_type=.*|build_type='$build_type'|" \
    -e "s|^cppad_prefix=.*|cppad_prefix='$cppad_prefix'|" \
    -e "s|^eigen_prefix=.*|eigen_prefix='$cppad_prefix/eigen'|" \
    -e "s|^ipopt_prefix=.*|ipopt_prefix='$cppad_prefix'|" \
    -e "s|^extra_cxx_flags=.*|extra_cxx_flags='$extra_cxx_flags'|" \
    -e "s|^cmake_libdir=.*|cmake_libdir='lib64'|" \
    -e "s|^ldlt_cholmod=.*|ldlt_cholmod='yes'|" \
    -e "s|^optimize_cppad_function=.*|optimize_cppad_function='$optimize'|" \
    -e "s|^for_hes_sparsity=.*|for_hes_sparsity='yes'|" \
#
# supress call to cppad_mixed build_type.sh
sed -i bin/example_install.sh \
    -e 's|bin/build_type.sh .*|:|' \
    -e 's|for cmd in check speed install|for cmd in install|'
# -----------------------------------------------------------------------------
# cppad_mixed example install
echo_eval bin/example_install.sh use
#
# -----------------------------------------------------------------------------
echo 'get_cppad_mixed.sh: OK'
exit 0
