#! /bin/bash -e
# -----------------------------------------------------------------------------
#         cppad_py: A C++ Object Library and Python Interface to Cppad
#          Copyright (C) 2017-18 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# -----------------------------------------------------------------------------
# bash function that echos and executes a command
echo_eval() {
	echo $*
	eval $*
}
# -----------------------------------------------------------------------------
if [ "$0" != "bin/doc2py.sh" ]
then
	echo "bin/doc2py.sh: must be executed from its parent directory"
	exit 1
fi
# -----------------------------------------------------------------------------
if [ "$1" == '' ]
then
	echo 'usage: bin/doc2py.sh file section'
	echo 'file: is a file name in the lib/cplusplus directory'
	echo 'section: is an omhelp section name in that file.'
	exit 1
fi
file="$1"
section="$2"
# -----------------------------------------------------------------------------
git checkout lib/cplusplus/$file
git checkout lib/python/py_lib.omh
new_file="lib/python/$section.py"
# -----------------------------------------------------------------------------
if ! grep "\$begin $section" lib/cplusplus/$file > /dev/null
then
	echo "cannot find '\$begin $section' in lib/cplusplus/$file"
	exit 1
fi
if [ -e "$new_file" ]
then
	echo "The file $new_file already exists."
	exit 1
fi
# -----------------------------------------------------------------------------
echo "creating $new_file"
#
cat << EOF > $new_file
# -----------------------------------------------------------------------------
#         cppad_py: A C++ Object Library and Python Interface to Cppad
#          Copyright (C) 2017-18 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# -----------------------------------------------------------------------------
EOF
#
#
sed -n -e "/\$begin $section/,/\$end/p" lib/cplusplus/$file  > doc2bin.$$
sed doc2bin.$$ \
	-e 's|^\([^\t]\)| \1|' \
	-e 's|^|#|' \
	-e "s|\$begin $section|\$begin py_$section|" \
	-e 's|$begin.*\$\$|& $newlinech #$$|' \
	>> $new_file
rm doc2bin.$$
cat << EOF >> $new_file
# -----------------------------------------------------------------------------
# If necessary, put special $section code here and change __init__.py
# to import this version instead of version in cppad_py.cppad_py_swig
EOF
git add $new_file
# -----------------------------------------------------------------------------
echo "editing lib/cplusplus/$file"
sed -i lib/cplusplus/$file \
	-e "/\$begin $section/,/\$end/s|cppad_py[.]|cppad_py::|" \
	-e "s|\$begin $section|\$begin cpp_$section|"
# -----------------------------------------------------------------------------
echo "editing lib/python/py_lib.omh"
sed -i lib/python/py_lib.omh \
	-e "s|%\$\\\$|\\n\\t%$new_file&|"
# -----------------------------------------------------------------------------
echo 'bin/doc2py.sh: OK'
exit 0
