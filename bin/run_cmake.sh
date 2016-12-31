#! /bin/bash -e
# -----------------------------------------------------------------------------
#         cppad_swig: A C++ Object Library and SWIG Interface to CppAD
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
if [ "$0" != "bin/run_cmake.sh" ]
then
	echo "bin/run_cmake.sh: must be executed from its parent directory"
	exit 1
fi
# -----------------------------------------------------------------------------
if [ ! -e build ]
then
	echo_eval mkdir build
fi
echo_eval cd build
# -----------------------------------------------------------------------------
verbose_makefile='false'
cxx_flags='-std=c++11'
build_type='debug'
#
cmake \
	-D CMAKE_VERBOSE_MAKEFILE="$verbose_makefile" \
	-D CMAKE_CXX_FLAGS="$cxx_flags" \
	-D CMAKE_BUILD_TYPE="$build_type" \
	..
# -----------------------------------------------------------------------------
echo 'bin/run_cmake.sh: OK'
exit 0
