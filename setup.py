# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileCopyrightText: Bradley M. Bell <bradbell@seanet.com>
# SPDX-FileContributor: 2017-23 Bradley M. Bell
# ----------------------------------------------------------------------------
r'''
{xrst_begin_parent setup.py}
{xrst_spell
   cd
   dist
   dependencies
   gz
   pyproject
   toml
   grep
   pytest
   xam
}

Install cppad_py Python Module
##############################

See Also
********
:ref:`old_setup.py-name`

Errors
******
If you encounter an error during this process,
see :ref:`setup.py.error-name` .

cppad_py.git
************
To begin the install process,
create the cppad_py.git directory and make it the current
working directory as follows::

   git clone https://github.com/bradbell/cppad_py.git cppad_py.git
   cd cppad_py.git


version
*******
We use version for its value in the pyproject.toml file
(not including the quotes).
You can set the shell variable version to
this value, and see the value, with the following commands::

   eval $(grep '^version *=' pyproject.toml | sed -e 's| ||g')
   echo $version

System Dependencies
*******************
The following command will use your system package manager to
install some packages required by cppad_py::

   bin/system_depend.sh

Simple Case
***********
In the simple case,
the install setting :ref:`install_settings.py@include_mixed` is false.
After possibly changing some of the other settings in
:ref:`install_settings.py-name`, execute the following commands::

   bin/get_cppad.sh
   python3 -m build
   pip install dist/cppad_py-$version.tar.gz

You may need to add ``--user`` of specify some other install
prefix in the pip command above.
If you use this form of the install,
you will not be able to use any of the :ref:`mixed-name` routines.

Example
=======
If you place the Python Code below in the file ``temp.py`` ,
the following command should execute without error::

   python3 temp.py

Python Code:
{xrst_literal
   readme.md
   # BEGIN PYTHON
   # END PYTHON
}

Testing
=======
The following command will test this install::

   pytest example/python/core/*_xam.py


Mixed Case
**********
In the mixed case, :ref:`install_settings.py@include_mixed` is true.
After possibly changing some of the other settings in
:ref:`install_settings.py-name`, execute the following commands::

   bin/get_cppad_mixed.sh
   python3 -m build
   pip install dist/cppad_py-$version.tar.gz

If you use this form of the install,
you will be able to use any of the :ref:`mixed-name` routines.

Testing
=======
The following command will test this install::

   pytest example/python/*/*_xam.py

{xrst_end setup.py}
'''
# ----------------------------------------------------------------------------
import sys
import re
import os
#
from setuptools                       import setup, Extension
from setuptools.command.build_py      import build_py
# ----------------------------------------------------------------------------
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
   extra_link_args.append( f'-Wl,-rpath,{directory}' )
for lib in libraries :
   extra_link_args.append( f'-l{lib}' )
#
# libraries
# Theese values are now in extra_link_args
libraries    = list()
#
# extra_compile_args
extra_compile_args = list()
if extra_cxx_flags != '' :
   extra_compile_args += extra_cxx_flags.split()
if include_mixed == 'true' :
   extra_compile_args += [ '-D', 'INCLUDE_MIXED' ]
# gcc seems to give a wrong result checking array bounds during compile
extra_compile_args += [ '-Wno-array-bounds' ]
# clang warns when one uses bitwise operations for logicals
extra_compile_args += [ '-Wno-bitwise-instead-of-logical' ]
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
# ----------------------------------------------------------------------------
r'''
{xrst_begin setup.py.error}
{xrst_spell
   cholmod
   homebrew
   suitesparse
   cxx
   Wno
   var
}

setup.py Error Messages
#######################

cholmod.h
*********
This message can only occur when
:ref:`install_settings.py@include_mixed` is true.

Message
=======

| |tab| ... fatal error: 'cholmod.h' file not found
| |tab| # include <cholmod.h>

Solution
========
If you get this message, find out where ``cholmod.h`` is on your system.
For example, if you are using homebrew on the Mac, the following command
will find cholmod.h::

   find -L $HOMEBREW_PREFIX -name 'cholmod.h'

On one system, the result of this command was::

   /opt/homebrew/include/cholmod.h
   /opt/homebrew/var/homebrew/linked/suite-sparse/include/cholmod.h
   /opt/homebrew/opt/suite-sparse/include/cholmod.h
   /opt/homebrew/opt/suitesparse/include/cholmod.h
   /opt/homebrew/Cellar/suite-sparse/7.1.0/include/cholmod.h

So cholmod was installed in the /opt/homebrew/include directory.
Changing :ref:`install_settings.py@extra_cxx_flags` as follows
solved the problem::

   extra_cxx_flags  = '-Wall -pedantic-errors -Wno-unused-result -std=c++11'
   extra_cxx_flags += '-I /opt/homebrew/include'


{xrst_end setup.py.error}
'''
