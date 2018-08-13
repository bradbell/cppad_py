# -----------------------------------------------------------------------------
#         cppad_py: A C++ Object Library and Python Interface to Cppad
#          Copyright (C) 2017-18 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# -----------------------------------------------------------------------------
# bin/get_cppad.sh assumes variable = value on same line.
# BEGIN_USER_SETTINGS
verbose_makefile = "false"
build_type       = "debug"
cppad_prefix     = "build/prefix"
test_cppad       = "fasle"
extra_cxx_flags  = "-Wall -pedantic-errors -Wno-unused-result -std=c++11"
# END_USER_SETTINGS
# -----------------------------------------------------------------------------
# extra flags to supress wanings in swig code
swig_cxx_flags = "-Wno-class-memaccess"
import re
import os
import sys
import subprocess
import shutil
from distutils.core import setup, Extension
# -----------------------------------------------------------------------------
def quote_str(s) :
	return "'" + s + "'"
# -----------------------------------------------------------------------------
# copy lib/python -> cppad_py
if os.path.exists('cppad_py') :
	shutil.rmtree('cppad_py')
shutil.copytree('lib/python', 'cppad_py');
# -----------------------------------------------------------------------------
# python_version
python_major_version = sys.version_info.major
python_minor_version = sys.version_info.minor
if python_major_version != 2 and python_major_version != 3 :
	msg  = 'setup.py: python major version number '
	msg += str( python_major_version ) + ' is not 2 or 3'
	sys.exit(msg)
python_version = str(python_major_version) + "." + str(python_minor_version)
file_ptr = open('cppad_py/python_version', 'w')
file_ptr.write(python_version + '\n')
file_ptr.close()
# -----------------------------------------------------------------------------
# run cmake
cppad_prefix_absolute = os.getcwd() + '/' + cppad_prefix
if not os.path.exists('build') :
	os.mkdir('build')
os.chdir('build')
if os.path.exists('CMakeCache.txt') :
	os.remove('CMakeCache.txt')
command = [
	'cmake',
	'-D', 'CMAKE_VERBOSE_MAKEFILE=' + quote_str(verbose_makefile),
	'-D', 'CMAKE_BUILD_TYPE='       + quote_str(build_type),
	'-D', 'cppad_prefix='           + quote_str(cppad_prefix_absolute),
	'-D', 'extra_cxx_flags='        + quote_str(extra_cxx_flags),
	'-D', 'python_version='         + quote_str( python_version ),
	'..'
]
print( ' '.join(command) )
flag    = subprocess.call(command)
if flag != 0 :
		sys.exit('setup.py: cmake command failed')
os.chdir('..')
# -----------------------------------------------------------------------------
# In lib/example/python: check_all.py.in -> check_all.py
top_srcdir  = os.getcwd()
sed_cmd     = 's|@CMAKE_SOURCE_DIR@|' + top_srcdir + '|'
sed_in      = open('lib/example/python/check_all.py.in', 'r')
sed_out     = open('lib/example/python/check_all.py',    'w')
command = [ 'sed', '-e', sed_cmd ]
flag = subprocess.call(command, stdin=sed_in, stdout=sed_out )
if flag != 0 :
	sys.exit('setup.py: failed to create lib/example/python/check_all.py')
# -----------------------------------------------------------------------------
# cppad_include_dir
cppad_include_dir = os.getcwd() + '/build/prefix/include'
# -----------------------------------------------------------------------------
# cppad_py_version
fp      = open('CMakeLists.txt', 'r')
string  = fp.read()
pattern = '\\nSET\( *cppad_py_version  *"([0-9]*)"'
match   = re.search(pattern, string)
if not match :
	sys.exit('setup.py: cannot find cppad_py version in CMakeLists.txt')
cppad_py_version = match.group(1)
# -----------------------------------------------------------------------------
# build/lib/cppad_py_swig_wrap.cpp, build/lib/cppad_py_swig.py
#
# change inpto cppad_py directory so that cppad_py.py is output there
if not os.path.exists('cppad_py') :
	os.mkdir('cppad_py')
os.chdir('cppad_py')
command = [
	'swig',
	'-c++',
	'-python',
	'-I../include',
	'-o', 'cppad_py_swig_wrap.cpp',
	'../lib/cppad_py_swig.i'
]
if python_major_version == 3 :
	command.insert(1, '-py3')
flag    = subprocess.call(command)
if flag != 0 :
		sys.exit('setup.py: swig command failed')
#
# change back to top soruce directory
os.chdir('..')
# -----------------------------------------------------------------------------
# extension_sources
cppad_py_extension_sources = [ 'cppad_py/cppad_py_swig_wrap.cpp' ]
for name in os.listdir('lib/cplusplus') :
	if name.endswith('.cpp') :
		cppad_py_extension_sources.append( 'lib/cplusplus/' + name)
# -----------------------------------------------------------------------------
# extension_module
include_dirs     = [ cppad_include_dir ]
include_dirs.append( os.getcwd() + '/build/lib' )
include_dirs.append( os.getcwd() + '/include' )
extra_compile_args  = extra_cxx_flags.split()
extra_compile_args += swig_cxx_flags.split()
undef_macros        = list()
if build_type == 'debug' :
	undef_macros = [ 'NDEBUG' ]
	extra_compile_args.append( '-O1' )
