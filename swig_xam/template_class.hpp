# ifndef CPPAD_PY_EXAMPLE_TEMPLATE_CLASS
# define CPPAD_PY_EXAMPLE_TEMPLATE_CLASS
/* -----------------------------------------------------------------------------
           cppad_py: A C++ Object Library and Python Interface to Cppad
            Copyright (C) 2017-18 Bradley M. Bell (bradbell@seanet.com)
                This program is distributed under the terms of the
                GNU General Public License version 3.0 or later see
                      https://www.gnu.org/licenses/gpl-3.0.txt
----------------------------------------------------------------------------- */
// BEGIN C++
# include "swig_xam.hpp"

// template_class(value)
template <class Type>
template_class<Type>::template_class(const Type& value) : value_(value)
{ };

// value()
template <class Type>
Type template_class<Type>::value (void) const
{	return value_; }

// additon
template <class Type> template_class<Type>
template_class<Type>::operator+(const template_class& right) const
{	return template_class( value_ + right.value_ ); }

// equality
template <class Type> bool
template_class<Type>::operator==(const template_class& right) const
{	return ( value_ == right.value_ ); }
// END C++
/*
$begin  swig_xam_template_class.hpp$$

$section Swig Example: C++ Template Class Implementation$$

$srcfile%swig_xam/template_class.hpp%0%// BEGIN C++%// END C++%$$

$end
--------------------------------------------------------------------------
*/
# endif
