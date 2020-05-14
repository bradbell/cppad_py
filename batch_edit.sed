# ----------------------------------------------------------------------------
# None of the lists below can have white space or a dollar sign in an entry.
#
# list of directories that are added to the repository by batch_edit.sh
# new_directories='
# '
# list of files that are deleted by batch_edit.sh
# delete_files='
# '
# List of files that are not edited by the sed commands in this file
# (with the possible exception of the extra_seds commands).
# The files in bin/devel.sh ignore_files are automatically in this list.
# ignore_files='
# '
# list of files and or directories that are moved to new names
# move_paths='
#	example/python/numeric/runge4.py
#	example/python/numeric/runge4_one_step_xam.py
#	example/python/numeric/runge4_multi_step_xam.py
# '
# list of sed commands that map old file and directory names to new names.
# The characters @s, @d, @n get converted to a space, dollar sign, new line.
# move_seds='
#	s|runge4.py|ode_solve.py|
#	s|runge4_one_step_xam.py|ode_one_step_xam.py|
#	s|runge4_multi_step_xam.py|ode_multi_step_xam.py|
# '
# list of files that get edited by the extra_seds command
# extra_files='
# '
# list of sed commands that are applied to the extra files,
# after the other sed commands in this file.
# The characters @s, @d, @n get converted to a space, dollar sign, new line.
# extra_seds='
# '
# ----------------------------------------------------------------------------
# Put other sed commands below here and without # at start of line
s|import runge4|import ode_solve|g
s|runge4.py|ode_solve.py|g
s|runge4_one_step|ode_one_step|g
s|runge4_multi_step|ode_multi_step|g
s|runge4\.one_step|ode_solve.one_step|g
s|runge4\.multi_step|ode_solve.multi_step|g
