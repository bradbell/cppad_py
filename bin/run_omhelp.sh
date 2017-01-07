#! /bin/bash -e
# -----------------------------------------------------------------------------
#         cppad_swig: A C++ Object Library and Swig Interface to Cppad
#          Copyright (C) 2017-17 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#          GNU Affero General Public License version 3.0 or later see
#                     http://www.gnu.org/licenses/agpl.txt
# -----------------------------------------------------------------------------
# bash function that echos and executes a command
echo_eval() {
	echo $*
	eval $*
}
# -----------------------------------------------------------------------------
if [ "$0" != "bin/run_omhelp.sh" ]
then
	echo "bin/run_omhelp.sh: must be executed from its parent directory"
	exit 1
fi
# -----------------------------------------------------------------------------
if [ "$1" != 'xml' ] && [ "$1" != 'htm' ]
then
	echo 'bin/run_omhelp.sh (xml|htm)'
	exit 1
fi
# -----------------------------------------------------------------------------
if [ ! -e build ]
then
	echo 'bin/run_omhelp.sh: build directory does not exist.'
	echo 'execute bin/run_cmake.sh to create it and then re-run this command'
	exit 1
fi
cd build
make auto_lib
cd ..
# -----------------------------------------------------------------------------
if [ -e doc ]
then
	echo_eval rm -r doc
fi
mkdir doc
cd doc
if [ "$1" == 'htm' ]
then
	omhelp ../cppad_swig.omh -noframe -debug
else
	omhelp ../cppad_swig.omh -noframe -debug -xml
fi
# -----------------------------------------------------------------------------
echo 'bin/run_omhelp.sh: OK'
exit 0
