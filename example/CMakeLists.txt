# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileCopyrightText: Bradley M. Bell <bradbell@seanet.com>
# SPDX-FileContributor: 2017-22 Bradley M. Bell
# ----------------------------------------------------------------------------
#
# initialize check_depends
SET(check_example_depends "")
#
# sub-directories for C++ and Python
ADD_SUBDIRECTORY(cplusplus)
ADD_SUBDIRECTORY(python)
#
ADD_CUSTOM_TARGET(check_example "" DEPENDS ${check_example_depends})
MESSAGE(STATUS "make check_example: available")
#
# Change check_example_depends in parent environment
add_to_list(check_depends check_example)
SET(check_depends "${check_depends}" PARENT_SCOPE)
