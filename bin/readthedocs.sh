#! /bin/bash -e
# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileCopyrightText: Bradley M. Bell <bradbell@seanet.com>
# SPDX-FileContributor: 2017-22 Bradley M. Bell
# ----------------------------------------------------------------------------
run_branch='master'
doc_branch='temp'
# -----------------------------------------------------------------------------
# bash function that echos and executes a command
echo_eval() {
   echo $*
   eval $*
}
# -----------------------------------------------------------------------------
if [ "$0" != 'bin/readthedocs.sh' ]
then
   echo 'must execut bin/readthedocs.sh from its parent directory'
   exit 1
fi
# -----------------------------------------------------------------------------
branch=$(git branch | sed -n -e '/^*/p')
if [ "$branch" != "* $run_branch" ]
then
   echo "bin/readthedocs.sh: can onlybe run on $run_branch branch"
   exit 1
fi
# -----------------------------------------------------------------------------
git_status=$(git status -s)
if [ "$git_status" != '' ]
then
   echo 'bin/readthedocs.sh: git status -s is non-empty'
   exit 1
fi
# -----------------------------------------------------------------------------
if ! grep '^/rst/' .gitignore > /dev/null
then
   echo 'Cannot find following line in .gitignore'
   echo '/rst/'
   exit 1
fi
# -----------------------------------------------------------------------------
file_list='.nojekyll .gitignore .readthedocs.yaml'
if ! git show-ref $doc_branch > /dev/null
then
cat << EOF > .readthedocs.yaml
version: 2
build:
   os: "ubuntu-20.04"
   tools:
      python: "3.10"
   jobs:
      post_build:
         - cp rst/_sources/*.txt build/html/_sources
EOF
cat << EOF
readthedocs.sh: git cannot find the $doc_branch branch.
Use the following commands to create it:

   git checkout --orphan $doc_branch
   git reset --hard

   git show $run_branch:.gitignore > .gitignore
   sed -i .gitignore -e 's|^/rst/$|# &|'

   touch .nojekyll

   git add $file_list
   git commit -m 'create $doc_branch branch' $file_list
   git checkout $run_branch
EOF
   exit 1
fi
if ! git show-ref --heads --quiet $doc_branch
then
   echo "Cannot find local copy of the following $doc_branch branch"
   git show-ref | grep $doc_branch
    echo 'Perhaps the following would create the local copy ?'
    echo "  git checkout -b $doc_branch origin/$doc_branch"
    echo "  git checkout $run_branch"
   exit 1
fi
# -----------------------------------------------------------------------------
# xsrst
dir=./build/rst
if [ -e $dir ]
then
   echo_eval rm -r $dir
fi
echo_eval xrst --page_source --rst_only
if [ ! -e $dir ]
then
   echo "readthedocs.sh: xrst did not create the $dir directory"
   exit 1
fi
# -----------------------------------------------------------------------------
# version
version=$(version.sh get)
# -----------------------------------------------------------------------------
# doc_branch
echo_eval git checkout $doc_branch
#
# ./rst
if [ -e ./rst ]
then
   echo_eval rm -r ./rst
fi
echo_eval cp -r ./build/rst ./rst
#
# git delete
delete_list=$(git status -s | grep '^ D ' | sed -e 's|^ D ||')
if [ "$delete_list" != '' ]
then
    echo_eval git rm $delete_list
fi
#
# git add
modify_list=$(git status -s | grep '^ M ' | sed -e 's|^ M ||')
new_list=$(git status -s | grep '^[?][?] ' | sed -e 's|^[?][?] ||')
if [ "$modify_list" != '' ] || [ "$new_list" != '' ]
then
    echo_eval git add $new_list $modify_list
fi
#
list=$(git status -s)
if [ "$list" != '' ]
then
   echo "Currently in $doc_branch branch. The following will commit changes"
   echo "   git commit -m '$doc_branch: advance to version $version'"
fi
# -----------------------------------------------------------------------------
echo 'readthedocs.sh: OK'
exit 0
