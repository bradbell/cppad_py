/* -----------------------------------------------------------------------------
           cppad_swig: A C++ Object Library and Swig Interface to Cppad
            Copyright (C) 2017-17 Bradley M. Bell (bradbell@seanet.com)
                This program is distributed under the terms of the
            GNU Affero General Public License version 3.0 or later see
                       http://www.gnu.org/licenses/agpl.txt
----------------------------------------------------------------------------- */
# include <cppad/cppad.hpp>
# include <cppad/swig/function.hpp>

namespace cppad_swig { // BEGIN_CPPAD_SWIG_NAMESPACE

// independent is a friend for ad_double
std::vector<a_double> independent(const std::vector<double>& x)
{	using CppAD::AD;
	size_t n = x.size();
	CppAD::vector< AD<double> > ax(n);
	for(size_t j = 0; j < n; j++)
		ax[j] = x[j];
	CppAD::Independent(ax);
	std::vector<a_double> result(n);
	for(size_t j = 0; j < n; j++)
		result[j] = a_double( &ax[j] );
	return result;
}

// abort_recording
void abort_recording(void)
{	CppAD::AD<double>::abort_recording();
}

} // END_CPPAD_SWIG_NAMESPACE
