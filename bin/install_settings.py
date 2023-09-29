#! /usr/bin/env python3
# -----------------------------------------------------------------------------
# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileCopyrightText: Bradley M. Bell <bradbell@seanet.com>
# SPDX-FileContributor: 2017-23 Bradley M. Bell
# ----------------------------------------------------------------------------
cmake_install_prefix = '$HOME/prefix/cppad_py'
extra_cxx_flags      = '-Wall -pedantic-errors -Wno-unused-result -std=c++11'
build_type           = 'release'
include_mixed        = 'false'
test_cppad           = 'false'
verbose_makefile     = 'false'
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
