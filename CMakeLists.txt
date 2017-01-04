# -----------------------------------------------------------------------------
#         cppad_swig: A C++ Object Library and Swig Interface to Cppad
#          Copyright (C) 2017-17 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#          GNU Affero General Public License version 3.0 or later see
#                     http://www.gnu.org/licenses/agpl.txt
# -----------------------------------------------------------------------------
# preamble
CMAKE_MINIMUM_REQUIRED(VERSION 2.8)
PROJECT(cppad_swig)
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
# cmake_argument(variable default type description)
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
	SET(${variable} "${default}" CACHE ${type} "${description}")
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
print_variable(CMAKE_VERBOSE_MAKEFILE)
print_variable(CMAKE_CXX_FLAGS)
print_variable(CMAKE_BUILD_TYPE)
# -----------------------------------------------------------------------------
# cppad_prefix
cmake_argument(cppad_prefix NOTFOUND PATH "prefix used to install Cppad" )
IF( NOT cppad_prefix )
	MESSAGE(FATAL_ERROR "cppad_prefix is not defined by cmake command line")
ENDIF( NOT cppad_prefix )
INCLUDE_DIRECTORIES( ${cppad_prefix}/include )
# -----------------------------------------------------------------------------
# compiler flags
cmake_argument(cppad_cxx_flags "" STRING
"Flags, in addititon to CMAKE_CXX_FLAGS, used when compiling cppad_swig code."
)
cmake_argument(swig_cxx_flags "" STRING
"Flags, in addititon to CMAKE_CXX_FLAGS, used when Swig wrapper code."
)
# -----------------------------------------------------------------------------
#
# Initialize list of tests as empty (added to by sub-directories below)
SET(check_depends "")
#
# sub-directories
ADD_SUBDIRECTORY(example)
ADD_SUBDIRECTORY(lib)
#
IF( "${check_depends}" STREQUAL "" )
	MESSAGE(FATAL_ERROR "no correctnes checks are available")
ENDIF( "${check_depends}" STREQUAL "" )
#
# Add the check target
ADD_CUSTOM_TARGET(check DEPENDS ${check_depends})
MESSAGE(STATUS "make check: available")
