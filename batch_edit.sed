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
#	include/cppad/py/utility.hpp
#	lib/cplusplus/utility.cpp
# '
# sed command that maps old file and or directory names to new file names
# move_sed='
#	s|utility|cppad_vec|
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
s|utility.hpp|cppad_vec.hpp|
s|utility.cpp|cppad_vec.cpp|
s|UTILITY_HPP|CPPAD_VEC_HPP|
