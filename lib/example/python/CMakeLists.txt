# -----------------------------------------------------------------------------
#         cppad_swig: A C++ Object Library and Swig Interface to Cppad
#          Copyright (C) 2017-17 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#          GNU Affero General Public License version 3.0 or later see
#                     http://www.gnu.org/licenses/agpl.txt
# -----------------------------------------------------------------------------
assert(m4_executable)
#
# List of automatically generated source files
SET(auto_list
	a_double_xam.py
	a_fun_xam.py
	vector_ad_xam.py
	vector_double_xam.py
)
SET(auto_output_list "")
FOREACH( xam_file ${xam_file_list} )
	STRING(REGEX REPLACE "[.]xam" ".py" source_file ${xam_file})
	STRING(REGEX REPLACE "/"      "_"   source_file ${source_file})
	ADD_CUSTOM_COMMAND(
		OUTPUT ${CMAKE_CURRENT_BINARY_DIR}/${source_file}
		COMMAND ${m4_executable}
		-D language_=python
		-I ${CMAKE_SOURCE_DIR}/lib/xam
		${CMAKE_SOURCE_DIR}/lib/xam/${xam_file}
		> ${CMAKE_CURRENT_BINARY_DIR}/${source_file}
	)
	add_to_list(auto_output_list ${CMAKE_CURRENT_BINARY_DIR}/${source_file} )
ENDFOREACH( xam_file ${xam_file_list} )
ADD_CUSTOM_TARGET(auto_lib_python DEPENDS ${auto_output_list} )
MESSAGE(STATUS "make auto_lib_python: available")
#
# ----------------------------------------------------------------------------
assert( SWIG_FOUND )
FIND_PACKAGE(PythonInterp)
FIND_PACKAGE(PythonLibs)
IF ( PythonLibs_FOUND AND PythonInterp_FOUND)
	ADD_CUSTOM_COMMAND(
		OUTPUT ${CMAKE_CURRENT_BINARY_DIR}/check_all.py
		COMMAND
		${CMAKE_COMMAND} -E copy
		${CMAKE_CURRENT_SOURCE_DIR}/check_all.py
		${CMAKE_CURRENT_BINARY_DIR}/check_all.py
	)
	# which version of Python did we find
	SET(lib    "${PYTHONLIBS_VERSION_STRING}" )
	SET(interp "${PYTHON_VERSION_STRING}" )
	IF( NOT ( "${lib}" STREQUAL "${interp}" ) )
		MESSAGE(FATAL_ERROR,
			"cmake Python library ${lib} not same as interpertor ${interp}"
		)
	ENDIF( NOT ( "${lib}" STREQUAL "${interp}" ) )

	# treat like a C++ files
	SET_SOURCE_FILES_PROPERTIES(
		${swig_control_file} PROPERTIES CPLUSPLUS ON
	)

	# Swig flags when processing this file
	SET_SOURCE_FILES_PROPERTIES(
		${swig_control_file} PROPERTIES SWIG_FLAGS "-Wall"
	)

	# include directory determined by find PythonLibs
	INCLUDE_DIRECTORIES(${PYTHON_INCLUDE_PATH})

	# SWIG_ADD_MODULE(name language [ files ])
	SWIG_ADD_MODULE(py_cppad python ${swig_control_file} )

	# SWIG_LINK_LIBRARIES(name [ libraries ])
	SWIG_LINK_LIBRARIES(py_cppad cppad_swig_lib ${PYTHON_LIBRARIES})

	# additional flags for compiling Swig wrapper
	SET_TARGET_PROPERTIES( ${SWIG_MODULE_py_cppad_REAL_NAME}
		 PROPERTIES COMPILE_FLAGS "${swig_cxx_flags}"
	)

	# check_lib_python
	ADD_CUSTOM_TARGET(check_lib_python
		${PYTHON_EXECUTABLE} check_all.py
		DEPENDS
		${SWIG_MODULE_py_cppad_REAL_NAME}
		${CMAKE_CURRENT_BINARY_DIR}/check_all.py
		auto_lib_python
	)
	MESSAGE(STATUS "make check_lib_python: available")

	# Change check depends in parent environment
	add_to_list(check_lib_depends check_lib_python)
	SET(check_lib_depends "${check_lib_depends}" PARENT_SCOPE)

ENDIF ( PythonLibs_FOUND AND PythonInterp_FOUND)
