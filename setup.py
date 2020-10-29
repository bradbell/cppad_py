# -----------------------------------------------------------------------------
#         cppad_py: A C++ Object Library and Python Interface to Cppad
#          Copyright (C) 2017-20 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# -----------------------------------------------------------------------------
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
    sys.exit( 'setup.py: ' + msg )
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
        print(command_list[0] , ': OK')
    return output
# -----------------------------------------------------------------------------
src_distribution = 'sdist' in sys.argv
# Examples and tests are not included in pip distribution
pip_distribution = not os.path.isfile( 'example/python/check_all.py.in' )
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
# cppad_prefix
pattern = '''\ncppad_prefix=['"]([^'"]*)['"]'''
match   = re.search(pattern, string)
if not match :
    sys_exit('cannot find cppad_prefix in bin/get_cppad.sh')
cppad_prefix = match.group(1)
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
# -----------------------------------------------------------------------------
# check for $HOME in cppad_prefix
index = cppad_prefix.find('$HOME')
if index >= 0 :
    cppad_prefix = cppad_prefix.replace( '$HOME', os.environ['HOME'] )
# -----------------------------------------------------------------------------
# check if we need to install a local copy of cppad
cppad_include_file = cppad_prefix + '/include/cppad/cppad.hpp'
if not os.path.isfile( cppad_include_file ) :
    msg  = 'Cannot find ' + cppad_include_file + '\n'
    if include_mixed == 'true' :
        msg += 'use bin/get_cppad_mixed.sh to create it'
    else :
        msg += 'use bin/get_cppad_sh to create it'
    sys_exit(msg)
# bin/build_local.py
if pip_distribution :
    # Only using cmake to determine if -stdlib=libc++ is available
    # and the location of the cppad_lib library
    # so remove all SUB_DIRECTORY commands in CMakeLists.txt
    fp      = open('CMakeLists.txt', 'r')
    fp_data = fp.read()
    fp.close()
    pattern = r'\n(ADD_SUBDIRECTORY\([^(]*\))'
    fp_data = re.sub(pattern, r'\n# \1', fp_data)
    pattern = r'FATAL_ERROR ("no correctnes checks are available")'
    fp_data = re.sub(pattern, r'STATUS \1', fp_data)
    #
    fp      = open('CMakeLists.txt', 'w')
    fp.write(fp_data)
    fp.close()
command_list = [ 'bin/build_local.py' ]
sys_command(command_list)
#
# cxx_has_stdlib
fp      = open('build/cxx_has_stdlib')
fp_data = fp.read()
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
include_dirs        = [ cppad_prefix + '/include', 'include' ]
library_dirs        = [ cppad_prefix + '/lib', cppad_prefix + '/lib64' ]
libraries           = [ 'cppad_lib' ]
extra_compile_args  = extra_cxx_flags.split()
if cxx_has_stdlib :
    extra_link_args = ['-stdlib=libc++' ]
    extra_compile_args.append('-stdlib=libc++')
else :
    extra_link_args = list()
if include_mixed == 'true' :
    eigen_dir           = cppad_prefix + '/eigen/include'
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
# -----------------------------------------------------------------------------
# setup
setup_result = setup(
    name         = 'cppad_py',
    version      = cppad_py_version,
    license      = 'GPL3',
    description  = 'A C++ Object Library and Python Interface to CppAD',
    author       = 'Bradley M. Bell',
    author_email = 'bradbell@seanet.com',
    url          = 'https://github.com/bradbell/cppad_py',
    ext_modules  = [ extension_module ],
    packages     = [ 'cppad_py' ],
    package_dir  = { 'cppad_py' : 'cppad_py' },
    scripts      = [ 'bin/xsrst.py' ],
)
# -----------------------------------------------------------------------------
# 2DO: figure out when setup.py install not puttin cppad_py in python_path ?
command_list  = [ 'find', '-L',  cppad_prefix, '-name', 'site-packages' ]
python_path   = sys_command( command_list ).replace('\n', '')
if not os.path.isdir( python_path + '/cppad_py' ) :
    command_list  = [ 'find', '-L', python_path , '-name', 'cppad_py' ]
    cppad_py_path = sys_command( command_list ).replace('\n', '')
    shutil.copytree( cppad_py_path, python_path + '/cppad_py' )
