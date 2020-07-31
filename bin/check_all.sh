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
        rm $tmpfile
        exit 1
    fi
    cat $tmpfile >> $logfile
}
# -----------------------------------------------------------------------------
if [ "$0" != "bin/check_all.sh" ]
then
    echo "bin/check_all.sh: must be executed from its parent directory"
    exit 1
fi
# -----------------------------------------------------------------------------
eval $(grep '^build_type *=' bin/get_cppad.sh)
eval $(grep '^cppad_prefix *=' bin/get_cppad.sh)
eval $(grep '^extra_cxx_flags *=' bin/get_cppad.sh)
# -----------------------------------------------------------------------------
if  ls $cppad_prefix/lib/libcppad_lib.* >& /dev/null
then
    LD_LIBRARY_PATH="$cppad_prefix/lib:$LD_LIBRARY_PATH"
elif  ls $cppad_prefix/lib64/libcppad_lib.\* >& /dev/null
then
    LD_LIBRARY_PATH="$cppad_prefix/lib64:$LD_LIBRARY_PATH"
else
    echo 'check_all.sh: cannot find libcppad_lib.* re-run bin/get_cppad.sh ?'
    exit 1
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
echo_eval bin/check_xsrst.sh
echo_eval_log bin/run_xsrst.sh
# -----------------------------------------------------------------------------
if [ "$build_type" == 'release' ]
then
    setup_args='build_ext'
elif [ "$build_type" == 'debug' ]
then
    setup_args='build_ext --debug'
else
    echo 'bin/check_all.sh: build_type in bin/get_cppad.sh not debug or release'
    exit 1
fi
echo_eval_log python3 setup.py $setup_args
echo_eval_log cd build
echo_eval_log make check
echo_eval_log cd ../example/python
echo_eval_log python3 check_all.py
echo_eval_log cd ../..
#
# 2DO: figure out where this waring is coming from and what it means
sed -i $logfile -e '/fun\.hpp:52: Warning 362: operator= ignored/d'
#
if [ "$build_type" == 'debug' ]
then
    if grep 'warning.*_FORTIFY_SOURCE' $logfile > /dev/null
    then
        grep 'warning.*_FORTIFY_SOURCE' $logfile | head -1
        sed -i $logfile -e '/warning.*_FORTIFY_SOURCE/d'
    fi
fi
#
if grep -i 'warning' $logfile
then
    echo 'check_all.sh: Error: see warnings in check_all.log'
    rm $tmpfile
    exit 1
fi
# -----------------------------------------------------------------------------
bin/check_install.sh
# -----------------------------------------------------------------------------
rm $tmpfile
echo 'bin/check_all.sh: OK'
exit 0
