/* -----------------------------------------------------------------------------
           cppad_swig: A C++ Object Library and Swig Interface to Cppad
            Copyright (C) 2017-17 Bradley M. Bell (bradbell@seanet.com)
                This program is distributed under the terms of the
            GNU Affero General Public License version 3.0 or later see
                       http://www.gnu.org/licenses/agpl.txt
----------------------------------------------------------------------------- */
/*
$begin swig_xam.i$$
$spell
	xam
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

$head C++ Includes$$
This include file defines the interface to the C++ object library.
$codep */
%{
# include "swig_xam.hpp"
%}
/* $$
see $cref swig_xam_lib$$.

$head py_swig_xam$$
This is the name of the Python Swig interface to the C++ library.
$codep */
# ifdef SWIGPYTHON
%module py_swig_xam
# endif
/*$$
see $cref check_swig_xam.py$$.

$head m_swig_xam$$
This is the name of the Octave Swig interface to the C++ library.
$codep */
# ifdef SWIGOCTAVE
%module m_swig_xam
# endif
/*$$
see $cref check_swig_xam.m$$.

$head pl_swig_xam$$
This is the name of the Perl Swig interface to the C++ library.
$codep */
# ifdef SWIGPERL
%module pl_swig_xam
# endif
/* $$
see $cref check_swig_xam.pl$$.

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
where $cref/Type/swig_xam_template_class/Type/$$ is $code double$$.
$codep */
%include "swig_xam.hpp"
%template(double_class)  template_class<double>;
/* $$

$head vector_double$$
This is a Swig interface to a $codei%std::vector<%Type%>%$$
where $icode Type$$ is $code double$$.
$codep */
%include "std_vector.i"
%template(vector_double) std::vector<double>;
/* $$

$childtable%
	swig_xam/swig_xam_lib.omh%
	swig_xam/python/check_swig_xam.py%
	swig_xam/octave/check_swig_xam.m%
	swig_xam/perl/check_swig_xam.pl
%$$
$end
*/

