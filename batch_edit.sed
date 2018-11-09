# ----------------------------------------------------------------------------
# list of directories that are added to the repository by batch_edit.sh
# new_directories='
# '
# list of files that are deleted by batch_edit.sh
# delete_files='
# '
# list of files that are not edited by the sed commands in this file
# (with the possible exception of the extra_sed commands)
# ignore_files='
# '
# list of files and or directories that are moved to new names
# move_paths='
# lib/example/cplusplus/sparse_rcv_xam.cpp
# lib/example/python/sparse_rcv_xam.py
# lib/python/sparse_rcv.py
# '
# sed command that maps old file and or directory names to new file names
# move_sed='
#	s|sparse_rcv|sparse_rcd|
# '
# list of files that get edited by the extra_sed command
# extra_files='
# '
# sed command that is applied to the extra files
# (after the other sed commands in this file)
# extra_sed='
# '
# ----------------------------------------------------------------------------
# Put other sed commands below here and without # at start of line
#
s|sparse_rcv\([a-z_]*\)[.]cpp|sparse_rcd\1.cpp|
s|sparse_rcv\([a-z_]*\)[.]py|sparse_rcd\1.py|
#
# fix claim sparse_rcd in sparse_hes_xam.cpp
#
s|cppad_py::sparse_rcv|cppad_py::sparse_rcd|g
s|sparse_rcv\ |sparse_rcd\ |g
#
# fix import sparse_rcd in __init__.py
s|from cppad_py[.]sparse_rcv\([a-z_]*\) |from cppad_py.sparse_rcd\1   |
#
# fix the property name
#
s|subset[.]rcv|subset.rcd|g