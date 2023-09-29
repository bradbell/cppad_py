#! /usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileCopyrightText: Bradley M. Bell <bradbell@seanet.com>
# SPDX-FileContributor: 2017-23 Bradley M. Bell
# ----------------------------------------------------------------------------
import re
import os
import sys
import subprocess
import shutil
import sysconfig
# -----------------------------------------------------------------------------
def sys_exit(msg) :
   sys.exit( 'build_local.py: ' + msg )
#
def sys_command(command_list) :
   command_str = " ".join(command_list)
   try :
      print(command_str)
      output = subprocess.check_output(
         command_list, stderr=subprocess.STDOUT
      )
   except subprocess.CalledProcessError as process_error:
      output = str(process_error.output, 'utf-8')
      print(output)
      sys_exit(command_list[0] + ': Error')
   else :
      output = str(output, 'utf-8')
      if len(output) > 0 :
         print(output)
      print(command_list[0] + ': OK')
   return output
# -----------------------------------------------------------------------------
# Checks
#
if sys.argv[0] != 'bin/build_local.py' :
   sys.exit('usage: bin/build_local.py')
#
if len(sys.argv) != 1 :
   sys.exit('program does not expect command line arguments')
# -----------------------------------------------------------------------------
#
# install_settings
sys.path.insert(0, os.getcwd() + '/bin')
import install_settings
install_settings = install_settings.install_settings()
sys.path.pop(0)
#
# extra_cxx_flags
extra_cxx_flags = install_settings['extra_cxx_flags']
#
# build_type
build_type = install_settings['build_type']
#
# include_mixed
include_mixed = install_settings['include_mixed']
#
# cmake_install_prefix
cmake_install_prefix = install_settings['cmake_install_prefix']
#
# -----------------------------------------------------------------------------
# libdir
libdir = sys_command( [ 'bin/libdir.py' ] )
# -----------------------------------------------------------------------------
# Set build and cmake_install_prefix to debug or release version
command_list = ['bin/build_type.sh']
sys_command(command_list)
# -----------------------------------------------------------------------------
# Check CppAD install
cppad_include_file = cmake_install_prefix + '/include/cppad/cppad.hpp'
if not os.path.isfile( cppad_include_file ) :
   msg  = 'Cannot find ' + cppad_include_file + '\n'
   msg += 'use bin/get_cppad.sh or bin/get_cppad_mixed.sh to create it.'
   sys_exit(msg)
# -----------------------------------------------------------------------------
# Run swig
#
# remove old cppad_py
if os.path.exists('cppad_py') :
   shutil.rmtree('cppad_py')
#
# copy lib/python/cppad_py to cppad_py
shutil.copytree('lib/python/cppad_py', 'cppad_py');
#
# make cure build/lib exists
for subdir in [ 'build', 'build/lib' ] :
   if not os.path.isdir(subdir) :
      os.mkdir(subdir)
#
# remove swig output files
for file_out in [
   'build/lib/cppad_py_swigPYTHON_wrap.cxx',
   'cppad_py/cppad_swig.py'
] :
   if os.path.isfile(file_out) :
      os.remove(file_out)
#
# swig command
command_list = [ 'swig', '-c++', '-python', '-I./include' ]
if include_mixed == 'true' :
   command_list += [ '-DINCLUDE_MIXED' ]
if build_type == 'release' :
   command_list += [ '-DNDEBUG' ]
command_list += [ '-o' , 'build/lib/cppad_py_swigPYTHON_wrap.cxx']
command_list += [ '-outdir', 'cppad_py' ]
command_list += [ 'lib/cppad_py_swig.i' ]
#
# run the command
sys_command(command_list)
# -----------------------------------------------------------------------------
# Run cmake
#
# cmake needs PKG_CONFIG_PATH
os.environ['PKG_CONFIG_PATH'] = \
   cmake_install_prefix + '/' + libdir + '/pkgconfig'
#
# remove cache file from a previous run
os.chdir('build')
if os.path.isfile( 'CMakeCache.txt' ) :
   os.remove('CMakeCache.txt')
#
command_list = [
   "cmake",
   "-D", "CMAKE_VERBOSE_MAKEFILE=1",
   "-D", "CMAKE_BUILD_TYPE="          + build_type,
   "-D", "cmake_install_prefix="      + cmake_install_prefix,
   "-D", "extra_cxx_flags="           + extra_cxx_flags,
   "-D", "include_mixed="             + include_mixed,
   ".."
]
sys_command(command_list)
os.chdir('..')
# -----------------------------------------------------------------------------
# Run make
os.chdir('build')
command_list = [ 'make' ]
sys_command(command_list)
os.chdir('..')
# -----------------------------------------------------------------------------
# copy build/lib/lib_cppad_swig.* to cppad_py/_cppad_swig.*
count = 0
for fname in os.listdir('build/lib') :
   if fname.startswith('lib_cppad_swig.') :
         src_file = 'build/lib/' + fname
         dst_file = 'cppad_py/' + fname[3:]
         shutil.copyfile(src_file, dst_file)
         shutil.copymode(src_file, dst_file)
         count = count + 1
if count != 1 :
   msg  = "build_local.py: warning: can't find build/lib/lib_cppad_swig.*"
   msg += 'it should have bee created by "make" command in "build" directory'
   sys.exit(msg)
# -----------------------------------------------------------------------------
print('build_local: OK')
sys.exit(0)
