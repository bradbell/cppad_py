#! /bin/bash -e
# -----------------------------------------------------------------------------
#         cppad_py: A C++ Object Library and Python Interface to Cppad
#          Copyright (C) 2017-20 Bradley M. Bell (bradbell$seanet.com)
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
if [ "$0" != "bin/build_type.sh" ]
then
    echo "bin/build_type.sh: must be executed from its parent directory"
    exit 1
fi
# -----------------------------------------------------------------------------
eval $(grep '^build_type *=' bin/get_cppad.sh)
eval $(grep '^cppad_prefix *=' bin/get_cppad.sh)
if [ "$build_type" != 'debug' ] && [ "$build_type" != 'release' ]
then
    echo 'build_type.sh: build_type in get_cppad.sh is not debug or release'
    exit 1
fi
if ! echo $cppad_prefix | grep '^/' > /dev/null
then
    # convert cppad_prefix to an absolute path
    cppad_prefix="$(pwd)/$cppad_prefix"
fi
echo "build_type=$build_type"
echo "cppad_prefix=$cppad_prefix"
# -----------------------------------------------------------------------------
for target in $cppad_prefix build
do
    # link target to target.build_type
    if [ ! -d "$target.$build_type" ]
    then
        echo_eval mkdir -p "$target.$build_type"
    fi
    if [ -e "$target" ]
    then
        if [ ! -L "$target" ]
        then
            echo "build_type.sh: $target is not a symbolic link"
            exit 1
        fi
        echo_eval rm "$target"
    fi
    echo_eval ln -s $target.$build_type $target
done
# -----------------------------------------------------------------------------
echo 'build_type.sh: OK'
exit 0
