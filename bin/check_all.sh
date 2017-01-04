#! /bin/bash -e
# -----------------------------------------------------------------------------
#         cppad_swig: A C++ Object Library and Swig Interface to CppAD
#          Copyright (C) 2017-17 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#          GNU Affero General Public License version 3.0 or later see
#                     http://www.gnu.org/licenses/agpl.txt
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
# -----------------------------------------------------------------------------
if [ -e $logfile ]
then
	echo check_all.log
	rm $logfile
fi
echo_eval_log bin/run_omhelp.sh xml
echo_eval_log bin/run_cmake.sh
echo_eval_log cd build
echo_eval_log make check
rm $tmpfile
#
check_list='
	example_python
	example_octave
	example_perl
	example
	lib_python
	lib_octave
	lib_perl
	lib
'
for check in $check_list
do
	if ! grep "make check_$check: available" $logfile > /dev/null
	then
		echo "check_all.sh:	make check_$check is missing"
		exit 1
	fi
done
#
if grep -i 'warning' $logfile
then
	echo 'check_all.sh: Error: see warnings in check_all.log'
	exit 1
fi
# -----------------------------------------------------------------------------
echo 'bin/check_all.sh: OK'
exit 0