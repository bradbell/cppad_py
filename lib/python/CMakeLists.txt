# -----------------------------------------------------------------------------
#         cppad_swig: A C++ Object Library and SWIG Interface to CppAD
#          Copyright (C) 2017-17 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#          GNU Affero General Public License version 3.0 or later see
#                     http://www.gnu.org/licenses/agpl.txt
# -----------------------------------------------------------------------------
assert( SWIG_FOUND )
FIND_PACKAGE(PythonInterp)
FIND_PACKAGE(PythonLibs)
# ----------------------------------------------------------------------------
IF ( PythonLibs_FOUND AND PythonInterp_FOUND)
	# create check_all.py for this directory
	CONFIGURE_FILE(
		${CMAKE_CURRENT_SOURCE_DIR}/check_all.py.in
		${CMAKE_CURRENT_BINARY_DIR}/check_all.py
	)

	# which version of python did we find
	SET(lib    "${PYTHONLIBS_VERSION_STRING}" )
	SET(interp "${PYTHON_VERSION_STRING}" )
	IF( NOT ( "${lib}" STREQUAL "${interp}" ) )
		MESSAGE(FATAL_ERROR,
			"cmake python library ${lib} not same as interpertor ${interp}"
		)
	ENDIF( NOT ( "${lib}" STREQUAL "${interp}" ) )

	# treat like a C++ files
	SET_SOURCE_FILES_PROPERTIES(
		${swig_control_file} PROPERTIES CPLUSPLUS ON
	)

	# swig flags when processing this file
	SET_SOURCE_FILES_PROPERTIES(
		${swig_control_file} PROPERTIES SWIG_FLAGS "-Wall"
	)

	# include directory determined by find PythonLibs
	INCLUDE_DIRECTORIES(${PYTHON_INCLUDE_PATH})

	# SWIG_ADD_MODULE(name language [ files ])
	SWIG_ADD_MODULE(py_cppad python ${swig_control_file} )

	# SWIG_LINK_LIBRARIES(name [ libraries ])
	SWIG_LINK_LIBRARIES(py_cppad cppad_swig_lib ${PYTHON_LIBRARIES})

	# check_lib_python
	ADD_CUSTOM_TARGET(check_lib_python
		python check_all.py
		DEPENDS
		${SWIG_MODULE_py_cppad_REAL_NAME}
		${CMAKE_CURRENT_BINARY_DIR}/check_all.py
	)
	MESSAGE(STATUS "make check_lib_python: available")

	# Change check depends in parent environment
	add_to_list(check_lib_depends check_lib_python)
	SET(check_lib_depends "${check_lib_depends}" PARENT_SCOPE)

ENDIF ( PythonLibs_FOUND AND PythonInterp_FOUND)
