
# -----------------------------------------------------------------------------
#         cppad_swig: A C++ Object Library and SWIG Interface to CppAD
#          Copyright (C) 2017-17 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#          GNU Affero General Public License version 3.0 or later see
#                     http://www.gnu.org/licenses/agpl.txt
# -----------------------------------------------------------------------------
# parent directory should ensure SWIG was found
assert( SWIG_FOUND )
#
# Initialize check for this directory
SET(check_lib_depends "")
#
# directory used for cppad_swig include files
INCLUDE_DIRECTORIES( ${CMAKE_SOURCE_DIR}/include )
INCLUDE_DIRECTORIES( ${CMAKE_CURRENT_BINARY_DIR} )
#
# include the swig specific macros
INCLUDE( ${CMAKE_ROOT}/Modules/UseSWIG.cmake )
#
# swig_control_file: used by the sub-directories below
SET(swig_control_file "${CMAKE_CURRENT_SOURCE_DIR}/cppad_swig.i" )
#
# The following enables cmake to handle windows dlls; see
# https://cmake.org/Wiki/BuildingWinDLL
include (GenerateExportHeader)
#
# cppad_swig_lib (library used by sub-directories below)
ADD_LIBRARY(cppad_swig_lib SHARED
	a_double.cpp
	a_fun.cpp
	function.cpp
)
# The file cppad_swig_lib_export.h, in the current binary directory, will
# define the symbol CPPAD_SWIG_LIB_PUBLIC. This symbol should be used to
# export cppad_swig_lib, when it is being compiled, and import it when
# cppad_swig_lib is being linked.
GENERATE_EXPORT_HEADER( cppad_swig_lib
	BASE_NAME         cppad_swig_lib
	EXPORT_MACRO_NAME CPPAD_SWIG_LIB_PUBLIC
	EXPORT_FILE_NAME  cppad_swig_lib_export.h
	STATIC_DEFINE     CPPAD_SWIG_LIB_BUILT_AS_STATIC
)
#
# additional flags for compiling cppad_swig library
SET_TARGET_PROPERTIES(
	cppad_swig_lib PROPERTIES COMPILE_FLAGS "${cppad_cxx_flags}"
)
#
# swig extra dependencies used by sub-directories below
SET(SWIG_MODULE_cppad_swig_EXTRA_DEPS
	"${CMAKE_SOURCE_DIR}/include/cppad/swig/a_double.hpp"
	"${CMAKE_SOURCE_DIR}/include/cppad/swig/a_fun.hpp"
	"${CMAKE_SOURCE_DIR}/include/cppad/swig/function.hpp"
)
#
# sub-directories for each language
ADD_SUBDIRECTORY(python)
ADD_SUBDIRECTORY(octave)
ADD_SUBDIRECTORY(perl)
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
