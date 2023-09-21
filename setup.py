# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileCopyrightText: Bradley M. Bell <bradbell@seanet.com>
# SPDX-FileContributor: 2017-23 Bradley M. Bell
# ----------------------------------------------------------------------------
r"""
{xrst_begin setup.py}
{xrst_spell
   cd
   dist
   gz
}

Install cppad_py Python Module
##############################

See Also
********
:ref:`old_setup.py-name`

Requirements
************
{xrst_toc_table
   bin/get_cppad.sh
   bin/get_cppad_mixed.sh
}

Simple Case
***********
In the simple case, :ref:`get_cppad.sh@Settings@include_mixed` is false.
If :ref:`get_cppad.sh@Settings@build_type` is debug (release),
cppad_py will run slower (faster) and do more (less) error detection.

#. bin/get_cppad.sh
#. git clone https://github.com/bradbell/cppad_py.git cppad_py.git
#. cd cppad_py.git
#. python3 -m build
#. pip install dist/cppad_py-\*.tar.gz --user

If you use this form of the install,
you will not be able to use any of the :ref:`mixed-name` routines.
You should now be able to execute the following example:
{xrst_literal
   readme.md
   # BEGIN PYTHON
   # END PYTHON
}


Mixed Case
**********
In the mixed case, :ref:`get_cppad.sh@Settings@include_mixed` is true.

#. bin/get_cppad_mixed.sh
#. git clone https://github.com/bradbell/cppad_py.git cppad_py.git
#. cd cppad_py.git
#. python3 -m build
#. pip install dist/cppad_py-\*.tar.gz --user

If you use this form of the install,
you will be able to use any of the :ref:`mixed-name` routines.

{xrst_end setup.py}
"""
# ----------------------------------------------------------------------------
import sys
import re
import os
#
from setuptools                       import setup, Extension
from setuptools.command.build_py      import build_py
# -----------------------------------------------------------------------------
# bin/get_cppad.sh settings
#
# file_data
file_obj   = open('bin/get_cppad.sh', 'r')
file_data  = file_obj.read()
file_obj.close()
#
# extra_cxx_flags
pattern = r"\nextra_cxx_flags='([^']*)'"
match   = re.search(pattern, file_data)
if not match :
   sys.exit('cannot find extra_cxx_flags in bin/get_cppad.sh')
extra_cxx_flags = match.group(1)
#
# cmake_install_prefix
pattern = '''\ncmake_install_prefix=['"]([^'"]*)['"]'''
match   = re.search(pattern, file_data)
if not match :
   sys.exit('cannot find cmake_install_prefix in bin/get_cppad.sh')
cmake_install_prefix = match.group(1)
#
# build_type
pattern = r"\nbuild_type='([^']*)'"
match   = re.search(pattern, file_data)
if not match :
   sys.exit('cannot find build_type in bin/get_cppad.sh')
build_type = match.group(1)
if build_type != 'debug' and build_type != 'release' :
   sys.exit('build_type is not debug or release in bin/get_cppad.sh')
#
# include_mixed
pattern = r"\ninclude_mixed='([^']*)'"
match   = re.search(pattern, file_data)
if not match :
   sys.exit('cannot find include_mixed in bin/get_cppad.sh')
include_mixed = match.group(1)
if include_mixed != 'true' and include_mixed != 'false' :
   sys.exit('include_mixed is not true or false in bin/get_cppad.sh')
# ----------------------------------------------------------------------------
# cmake_install_prefix
pattern = r'$HOME'
replace = os.environ['HOME']
cmake_install_prefix = cmake_install_prefix.replace(pattern, replace)
#
# swig_opts
swig_opts = [ '-c++', '-I./include', '-outdir', 'lib/python/cppad_py' ]
if include_mixed == 'true' :
   swig_opts += [ '-DINCLUDE_MIXED' ]
if build_type == 'release' :
   swig_opts += [ '-DNDEBUG' ]
#
# extension_sources
extension_sources = [ 'lib/cppad_py_swig.i' ]
for name in os.listdir('lib/cplusplus') :
   if name.endswith('.cpp' ) :
      extension_sources.append( 'lib/cplusplus/' + name)
#
# include_dirs
include_dirs  = [ cmake_install_prefix + '/include', 'include' ]
#
# library_dirs
library_dirs = list()
for lib in [ 'lib' , 'lib64' ] :
   directory = f'{cmake_install_prefix}/{lib}'
   if os.path.isdir( directory ) :
      library_dirs.append(directory)
#
# libraries
libraries = list()
if include_mixed == 'true' :
   libraries += [ 'cppad_mixed', 'ipopt', 'gsl', 'cholmod' ]
libraries += [ 'cppad_lib' ]
#
# extra_link_args
extra_link_args = list()
for directory in library_dirs :
   extra_link_args.append( f'-Wl,-rpath={directory}' )
for lib in libraries :
   extra_link_args.append( f'-l{lib}' )
#
# libraries
# Theese values are now in extra_link_args
libraries    = list()
#
# extra_compile_args
extra_compile_args = [ '-Wno-array-bounds' ]
if extra_cxx_flags != '' :
   extra_compile_args = extra_cxx_flags.split()
if include_mixed == 'true' :
   extra_compile_args += [ '-D', 'INCLUDE_MIXED' ]
#
# undef_macros
undef_macros        = list()
if build_type == 'debug' :
   undef_macros = [ 'NDEBUG' ]
#
# ext_module
extension_module = Extension(
   '_cppad_swig',
   sources            = extension_sources,
   swig_opts          = swig_opts,
   include_dirs       = include_dirs,
   library_dirs       = library_dirs,
   libraries          = libraries,
   extra_compile_args = extra_compile_args,
   extra_link_args    = extra_link_args,
   undef_macros       = undef_macros,
)
#
# my_build_py
# Build extensions before python or cppad_swig.py will not be current;
# see https://github.com/yanqd0/swig-python-demo
class my_build_py(build_py):
   def run(self):
      #
      # file_name
      file_name = 'lib/python/cppad_py/cppad_swig.py'
      #
      # build_ext first to create file_name which is needed by build_py.
      self.run_command('build_ext')
      #
      # 2DO: fix setup.py so the following kludge is not needed because
      # pip installs _cppad_swig.*.so file in site-packages instead of
      # site-packages/cppad_py (where swig expects it to be).
      file_obj  = open(file_name, 'r')
      file_data = file_obj.read()
      file_obj.close()
      pattern   = r'\nif.*:\n( *from [.] import _cppad_swig)'
      replace   = r'\nif False :\n\1'
      file_data = re.sub(pattern, replace, file_data)
      file_obj  = open(file_name, 'w')
      file_obj.write(file_data)
      file_obj.close()
      #
      # build_py
      super(build_py, self).run()
# ----------------------------------------------------------------------------
#
# setup
setup(
   url          = 'https://cppad-py.readthedocs.io',
   ext_modules  = [ extension_module ],
   packages     = [ 'cppad_py' ],
   package_dir  = { 'cppad_py' : 'lib/python/cppad_py' },
   cmdclass     = {
      'build_py' : my_build_py,
   }
)
