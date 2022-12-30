#! /bin/bash -e
#
# git ls-files: list files in the git repository
# sed:          remove files in the test_rst directory
git ls-files | sed -e '/^rst[/]/d'
