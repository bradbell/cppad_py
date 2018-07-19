#! /bin/bash -e
# -----------------------------------------------------------------------------
#         cppad_py: A C++ Object Library and Python Interface to Cppad
#          Copyright (C) 2017-18 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# -----------------------------------------------------------------------------
# bash function that echos and executes a command
logfile=`pwd`/check_all.log
tmpfile=`pwd`/check_all.$$
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
if [ ! -e 'build/prefix/include/cppad/cppad.hpp' ]
then
	echo 'check_all.sh: must first run bin/get_cppad.sh'
	exit 1
fi
# -----------------------------------------------------------------------------
# python_major_version
set +e
random_01=`expr $RANDOM % 2`
set -e
python_major_version=`expr $random_01 + 2`
echo "Testing python$python_major_version"
# -----------------------------------------------------------------------------
# clean out old informaiton
if [ -e $logfile ]
then
	echo "rm check_all.log"
	rm $logfile
fi
# -----------------------------------------------------------------------------
# run checks
list=`ls bin/check_*`
for check in $list
do
	if [ "$check" != 'bin/check_all.sh' ]
	then
		echo_eval_log $check
	fi
done
# -----------------------------------------------------------------------------
#
echo_eval_log check_copyright.sh
echo_eval_log run_omhelp.sh doc
echo_eval_log python$python_major_version setup.py build_ext --inplace --quiet
echo_eval_log cd build
echo_eval_log make clean
echo_eval_log make check
echo_eval_log cd ..
#
if grep -i 'warning' $logfile
then
	echo 'check_all.sh: Error: see warnings in check_all.log'
	rm $tmpfile
	exit 1
fi
# -----------------------------------------------------------------------------
rm $tmpfile
echo 'bin/check_all.sh: OK'
exit 0
