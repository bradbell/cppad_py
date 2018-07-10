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
if ! grep "\$begin $section" lib/cplusplus/$file > /dev/null
then
	echo "cannot find '\$begin $section' in lib/cplusplus/$file"
	exit 1
fi
if [ -e "lib/python/$section.py" ]
then
	echo "The file lib/python/$section.py already exists."
	exit 1
fi
# -----------------------------------------------------------------------------
echo "creating lib/python/$section.py"
#
cat << EOF > lib/python/$section.py
# -----------------------------------------------------------------------------
#         cppad_py: A C++ Object Library and Python Interface to Cppad
#          Copyright (C) 2017-18 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# -----------------------------------------------------------------------------
EOF
#
git checkout lib/cplusplus/$file
#
sed -n -e "/\$begin $section/,/\$end/p" lib/cplusplus/$file  > doc2bin.$$
sed doc2bin.$$ \
	-e 's|^\([^\t]\)| \1|' \
	-e 's|^|#|' \
	-e "s|\$begin $section|\$begin py_$section|" \
	-e 's|$begin.*\$\$|& $newlinech #$$|' \
	>> lib/python/$section.py
rm doc2bin.$$
#
sed -i lib/cplusplus/$file \
	-e "/\$begin $section/,/\$end/s|cppad_py[.]|cppad_py::|" \
	-e "s|\$begin $section|\$begin cpp_$section|"

# -----------------------------------------------------------------------------
echo 'bin/doc2py.sh: OK'
exit 0
