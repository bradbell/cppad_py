# -----------------------------------------------------------------------------
#         cppad_swig: A C++ Object Library and Swig Interface to Cppad
#          Copyright (C) 2017-17 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#          GNU Affero General Public License version 3.0 or later see
#                     http://www.gnu.org/licenses/agpl.txt
# -----------------------------------------------------------------------------
assert(m4_executable)
#
# List of automatically generated source files
SET(auto_list
	a_double_xam.pm
	a_fun_xam.pm
	vector_ad_xam.pm
	vector_double_xam.pm
)
SET(auto_output_list "")
FOREACH( xam_file ${xam_file_list} )
	STRING(REGEX REPLACE "[.]xam" ".pm" source_file ${xam_file})
	STRING(REGEX REPLACE "/"      "_"   source_file ${source_file})
	ADD_CUSTOM_COMMAND(
		OUTPUT ${CMAKE_CURRENT_BINARY_DIR}/${source_file}
		COMMAND ${m4_executable}
		-D language_=perl
		-I ${CMAKE_SOURCE_DIR}/lib/xam
		${CMAKE_SOURCE_DIR}/lib/xam/${xam_file}
		> ${CMAKE_CURRENT_BINARY_DIR}/${source_file}
	)
	add_to_list(auto_output_list ${CMAKE_CURRENT_BINARY_DIR}/${source_file} )
ENDFOREACH( xam_file ${xam_file_list} )
ADD_CUSTOM_TARGET(auto_lib_perl DEPENDS ${auto_output_list} )
MESSAGE(STATUS "make auto_lib_perl: available")
#
# ----------------------------------------------------------------------------
assert( SWIG_FOUND )
FIND_PACKAGE(PerlLibs)
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

	# Swig Perl warns that it does not support *=, or /=,
	# supress these warnings.
	SET(CMAKE_SWIG_FLAGS -Wextra -w367,368 )

	# include directory determined by find PerlLibs
	INCLUDE_DIRECTORIES( SYSTEM ${PERL_INCLUDE_PATH})

	# SWIG_ADD_MODULE(name language [ files ])
	SWIG_ADD_MODULE(pm_cppad perl ${swig_control_file} )

	# SWIG_LINK_LIBRARIES(name [ libraries ])
	SWIG_LINK_LIBRARIES(pm_cppad cppad_swig_lib ${PYTHON_LIBRARIES})

	# additional flags for compiling Swig wrapper
	SET_TARGET_PROPERTIES( ${SWIG_MODULE_pm_cppad_REAL_NAME}
		 PROPERTIES COMPILE_FLAGS "${swig_cxx_flags}"
	)

	# check_lib_perl
	ADD_CUSTOM_TARGET(check_lib_perl
		perl check_all.pl
		DEPENDS
		${SWIG_MODULE_pm_cppad_REAL_NAME}
		${CMAKE_CURRENT_BINARY_DIR}/check_all.pl
		auto_lib_perl
	)
	MESSAGE(STATUS "make check_lib_perl: available")

	# Change check depends in parent environment
	add_to_list(check_lib_depends check_lib_perl)
	SET(check_lib_depends "${check_lib_depends}" PARENT_SCOPE)

ENDIF ( PERLLIBS_FOUND )
