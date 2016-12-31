/* -----------------------------------------------------------------------------
           cppad_swig: A C++ Object Library and SWIG Interface to CppAD
            Copyright (C) 2017-17 Bradley M. Bell (bradbell@seanet.com)
                This program is distributed under the terms of the
            GNU Affero General Public License version 3.0 or later see
                       http://www.gnu.org/licenses/agpl.txt
----------------------------------------------------------------------------- */
/* swig_example.i */
%{
# include "swig_example.hpp"
%}

# ifdef SWIGPYTHON
%module py_example
# endif
# ifdef SWIGOCTAVE
%module m_example
# endif
# ifdef SWIGPERL
%module pl_example
# endif


%include "cpointer.i"
%pointer_class(int, int_class);

%include "carrays.i"
%array_functions(int, int_array_ptr);
%array_class(int, int_array_class);

%include "std_vector.i"

%include "swig_example.hpp"

%template(double_class)  template_class<double>;
%template(vector_double) std::vector<double>;
