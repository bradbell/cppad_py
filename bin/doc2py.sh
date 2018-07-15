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
if [ "$3" != '.py' ] && [ "$3" != '.omh' ]
then
	echo 'usage: bin/doc2py.sh file section ext'
	echo 'file:    is a file name in the lib/cplusplus directory'
	echo 'section: is an omhelp section name in that file.'
	echo 'ext:     is either .py for wrappers, and .omh if no wrapper needed'
	exit 1
fi
file="$1"
section="$2"
ext="$3"
# -----------------------------------------------------------------------------
git checkout lib/cplusplus/$file
new_file="lib/python/$section$ext"
# -----------------------------------------------------------------------------
if ! grep "\$begin $section" lib/cplusplus/$file > /dev/null
then
	echo "cannot find '\$begin $section' in lib/cplusplus/$file"
	exit 1
fi
if [ -e "$new_file" ]
then
	echo_eval rm $new_file
fi
# -----------------------------------------------------------------------------
echo "creating $new_file"
#
cat << EOF > $new_file
-------------------------------------------------------------------------------
          cppad_py: A C++ Object Library and Python Interface to Cppad
           Copyright (C) 2017-18 Bradley M. Bell (bradbell@seanet.com)
               This program is distributed under the terms of the
               GNU General Public License version 3.0 or later see
                     https://www.gnu.org/licenses/gpl-3.0.txt
-------------------------------------------------------------------------------
EOF
sed -n -e "/\$begin $section\\\$/,/\$end/p" lib/cplusplus/$file  >> $new_file
if [ "$ext" == '.omh' ]
then
	sed -i $new_file \
	-e "s|\$begin $section|\$begin py_$section|" \
	-e "/\$cref.C++.${section}_xam.cpp.\$\\\$,/d" \
	-e "s|\$cref/Python/${section}_xam.py/.*|\$cref ${section}_xam.py\$\$|" \
	-e "/lib.example.cplusplus.${section}_xam.cpp/d" \
	>> $new_file
else
	sed -i $new_file \
	-e '1,7s|^ |#|' \
	-e '1,7s|^--|# |' \
	-e '8,$s|^\([^\t]\)| \1|' \
	-e '8,$s|^|#|' \
	-e "s|\$begin $section|\$begin py_$section|" \
	-e 's|$begin.*\$\$|& $newlinech #$$|' \
	-e "/\$cref.C++.${section}_xam.cpp.\$\\\$,/d" \
	-e "s|\$cref/Python/${section}_xam.py/.*|\$cref ${section}_xam.py\$\$|" \
	-e "/lib.example.cplusplus.${section}_xam.cpp/d" \
	-e 's|/cpp_\([a-z_]*\)/|/py_\1/|g' \
	>> $new_file
fi
git add $new_file
# -----------------------------------------------------------------------------
echo "editing lib/cplusplus/$file"
sed -i lib/cplusplus/$file \
	-e "/\$begin $section/,/\$end/s|cppad_py[.]|cppad_py::|" \
	-e "s|\$begin $section|\$begin cpp_$section|" \
	-e "/\$cref.Python.${section}_xam.py.\$\\\$./d" \
	-e "s|\$cref/C++/${section}_xam.cpp/.*|\$cref ${section}_xam.cpp\$\$|" \
	-e "/lib.example.python.${section}_xam.py/d" \
	-e "s|\\(lib.example.cplusplus.${section}_xam.cpp\\)%|\\1|"
# -----------------------------------------------------------------------------
# fix cross references in all c++ files
list=`ls lib/cplusplus/*.cpp`
for file in $list
do
	sed -i $file \
		-e "s|/${section}/|/cpp_${section}/|g" \
		-e "s|\$cref $section\\\$|\$cref cpp_$section\$|"
done
# -----------------------------------------------------------------------------
# fix cross references in all python files
list=`ls lib/python/*.py`
for file in $list
do
	sed -i $file -e "s|/${section}/|py_&|g"
done
# -----------------------------------------------------------------------------
echo 'bin/doc2py.sh: OK'
exit 0
