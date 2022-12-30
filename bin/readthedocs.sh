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
if ! git show-ref $doc_branch > /dev/null
then
cat << EOF
readthedocs.sh: Cannot file the $doc_branch branch.
Start with a copy of the remote repository with no extra files; i.e.,
      git status -s
is empty. Then use the following commands to create the $doc_branch branch:

   git checkout --orphan $doc_branch
   git reset --hard
   git show $run_branch:.gitignore > .gitignore
   touch .nojekyll
   sed -i .gitignore -e 's|^/rst/$|# &|'

   git add .nojekyll .gitignore
   git commit -m 'create $doc_branch branch' .nojekyll .gitignore
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
xrst --page_source --rst_only
if [ ! -e $dir ]
then
   echo "readthedocs.sh: expected xrst to create the $dir directory"
   exit 1
fi
echo_eval rm -r $dir/.doctrees
# -----------------------------------------------------------------------------
# branch
echo_eval git checkout $doc_branch
#
# ./rst
if [ ! -d ./rst ]
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
   if [ "$first_version" == 'yes' ]
   then
      echo "   git commit -m '$doc_branch: advance to version $version'"
   fi
fi
# -----------------------------------------------------------------------------
echo 'readthedocs.sh: OK'
exit 0
