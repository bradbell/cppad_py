# ifndef CPPAD_SWIG_FUNCTION_HPP
# define CPPAD_SWIG_FUNCTION_HPP
/* -----------------------------------------------------------------------------
           cppad_swig: A C++ Object Library and Swig Interface to Cppad
            Copyright (C) 2017-17 Bradley M. Bell (bradbell@seanet.com)
                This program is distributed under the terms of the
            GNU Affero General Public License version 3.0 or later see
                       http://www.gnu.org/licenses/agpl.txt
----------------------------------------------------------------------------- */
# include <vector>
# include <cppad/swig/a_double.hpp>
# ifdef SWIG
#	define CPPAD_SWIG_LIB_PUBLIC
# else
#	include <cppad_swig_lib_export.h>
# endif

namespace cppad_swig { // BEGIN_CPPAD_SWIG_NAMESPACE

// independent
CPPAD_SWIG_LIB_PUBLIC
std::vector<a_double> independent(const std::vector<double>& x);

// abort_recording
CPPAD_SWIG_LIB_PUBLIC
void abort_recording(void);

} // END_CPPAD_SWIG_NAMESPACE

# endif
