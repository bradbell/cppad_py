#! /bin/bash -e
# -----------------------------------------------------------------------------
#         cppad_py: A C++ Object Library and Python Interface to Cppad
#          Copyright (C) 2017-22 Bradley M. Bell (bradbell@seanet.com)
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
if [ "$0" != 'bin/run_sphinx.sh' ]
then
   echo 'must execut bin/run_sphinx.sh from its parent directory'
   exit 1
fi
# -----------------------------------------------------------------------------
if [ "$1" != 'html' ] && [ "$1" != 'pdf' ]
then
   echo 'usage: bin/run_sphinx (html|pdf)'
   exit 1
fi
target="$1"
# -----------------------------------------------------------------------------
project='cppad_py'
if ! grep "{xrst_begin $project}" cppad_py.xrst > /dev/null
then
   echo "can not find {xrst_begin $project} in cppad_py.xrst"
   exit 1
fi
# -----------------------------------------------------------------------------
# xsrst
xrst --target $target --output doc cppad_py.xrst
# -----------------------------------------------------------------------------
echo 'run_sphinx.sh: OK'
exit 0
