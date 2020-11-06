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
def sys_command(command_list, cmakelists_txt=None) :
    command_str = " ".join(command_list)
    try :
        print(command_str)
        output = subprocess.check_output(
            command_list, stderr=subprocess.STDOUT
        )
    except subprocess.CalledProcessError as process_error:
        if not (cmakelists_txt is None) :
            # used during cmake command which is run in build directory
            fp = open('../CMakeLists.txt', 'w')
            fp.write(cmakelists_txt)
            fp.close()
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
# cmake_install_prefix
pattern = '''\ncmake_install_prefix=['"]([^'"]*)['"]'''
match   = re.search(pattern, string)
if not match :
    sys_exit('cannot find cmake_install_prefix in bin/get_cppad.sh')
cmake_install_prefix = match.group(1)
#
# cmake_install_prefix
pattern = '''\ncppad_libdir=['"]([^'"]*)['"]'''
match   = re.search(pattern, string)
if not match :
    sys_exit('cannot find cppad_libdir in bin/get_cppad.sh')
cppad_libdir = match.group(1)
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
        msg += 'use bin/get_cppad_mixed.sh to create it'
    else :
        msg += 'use bin/get_cppad_sh to create it'
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
# Run cmake to get cxx_has_stdlib, cmake_cxx_compiler
#
# Do not needd cmake subdirectories for this purpose
fp      = open('CMakeLists.txt', 'r')
data_in = fp.read()
fp.close()
pattern  = r'\n(ADD_SUBDIRECTORY\([^(]*\))'
data_out = re.sub(pattern, r'\n# \1', data_in)
pattern  = r'FATAL_ERROR ("no correctnes checks are available")'
data_out = re.sub(pattern, r'STATUS \1', data_out)
#
fp      = open('CMakeLists.txt', 'w')
fp.write(data_out)
fp.close()
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
    "-D", "cppad_libdir="              + cppad_libdir,
    "-D", "extra_cxx_flags="           + extra_cxx_flags,
    "-D", "include_mixed="             + include_mixed,
    ".."
]
# pass data_in so CMakeLists.txt can be restored before exit if command fails
sys_command(command_list, cmakelists_txt = data_in)
os.chdir('..')
#
# restore CMAkeLists.tst
fp = open('CMakeLists.txt', 'w')
fp.write(data_in)
fp.close()
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
library_dirs        = [ cmake_install_prefix + '/' + cppad_libdir ]
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
    license      = 'GPL3',
    description  = 'A C++ Object Library and Python Interface to CppAD',
    author       = 'Bradley M. Bell',
    author_email = 'bradbell@seanet.com',
    url          = 'https://github.com/bradbell/cppad_py',
    ext_modules  = [ extension_module ],
    packages     = [ 'cppad_py' ],
    package_dir  = { 'cppad_py' : 'lib/python/cppad_py' },
    scripts      = [ 'bin/xsrst.py' ],
)
# -----------------------------------------------------------------------------
# 2DO: figure out why setup.py install not putting cppad_py in python_path ?
if install_distribution :
    command_list  = [ 'find', '-L',  cmake_install_prefix, '-name', 'site-packages' ]
    python_path   = sys_command( command_list ).replace('\n', '')
    print('python_path =', python_path)
    if not os.path.isdir( python_path + '/cppad_py' ) :
        command_list  = [ 'find', '-L', python_path , '-name', 'cppad_py' ]
        cppad_py_path = sys_command( command_list ).replace('\n', '')
        shutil.copytree( cppad_py_path, python_path + '/cppad_py' )
# -----------------------------------------------------------------------------
msg  = 'If you get a message that an object library is missing, try:\n\t'
msg += 'export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:'
msg += cmake_install_prefix + '/<libdir>\n'
msg += 'where <libdir> is "lib" or "lib64" or both.\n'
msg += 'If you have a Mac system, the following may fix this problem:\n\t'
msg += 'export DYLD_LIBRARY_PATH=$DYLD_LIBRARY_PATH:'
msg += cmake_install_prefix + '/<libdir>\n'
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
#   libdir
#   pkgconfig
#   matplotlib
# }
#
# Configure and Build the cppad_py Python Module
# ##############################################
#
# Syntax
# ******
#
# | ``python3 setup.py install --prefix=`` *prefix*
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
# LD_LIBRARY_PATH
# ***************
# Make sure the following directory is in your ``LD_LIBRARY_PATH``
# (in mac OS this path is called ``DYLD_LIBRARY_PATH``):
#
# | |tab| *prefix/lib*
#
# where *lib* is :ref:`cppad_libdir<get_cppad_sh.settings.cppad_libdir>`.
#
# PKG_CONFIG_PATH
# ***************
# Make sure the following directory is in your ``PKG_CONFIG_PATH``:
#
# | |tab| *prefix/lib/* ``pkgconfig``
#
# PYTHONPATH
# **********
# Make sure the following directory is in your ``PYTHONPATH``:
#
# | |tab| *prefix/lib/* ``python`` *major* . *minor* ``/site-packages``
#
# Install
# *******
# Use the following command to build and install cppad_py:
#
# | |tab| ``python3 setup.py install --prefix`` = *prefix*
#
# This will install ``cppad_py`` in the directory
#
# | |tab| *prefix/lib/* ``python`` *major.minor* ``/site-packages/cppad_py``
#
# where *lib* is :ref:`cppad_libdir<get_cppad_sh.settings.cppad_libdir>` ,
# *major* ( *minor* ) is the major (minor)
# version of *python* .
#
# Test
# ****
# These steps are optional and used to test that cppad_py
# works on your system before installing it.
# They do not yet work on mac OS.
# The following packages are additional requirements to execute these steps:
# `scipy <https://scipy.org/>`_
# `matplotlib <https://matplotlib.org/>`_.
#
#
# build_local.py
# ==============
# Build a local copy of the Python cppad_py module using the command:
#
# | |tab| ``bin/build_local.py``
#
# python
# ======
# The next step is to test the cppad_py on your system by executing
# the following commands starting in *top_srcdir* :
#
# | |tab| ``python3 example/python/check_all.py``
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
# Install Using Pip
# *****************
# There is an old version of cppad_py available using ``pip`` .
# To install for you entire system use:
#
# | |tab| ``pip install -i https://test.pypi.org/simple/ cppad_py``
#
# Children
# ********
# {xsrst_child_list
#   install_error.xsrst
#   bin/get_cppad.sh
# }
#
# {xsrst_end setup_py}
# -----------------------------------------------------------------------------
