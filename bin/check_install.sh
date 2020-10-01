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
# python
python='python3'
# build_type
eval $(grep '^build_type *=' bin/get_cppad.sh)
# cppad_prefix
eval $(grep '^cppad_prefix *=' bin/get_cppad.sh)
if ! echo $cppad_prefix | grep '^/' > /dev/null
then
    # convert cppad_prefix to an absolute path
    cppad_prefix="$(pwd)/$cppad_prefix"
fi
echo "build_type=$build_type"
echo "cppad_prefix=$cppad_prefix"
# ---------------------------------------------------------------------------
# remove old cppad_py
list=$(find -L $cppad_prefix -name 'cppad_py')
for dir in cppad_py $list
do
    if [ -e "$dir" ]
    then
        echo_eval rm -r $dir
    fi
done
#
if $python check_install.py >& /dev/null
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
cppad_path=`echo 'import numpy; print(numpy.__file__)' | python | sed \
    -e 's|/numpy/__init__.py||' \
    -e "s|^/.*/\(lib[^.]*\)/python|$cppad_prefix/\1/python|"`
PYTHONPATH="$cppad_path:$PYTHONPATH"
# ---------------------------------------------------------------------------
# install new version
if [ "$build_type" == 'debug' ]
then
    build_flag='--debug'
else
    build_flag=''
fi
echo_eval $python setup.py build_ext $build_flag install \
    --prefix=$cppad_prefix
echo_eval rm -r cppad_py
# ---------------------------------------------------------------------------
cat << EOF > check_install.py
import cppad_py
print( 'import cppad_py: OK')
EOF
echo_eval $python check_install.py
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
