#! /bin/bash -e
# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileCopyrightText: Bradley M. Bell <bradbell@seanet.com>
# SPDX-FileContributor: 2017-22 Bradley M. Bell
# ----------------------------------------------------------------------------
version=`grep '^SET(cppad_py_version' CMakeLists.txt | \
      sed -e 's|^[^"]*"\([^"]*\)".*|\1|'`
eval $(grep '^build_type *=' bin/get_cppad.sh)
if [ "$build_type" != 'release' ]
then
   echo 'check_pip.sh: build_type in get_cpapd.sh is not release'
   exit 1
fi
# -----------------------------------------------------------------------------
# bash function that echos and executes a command
echo_eval() {
   echo $*
   eval $*
}
# -----------------------------------------------------------------------------
if [ "$0" != "bin/check_pip.sh" ]
then
   echo "bin/check_pip.sh: must be executed from its parent directory"
   exit 1
fi
python='python3'
# ---------------------------------------------------------------------------
eval $(grep '^cmake_install_prefix *=' bin/get_cppad.sh)
#
if  ls $cmake_install_prefix/lib/libcppad_lib.* >& /dev/null
then
   LD_LIBRARY_PATH="$cmake_install_prefix/lib:$LD_LIBRARY_PATH"
elif  ls $cmake_install_prefix/lib64/libcppad_lib.\* >& /dev/null
then
   LD_LIBRARY_PATH="$cmake_install_prefix/lib64:$LD_LIBRARY_PATH"
else
   echo 'check_all.sh: cannot find libcppad_lib.* re-run bin/get_cppad.sh ?'
   exit 1
fi
# -----------------------------------------------------------------------------
list="
   dist
   cppad_py
"
for name in $list
do
   if [ -e $name ]
   then
      echo_eval rm -r $name
   fi
done
if [ -e cppad_py ]
then
   echo_eval rm -r cppad_py
fi
# ----------------------------------------------------------------------------
cat << EOF > check_pip.$$
import sys
import cppad_py
x = cppad_py.a_double(2.0)
assert x.value() == 2.0
sys.exit(0)
EOF
if python check_pip.$$ >& /dev/null
then
   echo_eval # pip uninstall cppad_py
   echo 'y' | pip uninstall cppad_py
fi
if python check_pip.$$ >& /dev/null
then
   'check_pip.sh: Cannot remove old copy of cppad_py'
   exit 1
fi
# ----------------------------------------------------------------------------
# pip install --no-binary :all:
# --global-option build --global-option --debug PACKAGE
#
echo_eval python setup.py sdist
echo_eval cd dist
echo_eval pip install --prefix="$HOME/prefix/cppad_py" \
   cppad_py-$version.tar.gz
# ----------------------------------------------------------------------------
# check installed not local copy
path2cppad_py=$(find $HOME/prefix/cppad_py -name 'site-packages')
PYTHONPATH="$path2cppad_py:$PYTHONPATH"
echo "PYTHONPATH+$PYTHONPATH"
if ! python ../check_pip.$$
then
   echo 'check_pip.sh: install failed'
   exit 1
fi
rm ../check_pip.$$
# ----------------------------------------------------------------------------
echo 'check_pip.sh: OK'
exit 0
