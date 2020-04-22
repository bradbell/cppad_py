#! /bin/bash -e
#! /bin/bash -e
# -----------------------------------------------------------------------------
#         cppad_py: A C++ Object Library and Python Interface to Cppad
#          Copyright (C) 2017-20 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# -----------------------------------------------------------------------------
version=`grep '^SET(cppad_py_version' CMakeLists.txt | \
		sed -e 's|^[^"]*"\([^"]*\)".*|\1|'`
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
list="
	dist
	cppad_py
	$HOME/prefix/cppad_py
	build/bdist.linux-x86_64
	build/lib.linux-x86_64-3.7
	build/temp.linux-x86_64-3.7
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
	echo_eval pip uninstall cppad_py
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
