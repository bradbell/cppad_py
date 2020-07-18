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
program=...
# -----------------------------------------------------------------------------
if [ "$0" != "bug/$program.sh" ]
then
    echo "bug/$program.sh must be executed from its parent directory"
    exit 1
fi
top_source_dir=`pwd`
# -----------------------------------------------------------------------------
if [ "$1" != '2' ] && [ "$1" != '3' ]
then
    echo "usage: bug/$program.sh python_major_version"
    echo 'where python_major_version is 2 or 3.'
    echo 'This program returns ok = False for both versions of python.'
    echo 'Must run setup.py with same version of python before this script.'
    exit 1
fi
python_major_version="$1"
# -----------------------------------------------------------------------------
if [ ! -e 'build/bug' ]
then
    echo_eval mkdir -p build/bug
fi
cd build/bug
# -----------------------------------------------------------------------------
cat << EOF > $program.py
import sys
import os
import numpy
sys.path.insert(0, '$top_source_dir')
import cppad_py
#
def fun() :
    ...
#
# initialize return variable
ok = True
# ---------------------------------------------------------------------
...
# ---------------------------------------------------------------------
if ok :
    sys.exit( '$program: OK' )
sys.exit( '$progam: Error' )
EOF
echo_eval python$python_major_version $program.py
