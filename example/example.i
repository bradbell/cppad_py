/* -----------------------------------------------------------------------------
           cppad_swig: A C++ Object Library and SWIG Interface to CppAD
            Copyright (C) 2017-17 Bradley M. Bell (bradbell@seanet.com)
                This program is distributed under the terms of the
            GNU Affero General Public License version 3.0 or later see
                       http://www.gnu.org/licenses/agpl.txt
----------------------------------------------------------------------------- */
/*
$begin example.i$$
$spell
	hpp
	py
	ifdef
	endif
	Perl
	cpointer
	ptr
	carrays
	std
$$

$section Swig Input File example.i$$

$children%
	example/python/check_py_example.py
%$$

$head C++ Includes$$
This include file defines the interface to the C++ object library.
$codep */
%{
# include "example.hpp"
%}
/* $$

$head py_example$$
This is the name of the Python Swig interface to the C++ library.
$codep */
# ifdef SWIGPYTHON
%module py_example
# endif
/*$$
see $cref check_py_example.py$$.

$head m_example$$
This is the name of the Octave Swig interface to the C++ library.
$codep */
# ifdef SWIGOCTAVE
%module m_example
# endif
/*$$

$head pl_example$$
This is the name of the Perl Swig interface to the C++ library.
$codep */
# ifdef SWIGPERL
%module pl_example
# endif
/* $$

$head int_class$$
This is a Swig interface to a an integer value.
$codep */
%include "cpointer.i"
%pointer_class(int, int_class);
/* $$

$head int_array_ptr$$
This is a Swig interface to a pointer to an array of integer values.
$codep */
%include "carrays.i"
%array_functions(int, int_array_ptr);
%array_class(int, int_array_class);
/* $$

$head double_class$$
This is a Swig interface to a $codei%template_class<%Type%>%$$
where $cref/Type/example_template_class/Type/$$ is $code double$$.
$codep */
%include "example.hpp"
%template(double_class)  template_class<double>;
/* $$

$head vector_double$$
This is a Swig interface to a $codei%std::vector<%Type%>%$$
where $icode Type$$ is $code double$$.
$codep */
%include "std_vector.i"
%template(vector_double) std::vector<double>;
/* $$
$end
*/

