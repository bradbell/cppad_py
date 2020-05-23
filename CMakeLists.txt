# -----------------------------------------------------------------------------
#         cppad_py: A C++ Object Library and Python Interface to Cppad
#          Copyright (C) 2017-20 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# -----------------------------------------------------------------------------
# cmake \
#	-D CMAKE_VERBOSE_MAKEFILE=value \
#	-D CMAKE_BUILD_TYPE=value \
#	-D cppad_prefix=value  \
#	-D extra_cxx_flags=value
#
# -----------------------------------------------------------------------------
# preamble
# Suppress warnging that WIN32 not defined on cygwin
SET(CMAKE_LEGACY_CYGWIN_WIN32 0) # remove when version below >= 2.8.4
CMAKE_MINIMUM_REQUIRED(VERSION 2.8)
SET(cppad_py_version "2020.5.22")
PROJECT(cppad_py)
# =============================================================================
# MACROS
# =============================================================================
# assert(variable)
#
# ${variable}: (in)
# This variable is checked to make sure it is true, and if it is not true,
# a fatal error message is printed.
MACRO(assert variable)
     IF( NOT ${variable} )
		MESSAGE(FATAL_ERROR
			"Error: ${variable} is false in ${CMAKE_CURRENT_LIST_FILE}"
		)
     ENDIF( NOT ${variable} )
ENDMACRO(assert)
# ----------------------------------------------------------------------------
# MACRO: print_variable(variable)
#
# ${variable}: (in)
# The variable name and ${${variable}} is the variable value.
MACRO(print_variable variable)
	MESSAGE(STATUS "${variable} = ${${variable}}" )
ENDMACRO(print_variable)
# -----------------------------------------------------------------------------
# MACRO: cmake_argument(variable default type description)
#
# ${variable}: (in)
# is the variable we are setting to its default value.
#
# ${$variable}} (out)
# The value of the variable. It can be changed on the cmake command line
# (or in the camke gui). The final value of the variable is printed with
# the cmake output.
#
# ${default}: (in)
# is the default value for this variable; i.e.,
# if it is not set by the cmake command line or gui.
#
# ${type}: (in)
# must be one of the following:
#	STRING, if the variable holds an arbitrary string.
#	PATH, if the variable holds a directory.
#	BOOL, if the variable only has the values true or false.
#
# ${description}: (in)
# Is a description of how the variable affects the Cppad install procedure.
MACRO(cmake_argument variable default type description)
	IF( NOT ( ${type} STREQUAL "STRING" ) )
	IF( NOT ( ${type} STREQUAL "PATH" ) )
	IF( NOT ( ${type} STREQUAL "BOOL" ) )
		print_variable(variable)
		print_variable(type)
		MESSAGE(FATAL_ERROR,
			"optional_cmake_agument: error in a CMakeLists.txt file."
		)
	ENDIF( NOT ( ${type} STREQUAL "BOOL" ) )
	ENDIF( NOT ( ${type} STREQUAL "PATH" ) )
	ENDIF( NOT ( ${type} STREQUAL "STRING" ) )
	#
	IF(NOT ${variable} )
		SET(${variable} "${default}" CACHE ${type} "${description}")
	ENDIF(NOT ${variable} )
	print_variable(${variable})
ENDMACRO( cmake_argument )
# -----------------------------------------------------------------------------
# MACRO: add_to_list(variable_list constant_value)
#
# ${variables_list}: (in/out)
# The variable containing the list of values.
# The original list may be ""; i.e., the empty list.
#
# ${constant_value}: (in)
# Is the value we are adding to the list. This value cannot be empty.
MACRO(add_to_list variable_list constant_value )
	IF( "${constant_value}" STREQUAL "" )
		print_variable(variable_list)
		print_variable(constant_value)
		MESSAGE(FATAL_ERROR "add_to_list: constant_value is empty")
	ENDIF( "${constant_value}" STREQUAL "" )
	IF( "${${variable_list}}" STREQUAL "" )
		SET( ${variable_list} ${constant_value} )
	ELSE( "${${variable_list}}" STREQUAL "" )
		SET( ${variable_list} ${${variable_list}} ${constant_value} )
	ENDIF( "${${variable_list}}" STREQUAL "" )
