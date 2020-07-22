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
sphinxdir='sphinx'
# -----------------------------------------------------------------------------
echo "bin/xsrst.py bin/xsrst.py $sphinxdir spell_file index_file"
if ! bin/xsrst.py bin/xsrst.py $sphinxdir spell_file  index_file 2> xsrst.$$
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
echo_eval cd sphinx
file_list=$(ls xsrst/*.rst | sed -e 's|^xsrst/||' )
for file in $file_list
do
    if [ "$file" != 'xsrst_py.rst' ]
    then
        if [ ! -e test_out/$file ]
        then
            echo "The output file $sphinxdir/test_out/$file does not exist."
            echo 'Check that the corresponding sections are correct and then:'
            echo "    cp $sphinxdir/xsrst/$file $sphinxdir/test_out/$file"
            exit 1
        elif ! diff test_out/$file xsrst/$file
        then
            echo "$sphinxdir/xsrst/$file changed; above is output of"
            echo "	diff test_out/$file xsrst/$file"
            echo 'If the new file is currect, replace old with new using:'
            echo "    cp $sphinxdir/xsrst/$file $sphinxdir/test_out/$file"
            exit 1
        else
            echo "$file: OK"
        fi
    fi
done
file_list=$(ls test_out/*.rst | sed -e 's|^test_out/||' )
for file in $file_list
do
    if [ ! -e xsrst/$file ]
    then
        echo "The output file $sphinxdir/xsrst/$file does not nexist."
        echo "Use he following command to remove $sphinxdir/test_out/$file ?"
        echo "	git rm $sphinxdir/test_out/$file"
        exit 1
    fi
done
# -----------------------------------------------------------------------------
if ! make html
then
    echo 'bin/check_xsrst.sh: see errors above during the command'
    echo '    cd sphinx'
    echo '    make html'
    exit 1
fi
# -----------------------------------------------------------------------------
echo "$0: OK"
exit 0
