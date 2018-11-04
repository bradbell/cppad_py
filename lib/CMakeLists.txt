# -----------------------------------------------------------------------------
#         cppad_py: A C++ Object Library and Python Interface to Cppad
#          Copyright (C) 2017-18 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# -----------------------------------------------------------------------------
# Initialize check for this directory
SET(check_lib_depends "")
#
# directory used for cppad_py_swig.include files
INCLUDE_DIRECTORIES( ${CMAKE_SOURCE_DIR}/include )
INCLUDE_DIRECTORIES( ${CMAKE_CURRENT_BINARY_DIR} )
#
# The following enables cmake to handle windows dlls; see
# https://cmake.org/Wiki/BuildingWinDLL
include (GenerateExportHeader)
#
# cppad_py_lib (library used by sub-directories below)
ADD_LIBRARY(cppad_py_lib SHARED
	cplusplus/a_double.cpp
	cplusplus/fun.cpp
	cplusplus/sparse.cpp
	cplusplus/error.cpp
)
# The file cppad_py_lib_export.h, in the current binary directory, will
# define the symbol CPPAD_PY_LIB_PUBLIC. This symbol should be used to
# export cppad_py_lib, when it is being compiled, and import it when
# cppad_py_lib is being linked.
GENERATE_EXPORT_HEADER( cppad_py_lib
	BASE_NAME           cppad_py_lib
	EXPORT_MACRO_NAME   CPPAD_PY_LIB_PUBLIC
	EXPORT_FILE_NAME    cppad_py_lib_export.h
	STATIC_DEFINE       CPPAD_PY_LIB_BUILT_AS_STATIC
)
#
# additional flags for compiling cppad_py library
SET_TARGET_PROPERTIES(
	cppad_py_lib PROPERTIES COMPILE_FLAGS "${cppad_cxx_flags}"
)
#
# example / test directory (add to check_lib_depends)
ADD_SUBDIRECTORY(example)
#
#
IF( NOT( "${check_lib_depends}" STREQUAL "" ) )
	# Add the check target
	ADD_CUSTOM_TARGET(check_lib DEPENDS ${check_lib_depends})
	MESSAGE(STATUS "make check_lib: available")
	#
	# Change check depends in parent environment
	add_to_list(check_depends check_lib )
	SET(check_depends "${check_depends}" PARENT_SCOPE)
ENDIF( NOT( "${check_lib_depends}" STREQUAL "" ) )