# -----------------------------------------------------------------------------
msg  = 'If you get a message that an object library is missing, try:\n\t'
msg += 'export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:'
msg += cppad_prefix + '/<libdir>\n'
msg += 'where <libdir> is "lib" or "lib64" or both.\n'
msg += 'If you have a Mac system, the following may fix this problem:\n\t'
msg += 'export DYLD_LIBRARY_PATH=$DYLD_LIBRARY_PATH:'
msg += cppad_prefix + '/<libdir>\n'
print(msg)
print('setup.py: OK')
sys.exit(0)
# -----------------------------------------------------------------------------
# {xsrst_comment_ch #}
#
# {xsrst_begin setup_py}
#
# .. include:: ../preamble.rst
#
# {xsrst_spell
#   bradbell
#   cppad
#   srcdir
#   cmake
#   pypi
# }
#
# Configure and Build the cppad_py Python Module
# ##############################################
#
# Syntax
# ******
#
# | ``python setup.py build_ext``
#
# External Requirements
# *********************

# #. `bash <https://en.wikipedia.org/wiki/Bash_(Unix_shell)>`_
# #. `python <https://www.python.org/>`_ version 3
# #. `numpy <https://numpy.org/>`_
# #. `cmake <https://cmake.org>`_
# #. `swig <http://www.swig.org/>`_
# #. `c++ <https://en.wikipedia.org/wiki/C++>`_
# #. `git <https://git-scm.com/>`_
#
# Install Using Pip
# *****************
# There is an old version of cppad_py available using ``pip`` .
# To install for you entire system use:
#
# | |tab| ``pip install -i https://test.pypi.org/simple/ cppad_py``
#
# {xsrst_children
#   install_error.xsrst
#   bin/get_cppad.sh
# }
# Install Errors
# **************
# If you get an error message during the install procedure above,
# or the one below, see :ref:`install_error<install_error>`.
# This will only install the release version.
# Installing a debug version is discussed below in the instructions
# for downloading and building from the source code.
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
# referred to as your top source directory.
#
# Configure
# *********
# Before running ``setup_py`` or ``bin/get_cppad.sh`` ,
# you should check and possibly change the
# :ref:`settings<get_cppad_sh.settings>` in ``bin/get_cppad.sh`` .
#
# Get cppad
# *********
# The next step is to get a copy of cppad using
# :ref:`get_cppad_sh<get_cppad_sh>`.
# If you want to use the :ref:`mixed` class, you will have to set
# :ref:`include_mixed<get_cppad_sh.settings.include_mixed>` to true
# and use ``bin/get_cppad_mixed.sh`` to install cppad and other
# non-standard requirements.
#
# Test
# ****
# These steps are optional if you already know that cppad_py
# works on your system.
#
# Build cppad_py
# ==============
# Build the Python cppad_py module using the command:
#
# | |tab| ``python setup.py build_ext``
#
# python
# ======
# The next step is to test the cppad_py on your system by executing
# the following commands starting in *top_srcdir* :
#
# | |tab| ``python example/python/check_all.py``
#
# c++
# ===
# After ``setup.py`` has run,
# you can also test the cppad_py c++ interface
# :ref:`cpp_lib<cpp_lib>` on your system by executing the following commands
# starting in *top_srcdir* :
#
# | |tab| ``cd build``
# | |tab| ``make check_example``
#
# import
# ======
# If you are in the *top_srcdir* directory,
# you should be able to import cppad_py using the following commands:
#
# | |tab| ``python3``
# | |tab| ``import cppad_py``
# | |tab| ``quit`` ()
#
# We need to install cppad_py so you can import it from any directory.
#
# Install
# *******
# Use the following command to build and install cppad_py:
#
# | |tab| ``python3 setup.py install --prefix`` = *prefix*
#
# This will install ``cppad_py`` in the directory
#
# | |tab| *prefix* ``/`` *lib* ``/python`` *major* . *minor* ``/site_packages/cppad_py``
#
# where *lib* is ``lib`` or ``lib64`` ,
# *major* ( *minor* ) is the major (minor)
# version of *python* .
#
# Python Path
# ***********
# Check that the directory
#
# | |tab| *prefix* ``/`` *lib* ``/python`` *major* . *minor* ``/site_packages``
#
# is in your python path.
# Once it is, you should be able to execute the following commands:
#
# | |tab| ``python3``
# | |tab| ``import sys``
# | |tab| ``print(sys.path`` )
# | |tab| ``quit`` ()
#
# {xsrst_end setup_py}
# -----------------------------------------------------------------------------
