#! /bin/bash -e
# -----------------------------------------------------------------------------
#         cppad_swig: A C++ Object Library and Swig Interface to Cppad
#          Copyright (C) 2017-17 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#          GNU Affero General Public License version 3.0 or later see
#                     http://www.gnu.org/licenses/agpl.txt
# -----------------------------------------------------------------------------
# bash function that echos and executes a command
echo_eval() {
	echo $*
	eval $*
}
# -----------------------------------------------------------------------------
if [ "$0" != "bin/new_file.sh" ]
then
	echo "bin/new_file.sh: must be executed from its parent directory"
	exit 1
fi
# -----------------------------------------------------------------------------
if [ "$1" == "" ]
then
	echo "bin/new_file.sh: file_name"
	exit 1
fi
file_name="$1"
if [ -e "$file_name" ]
then
	echo "$file_name exists"
	exit 1
fi
ext=`echo $file_name | sed -e 's/.*\.//'`
if [ "$ext" == "" ]
then
	echo "new_file.sh: file_name does not have an extension"
	exit 1
fi
# -----------------------------------------------------------------------------
case $ext in
	# =========================================================================
	cpp)
	cat << EOF  > $file_name
/* ----------------------------------------------------------------------------
          cppad_swig: A C++ Object Library and Swig Interface to Cppad
           Copyright (C) 2017-17 Bradley M. Bell (bradbell@seanet.com)
               This program is distributed under the terms of the
           GNU Affero General Public License version 3.0 or later see
                      http://www.gnu.org/licenses/agpl.txt
---------------------------------------------------------------------------- */
EOF
	;;
	# =========================================================================
	hpp)
	dir=`echo $file_name | sed -e 's|\(.*\)/[^/]*$|\1|'`
	if [ "$dir" != 'include/cppad/swig' ]
	then
		echo "new_file.sh: directory = $dir"
		echo 'files with .hpp extension must be include/cppad/swig'
		exit 1
	fi
	name=`echo $file_name | sed -e 's|include/||' | tr [a-z./] [A-Z__]`
	echo $name
	cat << EOF  > $file_name
# ifndef $name
# define $name
/* ----------------------------------------------------------------------------
          cppad_swig: A C++ Object Library and Swig Interface to Cppad
           Copyright (C) 2017-17 Bradley M. Bell (bradbell@seanet.com)
               This program is distributed under the terms of the
           GNU Affero General Public License version 3.0 or later see
                      http://www.gnu.org/licenses/agpl.txt
---------------------------------------------------------------------------- */

# endif
EOF
	;;
	# =========================================================================
	m4)
	dir=`echo $file_name | sed -e 's|\(.*\)/[^/]*$|\1|'`
	if [ "$dir" != 'lib/xam' ]
	then
		echo "new_file.sh: directory = $dir"
		echo "files with .sh extension must be in lib/xam directory"
		exit 1
	fi
	cat << EOF  > $file_name
# -----------------------------------------------------------------------------
#         cppad_swig: A C++ Object Library and Swig Interface to Cppad
#          Copyright (C) 2017-17 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#          GNU Affero General Public License version 3.0 or later see
#                     http://www.gnu.org/licenses/agpl.txt
# -----------------------------------------------------------------------------
# \$begin $file_name\$\$ \$newlinech #\$\$
# \$spell
# \$\$
# \$section REPLACE THIS TEXT\$\$
# REPLACE THIS TEXT
# \$end
EOF
	;;
	# =========================================================================
	omh)
	root_name=`echo $file_name | sed -e 's|.*/||' -e 's|\.omh$||'`
	cat << EOF  > $file_name
-------------------------------------------------------------------------------
          cppad_swig: A C++ Object Library and Swig Interface to Cppad
           Copyright (C) 2017-17 Bradley M. Bell (bradbell@seanet.com)
               This program is distributed under the terms of the
           GNU Affero General Public License version 3.0 or later see
                      http://www.gnu.org/licenses/agpl.txt
-------------------------------------------------------------------------------
\$begin $root_name\$\$
\$spell
\$\$

\$section \$\$

\$end
EOF
	;;
	# =========================================================================
	sh)
	dir=`echo $file_name | sed -e 's|\(.*\)/[^/]*$|\1|'`
	if [ "$dir" != 'bin' ]
	then
		echo "new_file.sh: directory = $dir"
		echo "files with .sh extension must be in bin directory"
		exit 1
	fi
	cat << EOF  > $file_name
#! /bin/bash -e
# -----------------------------------------------------------------------------
#         cppad_swig: A C++ Object Library and Swig Interface to Cppad
#          Copyright (C) 2017-17 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#          GNU Affero General Public License version 3.0 or later see
#                     http://www.gnu.org/licenses/agpl.txt
# -----------------------------------------------------------------------------
# bash function that echos and executes a command
echo_eval() {
	echo \$*
	eval \$*
}
# -----------------------------------------------------------------------------
if [ "\$0" != "$file_name" ]
then
	echo "$file_name: must be executed from its parent directory"
	exit 1
fi
# -----------------------------------------------------------------------------
REPLACE THIS LINE BY THE CODE FOR THIS SCRIPT.
# -----------------------------------------------------------------------------
echo '$file_name: OK'
exit 0
EOF
	echo_eval chmod +x $file_name
	;;
	# =========================================================================
	txt)
	cat << EOF > $file_name
# -----------------------------------------------------------------------------
#         cppad_swig: A C++ Object Library and Swig Interface to Cppad
#          Copyright (C) 2017-17 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#          GNU Affero General Public License version 3.0 or later see
#                     http://www.gnu.org/licenses/agpl.txt
# -----------------------------------------------------------------------------
EOF
	;;
	# =========================================================================
	xam)
	local_file=`echo "$file_name" | sed -e 's|lib/xam/||'`
	local_name=`echo $local_file | sed -e 's|/|_|g' -e 's|\.xam||'`
	cat << EOF > $file_name
include(xam.m4)dnl this comments out end of line character
header_($local_file)
c_ -----------------------------------------------------------------------------
c_         cppad_swig: A C++ Object Library and Swig Interface to Cppad
c_          Copyright (C) 2017-17 Bradley M. Bell (bradbell@seanet.com)
c_              This program is distributed under the terms of the
c_          GNU Affero General Public License version 3.0 or later see
c_                     http://www.gnu.org/licenses/agpl.txt
c_ -----------------------------------------------------------------------------
c_ $local_name
c_ -----------------------------------------------------------------------------
c_ BEGIN SOURCE
begin_bool_fun_0_(ok, $local_name)
REPLACE THIS WITH SOURCE CODE
end_
c_ END SOURCE
c_ -----------------------------------------------------------------------------
omhelp_($local_name,
Language_: REPLACE THIS WITH TITLE: Example and Test)
Eof_
EOF
	;;
	# =========================================================================
	*)
	echo "bin/new_file.sh: extension $ext is not yet supported."
	exit 1
esac
# ----------------------------------------------------------------------------
echo_eval git add $file_name
echo 'bin/new_file.sh: OK'
exit 0
