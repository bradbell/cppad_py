# -----------------------------------------------------------------------------
#         cppad_swig: A C++ Object Library and SWIG Interface to CppAD
#          Copyright (C) 2017-17 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#          GNU Affero General Public License version 3.0 or later see
#                     http://www.gnu.org/licenses/agpl.txt
# -----------------------------------------------------------------------------
assert( SWIG_FOUND )
FIND_PACKAGE(PerlLibs)
# ----------------------------------------------------------------------------
IF ( PERLLIBS_FOUND )
	# create check_all.pl for this directory
	CONFIGURE_FILE(
		${CMAKE_CURRENT_SOURCE_DIR}/check_all.pl.in
		${CMAKE_CURRENT_BINARY_DIR}/check_all.pl
	)

	# treat like a C++ files
	SET_SOURCE_FILES_PROPERTIES(
		${swig_control_file} PROPERTIES CPLUSPLUS ON
	)

	# swig -perl warns that it does not support *=, or /=,
	# supress these warnings.
	SET(CMAKE_SWIG_FLAGS -Wextra -w367,368 )

	# include directory determined by find PerlLibs
	INCLUDE_DIRECTORIES( SYSTEM ${PERL_INCLUDE_PATH})

	# SWIG_ADD_MODULE(name language [ files ])
	SWIG_ADD_MODULE(pl_cppad perl ${swig_control_file} )

	# SWIG_LINK_LIBRARIES(name [ libraries ])
	SWIG_LINK_LIBRARIES(pl_cppad cppad_swig_lib ${PYTHON_LIBRARIES})

	# check_lib_perl
	ADD_CUSTOM_TARGET(check_lib_perl
		perl check_all.pl
		DEPENDS
		${SWIG_MODULE_pl_cppad_REAL_NAME}
		${CMAKE_CURRENT_BINARY_DIR}/check_all.pl
	)
	MESSAGE(STATUS "make check_lib_perl: available")

	# Change check depends in parent environment
	add_to_list(check_lib_depends check_lib_perl)
	SET(check_lib_depends "${check_lib_depends}" PARENT_SCOPE)

ENDIF ( PERLLIBS_FOUND )
