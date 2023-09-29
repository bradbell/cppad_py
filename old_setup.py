# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileCopyrightText: Bradley M. Bell <bradbell@seanet.com>
# SPDX-FileContributor: 2017-23 Bradley M. Bell
# ----------------------------------------------------------------------------
# extra flags to supress wanings in swig code
import glob
import re
import os
import sys
import subprocess
import shutil
from setuptools import setup, Extension
# -----------------------------------------------------------------------------
def sys_exit(msg) :
   sys.exit( 'old_setup.py: ' + msg )
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
install_distribution = 'install' in sys.argv
src_distribution     = 'sdist' in sys.argv
# Examples and tests are not included in pip distribution
pip_distribution     = not os.path.isfile( 'example/python/check_all.py.in' )
# -----------------------------------------------------------------------------
# python_version
python_major_version = sys.version_info.major
python_minor_version = sys.version_info.minor
if python_major_version != 2 and python_major_version != 3 :
   msg  = 'python major version number '
   msg += str( python_major_version ) + ' is not 2 or 3'
   sys_exit(msg)
# -----------------------------------------------------------------------------
# CMakeLists.txt settings
#
# cppad_py_version
fp      = open('CMakeLists.txt', 'r')
string  = fp.read()
pattern = '\\nSET\( *cppad_py_version  *"([0-9]{4}[.][0-9]+[.][.0-9]*)"'
match   = re.search(pattern, string)
if not match :
   sys_exit('cannot find cppad_py version in CMakeLists.txt')
cppad_py_version = match.group(1)
fp.close()
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
# cmake_install_prefix
cmake_install_prefix = install_settings['cmake_install_prefix']
#
# build_type
build_type = install_settings['build_type']
#
# include_mixed
include_mixed = install_settings['include_mixed']
# ----------------------------------------------------------------------------
# libdir
libdir = sys_command( [ 'python3', 'bin/libdir.py' ] )
# -----------------------------------------------------------------------------
# Set prefix soft link for this build_type
sys_command( [ 'bash', 'bin/build_type.sh' ] )
# -----------------------------------------------------------------------------
# check for $HOME in cmake_install_prefix
index = cmake_install_prefix.find('$HOME')
if index >= 0 :
   cmake_install_prefix = cmake_install_prefix.replace( '$HOME', os.environ['HOME'] )
# -----------------------------------------------------------------------------
if install_distribution and os.path.isdir(cmake_install_prefix) :
   # remove old distribution
   command_list  = [ 'find', '-L',  cmake_install_prefix, '-name', 'site-packages' ]
   output_list   = sys_command( command_list ).split('\n')
   for dir_name in output_list :
      dir_name = dir_name.strip()
      if len(dir_name) > 0 :
         print('remove ' + dir_name)
         shutil.rmtree(dir_name)
# -----------------------------------------------------------------------------
# check if we need to install a local copy of cppad
cppad_include_file = cmake_install_prefix + '/include/cppad/cppad.hpp'
if not os.path.isfile( cppad_include_file ) :
   msg  = 'Cannot find ' + cppad_include_file + '\n'
   if include_mixed == 'true' :
      msg += 'use bin/get_cppad_mixed.sh to create it ?'
   else :
      msg += 'use bin/get_cppad.sh to create it ?'
   sys_exit(msg)
# -----------------------------------------------------------------------------
# Run swig
#
# remove old cppad_py (possibly created by build_local.py)
if os.path.exists('cppad_py') :
   shutil.rmtree('cppad_py')
#
# make cure build/lib exists
for subdir in [ 'build', 'build/lib' ] :
   if not os.path.isdir(subdir) :
      os.mkdir(subdir)
