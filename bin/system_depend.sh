#! /usr/bin/env bash
# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileCopyrightText: Bradley M. Bell <bradbell@seanet.com>
# SPDX-FileContributor: 2017-23 Bradley M. Bell
# ----------------------------------------------------------------------------
# {xrst_begin system_depend.sh}
# {xrst_spell
#     dependencies
# }
# {xrst_comment_ch #}
#
# Use System Package Manager to Install Some Dependencies
# #######################################################
#
# Syntax
# ******
# bin/system_depend.sh
#
# Discussion
# **********
# #.  This command must be executed from the
#     :ref:`setup.py@cppad_py.git` directory.
# #.  If :ref:`install_settings.py@include_mixed` is true,
#     extra dependencies will be installed by :ref:`get_cppad_mixed.sh-name` .
#
# {xrst_end system_depend.sh}
# ----------------------------------------------------------------------------
set -e -u
# --------------------------------------------------------------------------
if [ "$#" != 0 ]
then
   echo 'bin/system_depend.sh: does not expect any arguments'
   exit 1
fi
if [ "$0" != 'bin/system_depend.sh' ]
then
   echo 'bin/system_depend.sh: must be executed from cppad_py.git directory'
   exit 1
fi
# -----------------------------------------------------------------------------
# bash function that echos and executes a command
echo_eval() {
	echo $*
	eval $*
}
# --------------------------------------------------------------------------
user=$(whoami)
if [ "$user" == 'root' ]
then
   sudo=''
else
   sudo='sudo'
fi
# -----------------------------------------------------------------------------
# set system_type, system_install example_install.tmp
if which apt-get >& /dev/null
then
   system_type='debian'
   system_install="$sudo apt-get install -y"
   dpkg-query -l | sed -e 's|  *| |g' -e 's|^ii ||' > example_install.tmp
elif which dnf >& /dev/null
then
   system_type='red_hat'
   system_install="$sudo dnf install -y"
   dnf list installed | sed -e 's|  *| |g' > example_install.tmp
elif which yum >& /dev/null
then
   system_type='red_hat'
   system_install="$sudo yum install -y"
   yum list installed | sed -e 's|  *| |g' > example_install.tmp
elif which port >& /dev/null
then
   system_type='mac_port'
   system_install="$sudo port install"
   port installed | sed -e 's|^ *||g' > example_install.tmp
elif which brew >& /dev/null
then
   system_type='mac_brew'
   system_install='brew install'
   brew list | sed -e 's|  *|\n|g' > example_install.tmp
elif which setup-x86_64 >& /dev/null
then
   system_tpye='cygwin'
   system_install='setup-x86_64.exe -q -P'
   cygcheck -c -d | sed -e 's|  *|-|' > example_install.tmp
else
   echo "Cannot determine this system's package manager"
   exit 1
fi
# --------------------------------------------------------------------------
# system external installs for normal system requirements
if [ "$system_type" == 'debian' ]
then
   list='
      cmake
      git
      pkg-config
      g++
      swig
   '
elif [ "$system_type" == 'red_hat' ]
then
   list='
      cmake
      git
      pkgconf
      gcc-c++
      swig
   '
elif [ "$system_type" == 'mac_port' ]
then
   list='
      cmake
      pkgconfig
      swig
   '
elif [ "$system_type" == 'mac_brew' ]
then
   list='
      cmake
      suite-sparse
      pkg-config
      gsl
      openjdk
      swig
   '
   # make sure Ipopt configure sees brew version of javac (not /usr/bin/javac)
   PATH="/usr/local/opt/openjdk/bin:$PATH"
elif [ "$system_tpye" == 'cygwin' ]
then
   list='
      cmake
      git
      pkgconf
      gcc-core
      gcc-g++
      swig
   '
else
   echo 'example_install.sh: script error'
   exit 1
fi
for package in $list
do
   if grep "^$package[^a-zA-Z_]" example_install.tmp > /dev/null
   then
      version=`grep "^$package[^a-zA-Z_]" example_install.tmp | head -1`
      echo "using installed $version"
   elif grep "^$package\$" example_install.tmp > /dev/null
   then
      # brew list case
      echo "using installed $package"
   else
      echo_eval $system_install $package
   fi
done
rm example_install.tmp
