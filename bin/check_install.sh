#! /bin/bash -e
# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileCopyrightText: Bradley M. Bell <bradbell@seanet.com>
# SPDX-FileContributor: 2017-22 Bradley M. Bell
# ----------------------------------------------------------------------------
# bash function that echos and executes a command
echo_eval() {
   echo $*
   eval $*
}
# -----------------------------------------------------------------------------
if [ "$0" != "bin/check_install.sh" ]
then
   echo "bin/check_install.sh: must be executed from its parent directory"
   exit 1
fi
# -----------------------------------------------------------------------------
# build_type
eval $(grep '^build_type *=' bin/get_cppad.sh)
#
# cmake_install_prefix
eval $(grep '^cmake_install_prefix *=' bin/get_cppad.sh)
if ! echo $cmake_install_prefix | grep '^/' > /dev/null
then
   # convert cmake_install_prefix to an absolute path
   cmake_install_prefix="$(pwd)/$cmake_install_prefix"
fi
#
echo "build_type=$build_type"
echo "cmake_install_prefix=$cmake_install_prefix"
# ---------------------------------------------------------------------------
# Follow install instructions in setup.py
# ---------------------------------------------------------------------------
#
# prefix
cmd=$(grep '^cmake_install_prefix=' bin/get_cppad.sh)
eval $cmd
prefix="$cmake_install_prefix"
#
# libdir
libdir=$(bin/libdir.py)
#
# LD_LIBRARY_PATH
if which brew >& /dev/null
then
   # This is a mac
   export DYLD_LIBRARY_PATH="$prefix/$libdir"
else
   export LD_LIBRARY_PATH="$prefix/$libdir"
fi
#
# PKGCONFIG_PATH
export PKG_CONFIG_PATH="$prefix/$libdir/pkgconfig"
#
# Local Build
if ls build/lib.* >& /dev/null
then
   rm -r build/lib.*
fi
python3 setup.py bdist
name=$(ls build | grep '^lib\.' | sed -e 's|^lib\.||')
cp -r build/lib.$name/cppad_py cppad_py
#
# Local Test
PYTHONPATH=""
python3 example/python/check_all.py
#
# Install
python3 setup.py install --prefix=$prefix
#
# PYTHONPATH
minor=$(echo "import sys;print(sys.version_info.minor)" | python3)
dir="$prefix/$libdir/python3.$minor/site-packages"
if [ -d $dir ]
then
   export PYTHONPATH="$dir"
else
   dir="$prefix/local/$libdir/python3.$minor/site-packages"
   if [ -d $dir ]
   then
      export PYTHONPATH="$dir"
   else
      echo 'Cannot find sitepackages'
      exit 1
   fi
fi
#
# check installed version
if [ -e cppad_py ]
then
   echo 'check_install.sh: setup.py did not remove local cppad_py directory'
   exit 1
fi
python3 example/python/check_all.py
# ---------------------------------------------------------------------------
echo 'check_install.sh: OK'
exit 0
