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
if [ "$0" != "bin/run_xsrst.sh" ]
then
    echo "bin/run_xsrst.sh: must be executed from its parent directory"
    exit 1
fi
# -----------------------------------------------------------------------------
sphinx_dir='build/sphinx'
root_section='cppad_py'
#
if [ ! -e "$sphinx_dir" ]
then
    echo_eval mkdir $sphinx_dir
fi
list='
    conf.py
    index.rst
    preamble.rst
    spell_file
    index_file
    Makefile
'
for file in $list
do
    cp -r sphinx/$file $sphinx_dir/$file
done
echo "sed -i $sphinx_dir/conf.py -e s|^project *=.*|project = 'cppad_py'|"
sed -i $sphinx_dir/conf.py -e "s|^project *=.*|project = 'cppad_py'|"
#
echo "sed -i $sphinx_dir/index.rst -e s|xsrst/xsrst_py|xsrst/$root_section|"
sed -i $sphinx_dir/index.rst -e "s|xsrst/xsrst_py|xsrst/$root_section|"
#
echo_eval bin/xsrst.py doc.omh $sphinx_dir spell_file index_file
echo_eval cd $sphinx_dir
echo_eval make html
# -----------------------------------------------
echo 'run_xsrst.sh: OK'
exit 0
