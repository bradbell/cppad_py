#! /bin/bash -e
# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileCopyrightText: Bradley M. Bell <bradbell@seanet.com>
# SPDX-FileContributor: 2017-23 Bradley M. Bell
# ----------------------------------------------------------------------------
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
if [ "$1" != 'html' ] && [ "$1" != 'pdf' ]
then
   echo 'usage: bin/run_xrst (html|pdf)'
   exit 1
fi
target="$1"
# -----------------------------------------------------------------------------
# xsrst
if [ "$target" == 'html' ]
then
   xrst \
      --target html \
      --html_theme sphinx_rtd_theme \
      --local_toc
else
   xrst --target tex
   make -C build/tex cppad_py.pdf
fi
# -----------------------------------------------------------------------------
echo 'run_xrst.sh: OK'
exit 0
