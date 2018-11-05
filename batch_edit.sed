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
# '
# sed command that maps old file and or directory names to new file names
# move_sed='
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
s|a_fun|d_fun|g
s|d_fun af =|d_fun f =|g
s|^\(\t*\)af\( *\)=|\1f \2=|
s|af\([.,%$]\)|f\1|g
s|af = cppad_py.d_fun(|f = cppad_py.d_fun(|
s|self[.]af|self.f|g
/^#\t*af$/d
