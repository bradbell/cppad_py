# -----------------------------------------------------------------------------
#         cppad_py: A C++ Object Library and Python Interface to Cppad
#          Copyright (C) 2017-18 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# -----------------------------------------------------------------------------
FIND_PACKAGE(SWIG)
FIND_PACKAGE(PythonInterp 3)
FIND_PACKAGE(PythonLibs 3)
IF ( SWIG_FOUND AND PythonLibs_FOUND AND PythonInterp_FOUND )
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
	# include the Swig specific macros
	INCLUDE( ${CMAKE_ROOT}/Modules/UseSWIG.cmake )
	#
	# use include files in parent directory
	INCLUDE_DIRECTORIES( ${CMAKE_CURRENT_SOURCE_DIR}/.. )
	#
	# treat like a C++ files
	SET_SOURCE_FILES_PROPERTIES(../swig_xam.i PROPERTIES CPLUSPLUS ON)
	#
	# Swig flags when processing this file
	SET_SOURCE_FILES_PROPERTIES(./swig_xam.i PROPERTIES SWIG_FLAGS "-Wall")
	#
	# include directory determined by find PythonLibs
	INCLUDE_DIRECTORIES(${PYTHON_INCLUDE_PATH})
	#
	# add_swig_library(library language files)
	SET(module_files ../swig_xam.i ../function.cpp ../normal_class.cpp)
	add_swig_library(py_swig_xam python module_files)
	#
	# SWIG_LINK_LIBRARIES(name [ libraries ])
	SWIG_LINK_LIBRARIES(py_swig_xam ${PYTHON_LIBRARIES})
	#
	# additional flags for compiling Swig wrapper
	SET_TARGET_PROPERTIES( ${SWIG_MODULE_py_swig_xam_REAL_NAME}
		 PROPERTIES COMPILE_FLAGS "${swig_cxx_flags}"
	)
	#
	# example use of CMAKE_SWIG_OUTDIR (not necessary in this case)
	SET(CMAKE_SWIG_OUTDIR "${CMAKE_CURRENT_BINARY_DIR}")
	#
	# copy check_swig_xam.py from source to binary directory
	ADD_CUSTOM_TARGET(check_swig_xam_py
		"${CMAKE_COMMAND}" -E copy
		"${CMAKE_CURRENT_SOURCE_DIR}/check_swig_xam.py"
		"${CMAKE_CURRENT_BINARY_DIR}/check_swig_xam.py"
		DEPENDS
		"${CMAKE_CURRENT_SOURCE_DIR}/check_swig_xam.py"
	)
	#
	# check_swig_xam_python
	ADD_CUSTOM_TARGET(check_swig_xam_python
		${PYTHON_EXECUTABLE} check_swig_xam.py
		DEPENDS ${SWIG_MODULE_py_swig_xam_REAL_NAME} check_swig_xam_py
	)
	MESSAGE(STATUS "make check_swig_xam_python: available")
	#
	# add this check to list of checks for parent directory
	SET(check_swig_xam_depends
		${check_swig_xam_depends} check_swig_xam_python PARENT_SCOPE
	)
	#
ENDIF ( SWIG_FOUND AND PythonLibs_FOUND AND PythonInterp_FOUND)
