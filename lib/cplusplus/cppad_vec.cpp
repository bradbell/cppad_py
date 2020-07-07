/* -----------------------------------------------------------------------------
           cppad_py: A C++ Object Library and Python Interface to Cppad
            Copyright (C) 2017-20 Bradley M. Bell (bradbell@seanet.com)
                This program is distributed under the terms of the
                GNU General Public License version 3.0 or later see
                      https://www.gnu.org/licenses/gpl-3.0.txt
----------------------------------------------------------------------------- */
# include <cppad/cppad.hpp>
# include <cppad/py/a_double.hpp>
namespace cppad_py { // BEGIN_CPPAD_PY_NAMESPACE
/*
-------------------------------------------------------------------------------
$begin vec2cppad_double$$
$spell
	CppAD
	cppad
	py
	vec
$$

$section Convert an a_double Vector to a CppAD::AD<double> Vector$$

$head Syntax$$
$icode%v_out% = cppad_py::vec2cppad_double%(%v_in%)
%$$

$head Prototype$$
$srcthisfile%
	0%// BEGIN_VEC2CPPAD_DOUBLE%// END_VEC2CPPAD_DOUBLE%1
%$$

-------------------------------------------------------------------------------
$end
*/

// BEGIN_VEC2CPPAD_DOUBLE
std::vector< CppAD::AD<double> >
vec2cppad_double(const std::vector<a_double>& v_in )
// END_VEC2CPPAD_DOUBLE
{	std::vector< CppAD::AD<double> > v_out( v_in.size() );
	for(size_t i = 0; i < v_in.size(); ++i)
		v_out[i] = *( v_in[i].ptr() );
	return v_out;
}
/*
-------------------------------------------------------------------------------
$begin vec2a_double$$
$spell
	CppAD
	cppad
	py
	vec
$$

$section Convert a CppAD::AD<double> Vector to an a_double Vector$$

$head Syntax$$
$icode%v_out% = cppad_py::vec2a_double%(%v_in%)
%$$

$head Prototype$$
$srcthisfile%
	0%// BEGIN_VEC2A_DOUBLE%// END_VEC2A_DOUBLE%1
%$$

$end
-------------------------------------------------------------------------------
*/

// BEGIN_VEC2A_DOUBLE
std::vector<a_double>
vec2a_double(const std::vector< CppAD::AD<double> >& v_in )
// END_VEC2A_DOUBLE
{	std::vector<a_double> v_out( v_in.size() );
	for(size_t i = 0; i < v_in.size(); ++i)
		*(v_out[i].ptr()) = v_in[i];
	return v_out;
}

// ----------------------------------------------------------------------------
} // END_CPPAD_PY_NAMESPACE
