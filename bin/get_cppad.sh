#! /bin/bash -e
# -----------------------------------------------------------------------------
#         cppad_py: A C++ Object Library and Python Interface to Cppad
#          Copyright (C) 2017-18 Bradley M. Bell (bradbell@seanet.com)
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
if [ "$0" != "bin/get_cppad.sh" ]
then
	echo "bin/get_cppad.sh: must be executed from its parent directory"
	exit 1
fi
# -----------------------------------------------------------------------------
# CppAD version information
remote_repo='https://github.com/coin-or/CppAD.git'
cppad_version='20180703'
hash_code='643c1a5d43f3d6b8402a5b93773bfb768b0a3fae'
# -----------------------------------------------------------------------------
# cmake_binary_dir
cmd=`grep '^cmake_binary_dir=' bin/run_cmake.sh`
eval $cmd
# -----------------------------------------------------------------------------
# cmake_verbose_makefile
cmd=`grep '^cmake_verbose_makefile=' bin/run_cmake.sh`
eval $cmd
# -----------------------------------------------------------------------------
# test_cppad
cmd=`grep '^test_cppad=' bin/run_cmake.sh`
eval $cmd
# -----------------------------------------------------------------------------
if [ ! -e "$cmake_binary_dir" ]
then
	echo_eval mkdir $cmake_binary_dir
fi
echo_eval cd $cmake_binary_dir
cmake_binary_path=`pwd`
#
if [ -e "cppad-$cppad_version.git" ]
then
	echo_eval rm -rf cppad-$cppad_version.git
fi
echo_eval git clone $remote_repo cppad-$cppad_version.git
echo_eval cd cppad-$cppad_version.git
echo_eval git checkout --quiet $hash_code
check=`grep '^SET(cppad_version' CMakeLists.txt | \
		sed -e 's|^[^"]*"\([^"]*\)".*|\1|'`
if [ "$check" != "$cppad_version" ]
then
	echo "get_cppad.sh: cppad_version = $cppad_version"
	echo "cppad_version in cppad-$cppad_version.git/CMakeLists.txt = $check"
	exit 1
fi
#
echo_eval mkdir build
echo_eval cd build
cmake -D CMAKE_VERBOSE_MAKEFILE="$cmake_verbose_makefile" \
	-D cppad_prefix="$cmake_binary_path/prefix"  \
	-D cppad_cxx_flags="$cppad_cxx_flags" \
	..
#
if [ "$test_cppad" == 'yes' ]
then
	make check
fi
make install
# -----------------------------------------------------------------------------
echo 'get_cppad.sh: OK'
exit 0
# -----------------------------------------------------------------------------
# $begin get_cppad.sh$$ $newlinech #$$
# $spell
#	Cppad
#	cmake
# $$
#
# $section Get Cppad$$
#
# $head Syntax$$
# $codei%bin/get_cppad.sh%$$
#
# $head Source Directory$$
# This program must be run from the
# $cref/source directory/cppad_py/Source Directory/$$.
#
# $head run_cmake.sh$$
# This program uses some of the settings in $cref run_cmake.sh$$.
#
# $end
# -----------------------------------------------------------------------------
