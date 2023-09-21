#! /usr/bin/env bash
# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileCopyrightText: Bradley M. Bell <bradbell@seanet.com>
# SPDX-FileContributor: 2017-23 Bradley M. Bell
# ----------------------------------------------------------------------------
set -e -u
# bash function that echos and executes a command
echo_eval() {
   echo $*
   eval $*
}
# -----------------------------------------------------------------------------
if [ "$0" != 'bin/run_xrst.sh' ]
then
   echo 'must execut bin/run_xrst.sh from its parent directory'
   exit 1
fi
# -----------------------------------------------------------------------------
if [ "$#" != 0 ]
then
   echo 'bin/run_xrst.sh does not expect any arguments'
   exit 1
fi
# -----------------------------------------------------------------------------
if [ -e build/html ]
then
   rm -r build/html
fi
xrst \
   --target html \
   --html_theme sphinx_rtd_theme \
   --local_toc
# -----------------------------------------------------------------------------
echo 'run_xrst.sh: OK'
exit 0
