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
# cppad_prefix
eval $(grep '^cppad_prefix *=' bin/get_cppad.sh)
if ! echo $cppad_prefix | grep '^/' > /dev/null
then
    # convert cppad_prefix to an absolute path
    cppad_prefix="$(pwd)/$cppad_prefix"
fi
#
# cppad_libdir
eval $(grep '^cppad_libdir *=' bin/get_cppad.sh)
#
echo "build_type=$build_type"
echo "cppad_prefix=$cppad_prefix"
echo "cppad_libdir=$cppad_libdir"
# ---------------------------------------------------------------------------
# LD_LIBRARY_PATH
# PYTHONPATH
cat << EOF > check_install.py
import sys
minor = sys.version_info.minor
print( minor )
sys.exit(0)
EOF
minor=$(python check_install.py)
export LD_LIBRARY_PATH="${cppad_prefix}/${cppad_libdir}"
export PYTHONPATH="$LD_LIBRARY_PATH/python3.$minor/site-packages"
echo "LD_LIBRARY_PATH=$LD_LIBRARY_PATH"
echo "PYTHONPATH=$PYTHONPATH"
# ---------------------------------------------------------------------------
# remove old cppad_py and xsrst.py
if [ -e "$cppad_prefix" ]
then
    list=$(find -L "$cppad_prefix" \
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
echo_eval python3 setup.py install --prefix=$cppad_prefix
# ---------------------------------------------------------------------------
echo_eval python3 check_install.py
rm check_install.py
# ---------------------------------------------------------------------------
cppad_path="$cppad_prefix/bin"
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
