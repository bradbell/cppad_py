/* -----------------------------------------------------------------------------
           cppad_swig: A C++ Object Library and Swig Interface to CppAD
            Copyright (C) 2017-17 Bradley M. Bell (bradbell@seanet.com)
                This program is distributed under the terms of the
            GNU Affero General Public License version 3.0 or later see
                       http://www.gnu.org/licenses/agpl.txt
----------------------------------------------------------------------------- */
/* -----------------------------------------------------------------------------
           cppad_swig: A C++ Object Library and Swig Interface to CppAD
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
# include <cppad/swig/function.hpp>
%}

# ifdef SWIGPYTHON
%module py_cppad
# endif
# ifdef SWIGOCTAVE
%module m_cppad
# endif
# ifdef SWIGPERL
%module pl_cppad
# endif

%ignore  ptr;
%include "std_vector.i"
%include <cppad/swig/a_double.hpp>
%include <cppad/swig/a_fun.hpp>
%include <cppad/swig/function.hpp>

%template(vector_double) std::vector<double>;
%template(vector_ad)     std::vector<a_double>;

