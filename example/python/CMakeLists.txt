# -----------------------------------------------------------------------------
#         cppad_swig: A C++ Object Library and SWIG Interface to CppAD
#          Copyright (C) 2017-17 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#          GNU Affero General Public License version 3.0 or later see
#                     http://www.gnu.org/licenses/agpl.txt
# -----------------------------------------------------------------------------
FIND_PACKAGE(SWIG)
FIND_PACKAGE(PythonInterp)
FIND_PACKAGE(PythonLibs)
IF ( SWIG_FOUND AND PythonLibs_FOUND AND PythonInterp_FOUND )
	#
	# which version of python did we find
	SET(lib    "${PYTHONLIBS_VERSION_STRING}" )
	SET(interp "${PYTHON_VERSION_STRING}" )
	IF( NOT ( "${lib}" STREQUAL "${interp}" ) )
		MESSAGE(FATAL_ERROR,
			"cmake python library ${lib} not same as interpertor ${interp}"
		)
	ENDIF( NOT ( "${lib}" STREQUAL "${interp}" ) )
	#
	# include the swig specific macros
	INCLUDE( ${CMAKE_ROOT}/Modules/UseSWIG.cmake )
	#
	# use include files in parent directory
	INCLUDE_DIRECTORIES( ${CMAKE_CURRENT_SOURCE_DIR}/.. )
	#
	# treat like a C++ files
	SET_SOURCE_FILES_PROPERTIES(../example.i PROPERTIES CPLUSPLUS ON)
	#
	# swig flags when processing this file
	SET_SOURCE_FILES_PROPERTIES(./example.i PROPERTIES SWIG_FLAGS "-Wall")
	#
	# include directory determined by find PythonLibs
	INCLUDE_DIRECTORIES(${PYTHON_INCLUDE_PATH})
	#
	# SWIG_ADD_MODULE(name language [ files ])
	SET(module_files ../example.i ../function.cpp ../normal_class.cpp)
	SWIG_ADD_MODULE(py_example python ${module_files})
	#
	# SWIG_LINK_LIBRARIES(name [ libraries ])
	SWIG_LINK_LIBRARIES(py_example ${PYTHON_LIBRARIES})
	#
	# additional flags for compiling swig wrapper
	SET_TARGET_PROPERTIES( ${SWIG_MODULE_py_example_REAL_NAME}
		 PROPERTIES COMPILE_FLAGS "${swig_cxx_flags}"
	)
	#
	# example use of CMAKE_SWIG_OUTDIR (not necessary in this case)
	SET(CMAKE_SWIG_OUTDIR "${CMAKE_CURRENT_BINARY_DIR}")
	#
	# copy check_py_example.py from source to binary directory
	ADD_CUSTOM_TARGET(check_py_example
		"${CMAKE_COMMAND}" -E copy
		"${CMAKE_CURRENT_SOURCE_DIR}/check_py_example.py"
		"${CMAKE_CURRENT_BINARY_DIR}/check_py_example.py"
		DEPENDS
		"${CMAKE_CURRENT_SOURCE_DIR}/check_py_example.py"
	)
	#
	# check_example_python
	ADD_CUSTOM_TARGET(check_example_python
		${PYTHON_EXECUTABLE} check_py_example.py
		DEPENDS ${SWIG_MODULE_py_example_REAL_NAME} check_py_example
	)
	MESSAGE(STATUS "make check_example_python: available")
	#
	# add this check to list of checks for parent directory
	SET(check_example_depends
		${check_example_depends} check_example_python PARENT_SCOPE
	)
	#
ENDIF ( SWIG_FOUND AND PythonLibs_FOUND AND PythonInterp_FOUND)
