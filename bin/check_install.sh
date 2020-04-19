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
python='python3'
# ---------------------------------------------------------------------------
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
# ---------------------------------------------------------------------------
cat << EOF > junk.$$
import cppad_py
print( 'import cppad_py: OK')
EOF
if $python junk.$$ >& /dev/null
then
	echo 'cannot remove old copy cppad_py in python path'
	exit 0
fi
# ---------------------------------------------------------------------------
# install new version
echo_eval $python setup.py build_ext --debug install \
	--prefix=$HOME/prefix/cppad_py
echo_eval rm -r cppad_py
#
path2cppad_py=$(find $HOME/prefix/cppad_py -name 'site-packages')
PYTHONPATH="$path2cppad_py:$PYTHONPATH"
#
echo_eval $python junk.$$
#
echo 'check_install.sh: OK'
exit 0
