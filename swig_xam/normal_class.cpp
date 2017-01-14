/* -----------------------------------------------------------------------------
           cppad_swig: A C++ Object Library and Swig Interface to Cppad
            Copyright (C) 2017-17 Bradley M. Bell (bradbell@seanet.com)
                This program is distributed under the terms of the
            GNU Affero General Public License version 3.0 or later see
                       http://www.gnu.org/licenses/agpl.txt
----------------------------------------------------------------------------- */
// BEGIN C++
# include "swig_xam.hpp"

// normal_class()
normal_class::normal_class(void)
{ };

// normal_class(value)
normal_class::normal_class(int value) : value_(value)
{ };

// destructor
normal_class::~normal_class(void)
{ };

// value()
int normal_class::value (void) const
{	return value_; }

// additon
normal_class normal_class::operator+(const normal_class& right) const
{	return normal_class( value_ + right.value_ ); }

// equality
bool normal_class::operator==(const normal_class& right) const
{	return ( value_ == right.value_ ); }
// END C++
/*
$begin  example_normal_class_cpp$$

$section Example C++ Class Implementations$$

$srcfile%swig_xam/normal_class.cpp%0%// BEGIN C++%// END C++%$$

$end
--------------------------------------------------------------------------
*/
