# -----------------------------------------------------------------------------
#         cppad_py: A C++ Object Library and Python Interface to Cppad
#          Copyright (C) 2017-20 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# -----------------------------------------------------------------------------
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
    cppad_swig
    ${cppad_lib_path}
    ${PYTHON_LIBRARIES}
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
