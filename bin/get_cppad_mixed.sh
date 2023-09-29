#! /bin/bash -e
# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileCopyrightText: Bradley M. Bell <bradbell@seanet.com>
# SPDX-FileContributor: 2017-23 Bradley M. Bell
# ----------------------------------------------------------------------------
#
#
# {xrst_begin get_cppad_mixed.sh}
# {xrst_spell
#     caching
#     cmake
#     cxx
#     rm
#     uninstall
# }
# {xrst_comment_ch #}
#
# Get cppad_mixed
# ###############
#
# Syntax
# ******
# ``bin/get_cppad_mixed.sh``
# ``bin/rm_cppad_mixed.sh``
#
# Top Source Directory
# ********************
# This program must be run from the
# :ref:`top_source_directory<old_setup.py@Download@Top Source Directory>`.
#
# Purpose
# *******
# If you are going to use the python ``cppad_mixed`` module,
# you will need to run this script to install the corresponding
# C++ module. This script includes the installation of cppad so it is not
# necessary to also run :ref:`get_cppad.sh-name`.
#
# Settings
# ********
# This scripts uses the
# :ref:`get_cppad.sh-name` for
# *cmake_install_prefix* , *extra_cxx_flags*, and *build_type* .
#
# Caching
# *******
# This script caches previous builds so that
# when you re-run the script it does not re-do all the work.
# If you have trouble, try deleting the directory
#
# | |tab| ``external/cppad_mixed.git``
#
# and re-running this script.
#
#
# Uninstall
# *********
# {xrst_toc_table
#     bin/rm_cppad_mixed.sh
# }
#
# {xrst_end get_cppad_mixed.sh}
# ---------------------------------------------------------------------------
# CppAD mixed version information
web_page='https://github.com/bradbell/cppad_mixed.git'
hash_key='1a3f3c75b02be9f013fed53a8e4bcd28e6430bd7'
version='20230913'
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
# build_type, extra_cxx_flags, cmake_install_prefix, include_mixed
eval $(bin/install_settings.py)
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
replace='true'
echo_eval bin/example_install.sh $run_test $replace
# -----------------------------------------------------------------------------
# cmake_install_prefix/include/Eigen
target="$cmake_install_prefix/eigen/include/eigen3/Eigen"
link_name="$cmake_install_prefix/include/Eigen"
if [ ! -d $target ]
then
   echo "get_cppad_mixed.sh: expected directory $target"
   exit 1
fi
if [ -e "$link_name" ]
then
   rm $link_name
fi
ln -s $target $link_name
ls -l $link_name
# -----------------------------------------------------------------------------
echo 'get_cppad_mixed.sh: OK'
exit 0
