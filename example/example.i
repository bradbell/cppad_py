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

$section A Simple Example for Using Swig with C++$$

$childtable%
	example/python/check_py_example.py%
	example/octave/check_m_example.m%
	example/perl/check_pl_example.pl%
	example/example_lib.omh
%$$

$head C++ Includes$$
This include file defines the interface to the C++ object library.
$codep */
%{
# include "example.hpp"
%}
/* $$
see $cref example_lib$$.

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
see $cref check_m_example.m$$.

$head pl_example$$
This is the name of the Perl Swig interface to the C++ library.
$codep */
# ifdef SWIGPERL
%module pl_example
# endif
/* $$
see $cref check_pl_example.pl$$.

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
/* $$

$head int_array_class$$
This is a Swig interface to a pointer to an integer array class
$codep */
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

