#! /bin/bash -e
# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileCopyrightText: Bradley M. Bell <bradbell@seanet.com>
# SPDX-FileContributor: 2017-22 Bradley M. Bell
# ----------------------------------------------------------------------------
run_branch='master'
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
# .readthedocs.yaml
# Changes to this file need to be checked in to be used by Read the Docs
cat << EOF > .readthedocs.yaml
version: 2

build:
   os: "ubuntu-20.04"
   tools:
      python: "3.10"
   jobs:
      post_install:
         - pip install furo
      post_build:
         - cp build/html/_sources/*.txt rst/_build/html/_sources

sphinx:
   configuration: rst/conf.py
EOF
# -----------------------------------------------------------------------------
# xsrst
dir_list='
   ./build/rst
   ./build/html
'
for dir in $dir_list
do
   if [ -e $dir ]
   then
      echo_eval rm -r $dir
   fi
done
echo_eval xrst --page_source
for dir in $dir_list
do
   if [ ! -e $dir ]
   then
      echo "readthedocs.sh: xrst did not create the $dir directory"
      exit 1
   fi
done
# -----------------------------------------------------------------------------
# version
version=$(version.sh get)
# -----------------------------------------------------------------------------
# ./rst
if [ -e ./rst ]
then
   echo_eval rm -r ./rst
fi
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
