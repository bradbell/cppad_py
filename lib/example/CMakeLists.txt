# -----------------------------------------------------------------------------
#         cppad_swig: A C++ Object Library and Swig Interface to Cppad
#          Copyright (C) 2017-17 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# -----------------------------------------------------------------------------
#
# List of *.xam files in relative to lib/xam directory
SET(xam_file_list
	a_double/cond_assign_xam.xam
	a_double/property_xam.xam
	a_double/unary_fun_xam.xam
	a_double/unary_op_xam.xam
	a_double/assign_xam.xam
	a_double/ad_binary_xam.xam
	a_double/compare_xam.xam
	vector/size_xam.xam
	vector/set_get_xam.xam
	a_fun/property_xam.xam
	a_fun/optimize_xam.xam
	a_fun/jacobian_xam.xam
	a_fun/hessian_xam.xam
	a_fun/forward_xam.xam
	a_fun/reverse_xam.xam
	a_fun/abort_xam.xam
	sparse/rc_xam.xam
	sparse/rcv_xam.xam
	sparse/jac_pattern_xam.xam
	sparse/hes_pattern_xam.xam
	sparse/jac_xam.xam
	sparse/hes_xam.xam
	error/message_xam.xam
)
#
# sub-directories for each language (add to check_lib_depend)
ADD_SUBDIRECTORY(cplusplus)
ADD_SUBDIRECTORY(python)
ADD_SUBDIRECTORY(octave)
ADD_SUBDIRECTORY(perl)
#
# Change check_lib_depends in parent environment
SET(check_lib_depends "${check_lib_depends}" PARENT_SCOPE)
