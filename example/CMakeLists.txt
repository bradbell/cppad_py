# -----------------------------------------------------------------------------
#         cppad_py: A C++ Object Library and Python Interface to Cppad
#          Copyright (C) 2017-18 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# -----------------------------------------------------------------------------
#
# sub-directories for C++ and Python
ADD_SUBDIRECTORY(cplusplus)
#
# Change check_lib_depends in parent environment
SET(check_lib_depends "${check_lib_depends}" PARENT_SCOPE)
