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
	STRING(REGEX REPLACE "[.]xam" ".cpp" source_file ${xam_file})
	STRING(REGEX REPLACE "/"      "_"    source_file ${source_file})
	ADD_CUSTOM_COMMAND(
		OUTPUT ${CMAKE_CURRENT_BINARY_DIR}/${source_file}
		COMMAND ${m4_executable}
		-D Language_=cplusplus
		-I ${CMAKE_SOURCE_DIR}/lib/xam
		${CMAKE_SOURCE_DIR}/lib/xam/${xam_file}
		> ${CMAKE_CURRENT_BINARY_DIR}/${source_file}
		DEPENDS
		${CMAKE_SOURCE_DIR}/lib/xam/${xam_file}
		${CMAKE_SOURCE_DIR}/lib/xam/cplusplus.m4
	)
	add_to_list(auto_output_list ${CMAKE_CURRENT_BINARY_DIR}/${source_file} )
ENDFOREACH( xam_file ${xam_file_list} )
ADD_CUSTOM_TARGET(auto_lib_cplusplus DEPENDS ${auto_output_list} )
MESSAGE(STATUS "make auto_lib_cplusplus: available")
# -----------------------------------------------------------------------------
# lib_cplusplus_check_all
ADD_EXECUTABLE(lib_cplusplus_check_all EXCLUDE_FROM_ALL
	check_all.cpp ${auto_output_list}
)
# additional flags for compiling cppad code
SET_TARGET_PROPERTIES(
	lib_cplusplus_check_all PROPERTIES COMPILE_FLAGS "${cppad_cxx_flags}"
)
# link in cppad_swig library
TARGET_LINK_LIBRARIES(lib_cplusplus_check_all cppad_swig_lib)
#
# check_lib_cplusplus
ADD_CUSTOM_TARGET(check_lib_cplusplus
	lib_cplusplus_check_all
	DEPENDS lib_cplusplus_check_all
)
MESSAGE(STATUS "make check_lib_cplusplus: available")

# Change check depends in parent environment
add_to_list(check_lib_depends check_lib_cplusplus)
SET(check_lib_depends "${check_lib_depends}" PARENT_SCOPE)
