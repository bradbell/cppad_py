// $Id$
# ifndef CPPAD_SWIG_FUNCTION_HPP
# define CPPAD_SWIG_FUNCTION_HPP
/* -----------------------------------------------------------------------------
           cppad_swig: A C++ Object Library and SWIG Interface to CppAD
            Copyright (C) 2017-17 Bradley M. Bell (bradbell@seanet.com)
                This program is distributed under the terms of the
            GNU Affero General Public License version 3.0 or later see
                       http://www.gnu.org/licenses/agpl.txt
----------------------------------------------------------------------------- */
# include <vector>
# include <cppad/swig/a_double.hpp>

// independent
std::vector<a_double> independent(const std::vector<double>& x);

// abort_recording
void abort_recording(void);

# endif
