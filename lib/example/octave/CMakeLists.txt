# -----------------------------------------------------------------------------
#         cppad_swig: A C++ Object Library and Swig Interface to Cppad
#          Copyright (C) 2017-17 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#          GNU Affero General Public License version 3.0 or later see
#                     http://www.gnu.org/licenses/agpl.txt
# -----------------------------------------------------------------------------
assert(m4_executable)
#
SET(auto_output_list "")
FOREACH( xam_file ${xam_file_list} )
	STRING(REGEX REPLACE "[.]xam" ".m" source_file ${xam_file})
	STRING(REGEX REPLACE "/"      "_"  source_file ${source_file})
	ADD_CUSTOM_COMMAND(
		OUTPUT ${CMAKE_CURRENT_BINARY_DIR}/${source_file}
		COMMAND ${m4_executable}
		-D Language_=octave
		-I ${CMAKE_SOURCE_DIR}/lib/xam
		${CMAKE_SOURCE_DIR}/lib/xam/${xam_file}
		> ${CMAKE_CURRENT_BINARY_DIR}/${source_file}
		DEPENDS
		${CMAKE_SOURCE_DIR}/lib/xam/${xam_file}
		${CMAKE_SOURCE_DIR}/lib/xam/octave.m4
	)
	add_to_list(auto_output_list ${CMAKE_CURRENT_BINARY_DIR}/${source_file} )
ENDFOREACH( xam_file ${xam_file_list} )
ADD_CUSTOM_TARGET(auto_lib_octave DEPENDS ${auto_output_list} )
MESSAGE(STATUS "make auto_lib_octave: available")
#
# -----------------------------------------------------------------------------
assert( SWIG_FOUND )
FIND_PROGRAM(octave_config NAMES octave-config)
IF( octave_config )
	ADD_CUSTOM_COMMAND(
		OUTPUT ${CMAKE_CURRENT_BINARY_DIR}/check_all.m
		COMMAND
		${CMAKE_COMMAND} -E copy
		${CMAKE_CURRENT_SOURCE_DIR}/check_all.m
		${CMAKE_CURRENT_BINARY_DIR}/check_all.m
	)
	# treat like a C++ files
	SET_SOURCE_FILES_PROPERTIES(
		${swig_control_file} PROPERTIES CPLUSPLUS ON
	)

	# Swig Octave warns that it does not support +=, -=, *=, or /=,
	# (but is does and the code works) so supress these warnings.
	# 2DO: Ask swig mailing list what is going on here.
	SET(CMAKE_SWIG_FLAGS -Wextra -w365,366,367,368 )

	# Octave include directories
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

	# Octave library dcirectories
	EXECUTE_PROCESS(
		COMMAND ${octave_config} -p OCTLIBDIR
		OUTPUT_VARIABLE  octave_library_dirs
		OUTPUT_STRIP_TRAILING_WHITESPACE
	)

	# liboctinterp
	FIND_LIBRARY(octave_liboctinterp
		NAMES octinterp liboctinterp
		PATHS "${octave_library_dirs}"
	)

	# liboctave
	FIND_LIBRARY(octave_liboctave
		NAMES octave liboctave
		PATHS "${octave_library_dirs}"
	)

	# include directory determined by find octive-config
	INCLUDE_DIRECTORIES( SYSTEM ${octave_include_dirs})

	# SWIG_ADD_MODULE(name language [ files ])
	SWIG_ADD_MODULE(m_cppad octave ${swig_control_file} )

	# SWIG_LINK_LIBRARIES(name [ libraries ])
	SWIG_LINK_LIBRARIES(m_cppad
		cppad_swig_lib ${octave_liboctinterp} ${octave_liboctave}
	)

	# additional flags for compiling Swig wrapper
	SET_TARGET_PROPERTIES( ${SWIG_MODULE_m_cppad_REAL_NAME}
		 PROPERTIES COMPILE_FLAGS "${swig_cxx_flags}"
	)

	# check_lib_octave
	ADD_CUSTOM_TARGET(check_lib_octave
		octave check_all.m
		DEPENDS
		${SWIG_MODULE_m_cppad_REAL_NAME}
		${CMAKE_CURRENT_BINARY_DIR}/check_all.m
		auto_lib_octave
	)
	MESSAGE(STATUS "make check_lib_octave: available")

	# Change check depends in parent environment
	add_to_list(check_lib_depends check_lib_octave)
	SET(check_lib_depends "${check_lib_depends}" PARENT_SCOPE)

ENDIF( octave_config )