ENDMACRO(add_to_list)
# -----------------------------------------------------------------------------
# make sure we have Swig available
FIND_PACKAGE(SWIG)
IF( NOT SWIG_FOUND )
	MESSAGE(FATAL_ERROR "Aborting because cmake cannot find Swig")
ENDIF( NOT SWIG_FOUND )
# -----------------------------------------------------------------------------
# print important system variables
print_variable(CMAKE_BINARY_DIR)
print_variable(CMAKE_VERBOSE_MAKEFILE)
print_variable(CMAKE_CXX_FLAGS)
print_variable(CMAKE_BUILD_TYPE)
# -----------------------------------------------------------------------------
# cppad_prefix, corresponding include directories and library
IF ( cppad_prefix )
	IF( cppad_prefix MATCHES "^[^/].*" )
		SET(cppad_prefix "${CMAKE_SOURCE_DIR}/${cppad_prefix}")
	ENDIF( cppad_prefix MATCHES "^[^/].*" )
ENDIF ( cppad_prefix )
cmake_argument(cppad_prefix NOTFOUND PATH "prefix used to install Cppad" )
IF( NOT cppad_prefix )
	MESSAGE(FATAL_ERROR "cppad_prefix is not defined by cmake command line")
ENDIF( NOT cppad_prefix )
#
# cppad include directory
IF(EXISTS ${cppad_prefix}/include)
	INCLUDE_DIRECTORIES( ${cppad_prefix}/include )
ELSE(EXISTS ${cppad_prefix}/include)
	MESSAGE(FATAL_ERROR "cppad include direcotry not ${cppad_prefix}/include")
ENDIF(EXISTS ${cppad_prefix}/include)
#
# cppad_library
FIND_LIBRARY(
	cppad_lib_path
	"cppad_lib"
	PATHS "${cppad_prefix}/lib"
	NO_DEFAULT_PATH
)
STRING(FIND "${cppad_lib_path}" "${cppad_prefix}" result)
IF( NOT ${result} EQUAL "0" )
	MESSAGE(FATAL_ERROR "can't find cppad object library below ${cppad_prefix}")
ENDIF( NOT ${result} EQUAL "0" )
# The message below about value of cppad_lib_path is used by setup.py
MESSAGE(STATUS "cppad_lib_path = \"${cppad_lib_path}\"")
# -----------------------------------------------------------------------------
# extra_cxx_flags
cmake_argument(extra_cxx_flags "" STRING
	"Flags, added to CMAKE_CXX_FLAGS, used when compiling cppad_py code."
)
# -----------------------------------------------------------------------------
# directory for including <cppad/py/cppad_py.hpp>
INCLUDE_DIRECTORIES( "${CMAKE_SOURCE_DIR}/include" )
# -----------------------------------------------------------------------------
# cxx_has_stdlib
# The message below about value of cxx_has_stdlib is used by setup.py
include(CheckCXXCompilerFlag)
CHECK_CXX_COMPILER_FLAG("-stdlib=libc++" cxx_has_stdlib)
IF( cxx_has_stdlib )
	MESSAGE(STATUS "cxx_has_stdlib = \"true\"" )
	SET(CMAKE_SHARED_LINKER_LFAGS "-stdlib=libc++")
	SET(extra_cxx_flags "${extra_cxx_flags} --stdlib=libc++")
ELSE( cxx_has_stdlib )
	MESSAGE(STATUS "cxx_has_stdlib = \"false\"" )
ENDIF( cxx_has_stdlib )
#
# Initialize list of tests as empty (added to by sub-directories below)
SET(check_depends "")
#
# sub-directories
ADD_SUBDIRECTORY(lib)
ADD_SUBDIRECTORY(example)
#
IF( "${check_depends}" STREQUAL "" )
	MESSAGE(FATAL_ERROR "no correctnes checks are available")
ENDIF( "${check_depends}" STREQUAL "" )
#
# Add the check target
ADD_CUSTOM_TARGET(check DEPENDS ${check_depends})
MESSAGE(STATUS "make check: available")
