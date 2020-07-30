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
if [ "$0" != 'bin/check_tab.sh' ]
then
    echo 'must execut bin/check_tab.sh from its parent directory'
    exit 1
fi
# -----------------------------------------------------------------------------
list=`git ls-files | sed -e '/^sphinx\/Makefile$/d'`
ok='yes'
for file in $list
do
    if grep $'\t' $file > /dev/null
    then
        echo "$file has a tabs"
        read -p "Try to convert them to spaces [y/n] ?" response
        if [ "$response" == 'y' ]
        then
            echo_eval tab2space.sh $file
        elif [ "$response" != 'n' ]
        then
            echo 'response was not y or n'
            exit 1
        fi
        ok='no'
    fi
done
if [ "$ok" == 'no' ]
then
    echo 'check_tab.sh: Error'
    exit 1
fi
echo 'check_tab.sh: OK'
exit 0
