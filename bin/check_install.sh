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
# ---------------------------------------------------------------------------
# remove old cppad_py
name="$HOME/prefix/cppad_py"
if [ -e $name ]
then
	echo_eval rm -r $name
fi
name="cppad_py"
if [ -e $name ]
then
	echo_eval rm -r $name
fi
#
cat << EOF > check_install.py
import cppad_py
print( 'import cppad_py: OK')
EOF
if $python check_install.py >& /dev/null
then
	echo 'cannot remove old copy cppad_py in python path. Try'
	echo 'pip uninstall cppad-py'
	exit 1
fi
# ---------------------------------------------------------------------------
cppad_path=`echo 'import numpy; print(numpy.__file__)' | python | sed \
	-e 's|/numpy/__init__.py||' \
	-e "s|^/.*/\(lib[^.]*\)/python|$HOME/prefix/cppad_py/\1/python|"`
PYTHONPATH="$cppad_path:$PYTHONPATH"
# ---------------------------------------------------------------------------
# install new version
if [ "$build_type" == 'debug' ]
then
	build_flag='--sebug'
else
	build_flag=''
fi
echo_eval $python setup.py build_ext $buld_flag install \
	--prefix=$HOME/prefix/cppad_py
echo_eval rm -r cppad_py
# ---------------------------------------------------------------------------
echo_eval $python check_install.py
# ---------------------------------------------------------------------------
rm check_install.py
echo 'check_install.sh: OK'
exit 0
