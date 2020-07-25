#! /bin/bash -e
# -----------------------------------------------------------------------------
#         cppad_py: A C++ Object Library and Python Interface to Cppad
#          Copyright (C) 2017-20 Bradley M. Bell (bradbell@seanet.com)
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
#
# make sure we are on the master branch
branch=`git branch | sed -n -e '/^\*/p'`
if [ "$branch" != '* master' ]
then
	echo 'gh_pages.sh: can only be executed starting with master branch'
	exit 1
fi
#
# make sure the gh-pages branch exists
if ! git show-ref gh-pages > /dev/null
then
cat << EOF
gh_pages.sh: Cannot file the gh-pages branch.
Start with a copy of the remote repository with no extra files; i.e.,
		git status -s
is empty. Then use the following commands to create the gh-pages branch:

	git checkout --orphan gh-pages
	git reset --hard
	git show master:.gitignore > .gitignore
	touch .nojekyll
	sed -i .gitignore -e 's|^/doc/$|# &|'

	echo '<html><script>'                     >  index.html
	echo '	window.location.href="doc/index.html";' >> index.html
	echo '</script></html>'                  >> index.html

	git add .nojekyll .gitignore index.html
	git commit -m 'create gh-pages branch' .nojekyll .gitignore index.html
	git checkout master
EOF
	exit 1
fi
if ! git show-ref --heads --quiet gh-pages
then
	echo 'Cannot find local copy of the following gh-pages branches'
	git show-ref | grep gh-pages
    echo 'Perhaps the following would create the local copy ?'
    echo '  git checkout -b gh-pages origin/gh-pages'
    echo '  git checkout master'
	exit 1
fi
#
# make sure certian files exits on gh-pages branch
for name in .nojekyll .gitignore
do
	if ! git show gh-pages:$name > /dev/null
	then
		echo "gh_pages.sh: cannot find $name in the gh-pages branch"
		exit 1
	fi
done
#
# version
version=`version.sh get`
# -----------------------------------------------------------------------------
# build documentation
echo_eval bin/run_xsrst.sh
# -----------------------------------------------------------------------------
# checkout gh-pages
echo_eval git checkout gh-pages
#
# remove old version of documentation
echo_eval rm -r doc
#
# copy new version of documentation
echo_eval cp -r build/sphinx/_build doc
#
# delete list
delete_list=$(git status -s | grep '^ D ' | sed -e 's|^ D ||')
if [ "$delete_list" != '' ]
then
    echo_eval git rm $delete_list
fi
#
# add_list
modify_list=$(git status -s | grep '^ M ' | sed -e 's|^ M ||')
new_list=$(git status -s | grep '^[?][?] ' | sed -e 's|^[?][?] ||')
if [ "$modify_list" != '' ] || [ "$new_list" != '' ]
then
    echo_eval git add $add_list $modify_list
fi
#
# -----------------------------------------------------------------------------
list=`git status -s`
if [ "$list" != '' ]
then
	echo 'Currently in the gh-pages branch. The following will commit changes'
	echo "	git commit -m 'update gh-pages to version $version'"
fi
# -----------------------------------------------------------------------------
echo 'gh_pages.sh: OK'
exit 0
