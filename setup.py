# -----------------------------------------------------------------------------
#         cppad_py: A C++ Object Library and Python Interface to Cppad
#          Copyright (C) 2017-18 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# -----------------------------------------------------------------------------
# Under Construction
# The following commands appear to work:
#	bin/run_cmake.sh
#	python3 setup.py build_ext --inplace
#	cd build
#	make check
# -----------------------------------------------------------------------------
import re
import os
import sys
import subprocess
from distutils.core import setup, Extension
# -----------------------------------------------------------------------------
# cppad_include_dir
fp      = open('bin/run_cmake.sh', 'r')
string  = fp.read()
pattern = '\\ncppad_version=\'([0-9]*)\''
match   = re.search(pattern, string)
if not match :
	sys.exit('setup.py: cannot find cppad_version in bin/run_cmake.sh')
cppad_version     = match.group(1)
cppad_include_dir = os.getcwd() + '/build/cppad-' + cppad_version + '.git'
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
flag    = subprocess.call(command)
if flag != 0 :
		sys.exit('setup.py: swig command failed')
#
# change back to top soruce directory
os.chdir('..')
# -----------------------------------------------------------------------------
# extension_sources
cppad_py_extension_sources = [ 'cppad_py/cppad_py_swig_wrap.cpp' ]
for name in os.listdir('lib') :
	if name.endswith('.cpp') :
		cppad_py_extension_sources.append( 'lib/' + name)
# -----------------------------------------------------------------------------
# extension_module
cppad_py_swig_include_dirs     = [ cppad_include_dir ]
cppad_py_swig_include_dirs.append( os.getcwd() + '/build/lib' )
cppad_py_swig_include_dirs.append( os.getcwd() + '/include' )
#
print(cppad_py_swig_include_dirs)
cppad_py_extension_name   = 'cppad_py/_cppad_py_swig'
extension_module          = Extension(
	cppad_py_extension_name,
	cppad_py_extension_sources,
	include_dirs = cppad_py_swig_include_dirs
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
