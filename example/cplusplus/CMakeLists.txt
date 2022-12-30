# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileCopyrightText: Bradley M. Bell <bradbell@seanet.com>
# SPDX-FileContributor: 2017-22 Bradley M. Bell
# ----------------------------------------------------------------------------
# list of C++ source files in CMAKE_CURRENT_SOURCE_DIR
FILE(GLOB cplusplus_source_list "*.cpp")
#
# example_cplusplus_check_all
ADD_EXECUTABLE(example_cplusplus_check_all
   EXCLUDE_FROM_ALL ${cplusplus_source_list}
)
# additional flags for compiling cppad code
SET_TARGET_PROPERTIES(
   example_cplusplus_check_all PROPERTIES COMPILE_FLAGS "${extra_cxx_flags}"
)
# link in cppad_py and cppad_lib libraries
TARGET_LINK_LIBRARIES(
   example_cplusplus_check_all
   _cppad_swig
)
#
# check_example_cplusplus
ADD_CUSTOM_TARGET(check_example_cplusplus
   example_cplusplus_check_all
   DEPENDS example_cplusplus_check_all
)
MESSAGE(STATUS "make check_example_cplusplus: available")

# Change check depends in parent environment
add_to_list(check_example_depends check_example_cplusplus)
SET(check_example_depends "${check_example_depends}" PARENT_SCOPE)
