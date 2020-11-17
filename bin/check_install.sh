#! /bin/bash -e
# -----------------------------------------------------------------------------
#         cppad_py: A C++ Object Library and Python Interface to Cppad
#          Copyright (C) 2017-20 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# -----------------------------------------------------------------------------
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
# remove old cppad_py and xsrst.py
# ---------------------------------------------------------------------------
if [ -e "$cmake_install_prefix" ]
then
    list=$(find -L "$cmake_install_prefix" \
        -name 'cppad_py' -or   \
        -name 'cppad_py-*' -or \
        -name 'xsrst.py' )
    for name in dist cppad_py.egg-info cppad_py $list
    do
        if [ -e "$name" ]
        then
            echo_eval rm -r $name
        fi
    done
fi
#
if echo 'import cppad_py' | python3 >& /dev/null
then
    echo 'check_install.py: cannot remove old cppad_py in python path. Try'
    echo '    pip uninstall cppad_py'
    echo '    bin/check_install.sh'
    exit 1
fi
if which xsrst.py >& /dev/null
then
    echo 'check_install.py: cannot remove old xsrst.py in execution path.'
    echo 'Use the following command to see where it is:'
    echo '  which xsrst.py'
    exit 1
fi
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
# PYTHONPATH
minor=$(echo "import sys;print(sys.version_info.minor)" | python3)
export PYTHONPATH=$prefix/$libdir/python3.$minor/site-packages
#
# Install
python3 setup.py install --prefix=$prefix
#
# Test Installed Version
if [ -e cppad_py ]
then
    echo 'check_install.sh: setup.py did not remove local cppad_py directory'
fi
python3 example/python/check_all.py
# ---------------------------------------------------------------------------
xsrst_path="$cmake_install_prefix/bin/xsrst.py"
if [ ! -x "$xsrst_path" ]
then
    echo "check_install.sh: $xsrst_path is not an executale file"
    exit 1
fi
# ---------------------------------------------------------------------------
echo 'check_install.sh: OK'
exit 0
