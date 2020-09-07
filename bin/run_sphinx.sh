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
if ! grep BEGIN_LATEX_MACROS sphinx/preamble.rst > /dev/null
then
    echo "bin/run_sphinx: can't find BEGIN_LATEX_MACROS in sphinc/premable.rst"
fi
if ! grep END_LATEX_MACROS sphinx/preamble.rst > /dev/null
then
    echo "bin/run_sphinx: can't find END_LATEX_MACROS in sphinc/premable.rst"
fi
# -----------------------------------------------------------------------------
project='cppad_py'
if ! grep "{xsrst_begin $project}" doc.xsrst > /dev/null
then
    echo "can not find {xsrst_begin $project} in doc.xsrst"
    exit 1
fi
# -----------------------------------------------------------------------------
# xsrst
echo_eval bin/xsrst.py doc.xsrst sphinx spelling keyword
# -----------------------------------------------------------------------------
cd sphinx
# -----------------------------------------------------------------------------
# html
if [ "$target" == 'html' ]
then
    make html
    echo 'run_sphinx.sh: OK'
    exit 0
fi
# -----------------------------------------------------------------------------
# pdf
diff=$(git diff preamble.rst)
if [ "$diff" != '' ]
then
    echo 'bin/run_sphinx.sh pdf:'
    echo 'sphinx/preamble.rst has changed.'
    echo 'You must first test bin/run_sphinx.sh html.'
    echo 'Then check in preamble.rst before testing bin/run_sphinx.sh pdf.'
    exit 1
fi
echo "sed -i preamble.rst -e '/BEGIN_LATEX_MACROS/,/END_LATEX_MACROS/d'"
sed -i preamble.rst -e '/BEGIN_LATEX_MACROS/,/END_LATEX_MACROS/d'
make latexpdf
git checkout preamble.rst
# -----------------------------------------------------------------------------
echo 'run_sphinx.sh: OK'
exit 0
