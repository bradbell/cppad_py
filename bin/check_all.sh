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
echo_eval_log run_omhelp.sh doc
# -----------------------------------------------------------------------------
# debug_01
set +e
debug_01=`expr $RANDOM % 2`
set -e
if [ "$debug_01" == '0' ]
then
	echo 'Testing release version'
else
	echo 'Testing debug version'
fi
# -----------------------------------------------------------------------------
if [ "$debug_01" == '0' ]
then
	setup_args='build_ext --quiet'
elif [ "$debug_01" == '1' ]
then
	setup_args='build_ext --quiet --debug --undef NDEBUG'
else
	echo 'bin/check_all.sh: program error'
	exit 1
fi
echo_eval_log python3 setup.py $setup_args
# -----------------------------------------------------------------------------
eval $(grep '^verbose_makefile *=' setup.py | sed -e 's| ||g')
eval $(grep '^build_type *=' setup.py | sed -e 's| ||g')
eval $(grep '^cppad_prefix *=' setup.py | sed -e 's| ||g')
eval $(grep '^extra_cxx_flags *=' setup.py | sed -e 's| ||g')
if !  echo $cppad_prefix | grep '^/' > /dev/null
then
	cppad_prefix=$(pwd)/$cppad_prefix
fi
echo_eval_log cd build
cmake \
	-D CMAKE_VERBOSE_MAKEFILE="$verbose_maekfile" \
	-D CMAKE_BUILD_TYPE="$build_type" \
	-D cppad_prefix="$cppad_prefix" \
	-D extra_css_flags="$extra_cxx_flags" \
	..
#
echo_eval_log make check
echo_eval_log cd ../lib/example/python
echo_eval_log python3 check_all.py
echo_eval_log cd ../../..
#
# 2DO: figure out where this waring is coming from and what it means
sed -i $logfile -e '/fun\.hpp:52: Warning 362: operator= ignored/d'
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
