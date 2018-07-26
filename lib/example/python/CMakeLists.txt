# -----------------------------------------------------------------------------
#         cppad_py: A C++ Object Library and Python Interface to Cppad
#          Copyright (C) 2017-18 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# -----------------------------------------------------------------------------
#
# list of python source files in CMAKE_CURRENT_SOURCE_DIR
FILE(GLOB python_source_list "*.py")
#
# commands to copy the files to CMAKE_CURRENT_BINARY_DIR
SET(python_copy_list "")
FOREACH(source_file ${python_source_list} )
	STRING(REGEX REPLACE ".*/" "" local_file ${source_file})
	ADD_CUSTOM_COMMAND(
		OUTPUT ${CMAKE_CURRENT_BINARY_DIR}/${local_file}
		COMMAND
		${CMAKE_COMMAND} -E copy
		${CMAKE_CURRENT_SOURCE_DIR}/${local_file}
		${CMAKE_CURRENT_BINARY_DIR}/${local_file}
	)
	add_to_list(python_copy_list ${CMAKE_CURRENT_BINARY_DIR}/${local_file} )
#
ENDFOREACH(source_file ${python_source_list} )
ADD_CUSTOM_TARGET(auto_lib_python DEPENDS ${python_copy_list} )
MESSAGE(STATUS "make auto_lib_python: available")
#
FIND_PACKAGE(PythonInterp ${python_version})
FIND_PACKAGE(PythonLibs ${python_version})
IF ( NOT ( PythonLibs_FOUND AND PythonInterp_FOUND ) )
	MESSAGE(FATAL_ERROR,
		"cmake cannot find Python or its libraries"
	)
ENDIF ( NOT ( PythonLibs_FOUND AND PythonInterp_FOUND ) )
#
# which version of Python did we find
SET(lib    "${PYTHONLIBS_VERSION_STRING}" )
SET(interp "${PYTHON_VERSION_STRING}" )
IF( NOT ( "${lib}" STREQUAL "${interp}" ) )
	MESSAGE(FATAL_ERROR,
		"cmake Python library ${lib} not same as interpertor ${interp}"
	)
ENDIF( NOT ( "${lib}" STREQUAL "${interp}" ) )
#
# report the version of python
MESSAGE(STATUS "Python version ${PYTHON_VERSION_STRING}")
#
# check_all.py
CONFIGURE_FILE( check_all.py.in check_all.py )
# ----------------------------------------------------------------------------
# check_lib_python
ADD_CUSTOM_TARGET(check_lib_python
	${PYTHON_EXECUTABLE} check_all.py
	DEPENDS
	auto_lib_python
)
MESSAGE(STATUS "make check_lib_python: available")
#
# Change check depends in parent environment
add_to_list(check_lib_depends check_lib_python)
SET(check_lib_depends "${check_lib_depends}" PARENT_SCOPE)