#
cppad_py_extension_name   = 'cppad_py/_cppad_py_swig'
extension_module          = Extension(
	cppad_py_extension_name                               ,
	cppad_py_extension_sources                            ,
	include_dirs       = include_dirs                     ,
	extra_compile_args = extra_compile_args               ,
	undef_macros       = undef_macros
)
# -----------------------------------------------------------------------------
# setup
setup(
	name         = 'cppad_py',
	version      = cppad_py_version,
	license      = 'GPL3',
	description  = 'A C++ Object Library and Python Interface to Cppad',
	author       = 'Bradley M. Bell',
	author_email = 'bradbell at seanet dot com',
	url          = 'https://github.com/bradbell/cppad_py',
	ext_modules  = [ extension_module ],
	packages     = [ 'cppad_py' ]
)
# -----------------------------------------------------------------------------
print('setup.py: OK')
sys.exit(0)
# -----------------------------------------------------------------------------
# $begin setup.py$$ $newlinech #$$
# $spell
#	makefile
#	cxx
#	inplace
#	undef
#	https://github.com/bradbell/cppad_py.git
#	srcdir
#	cplusplus
#	sys
# $$
#
# $section Configure and Build the cppad_py Python Module$$
#
# $head Syntax$$
# $icode%python% setup.py build_ext --inplace [--debug] [--undef NDEBUG]
# %$$
# where $icode python$$ is the Python executable you will be using with
# cppad_py.
#
# $head External Requirements$$
# $list number$$
# $href%https://en.wikipedia.org/wiki/C++%c++%$$.
# $lnext
# $href%https://cmake.org%cmake%$$.
# $lnext
# $href%https://git-scm.com/%git%$$.
# $lnext
# $href%http://www.swig.org/%swig%$$:
# There seems to be a problem with swig-3.0.8; see
# $href%https://github.com/bradbell/cppad_py/issues/3%issue 3%$$.
# $lnext
# $href%https://www.python.org/%python%$$: version 2 or 3.
# $lnext
# $href%http://www.numpy.org/%numpy%$$.
# $lend
#
# $head Download$$
# Use the following command to download the current version of cppad_py:
# $codei%
#	git clone https://github.com/bradbell/cppad_py.git %top_srcdir%
# %$$
#
# $subhead Top Source Directory$$
# The directory you choose for $icode top_srcdir$$ is
# referred to as your top source directory.
#
# $children%bin/get_cppad.sh
# %$$
# $head Configure$$
# Before running $code setup.py$$ or $cref get_cppad.sh$$,
# you should check and possibly change the following settings
# (which are near the top of $icode%top_srcdir%/setup.py%$$):
# $srcfile%setup.py%0%# BEGIN_USER_SETTINGS%# END_USER_SETTINGS%$$
# Each of these settings is described below:
#
# $subhead verbose_makefile$$
# This is either $code "true"$$ or $code "false"$$.
# If it is true, many of the compiler and Swig options used to
# build the system are output during the $code make$$ commands.
# If it is false, the output during the make commands just describes
# whats is being done without so much detail.
#
# $subhead build_type$$
# This is either $code "debug"$$, $code "release"$$.
#
# $subhead extra_cxx_flags$$
# Extra compiler flags used when compiling C++ code.
#
# $subhead cppad_prefix$$
# This is the directory where $cref get_cppad.sh$$ puts Cppad
# (relative to the top source directory).
#
# $subhead test_cppad$$
# This is either $code "true"$$ or $code "false"$$.
# If it is $code "true"$$, $cref get_cppad.sh$$ will build and run
# a separate check of Cppad for this system.
# This takes a significant amount of time, but may be useful
# if you have any problems.
#
# $head Get cppad$$
# The next step is to get a copy of cppad using $cref get_cppad.sh$$.
#
# $head Build cppad_py$$
# The next step is the build the Python cppad_py module using
# the command:
# $codei%
#	%python% setup.py build_ext --inplace --debug --undef NDEBUG
# %$$
# where $icode python$$ is the Python executable you will be
# using with cppad_py.
# If you want a faster version, with less error reporting, use
# $codei%
#	%python% setup.py build_ext --inplace
# %$$
#
# $head Testing$$
#
# $subhead python$$
# The next step is to test the cppad_py on your system by executing
# the following commands starting in $icode top_srcdir$$:
# $codei%
#	cd lib/example/python
#	%python% check_all.py
# %$$
# where $icode python$$ is the same version of python as above.
#
# $subhead c++$$
# You can also test the cppad_py c++ interface
# $cref cpp_lib$$ on your system by executing the following commands
# starting in $icode top_srcdir$$:
# $codei%
#	cd build
#	make check_lib_cplusplus
# %$$
#
# $subhead import$$
# If you are in $icode top_srcdir$$ you should be able to execute the
# following commands:
# $codei%
#	%python%
#	import cppad_py
#	quit()
# %$$
# We need to install cppad_py so you can import it from any directory.
#
#
# $head Installing$$
# Use the following command to install the debug version of cppad_py:
# $codei%
#	%python% setup.py build_ext --debug --undef NDEBUG install --prefix=%prefix%
# %$$
# or the following to install the release version:
# $codei%
#	%python% setup.py build_ext install --prefix=%prefix%
# %$$
# This will install $code cppad_py$$ in the directory
# $codei%
#	%prefix%/lib/python%major%.%minor%/site_packages/cppad_py
# %$$
# where $icode major$$ and $icode minor$$ are the major and minor
# versions for $icode python$$.
#
# $head Python Path$$
# You can check the current setting of your python path using the commands:
# $codei%
#	%python%
#	import sys
#	print(sys.path)
#	quit()
# %$$
# The directory $icode%prefix%/lib/python%major%.%minor%/site_packages%$$
# must be in your python path.
#
# $end
# -----------------------------------------------------------------------------
