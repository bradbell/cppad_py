# $Id$
# -----------------------------------------------------------------------------
#         cppad_swig: A C++ Object Library and SWIG Interface to CppAD
#          Copyright (C) 2017-17 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#          GNU Affero General Public License version 3.0 or later see
#                     http://www.gnu.org/licenses/agpl.txt
# -----------------------------------------------------------------------------
options(echo = FALSE)
# Turn R echo off (for R CMD BATCH execution)
#
# load the module
swig_module = 'swig_example'
dyn.load( paste( swig_module, .Platform$dynlib.ext, sep='') )
source( paste( swig_module, '.R', sep='') )
cacheMetaData(1)
#
# initialize error count
error_count = 0
# --------------------------------------------
# factorial_by_val
if( factorial_by_val(4) == 24 ) {
	write( 'factorial_by_val: OK', stdout() )
} else {
	write( 'factorial_by_val: Error', stdout() )
	error_count = error_count + 1
}
# ---------------------------------------------
# message_of_void
if( message_of_void() == 'OK' ) {
    write( 'message_of_void: OK', stdout() )
} else {
    write( 'message_of_void: Error', stdout() )
	error_count = error_count + 1
}
# ---------------------------------------------
# return error_count
quit(save = 'no', status = error_count, runLast = FALSE)
EOF
