# -----------------------------------------------------------------------------
#         cppad_swig: A C++ Object Library and Swig Interface to Cppad
#          Copyright (C) 2017-17 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# -----------------------------------------------------------------------------
# initialize check_swig_xam_depends
SET(check_swig_xam_depends "")
#
ADD_SUBDIRECTORY(python)
ADD_SUBDIRECTORY(octave)
ADD_SUBDIRECTORY(perl)
#
IF( NOT( "${check_swig_xam_depends}" STREQUAL "" ) )
	#
	# Add the check_swig_xam target
	ADD_CUSTOM_TARGET(check_swig_xam DEPENDS ${check_swig_xam_depends})
	MESSAGE(STATUS "make check_swig_xam: available")
	#
	# Change check depends in parent environment
	SET(check_depends ${check_depends} check_swig_xam PARENT_SCOPE)
	#
ENDIF( NOT( "${check_swig_xam_depends}" STREQUAL "" ) )