#
# remove swig output files
for file_out in [
   'build/lib/cppad_py_swigPYTHON_wrap.cxx',
   'lib/python/cppad_py/cppad_swig.py'
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
command_list += [ '-outdir', 'lib/python/cppad_py' ]
command_list += [ 'lib/cppad_py_swig.i' ]
#
# run the command
sys_command(command_list)
# -----------------------------------------------------------------------------
# Run cmake to get cxx_has_stdlib, cmake_cxx_compiler, and check_all.py
#
# remove cache file from a previous run
os.chdir('build')
if os.path.isfile( 'CMakeCache.txt' ) :
   os.remove('CMakeCache.txt')
#
# run cmake
command_list = [
   "cmake",
   "-D", "CMAKE_VERBOSE_MAKEFILE=1",
   "-D", "CMAKE_BUILD_TYPE="          + build_type,
   "-D", "cmake_install_prefix="      + cmake_install_prefix,
   "-D", "extra_cxx_flags="           + extra_cxx_flags,
   "-D", "include_mixed="             + include_mixed,
   ".."
]
# pass data_in so CMakeLists.txt can be restored before exit if command fails
sys_command(command_list)
os.chdir('..')
#
# cmake_cxx_compiler
fp = open('build/cmake_cxx_compiler')
cmake_cxx_compiler = fp.read()
fp.close()
#
# cxx_has_stdlib
fp      = open('build/cxx_has_stdlib')
fp_data = fp.read()
fp.close()
if fp_data == 'true' :
   cxx_has_stdlib = True
elif fp_data == 'false' :
   cxx_has_stdlib = False
else :
   msg = 'build/cxx_has_stdlib: contents is not "true" or "false"'
   sys_exit(msg)
# -----------------------------------------------------------------------------
# extension_sources
# Note that cppad_py_swigPYTHON_wrap.cxx is created by build_local.py
cppad_py_extension_sources = list()
cppad_py_extension_sources.append( 'build/lib/cppad_py_swigPYTHON_wrap.cxx')
for name in os.listdir('lib/cplusplus') :
   if name.endswith('.cpp') :
      cppad_py_extension_sources.append( 'lib/cplusplus/' + name)
# -----------------------------------------------------------------------------
# extension_module
include_dirs        = [ cmake_install_prefix + '/include', 'include' ]
library_dirs        = [ cmake_install_prefix + '/' + libdir ]
libraries           = [ 'cppad_lib' ]
extra_compile_args  = extra_cxx_flags.split()
if cxx_has_stdlib :
   extra_link_args = ['-stdlib=libc++' ]
   extra_compile_args.append('-stdlib=libc++')
else :
   extra_link_args = list()
if include_mixed == 'true' :
   eigen_dir           = cmake_install_prefix + '/eigen/include'
   extra_compile_args += [ '-D', 'INCLUDE_MIXED' , '-isystem' , eigen_dir ]
   libraries          += [ 'cppad_mixed', 'ipopt', 'gsl', 'cholmod' ]
#
undef_macros        = list()
if build_type == 'debug' :
   extra_compile_args.append( '-O0' )
   extra_compile_args.append( '-g')
   undef_macros = [ 'NDEBUG', '_FORTIFY_SOURCE' ]
#
cppad_py_extension_name   = 'cppad_py/_cppad_swig'
extension_module          = Extension(
   cppad_py_extension_name                               ,
   cppad_py_extension_sources                            ,
   include_dirs       = include_dirs                     ,
   extra_compile_args = extra_compile_args               ,
   undef_macros       = undef_macros                     ,
   extra_link_args    = extra_link_args                  ,
   library_dirs       = library_dirs                     ,
   libraries          = libraries                        ,
)
#
os.environ['CC'] = cmake_cxx_compiler
# -----------------------------------------------------------------------------
# setup
setup_result = setup(
   name         = 'cppad_py',
   version      = cppad_py_version,
   license      = 'GPL-3.0-or-later',
   description  = 'A C++ Object Library and Python Interface to CppAD',
   author       = 'Bradley M. Bell',
   author_email = 'bradbell@seanet.com',
   url          = 'https://github.com/bradbell/cppad_py',
   ext_modules  = [ extension_module ],
   packages     = [ 'cppad_py' ],
   package_dir  = { 'cppad_py' : 'lib/python/cppad_py' },
)
# -----------------------------------------------------------------------------
# 2DO: figure out why old_setup.py install not putting cppad_py in python_path ?
if install_distribution :
   command_list  = [ 'find', '-L',  cmake_install_prefix, '-name', 'site-packages' ]
   python_path   = sys_command( command_list ).replace('\n', '')
   print('python_path =', python_path)
   if not os.path.isdir( python_path + '/cppad_py' ) :
      command_list  = [ 'find', '-L', python_path , '-name', 'cppad_py' ]
      cppad_py_path = sys_command( command_list ).replace('\n', '')
      shutil.copytree( cppad_py_path, python_path + '/cppad_py' )
# -----------------------------------------------------------------------------
print('old_setup.py: OK')
sys.exit(0)
# -----------------------------------------------------------------------------
#
# {xrst_begin old_setup.py}
# {xrst_spell
#     bdist
#     cholmod
#     cmake
#     cmd
#     config
#     cp
#     cygpath
#     cygwin
#     devel
#     fortran
#     gcc
#     grep
#     gsl
#     lapack
#     libdir
#     libopenblas
#     ls
#     mingw
#     msys
#     pacman
#     pkg
#     pkgconfig
#     rm
#     scipy
#     setuptools
#     srcdir
#     suitesparse
#     unix
#     wget
# }
# {xrst_comment_ch #}
#
#
# Old Configure and Build the cppad_py Python Module
# ##################################################
#
# See Also
# ********
# :ref:`setup.py-name`
#
# Syntax
# ******
#
# | ``python3 old_setup.py install --prefix=``\ *prefix*
#
# External Requirements
# *********************
# #. `bash <https://en.wikipedia.org/wiki/Bash_(Unix_shell)>`_
# #. `cmake <https://cmake.org>`_
# #. `swig <http://www.swig.org/>`_
# #. `c++ <https://en.wikipedia.org/wiki/C++>`_
# #. `git <https://git-scm.com/>`_
# #. `pkg-config <https://www.freedesktop.org/wiki/Software/pkg-config>`_
# #. `python <https://www.python.org/>`_ version 3
# #. `python-numpy <https://numpy.org/>`_
# #. `python-scipy <https://scipy.org/>`_
# #. `python-setuptools <https://scipy.org/>`_
#
# Include Mixed Effects Modeling
# ==============================
# If :ref:`install_settings.py@include_mixed` is true,
# the external packages listed below are also required.
# Note that, for most cases, ``get_cppad_mixed.sh``
# will get all the required packages.
#
# #. The `wget <https://www.gnu.org/software/wget>`_ program.
# #. A fortran compiler.
# #. The `gsl <http://gnuwin32.sourceforge.net/packages/gsl.htm>`_ library
#    including its development headers.
# #. `suitesparse <http://faculty.cse.tamu.edu/davis/SuiteSparse%suitesparse>`_
#    package. Note that only cholmod is really required from suitesparse.
#
# Download
# ********
# Use the following command to download the current version of cppad_py:
#
# | |tab| ``git clone https://github.com/bradbell/cppad_py.git`` *top_srcdir*
#
# Top Source Directory
# ====================
# The directory you choose for *top_srcdir* is
# referred to as your *top_srcdir* directory.
# We suggest you use ``cppad_py.git`` for my *top_srcdir*
# so it is different from the ``cppad_py`` directory
# created by the instructions below.
#
# Configure
# *********
# Before running ``setup_py`` or ``bin/get_cppad.sh`` ,
# you should check and possibly change the
# :ref:`settings<get_cppad.sh@Settings>` in ``bin/get_cppad.sh`` .
#
# Get cppad
# *********
# The next step is to get a copy of cppad using
# :ref:`get_cppad.sh-name`.
# If you want to use the :ref:`mixed-title` class, you will have to set
# :ref:`include_mixed<install_settings.py@include_mixed>` to true
# and use ``bin/get_cppad_mixed.sh`` to install cppad and other
# non-standard requirements.
#
# prefix
# ******
# We use *prefix* to denote the prefix where cppad_py will be installed.
# This is the same as the value of
# :ref:`cmake_install_prefix<install_settings.py@cmake_install_prefix>` .
# You can create a variable with this value using the command
#
# | |tab| ``cmd=$(grep '^cmake_install_prefix=' bin/get_cppad.sh)``
# | |tab| ``eval $cmd``
# | |tab| ``prefix="$cmake_install_prefix"``
#
# libdir
# ******
# The value *libdir* is the suffix (after the prefix)
# where the libraries will be installed.
# This can be determined by running the command:
# {xrst_code sh}
#  bin/libdir.py ; echo
# {xrst_code}
# You can create a variable with this value using the command
#
# | |tab| ``libdir=$(bin/libdir.py)``
#
# LD_LIBRARY_PATH
# ***************
# Make sure the directory *prefix/libdir*
# is in your ``LD_LIBRARY_PATH``
# For example, if you set *prefix* and *libdir* as above,
#
# | |tab| ``export LD_LIBRARY_PATH=$prefix/$libdir``
#
# In mac OS ``LD_LIBRARY_PATH`` should be replaced by ``DYLD_LIBRARY_PATH`` .
# For example,
#
# | |tab| ``export DYLD_LIBRARY_PATH=$prefix/$libdir``
#
# In msys2 and cygwin you do not need to set ``LD_LIBRARY_PATH`` because
# static, instead of dynamic, libraries are used.
#
# PKG_CONFIG_PATH
# ***************
# Make sure the directory *prefix/libdir/*\ ``pkgconfig``
# is in your ``PKG_CONFIG_PATH``.
# For example,
#
# | |tab| ``export PKG_CONFIG_PATH=$prefix/$libdir/pkgconfig``
#
# Local Build
# ***********
# You should first remove any previous local copy of the Python cppad_py
# module (that might exist) using the command
#
# | |tab| ``rm -r build/lib.*``
#
# You can build a local copy of the Python cppad_py module using the
# following command in the *top_srcdir* :
#
# | |tab| ``python3 old_setup.py bdist``
#
# This will create the directory
#
# | |tab| ``build/lib.``\ *name*\ ``/cppad_py``
#
# where *name* identifies your system and version of python.
# For example, you can set a variable equal to the value of *name*
# by executing the command
#
# | |tab| ``name=$(ls build | grep '^lib\.' | sed -e 's|^lib\.||')``
#
# The next step is to copy the ``cppad_py`` directory to the
# *top_srcdir* . For example,
#
# | |tab| ``cp -r build/lib.$name/cppad_py cppad_py``
#
# Local Test
# **********
# You can test the local copy by executing the following commands in the
# *top_srcdir* directory:
#
# | |tab| ``PYTHONPATH=""``
# | |tab| ``python3 example/python/check_all.py``
#
# This test will use the local copy of *top_srcdir/*\ ``cppad_py``
# create by the local build instructions directly above.
#
# PYTHONPATH
# **********
# In order to use the installed version of cppad_py,
# you must add the directory
#
# | |tab| *prefix/libdir*\ ``/python3.``\ *minor*\ ``/site-packages``
#
# to your ``PYTHONPATH``
# where *minor* is the minor version corresponding to ``python3``.
# For example,
#
# | |tab| ``minor=$(echo "import sys;print(sys.version_info.minor)" | python3)``
# | |tab| ``export PYTHONPATH=$prefix/$libdir/python3.$minor/site-packages``
#
#
# Install
# *******
# Use the following command to build and install cppad_py:
#
# | |tab| ``python3 old_setup.py install --prefix=$prefix``
#
# (see :ref:`prefix<old_setup.py@prefix>` above for how to set this shell
# variable).
#
# This will install cppad_py in the directory
#
# | |tab| *prefix/libdir*\ ``/python3.``\ *minor* ``/site-packages/cppad_py``
#
#
# Test Install
# ************
# You can test the installed version by executing the command
#
# | |tab| ``python3 example/python/check_all.py``
#
# If the directory *top_srcdir/*\ ``cppad_py`` exists,
# you will be testing the local version, instead of the installed version.
# If this directory exists when the install command is run,
# it is removed by the install command.
#
# Mac Os
# ******
# The Mac Os system has only been tested using
# `brew <https://brew.sh>`_  and
# `port <https://www.macports.org>`_
# to install packages not included with the system.
#
# Cygwin
# ******
# A cygwin install, on 2021-05-06 and with
# :ref:`include_mixed<install_settings.py@include_mixed>` false,
# completed successfully by doing the following:
# First the following packages were added to the default set installed by the
# cygwin ``setup-x86_64`` program:
# gcc-core, gcc-g++, gcc-fortran,
# python3-devel, python-pip-wheel, python-setuptools-wheel,
# lapack-devel, libopenblas,
# git, vim, cmake, make, swig.
# Then the ``pip3`` program was used to install numpy and scipy.
# Then the install instructions above were used to install and test
# cppad_py.
#
# Msys2
# *****
# A msys2 install with,
# :ref:`include_mixed<install_settings.py@include_mixed>` false,
# was attempted on 2021-05-09.
# First the following packages were installed using pacman:
# vim, git, make, cmake, swig.
# Next the mingw-w64-x86_64 version of following packages were installed using
# pacman:  python, python-scipy, python-setuptools, gcc
# The problem is that old_setup.py is mixing windows and unix paths.
# An attempt was made to fix the environment variables using ``cygpath``
# utility, but other related problems still persisted.
#
# Errors
# ******
# {xrst_toc_table
#  install_error.xrst
# }
#
# {xrst_end old_setup.py}
# -----------------------------------------------------------------------------
