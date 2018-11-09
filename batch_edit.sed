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
s|d_fun_optimize_xam, |fun_optimize_xam,   |
s|d_fun_jacobian_xam, |fun_jacobian_xam,   |
s|d_fun_hessian_xam, |fun_hessian_xam,   |
s|d_fun_forward_xam, |fun_forward_xam,   |
s|d_fun_reverse_xam, |fun_reverse_xam,   |
s|d_fun_abort_xam, |fun_abort_xam,   |
#
s|d_fun_abort_xam|fun_abort_xam|
s|d_fun_optimize_xam|fun_optimize_xam|
s|d_fun_jacobian_xam|fun_jacobian_xam|
s|d_fun_hessian_xam|fun_hessian_xam|
s|d_fun_forward_xam|fun_forward_xam|
s|d_fun_reverse_xam|fun_reverse_xam|
s|d_fun_abort_xam|fun_abort_xam|
