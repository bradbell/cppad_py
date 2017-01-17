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
# include <cppad/swig/vector.hpp>
# include <cppad/swig/a_other.hpp>
%}

/*
$begin module$$
$spell
	Cppad
	Perl
	py
	namespace
$$

$section Cppad Swig Modules and Languages$$

$head Language$$
Is a source code language.
Note that in C++, the library functions are accessed directly,
while in the other languages they are accessed through the
corresponding Swig module.

$head Module Name$$
This is the name of the Swig module.
In C++ this is actually a $code namespace$$, instead of a
Swig module.

$head Module Reference$$
This is the source code, in the particular language,
used to reference functions that are in the module.

$head Table$$
$table
Language     $cnext Module Name        $cnext Module Reference      $rnext
C++          $cnext $code cppad_swig$$ $cnext $code cppad_swig::$$  $rnext
Octave       $cnext $code m_cppad$$    $cnext $code m_cppad.$$      $rnext
Perl         $cnext $code pm_cppad$$   $cnext $code pm_cppad::$$    $rnext
Python       $cnext $code py_cppad$$   $cnext $code m_cppad.$$
$tend

$end
*/
# ifdef SWIGPYTHON
%module py_cppad
# endif
# ifdef SWIGOCTAVE
%module m_cppad
# endif
# ifdef SWIGPERL
%module pm_cppad
# endif
/* ------------------------------------------------------------------------- */


%ignore  ptr;
%include "std_vector.i"
%include <cppad/swig/a_double.hpp>
%include <cppad/swig/a_fun.hpp>
%include <cppad/swig/a_other.hpp>

%template(vec_double) std::vector<double>;
%template(vec_a_double)     std::vector<cppad_swig::a_double>;


/*
-------------------------------------------------------------------------------
$begin a_double$$
$spell
	Cppad
$$

$section The Cppad Swig a_double Class$$

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

$section Cppad Swig AD Functions$$

$childtable%lib/a_fun.cpp%$$

$end
-------------------------------------------------------------------------------
$begin a_other$$
$spell
	Cppad
$$

$section Other Cppad Swig Functions and Documentation$$

$childtable%lib/a_other.cpp%$$

$end
-------------------------------------------------------------------------------
*/
