# -----------------------------------------------------------------------------
#         cppad_swig: A C++ Object Library and Swig Interface to Cppad
#          Copyright (C) 2017-17 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#          GNU Affero General Public License version 3.0 or later see
#                     http://www.gnu.org/licenses/agpl.txt
# -----------------------------------------------------------------------------
FIND_PACKAGE(SWIG)
FIND_PROGRAM(octave_config NAMES octave-config)
IF( SWIG_FOUND AND octave_config )
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
	# get Octave include directories
	EXECUTE_PROCESS(
		COMMAND ${octave_config} -p OCTINCLUDEDIR
		OUTPUT_VARIABLE  octave_include_dirs
		OUTPUT_STRIP_TRAILING_WHITESPACE
	)
	# unix style paths
	STRING(REGEX REPLACE
		"/octave$" "" octave_include_dirs ${octave_include_dirs}
	)
	# windows styple paths
	STRING(REGEX REPLACE
		"\\octave$" "" octave_include_dirs ${octave_include_dirs}
	)
	#
	# Octave library directories
	EXECUTE_PROCESS(
		COMMAND ${octave_config} -p OCTLIBDIR
		OUTPUT_VARIABLE  octave_library_dirs
		OUTPUT_STRIP_TRAILING_WHITESPACE
	)
	#
	# liboctinterp
	FIND_LIBRARY(octave_liboctinterp
		NAMES octinterp liboctinterp
		PATHS "${octave_library_dirs}"
	)
	#
	# liboctave
	FIND_LIBRARY(octave_liboctave
		NAMES octave liboctave
		PATHS "${octave_library_dirs}"
	)
	#
	# include directory determined by find octive-config
	# (treat like system include files to suppress warnings)
	INCLUDE_DIRECTORIES( SYSTEM ${octave_include_dirs})
	#
	# SWIG_ADD_MODULE(name language [ files ])
	SET(module_files ../swig_xam.i ../function.cpp ../normal_class.cpp)
	SWIG_ADD_MODULE(m_swig_xam octave ${module_files})
	#
	# SWIG_LINK_LIBRARIES(name [ libraries ])
	SWIG_LINK_LIBRARIES(m_swig_xam
		${octave_liboctinterp} ${octave_liboctave}
	)
	#
	# additional flags for compiling Swig wrapper
	SET_TARGET_PROPERTIES( ${SWIG_MODULE_m_swig_xam_REAL_NAME}
		 PROPERTIES COMPILE_FLAGS "${swig_cxx_flags}"
	)
	#
	# copy check_swig_xam.m from source to binary directory
	ADD_CUSTOM_TARGET(check_swig_xam_m
		"${CMAKE_COMMAND}" -E copy
		"${CMAKE_CURRENT_SOURCE_DIR}/check_swig_xam.m"
		"${CMAKE_CURRENT_BINARY_DIR}/check_swig_xam.m"
		DEPENDS
		"${CMAKE_CURRENT_SOURCE_DIR}/check_swig_xam.m"
	)
	# check_swig_xam_octave
	ADD_CUSTOM_TARGET(check_swig_xam_octave
		octave check_swig_xam.m
		DEPENDS ${SWIG_MODULE_m_swig_xam_REAL_NAME} check_swig_xam_m
	)
	MESSAGE(STATUS "make check_swig_xam_octave: available")
	#
	# add this check to list of checks for parent directory
	SET(check_swig_xam_depends
		${check_swig_xam_depends} check_swig_xam_octave PARENT_SCOPE
	)
	#
ENDIF( SWIG_FOUND AND octave_config )
