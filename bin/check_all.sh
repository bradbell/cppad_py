#! /usr/bin/env bash
# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileCopyrightText: Bradley M. Bell <bradbell@seanet.com>
# SPDX-FileContributor: 2017-23 Bradley M. Bell
# ----------------------------------------------------------------------------
set -e -u
# -----------------------------------------------------------------------------
# bash function that echos and executes a command
echo_eval() {
	echo $*
	eval $*
}
# ----------------------------------------------------------------------------
# bash function that echos and executes a command
logfile=`pwd`/check_all.log
tmpfile=`pwd`/check_all.tmp
echo_eval_log() {
   echo "$* >> check_all.log"
   echo $* >> $logfile
   if ! eval $* >& $tmpfile
   then
      if grep -i 'error' $tmpfile
      then
         echo 'check_all.sh: errors above are in check_all.log'
      else
         echo 'check_all.sh: see check_all.log for errors'
      fi
      cat $tmpfile >> $logfile
      exit_code 1
   fi
   cat $tmpfile >> $logfile
}
# -----------------------------------------------------------------------------
# cleanup and exit with specified code
exit_code() {
   if [ "$build_type" == 'debug' ]
   then
      sed -i bin/install_settings.py \
         -e "s|^build_type\( *\)=.*|build_type\1= 'release'|"
   fi
   if [ "$include_mixed" == 'true' ]
   then
      sed -i bin/install_settings.py \
         -e "s|^include_mixed\( *\)=.*|include_mixed\1= 'false'|"
   fi
   if [ -e $tmpfile ]
   then
      rm $tmpfile
   fi
   exit $1
}
# -----------------------------------------------------------------------------
if [ "$#" != 2 ]
then
   echo 'usage: bin/check_all.sh build_type include_mixed'
   echo 'where build_type is debug or release'
   echo 'and include_mixed is true or false'
   exit 1
fi
if [ "$0" != "bin/check_all.sh" ]
then
   echo "bin/check_all.sh: must be executed from its parent directory"
   exit 1
fi
if [ "$1" != 'debug' ] && [ "$1" != 'release' ]
then
   echo 'in/check_all.sh: first argument, build_type, is not debug or release'
   exit 1
fi
if [ "$2" != 'true' ] && [ "$2" != 'false' ]
then
   echo 'bin/check_all.sh: second argument, include_mixed, is not true or false'
   exit 1
fi
# -----------------------------------------------------------------------------
# build_type, cmake_install_prefix, extra_cxx_flags, include_mixed
eval $(bin/install_settings.py)
#
# libdir
libdir=$(bin/libdir.py)
#
if [ "$build_type" != 'release' ] || [ "$include_mixed" != 'false' ]
then
   echo 'check_all.sh: build type in bin/install_settings.py is not release'
   echo 'or include_mixed is not false.'
   echo 'This has been fixed, you should be able to just re-run this script.'
   # The exit_code function makes fix mentioned above
   exit_code 1
fi
if [ "$1" == 'debug' ]
then
   # This change will be undone by the exit_code function
   sed -i bin/install_settings.py \
      -e "s|^build_type\( *\)=.*|build_type\1= 'debug'|"
   build_type='debug'
fi
if [ "$2" == 'true' ]
then
   # This change will be undone by the exit_code function
   sed -i bin/install_settings.py  \
      -e "s|^include_mixed\( *\)=.*|include_mixed\1= 'true'|"
   include_mixed='true'
fi
#
# prefix, build
echo_eval_log bin/build_type.sh
# -----------------------------------------------------------------------------
export LD_LIBRARY_PATH="$cmake_install_prefix/$libdir"
echo "LD_LIBRARY_PATH=$LD_LIBRARY_PATH"
# -----------------------------------------------------------------------------
# clean out python distribution
minor=$(echo "import sys; print(sys.version_info.minor)" | python3)
if [ -e "$LD_LIBRARY_PATH/python3.$minor" ]
then
   echo_eval_log rm -r "$LD_LIBRARY_PATH/python3.$minor"
fi
if [ -e cppad_py ]
then
   echo_eval rm -r cppad_py
fi
if echo 'import cppad_py' | python >& /dev/null
then
   echo 'y' | pip uninstall cppad_py
fi
# -----------------------------------------------------------------------------
# clean out old informaiton
if [ -e $logfile ]
then
   echo "rm check_all.log"
   rm $logfile
fi
if ls build | grep '^lib\.' > /dev/null
then
   echo_eval_log rm -r "build/lib.*"
fi
if ls build | grep '^temp\.' > /dev/null
then
   echo_eval_log rm -r "build/temp.*"
fi
# -----------------------------------------------------------------------------
echo_eval_log check_copyright.sh
echo_eval_log bin/check_if_0.sh
echo_eval_log bin/check_tab.sh
echo_eval_log bin/check_guard.sh
echo_eval_log bin/run_xrst.sh
echo_eval_log bin/build_local.py
echo_eval_log cd build
echo_eval_log make check
echo_eval_log cd ..
echo_eval_log python3 example/python/check_all.py
echo_eval_log bin/check_install.sh
# -----------------------------------------------------------------------------
# check for warnings
#
# The FORTIFY_SOURCE has been undefined but the warning persists
cat << EOF > $tmpfile
/warning.*_FORTIFY_SOURCE/! b end
s|warning||g
s|\$| (not a problem)|
: end
EOF
#
if [ "$build_type" == 'debug' ]
then
   sed -i $logfile -f $tmpfile
fi
#
# check_all.py and run_sphins.sh run example/python/mixed/warning_xam.py
# and output 'warning_xam: OK', 'mixed_warning'.
if sed \
   -e '/warning_xam: OK/d' \
   -e '/setup.py install is deprecated/d' \
   -e '/you can list .license. under .dynamic./d' \
   -e '/easy_install command is deprecated/d' \
   -e '/warnings.warn(/d' \
   $logfile | \
   grep -i 'warning'
then
   echo 'check_all.sh: Error: see warnings in check_all.log'
   exit_code 1
fi
# -----------------------------------------------------------------------------
rm $tmpfile
echo 'bin/check_all.sh: OK'
exit_code 0
