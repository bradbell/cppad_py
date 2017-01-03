#! /bin/bash -e
# -----------------------------------------------------------------------------
#         cppad_swig: A C++ Object Library and SWIG Interface to CppAD
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
if [ "$0" != "bin/fix_msys_octave.sh" ]
then
	echo "bin/fix_msys_octave.sh: must be executed from its parent directory"
	exit 1
fi
# -----------------------------------------------------------------------------
cat << EOF > junk.sed
s|^#include <config\\.h>$|#include "config.h"|
s|^#include <base-list\\.h>$|#include "base-list.h"|
EOF
octave_include_dir=`octave-config -p  OCTINCLUDEDIR | sed -e 's|[\]|/|g'`
for name in oct.h comment-list.h
do
	file="$octave_include_dir/$name"
	if [ -e "$file.bak" ]
	then
		echo "skiping $name because following file already exists"
		echo "$file.bak"
	else
		sed "$file" -f junk.sed > fix_msys_octave.$$
		if ! diff "$file" fix_msys_octave.$$ > /dev/null
		then
			echo "Relpacing $name with following difference:"
			if ! diff "$file" fix_msys_octave.$$
			then
				mv "$file" "$file.bak"
				mv fix_msys_octave.$$ "$file"
				echo "Original file is in"
				echo "$file.bak"
			else
				echo 'fix_msys_octave.sh: program error'
				exit 1
			fi
		else
			echo "using original $file"
			rm fix_msys_octave.$$
		fi
	fi
done
# -----------------------------------------------------------------------------
echo 'bin/fix_msys_octave.sh: OK'
exit 0
