# -----------------------------------------------------------------------------
#         cppad_swig: A C++ Object Library and Swig Interface to Cppad
#          Copyright (C) 2017-17 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#          GNU Affero General Public License version 3.0 or later see
#                     http://www.gnu.org/licenses/agpl.txt
# -----------------------------------------------------------------------------
#
# lib_cplusplus_check_all
ADD_EXECUTABLE(lib_cplusplus_check_all EXCLUDE_FROM_ALL
	a_double_xam.cpp
	a_fun_xam.cpp
	check_all.cpp
	vector_ad_xam.cpp
	vector_double_xam.cpp
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
