#! /bin/bash -e
# -----------------------------------------------------------------------------
#         cppad_py: A C++ Object Library and Python Interface to Cppad
#          Copyright (C) 2017-22 Bradley M. Bell (bradbell$seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# -----------------------------------------------------------------------------
#
# {xrst_comment_ch #}
#
# {xrst_begin get_cppad_mixed_sh}
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
# :ref:`top_source_directory<setup_py@Download@Top Source Directory>`.
#
# Purpose
# *******
# If you are going to use the python ``cppad_mixed`` module,
# you will need to run this script to install the corresponding
# C++ module. This script includes the installation of cppad so it is not
# necessary to also run :ref:`get_cppad@sh<get_cppad@sh>`.
#
# Settings
# ********
# This scripts uses the
# :ref:`get_cppad@sh settings<get_cppad_sh@Settings>` for
# *cmake_install_prefix* , *extra_cxx_flags*, and *build_type* .
#
# {xrst_end get_cppad_mixed_sh}
# ---------------------------------------------------------------------------
# CppAD mixed version information
web_page='https://github.com/bradbell/cppad_mixed.git'
hash_key='bf05548b74dcf0df3f5af4ee5a3b6ee54383c6ed'
version='20220519'
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
# cmake_install_prefix
cmd=`grep '^cmake_install_prefix=' bin/get_cppad.sh`
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
minor=$(echo "import sys; print(sys.version_info.minor)" | python3)
# ---------------------------------------------------------------------------
libdir=$(bin/libdir.py)
export LD_LIBRARY_PATH="$cmake_install_prefix/$libdir"
export DYLD_LIBRARY_PATH="$LD_LIBRARY_PATH"
export PKG_CONFIG_PATH="$LD_LIBRARY_PATH/pkgconfig"
export PYTHONPATH="$LD_LIBRARY_PATH/python3.$minor/site-packages"
# ---------------------------------------------------------------------------
echo_eval bin/build_type.sh
# ---------------------------------------------------------------------------
# cd into external
if [ ! -e external ]
then
   mkdir external
fi
echo_eval cd external
# --------------------------------------------------------------------------
# clone cppad_mixed.git
if [ ! -e cppad_mixed.git ]
then
   echo_eval git clone $web_page cppad_mixed.git
fi
cd cppad_mixed.git
git reset --hard
echo_eval git checkout master
echo_eval git pull --ff-only
echo_eval git checkout --quiet $hash_key
check=`grep '^SET(cppad_mixed_version' CMakeLists.txt | \
   sed -e 's|^[^"]*"\([^"]*\).*|\1|'`
if [ "$version" != "$check" ]
then
   echo 'install_cppad_mixed.sh: version number does not agree with hash_key'
   echo "version=$version, check=$check"
   exit 1
fi
if [ "$build_type" == 'release' ]
then
   optimize='yes'
else
   optimize='no'
fi
# ----------------------------------------------------------------------------
# transfer cppad_py install options to cppad_mixed run_cmake.sh
dir=$(pwd)
echo "edit $dir/bin/run_cmake.sh"
sed \
   -e "s|^verbose_makefile=.*|verbose_makefile='no'|" \
   -e "s|^build_type=.*|build_type='$build_type'|" \
   -e "s|^cmake_install_prefix=.*|cmake_install_prefix='$cmake_install_prefix'|" \
   -e "s|^extra_cxx_flags=.*|extra_cxx_flags='$extra_cxx_flags'|" \
   -e "s|^cmake_libdir=.*|cmake_libdir='$libdir'|" \
   -e "s|^ldlt_cholmod=.*|ldlt_cholmod='yes'|" \
   -e "s|^optimize_cppad_function=.*|optimize_cppad_function='$optimize'|" \
   -e "s|^for_hes_sparsity=.*|for_hes_sparsity='yes'|" \
   bin/run_cmake.sh > run_cmake.$$
mv run_cmake.$$ bin/run_cmake.sh
chmod +x bin/run_cmake.sh
#
# check edit
list="
   ^verbose_makefile='no'
   ^build_type='$build_type'
   ^cmake_install_prefix='$cmake_install_prefix'
   ^cmake_libdir='$libdir'
   ^ldlt_cholmod='yes'
   ^optimize_cppad_function='$optimize'
   ^for_hes_sparsity='yes'
"
for pattern in $list
do
   if ! grep "$pattern" bin/run_cmake.sh > /dev/null
   then
      echo "get_cppad_mixed.sh: Edit of $dir/bin/run_cmake.sh failed"
      exit 1
   fi
done
# $extra_cxx_flags my have spaces in it
if ! grep "^extra_cxx_flags='$extra_cxx_flags'"  bin/run_cmake.sh > /dev/null
then
   echo "get_cppad_mixed.sh: Edit of $dir/bin/run_cmake.sh failed"
   exit 1
fi
# -----------------------------------------------------------------------------
# cppad_mixed example install
run_test='false'
replace='false'
echo_eval bin/example_install.sh $run_test $replace
#
# -----------------------------------------------------------------------------
echo 'get_cppad_mixed.sh: OK'
exit 0
