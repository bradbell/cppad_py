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
if [ "$0" != "bin/check_xsrst.sh" ]
then
    echo "bin/check_xsrst.sh: must be executed from its parent directory"
    exit 1
fi
test_dir='build/sphinx'
# -----------------------------------------------------------------------------
if [ -e "$test_dir" ]
then
    echo_eval rm -r $test_dir
fi
echo_eval mkdir -p $test_dir
list='
    conf.py
    index.rst
    preamble.rst
    spelling
    keyword
    Makefile
'
for file in $list
do
    cp -r sphinx/$file $test_dir/$file
done
echo "sed -i $test_dir/conf.py -e s|^project *=.*|project = 'xsrst'|"
sed -i $test_dir/conf.py -e "s|^project *=.*|project = 'xsrst'|"
#
echo "sed -i $test_dir/index.rst -e s|xsrst/cppad_py|xsrst/xsrst_py|"
sed -i $test_dir/index.rst -e "s|xsrst/cppad_py|xsrst/xsrst_py|"
# -----------------------------------------------------------------------------
echo "bin/xsrst.py html bin/xsrst.py $test_dir spelling keyword"
if ! bin/xsrst.py html bin/xsrst.py $test_dir spelling  keyword 2> xsrst.$$
then
    type_error='error'
else
    type_error='warning'
fi
if [ -s xsrst.$$ ]
then
    cat xsrst.$$
    rm xsrst.$$
    echo "$0: exiting due to $type_error above"
    exit 1
fi
rm xsrst.$$
# -----------------------------------------------------------------------------
file_list=$(ls $test_dir/xsrst/*.rst | sed -e "s|^$test_dir/xsrst/||" )
for file in $file_list
do
    if [ "$file" != 'xsrst_py.rst' ]
    then
        if [ ! -e sphinx/test_out/$file ]
        then
            echo "The output file sphinx/test_out/$file does not exist."
            echo 'Check that the corresponding sections are correct and then:'
            echo "    cp $test_dir/xsrst/$file sphinx/test_out/$file"
            exit 1
        elif ! diff sphinx/test_out/$file $test_dir/xsrst/$file
        then
            echo "$test_dir/xsrst/$file changed; above is output of"
            echo "    diff sphinx/test_out/$file $test_dir/xsrst/$file"
            echo 'If the new file is currect, replace old with new using:'
            echo "    cp $test_dir/xsrst/$file sphinx/test_out/$file"
            exit 1
        else
            echo "$file: OK"
        fi
    fi
done
file_list=$(ls sphinx/test_out/*.rst | sed -e 's|^sphinx/test_out/||' )
for file in $file_list
do
    if [ ! -e $test_dir/xsrst/$file ]
    then
        echo "The output file $test_dir/xsrst/$file does not nexist."
        echo "Use he following command to remove sphinx/test_out/$file ?"
        echo "    git rm sphinx/test_out/$file"
        exit 1
    fi
done
# -----------------------------------------------------------------------------
echo_eval cd $test_dir
if ! make html
then
    echo 'bin/check_xsrst.sh: see errors above during the command'
    echo "    cd $test_dir"
    echo '    make html'
    exit 1
fi
# -----------------------------------------------------------------------------
echo "$0: OK"
exit 0
