/* -----------------------------------------------------------------------------
           cppad_swig: A C++ Object Library and Swig Interface to Cppad
            Copyright (C) 2017-17 Bradley M. Bell (bradbell@seanet.com)
                This program is distributed under the terms of the
            GNU Affero General Public License version 3.0 or later see
                       http://www.gnu.org/licenses/agpl.txt
----------------------------------------------------------------------------- */
/* -----------------------------------------------------------------------------
           cppad_swig: A C++ Object Library and Swig Interface to Cppad
            Copyright (C) 2017-17 Bradley M. Bell (bradbell@seanet.com)
                This program is distributed under the terms of the
            GNU Affero General Public License version 3.0 or later see
                       http://www.gnu.org/licenses/agpl.txt
----------------------------------------------------------------------------- */
/* cppad_swig.i */
# ifdef SWIG
# define CPPAD_SWIG_LIB_PUBLIC
# else
# include <cppad_swig_lib_export.h>
# endif


%{
# include <cppad/swig/a_double.hpp>
# include <cppad/swig/a_fun.hpp>
# include <cppad/swig/typedef.hpp>
%}

# ifdef SWIGPYTHON
%module py_cppad
# endif
# ifdef SWIGOCTAVE
%module m_cppad
# endif
# ifdef SWIGPERL
%module pm_cppad
# endif

%ignore  ptr;
%include "std_vector.i"
%include <cppad/swig/a_double.hpp>
%include <cppad/swig/a_fun.hpp>

%template(vector_double) std::vector<double>;
%template(vector_ad)     std::vector<cppad_swig::a_double>;


/*
-------------------------------------------------------------------------------
$begin a_double$$

$section The a_double Class$$

$childtable%lib/a_double.cpp%$$

$end
-------------------------------------------------------------------------------
$begin vector$$
$spell
	Cppad
$$

$section Cppad Swig Vectors$$

$childtable%lib/vector.omh%$$

$end
-------------------------------------------------------------------------------
$begin a_fun$$
$spell
	Cppad
$$

$section Algorithmic Functions$$

$childtable%lib/a_fun.cpp%$$

$end
-------------------------------------------------------------------------------
*/
