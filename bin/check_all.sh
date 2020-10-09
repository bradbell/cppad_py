#! /bin/bash -e
# -----------------------------------------------------------------------------
#         cppad_py: A C++ Object Library and Python Interface to Cppad
#          Copyright (C) 2017-20 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# -----------------------------------------------------------------------------
# bash function that echos and executes a command
logfile=`pwd`/check_all.log
tmpfile=`pwd`/check_all.tmp
echo_eval_log() {
    echo "$* >> check_all.log"
    echo $* >> $logfile
    if ! eval $* >& $tmpfile
    then
        if grep -i 'error' $tmpfile
        then
            echo 'check_all.sh: errors above are in check_all.log'
        else
            echo 'check_all.sh: see check_all.log for errors'
        fi
        cat $tmpfile >> $logfile
        exit_code 1
    fi
    cat $tmpfile >> $logfile
}
# -----------------------------------------------------------------------------
# cleanup and exit with specified code
exit_code() {
    if [ "$build_type" == 'debug' ]
    then
        sed -i bin/get_cppad.sh -e "s|^build_type *=.*|build_type='release'|"
    fi
    if [ -e $tmpfile ]
    then
        rm $tmpfile
    fi
    exit $1
}
# -----------------------------------------------------------------------------
if [ "$0" != "bin/check_all.sh" ]
then
    echo "bin/check_all.sh: must be executed from its parent directory"
    exit_code 1
fi
if [ "$1" != 'debug' ] && [ "$1" != 'release' ]
then
    echo 'usage: bin/check_all.sh (debug|release)'
    exit_code 1
fi
# -----------------------------------------------------------------------------
eval $(grep '^build_type *=' bin/get_cppad.sh)
eval $(grep '^cppad_prefix *=' bin/get_cppad.sh)
eval $(grep '^extra_cxx_flags *=' bin/get_cppad.sh)
#
if ! echo $cppad_prefix | grep '^/' > /dev/null
then
    # convert cppad_prefix to an absolute path
    cppad_prefix="$(pwd)/$cppad_prefix"
fi
# -----------------------------------------------------------------------------
# set build_type
if [ "$build_type" != 'release' ]
then
    echo 'build_type in bin/get_cppad.sh is not release'
    echo 'This has been fixed, you should be able to just re-run this script.'
    exit_code 1
fi
if [ "$1" == 'debug' ]
then
    # This change will be undone by the exit_code function
    sed -i bin/get_cppad.sh -e "s|^build_type *=.*|build_type='debug'|"
    build_type='debug'
fi
echo_eval bin/build_type.sh
# -----------------------------------------------------------------------------
if  ls $cppad_prefix/lib/libcppad_lib.* >& /dev/null
then
    LD_LIBRARY_PATH="$cppad_prefix/lib:$LD_LIBRARY_PATH"
elif  ls $cppad_prefix/lib64/libcppad_lib.* >& /dev/null
then
    LD_LIBRARY_PATH="$cppad_prefix/lib64:$LD_LIBRARY_PATH"
else
    echo 'check_all.sh: cannot find libcppad_lib.* re-run bin/get_cppad.sh ?'
    exit_code 1
fi
# -----------------------------------------------------------------------------
# clean out old distribution
if [ -d 'cppad_py' ]
then
    echo_eval_log rm -r cppad_py
fi
if [ -d "$HOME/prefix/cppad_py" ]
then
    echo_eval_log rm -r "$HOME/prefix/cppad_py"
fi
if echo 'import cppad_py' | python >& /dev/null
then
    echo 'y' | pip uninstall cppad_py
fi
# -----------------------------------------------------------------------------
# clean out old informaiton
if [ -e $logfile ]
then
    echo "rm check_all.log"
    rm $logfile
fi
if ls build | grep '^lib\.' > /dev/null
then
    echo_eval rm -r "build/lib.*"
fi
if ls build | grep '^temp\.' > /dev/null
then
    echo_eval rm -r "build/temp.*"
fi
# -----------------------------------------------------------------------------
echo_eval_log check_copyright.sh
bin/check_tab.sh
echo_eval_log bin/check_xsrst.sh
echo_eval_log bin/run_sphinx.sh html
echo_eval_log bin/local_build.py
echo_eval_log cd build
echo_eval_log make check
echo_eval_log cd ../example/python
echo_eval_log python3 check_all.py
echo_eval_log cd ../..
echo_eval_log bin/check_install.sh
#
if [ "$build_type" == 'debug' ]
then
    if grep 'warning.*_FORTIFY_SOURCE' $logfile > /dev/null
    then
        count=$(grep 'warning.*_FORTIFY_SOURCE' $logfile | wc -l)
        echo "$count warinings about _FORTIFY_SOURCE deleted from check_all.log"
        sed -i $logfile -e '/warning.*_FORTIFY_SOURCE/d'
    fi
fi
# CppAD uses asserts to make sure this this is not a problem
sed -i $logfile -e "/match_op.hpp:.*warning: ‘arg_match\[[01]\]’/d"
#
if grep -i 'warning' $logfile
then
    echo 'check_all.sh: Error: see warnings in check_all.log'
    exit_code 1
fi
# -----------------------------------------------------------------------------
rm $tmpfile
echo 'bin/check_all.sh: OK'
exit_code 0
