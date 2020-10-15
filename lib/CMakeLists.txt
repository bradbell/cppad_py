# -----------------------------------------------------------------------------
#         cppad_py: A C++ Object Library and Python Interface to Cppad
#          Copyright (C) 2017-20 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# -----------------------------------------------------------------------------
# used cmake --help-policy CMP<nnnn> to get description of each policy
#
# Initialize check for this directory
SET(check_lib_depends "")
#
# directory used for swig.include files
INCLUDE_DIRECTORIES( ${CMAKE_SOURCE_DIR}/include )
INCLUDE_DIRECTORIES( ${CMAKE_CURRENT_BINARY_DIR} )
#
# The following enables cmake to handle windows dlls; see
# https://cmake.org/Wiki/BuildingWinDLL
include (GenerateExportHeader)
#
# _cppad_swig
# assume that swig has run with c++ output in ${CMAKE_CURRENT_BINARY_DIR}
ADD_LIBRARY(_cppad_swig SHARED
    cplusplus/a_double.cpp
    cplusplus/fun.cpp
    cplusplus/sparse.cpp
    cplusplus/convert_vec.cpp
    cplusplus/mixed.cpp
    ${CMAKE_CURRENT_BINARY_DIR}/cppad_py_swigPYTHON_wrap.cxx
)
SET_TARGET_PROPERTIES(
    _cppad_swig PROPERTIES COMPILE_FLAGS "${extra_cxx_flags}"
)
#
# libraries that cppad_swig depends on
TARGET_LINK_LIBRARIES(_cppad_swig
    cppad_lib
    cppad_mixed
    ipopt
    cholmod
    gsl
    ${Python_LIBRARIES}
)
#
# The file cppad_swig_export.h, in the current binary directory, will
# define the symbol CPPAD_PY_LIB_PUBLIC. This symbol should be used to
# export cppad_swig, when it is being compiled, and import it when
# cppad_swig is being linked.
GENERATE_EXPORT_HEADER(_cppad_swig
    BASE_NAME           cppad_swig
    EXPORT_MACRO_NAME   CPPAD_PY_LIB_PUBLIC
    EXPORT_FILE_NAME    cppad_swig_export.h
    STATIC_DEFINE       CPPAD_PY_LIB_BUILT_AS_STATIC
)
#
IF( NOT( "${check_lib_depends}" STREQUAL "" ) )
    # Add the check target
    ADD_CUSTOM_TARGET(check_lib DEPENDS ${check_lib_depends})
    MESSAGE(STATUS "make check_lib: available")
    #
    # Change check depends in parent environment
    add_to_list(check_depends check_lib )
    SET(check_depends "${check_depends}" PARENT_SCOPE)
ENDIF( NOT( "${check_lib_depends}" STREQUAL "" ) )
