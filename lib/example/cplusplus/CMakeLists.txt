# -----------------------------------------------------------------------------
#         cppad_py: A C++ Object Library and Python Interface to Cppad
#          Copyright (C) 2017-18 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# -----------------------------------------------------------------------------
# list of C++ source files in CMAKE_CURRENT_SOURCE_DIR
FILE(GLOB cplusplus_source_list "*.cpp")
#
# lib_cplusplus_check_all
ADD_EXECUTABLE(lib_cplusplus_check_all
	EXCLUDE_FROM_ALL ${cplusplus_source_list}
)
# additional flags for compiling cppad code
SET_TARGET_PROPERTIES(
	lib_cplusplus_check_all PROPERTIES COMPILE_FLAGS "${cppad_cxx_flags}"
)
# link in cppad_py library
TARGET_LINK_LIBRARIES(lib_cplusplus_check_all cppad_py_lib)
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
