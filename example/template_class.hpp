# ifndef CPPAD_SWIG_EXAMPLE_TEMPLATE_CLASS
# define CPPAD_SWIG_EXAMPLE_TEMPLATE_CLASS
/* -----------------------------------------------------------------------------
           cppad_swig: A C++ Object Library and Swig Interface to Cppad
            Copyright (C) 2017-17 Bradley M. Bell (bradbell@seanet.com)
                This program is distributed under the terms of the
            GNU Affero General Public License version 3.0 or later see
                       http://www.gnu.org/licenses/agpl.txt
----------------------------------------------------------------------------- */
// BEGIN C++
# include "example.hpp"

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
$begin  example_template_class.hpp$$

$section Example C++ Template Class Implementations$$

$srcfile%example/template_class.hpp%0%// BEGIN C++%// END C++%$$

$end
--------------------------------------------------------------------------
*/
# endif
