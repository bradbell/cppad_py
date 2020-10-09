#! /usr/bin/env python3
# -----------------------------------------------------------------------------
#         cppad_py: A C++ Object Library and Python Interface to Cppad
#          Copyright (C) 2017-20 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# -----------------------------------------------------------------------------
import re
import os
import sys
import subprocess
import shutil
def sys_exit(msg) :
    sys.exit( 'local_build.py: ' + msg )
# -----------------------------------------------------------------------------
# Checks
#
if sys.argv[0] != 'bin/local_build.py' :
    sys.exit('usage: bin/local_build.py')
#
if len(sys.argv) != 1 :
    sys.exit('program does not expect command line arguments')
# -----------------------------------------------------------------------------
# bin/get_cppad.sh settings
#
fp      = open('bin/get_cppad.sh', 'r')
string  = fp.read()
#
# extra_cxx_flags
pattern = r"\nextra_cxx_flags='([^']*)'"
match   = re.search(pattern, string)
if not match :
    sys_exit('cannot find extra_cxx_flags in bin/get_cppad.sh')
extra_cxx_flags = match.group(1)
#
# build_type
pattern = r"\nbuild_type='([^']*)'"
match   = re.search(pattern, string)
if not match :
    sys_exit('cannot find build_type in bin/get_cppad.sh')
build_type = match.group(1)
if build_type != 'debug' and build_type != 'release' :
    sys_exit('build_type is not debug or release in bin/get_cppad.sh')
#
# include_mixed
pattern = r"\ninclude_mixed='([^']*)'"
match   = re.search(pattern, string)
if not match :
    sys_exit('cannot find include_mixed in bin/get_cppad.sh')
include_mixed = match.group(1)
if include_mixed != 'true' and include_mixed != 'false' :
    sys_exit('include_mixed is not true or false in bin/get_cppad.sh')
#
# cppad_prefix
pattern = '''\ncppad_prefix=['"]([^'"]*)['"]'''
match   = re.search(pattern, string)
if not match :
    sys_exit('cannot find cppad_prefix in bin/get_cppad.sh')
cppad_prefix = match.group(1)
#
# check for $HOME in cppad_prefix
index = cppad_prefix.find('$HOME')
if index >= 0 :
    cppad_prefix = cppad_prefix.replace( '$HOME', os.environ['HOME'] )
# -----------------------------------------------------------------------------
cppad_include_file = cppad_prefix + '/include/cppad/cppad.hpp'
if not os.path.isfile( cppad_include_file ) :
    msg  = 'Cannot find ' + cppad_include_file + '\n'
    msg += 'use bin/get_cppad.sh or bin/get_cppad_mixed.sh to create it.'
    sys_exit(msg)
# -----------------------------------------------------------------------------
# Run cmake
if not os.path.isdir('build') :
    os.mkdir('build')
os.chdir('build')
if os.path.isfile( 'CMakeCache.txt' ) :
    os.remove('CMakeCache.txt')
command = [
    "cmake",
    "-D", "CMAKE_VERBOSE_MAKEFILE=1",
    "-D", "CMAKE_BUILD_TYPE=" + build_type,
    "-D", "cppad_prefix="     + cppad_prefix,
    "-D", "extra_cxx_flags="  + extra_cxx_flags,
    "-D", "include_mixed="    + include_mixed,
    ".."
]
try :
    print('command =', " ".join(command) )
    output = subprocess.check_output(command, stderr=subprocess.STDOUT)
except subprocess.CalledProcessError as process_error:
    output = str(process_error.output, 'utf-8')
    print(output)
    sys_exit('cmake command Error')
else :
    output = str(output, 'utf-8')
    print(output)
    print('cmake command OK')
# -----------------------------------------------------------------------------
# Run make
command = [ 'make' ]
try :
    print('command =', " ".join(command))
    output = subprocess.check_output(command, stderr=subprocess.STDOUT)
except subprocess.CalledProcessError as process_error:
    output = str(process_error.output, 'utf-8')
    print(output)
    sys_exit('make command Error')
else :
    output = str(output, 'utf-8')
    print(output)
    print('make command OK')
os.chdir('..')
# -----------------------------------------------------------------------------
# create cppad_py
#
# remove old cppad_py directory
if os.path.exists('cppad_py') :
    shutil.rmtree('cppad_py')
#
# copy lib/python/cppad_py directory
shutil.copytree('lib/python/cppad_py', 'cppad_py');
#
# copy cppad_swig.py to cppad_py
shutil.copyfile('build/lib/cppad_swig.py', 'cppad_py/cppad_swig.py')
#
# copy _cppad_swig.*
count = 0
for fname in os.listdir('build/lib') :
    if fname.startswith('_cppad_swig.') :
            src_file = 'build/lib/' + fname
            dst_file = 'cppad_py/' + fname
            shutil.copyfile(src_file, dst_file)
            shutil.copymode(src_file, dst_file)
            count = count + 1
if count != 1 :
    msg  = "setup.py: warning: can't find build/lib/_cppad_swig.* library\n"
    msg += 'it should have bee created by make command in build'
    sys.exit(msg)
# -----------------------------------------------------------------------------
print('local_build: OK')
sys.exit(0)
