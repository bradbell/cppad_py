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
if [ "$1" != 'debug' ] && [ "$1" != 'omh2xsrst' ] && [ "$1" != 'xsrst' ] && [ "$1" != 'sphinx' ]
then
    echo 'usage: bin/run_xsrst.sh (debug|omh2xsrst|xsrst|sphinx)'
    exit 1
fi
job="$1"
#
sphinx_dir='build/sphinx'
root_section='cppad_py'
#
if [ ! -e "$sphinx_dir" ]
then
    echo_eval mkdir $sphinx_dir
fi
if [ "$job" == 'debug' ] || [ "$job" == 'omh2xsrst' ]
then
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
    file_list=$(git grep -l '[$@]begin ')
    for file in $file_list
    do
        executable='no'
        if [[ -x $file ]]
        then
            executable='yes'
        fi
        echo "omh2xsrst.py $file $sphinx_dir/spell_file > junk.1.out"
        if [ "$job" == 'debug' ]
        then
            omh2xsrst.py $file $sphinx_dir/spell_file
        else :
            omh2xsrst.py $file $sphinx_dir/spell_file > junk.1.out
            echo_eval mv junk.1.out $file
            if [ "$executable" == 'yes' ]
            then
                chmod +x $file
            fi
        fi
    done
fi
if [ "$job" == 'xsrst' ]
then
    #
    file=$(git grep -l "{xsrst_begin $root_section}")
    echo_eval bin/xsrst.py $file $sphinx_dir spell_file index_file
fi
if [ "$job" == 'sphinx' ]
then
    echo_eval cd $sphinx_dir
    echo_eval make html
fi
# -----------------------------------------------
echo 'run_xsrst.sh: OK'
exit 0
