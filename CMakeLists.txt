# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileCopyrightText: Bradley M. Bell <bradbell@seanet.com>
# SPDX-FileContributor: 2017-23 Bradley M. Bell
# ----------------------------------------------------------------------------
# cmake \
#  -D CMAKE_VERBOSE_MAKEFILE=value \
#  -D CMAKE_BUILD_TYPE=value \
#  -D cmake_install_prefix=value  \
#  -D extra_cxx_flags=value \
#  -D include_mixed=value \
#  ..
#
# -----------------------------------------------------------------------------
# preamble
# Suppress warnging that WIN32 not defined on cygwin
CMAKE_MINIMUM_REQUIRED(VERSION 3.5)
PROJECT(cppad_py)
SET(cppad_py_version "2024.8.15")
CMAKE_POLICY(SET CMP0042 NEW)
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
#  STRING, if the variable holds an arbitrary string.
#  PATH, if the variable holds a directory.
#  BOOL, if the variable only has the values true or false.
#
# ${description}: (in)
# Is a description of how the variable affects the CppAD install procedure.
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
# =============================================================================
# Comamnd Line Arguments
# =============================================================================
# cmake_install_prefix
IF ( cmake_install_prefix )
   IF( cmake_install_prefix MATCHES "^[^/].*" )
      SET(cmake_install_prefix "${CMAKE_SOURCE_DIR}/${cmake_install_prefix}")
   ENDIF( cmake_install_prefix MATCHES "^[^/].*" )
ENDIF ( cmake_install_prefix )
cmake_argument(cmake_install_prefix NOTFOUND PATH "prefix used to install CppAD" )
IF( NOT cmake_install_prefix )
   MESSAGE(FATAL_ERROR "cmake_install_prefix is not defined by cmake command line")
ENDIF( NOT cmake_install_prefix )
# -----------------------------------------------------------------------------
# extra_cxx_flags
cmake_argument(extra_cxx_flags "" STRING
   "Flags, added to CMAKE_CXX_FLAGS, used when compiling cppad_py code."
)
# -----------------------------------------------------------------------------
# include_mixed
cmake_argument(
   include_mixed FALSE BOOL "include the python cppad_mixed interface"
)
IF( include_mixed )
   SET(extra_cxx_flags "${extra_cxx_flags} -D INCLUDE_MIXED" )
ENDIF( include_mixed )
# =============================================================================
# Find Installed Packages Information
# =============================================================================
# make sure we have Swig available
FIND_PACKAGE(SWIG)
IF( SWIG_FOUND )
   MESSAGE(STATUS "Found swig ${SWIG_VERSION}")
ELSE( SWIG_FOUND )
   MESSAGE(FATAL_ERROR "Cannot find Swig")
ENDIF( SWIG_FOUND )
# -----------------------------------------------------------------------------
# find python
FIND_PACKAGE(Python COMPONENTS Interpreter Development)
IF ( Python_Interpreter_FOUND )
   print_variable(Python_INTERPRETER_ID)
   print_variable(Python_STDLIB)
   print_variable(Python_SITELIB)
ELSE ( Python_Interpreter_FOUND )
   MESSAGE(FATAL_ERROR "Cannot find python interpreter")
ENDIF ( Python_Interpreter_FOUND )
IF ( Python_Development_FOUND )
   print_variable(Python_LIBRARIES)
   print_variable(Python_INCLUDE_DIRS)
   INCLUDE_DIRECTORIES(${Python_INCLUDE_DIRS})
ELSE ( Python_Development_FOUND )
   MESSAGE(FATAL_ERROR "Cannot find python interpreter")
ENDIF ( Python_Development_FOUND )
# -----------------------------------------------------------------------------
# set pkg-config information about cppad_mixed
FIND_PACKAGE(PkgConfig)
pkg_check_modules( cppad QUIET cppad )
IF( cppad_FOUND )
   MESSAGE(STATUS "Found cppad.pc file")
ELSE( cppad_FOUND )
   MESSAGE(STATUS "Cannot find cppad.pc file")
   MESSAGE(FATAL_ERROR  "PKG_CONFIG_PATH=$ENV{PKG_CONFIG_PATH}")
ENDIF( cppad_FOUND )
INCLUDE_DIRECTORIES( ${cppad_INCLUDE_DIRS} )
LINK_DIRECTORIES( ${cppad_LIBRARY_DIRS} )
IF( include_mixed )
   pkg_check_modules( cppad_mixed QUIET cppad_mixed )
   IF( cppad_mixed_FOUND )
      MESSAGE(STATUS "Found cppad_mixed.pc file")
   ELSE( cppad_mixed_FOUND )
      MESSAGE(STATUS "Cannot find cppad_mixed.pc file")
      MESSAGE(FATAL_ERROR  "PKG_CONFIG_PATH=$ENV{PKG_CONFIG_PATH}")
   ENDIF( cppad_mixed_FOUND )
   INCLUDE_DIRECTORIES( ${cppad_mixed_INCLUDE_DIRS} )
   LINK_DIRECTORIES( ${cppad_mixed_LIBRARY_DIRS} )
ELSE( include_mixed )
   SET(cppad_mixed_LIBRARIES "")
ENDIF( include_mixed )
print_variable(cppad_mixed_LIBRARIES)
# -----------------------------------------------------------------------------
# print important system variables
print_variable(CMAKE_BINARY_DIR)
print_variable(CMAKE_VERBOSE_MAKEFILE)
print_variable(CMAKE_CXX_FLAGS)
print_variable(CMAKE_BUILD_TYPE)
# -----------------------------------------------------------------------------
# directory for including <cppad/py/cppad_py.hpp>
INCLUDE_DIRECTORIES( "${CMAKE_SOURCE_DIR}/include" )
# -----------------------------------------------------------------------------
# cxx_has_stdlib
# The message below about value of cxx_has_stdlib is used by old_setup.py
include(CheckCXXCompilerFlag)
CHECK_CXX_COMPILER_FLAG("-stdlib=libc++" cxx_has_stdlib)
IF( cxx_has_stdlib )
   SET(cxx_has_stdlib "true")
   SET(CMAKE_SHARED_LINKER_LFAGS "-stdlib=libc++")
   SET(extra_cxx_flags "${extra_cxx_flags} --stdlib=libc++")
ELSE( cxx_has_stdlib )
   SET(cxx_has_stdlib "false")
ENDIF( cxx_has_stdlib )
print_variable(cxx_has_stdlib)
# -----------------------------------------------------------------------------
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
# -----------------------------------------------------------------------------
# Incormation used by old_setup.py
FILE(WRITE "${CMAKE_BINARY_DIR}/cxx_has_stdlib"     "${cxx_has_stdlib}")
FILE(WRITE "${CMAKE_BINARY_DIR}/cmake_cxx_compiler" "${CMAKE_CXX_COMPILER}")
# -----------------------------------------------------------------------------
