# -----------------------------------------------------------------------------
#         cppad_swig: A C++ Object Library and SWIG Interface to CppAD
#          Copyright (C) 2017-17 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#          GNU Affero General Public License version 3.0 or later see
#                     http://www.gnu.org/licenses/agpl.txt
# -----------------------------------------------------------------------------
# initialize check_example_depends
SET(check_example_depends "")
#
ADD_SUBDIRECTORY(python)
ADD_SUBDIRECTORY(octave)
ADD_SUBDIRECTORY(perl)
#
IF( NOT( "${check_example_depends}" STREQUAL "" ) )
	#
	# Add the check_example target
	ADD_CUSTOM_TARGET(check_example DEPENDS ${check_example_depends})
	MESSAGE(STATUS "make check_example: available")
	#
	# Change check depends in parent environment
	SET(check_depends ${check_depends} check_example PARENT_SCOPE)
	#
ENDIF( NOT( "${check_example_depends}" STREQUAL "" ) )
