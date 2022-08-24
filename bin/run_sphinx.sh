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
# preamble
preamble='sphinx/preamble.rst'
# -----------------------------------------------------------------------------
if ! grep BEGIN_LATEX_MACROS $preamble > /dev/null
then
    echo "bin/run_sphinx: can't find BEGIN_LATEX_MACROS in $premable"
fi
if ! grep END_LATEX_MACROS $preamble > /dev/null
then
    echo "bin/run_sphinx: can't find END_LATEX_MACROS in $premable"
fi
# -----------------------------------------------------------------------------
project='cppad_py'
if ! grep "{xsrst_begin $project}" doc.xrst > /dev/null
then
    echo "can not find {xsrst_begin $project} in doc.xrst"
    exit 1
fi
# -----------------------------------------------------------------------------
# xsrst
echo_eval bin/xsrst.py $target doc.xrst sphinx spelling keyword
# -----------------------------------------------------------------------------
# html
# -----------------------------------------------------------------------------
if [ "$target" == 'html' ]
then
    sphinx-build -b html sphinx doc/html
    echo 'run_sphinx.sh: OK'
    exit 0
fi
# -----------------------------------------------------------------------------
# pdf
# -----------------------------------------------------------------------------
#
diff=$(git diff $preamble)
if [ "$diff" != '' ]
then
    echo 'bin/run_sphinx.sh pdf:'
    echo "$preamble has changed."
    echo 'You must first test bin/run_sphinx.sh html.'
    echo "Then check in the new $preamble before running bin/run_sphinx.sh pdf."
    exit 1
fi
echo "sed -i $preamble -e '/BEGIN_LATEX_MACROS/,/END_LATEX_MACROS/d'"
sed -i $preamble -e '/BEGIN_LATEX_MACROS/,/END_LATEX_MACROS/d'
echo_eval sphinx-build -b latex sphinx doc/latex
echo_eval git checkout $preamble
echo_eval cd doc/latex
echo "sed -i cppad_py.tex -e 's|\\chapter{|\\section{|'"
sed -i cppad_py.tex -e 's|\\chapter{|\\section{|'
echo_eval make cppad_py.pdf
# -----------------------------------------------------------------------------
echo 'run_sphinx.sh: OK'
exit 0
