# ----------------------------------------------------------------------------
# list of directories that are added to the repository by batch_edit.sh
# new_directories='
# '
# list of files that are deleted by batch_edit.sh
# delete_files='
#	bin/batch_edit.sh
# '
# list of files that are not edited by the sed commands in this file
# (with the possible exception of the extra_sed commands)
# ignore_files='
# '
# list of files and or directories that are moved to new names
# (obtained using the command git ls-files | grep a_fun)
# move_paths='
# include/cppad/py/a_fun.hpp
# lib/cplusplus/a_fun.cpp
# lib/example/cplusplus/a_fun_abort_xam.cpp
# lib/example/cplusplus/a_fun_forward_xam.cpp
# lib/example/cplusplus/a_fun_hessian_xam.cpp
# lib/example/cplusplus/a_fun_jacobian_xam.cpp
# lib/example/cplusplus/a_fun_optimize_xam.cpp
# lib/example/cplusplus/a_fun_property_xam.cpp
# lib/example/cplusplus/a_fun_reverse_xam.cpp
# lib/example/python/a_fun_abort_xam.py
# lib/example/python/a_fun_forward_xam.py
# lib/example/python/a_fun_hessian_xam.py
# lib/example/python/a_fun_jacobian_xam.py
# lib/example/python/a_fun_optimize_xam.py
# lib/example/python/a_fun_property_xam.py
# lib/example/python/a_fun_reverse_xam.py
# lib/python/a_fun.py
# lib/python/a_fun_ctor.py
# lib/python/a_fun_forward.py
# lib/python/a_fun_hessian.py
# lib/python/a_fun_jacobian.py
# lib/python/a_fun_optimize.omh
# lib/python/a_fun_property.omh
# lib/python/a_fun_reverse.py
# '
# sed command that maps old file and or directory names to new file names
# move_sed='
#	s|a_fun|fun|
# '
# list of files that get edited by the extra_sed command
# extra_files='
#	lib/example/python/check_all.py.in
# '
# sed command that is applied to the extra files
# (after the other sed commands in this file)
# extra_sed='
#	s|a_fun_|fun_|
# '
# ----------------------------------------------------------------------------
# Put other sed commands below here and without # at start of line
#
s|a_fun\([a-z_]*\)[.]cpp|fun\1.cpp|
s|a_fun\([a-z_]*\)[.]py|fun\1.py|
s|a_fun\([a-z_]*\)[.]omh|fun\1.omh|
s|a_fun\([a-z_]*\)[.]hpp|fun\1.hpp|
#
# fix imports in lib/example/python/__init__.py
s|from cppad_py[.]a_fun\([a-z_]*\) |from cppad_py.fun\1   |
#
# fix lib/example/python function names imported by
# lib/example/python/check_all.py
s|^def a_fun_\([a-z_]*\)_xam()|def fun_\1_xam()|
