#! /usr/bin/env python3
# -----------------------------------------------------------------------------
# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileCopyrightText: Bradley M. Bell <bradbell@seanet.com>
# SPDX-FileContributor: 2017-23 Bradley M. Bell
# ----------------------------------------------------------------------------
r'''
{xrst_begin install_settings.py}
{xrst_spell
   cmake
   cxx
   dist
   eval
   getcwd
   makefile
   os
   sys
   usr
   wno
}

Settings Used by Install and Test Scripts
#########################################
You must edit the file ``bin/install_settings.py``
to change these settings from their default values.

Syntax
******
The syntax cases below must be executed from the
:ref:`setup.py@cppad_py.git` directory;
i.e., the directory that cppad_py was cloned into.

Python
======
This sets install_settings to a python dictionary that has a key-value
pair for of the settings listed below:
{xrst_code py}
sys.path.insert(0, os.getcwd() + '/bin')
import install_settings
install_settings = install_settings.install_settings()
sys.path.pop(0)
{xrst_code}

Bash
====
This prints the value for each of the install settings:
{xrst_code sh}
bin/install_settings.py
{xrst_code}
This sets a bash variable to its value for
each of the install settings:
{xrst_code sh}
eval $(bin/install_settings.py)
{xrst_code}

cmake_install_prefix
********************
This prefix is used to install cppad and cppad_mixed.
The :ref:`old_setup.py-name` script also uses this prefix to install
cppad_py. The new :ref:`setup.py-name` installs cppad_py
using ``pip`` , so its prefix is set independently.
{xrst_code py}'''
cmake_install_prefix = '$HOME/prefix/cppad_py'
r'''{xrst_code}

#. If this prefix starts with ''/'' ,
   it is an absolute path; e.g., ``/usr/local``.
#. If it does not start with ``/`` , it is relative to the
   :ref:`setup.py@cppad_py.git` directory.
   The install_settings return value for cmake_install prefix will be
   the corresponding absolute path.
#. It may include the shell variable ``$HOME`` but no other variables;
   e.g; ``$HOME/prefix`` .
   The install_settings return value for cmake_install prefix will have
   ``$HOME`` expanded to an absolute path.

extra_cxx_flags
***************
Extra compiler flags used when compiling c++ code not including the
debugging and optimization flags.
The ones below are example flags used by g++:
{xrst_code py}'''
extra_cxx_flags = '-Wall -pedantic-errors -Wno-unused-result -std=c++11'
r'''{xrst_code}

build_type
**********
This must be must ``debug`` or ``release`` .
The debug version has more error messaging while the release
version runs faster.
{xrst_code py}'''
build_type = 'release'
r'''{xrst_code}
If the *build_type* is not debug or release, install_settings.py will
terminate with an error message.

cmake_install_prefix
====================
The actual prefix used for the install is

| |tab| *cmake_install_prefix.build_type*

and a soft link is created from *cmake_install_prefix* to this directory.
This way you can switch between testing debug and release without re-running
`bin/get_cppad.sh`` or ``bin/get_cppad_mixed.sh`` .

build
=====
The subdirectory

| |tab| ``build.``\ *build_type*

is used by :ref:`old_setup.py-name` to compile and test the software and
a soft link is created from ``build`` to this subdirectory.
The new :ref:`setup.py-name` uses the ``dist`` directory to build the
cppad_py package.

include_mixed
*************
This flag is true (false) if we are (are not)
including the python cppad_mixed interface.
{xrst_code py}'''
include_mixed = 'false'
r'''{xrst_code}
If it is true, the install script ``bin/get_cppad_mixed.sh``
must be used to install CppAD together with the all the other cppad_mixed
requirements.
Otherwise, ``bin/get_cppad.sh`` should be used to install CppAD.
If the *include_mixed* is not true or false, install_settings.py will
terminate with an error message.

test_cppad
**********
This must be must true or false .
CppAD has a huge test suite and this can take a significant amount of time,
but it may be useful if you have problems.
{xrst_code py}'''
test_cppad = 'false'
r'''{xrst_code}

verbose_makefile
****************
This flag is true (false) a verbose version of the build description
will (will not) be printed.
{xrst_code py}'''
verbose_makefile = 'false'
r'''{xrst_code}
If the *verbose_makefile* is not true or false, install_settings.py will
terminate with an error message.

{xrst_end install_settings.py}
'''
#
# imports
import os
import sys
#
# build_type
if build_type != 'debug' and build_type != 'release' :
   msg = 'install_settings.py: build_type is not debug or release'
   sys.exit(msg)
#
# include_mixed
if include_mixed != 'true' and include_mixed != 'false' :
   msg = 'install_settings.py: include_mixed is not true or false'
   sys.exit(msg)
#
# verbose_makefile
if verbose_makefile != 'true' and verbose_makefile != 'false' :
   msg = 'install_settings.py: verbose_makefile is not true or false'
   sys.exit(msg)
#
# cmake_install_prefix
index = cmake_install_prefix.find('$HOME')
if index >= 0 :
   cmake_install_prefix = cmake_install_prefix.replace(
      '$HOME', os.environ['HOME']
   )
   assert cmake_install_prefix.startswith('/')
#
# cmake_install_prefix
if not cmake_install_prefix.startswith('/') :
   cmake_install_prefix = os.getcwd() + '/' + cmake_install_prefix
#
# install_settings
def install_settings() :
   settings = {
      'cmake_install_prefix' : cmake_install_prefix ,
      'extra_cxx_flags'      : extra_cxx_flags      ,
      'build_type'           : build_type ,
      'include_mixed'        : include_mixed ,
      'test_cppad'           : test_cppad ,
      'verbose_makefile'     : verbose_makefile ,
   }
   return settings
#
if __name__ == '__main__' :
   #
   # output
   output  = f"cmake_install_prefix='{cmake_install_prefix}'\n"
   output += f"extra_cxx_flags='{extra_cxx_flags}'\n"
   output += f"build_type='{build_type}'\n"
   output += f"include_mixed='{include_mixed}'\n"
   output += f"test_cppad='{test_cppad}'\n"
   output += f"verbose_makefile='{verbose_makefile}'\n"
   print(output)
