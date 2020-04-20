# -----------------------------------------------------------------------------
#         cppad_py: A C++ Object Library and Python Interface to Cppad
#          Copyright (C) 2017-20 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# -----------------------------------------------------------------------------
#
# initialize check_depends
SET(check_example_depends "")
#
# sub-directories for C++ and Python
ADD_SUBDIRECTORY(cplusplus)
#
ADD_CUSTOM_TARGET(check_example "" DEPENDS ${check_example_depends})
MESSAGE(STATUS "make check_example: available")
#
# Change check_example_depends in parent environment
add_to_list(check_depends check_example)
SET(check_depends "${check_depends}" PARENT_SCOPE)
