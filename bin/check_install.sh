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
# libdir
libdir=$(bin/libdir.py)
#
echo "build_type=$build_type"
echo "cmake_install_prefix=$cmake_install_prefix"
echo "libdir=$libdir"
# ---------------------------------------------------------------------------
# LD_LIBRARY_PATH
# PYTHONPATH
cat << EOF > check_install.py
import sys
minor = sys.version_info.minor
print( minor )
sys.exit(0)
EOF
minor=$(python3 check_install.py)
export LD_LIBRARY_PATH="${cmake_install_prefix}/${libdir}"
export DYLD_LIBRARY_PATH="$LD_LIBRARY_PATH"
export PYTHONPATH="$LD_LIBRARY_PATH/python3.$minor/site-packages"
echo "LD_LIBRARY_PATH=$LD_LIBRARY_PATH"
echo "PYTHONPATH=$PYTHONPATH"
# ---------------------------------------------------------------------------
# remove old cppad_py and xsrst.py
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
# ---------------------------------------------------------------------------
# check_install.py
cat << EOF > check_install.py
import cppad_py
print( 'import cppad_py: OK')
EOF
# ---------------------------------------------------------------------------
#
if python3 check_install.py >& /dev/null
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
# install new version
echo_eval python3 setup.py install --prefix=$cmake_install_prefix
# ---------------------------------------------------------------------------
echo_eval python3 example/python/check_all.py
rm check_install.py
# ---------------------------------------------------------------------------
cppad_path="$cmake_install_prefix/bin"
PATH="$cppad_path:$PATH"
if ! which xsrst.py >& /dev/null
then
    echo 'check_install.sh: cannot find xsrst.py in execution path'
    echo "PATH=$PATH"
    exit 1
fi
# ---------------------------------------------------------------------------
echo 'check_install.sh: OK'
exit 0
