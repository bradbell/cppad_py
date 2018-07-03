/* -----------------------------------------------------------------------------
           cppad_py: A C++ Object Library and Python Interface to Cppad
            Copyright (C) 2017-18 Bradley M. Bell (bradbell@seanet.com)
                This program is distributed under the terms of the
                GNU General Public License version 3.0 or later see
                      https://www.gnu.org/licenses/gpl-3.0.txt
----------------------------------------------------------------------------- */
/* cppad_py.i */
# ifdef SWIG
# define CPPAD_PY_LIB_PUBLIC
# else
# include <cppad_py_lib_export.h>
# endif


%{
# include <cppad/py/a_double.hpp>
# include <cppad/py/sparse.hpp>
# include <cppad/py/a_fun.hpp>
# include <cppad/py/vector.hpp>
# include <cppad/py/error.hpp>
%}

/*
$begin module$$
$spell
	Cppad
	Py
	Perl
	py
	namespace
$$

$section Cppad Py Modules and Languages$$

$head Language$$
Is a source code language.
Note that in C++, the library functions are accessed directly,
while in the other languages they are accessed through the
corresponding Swig module.

$head Module Name$$
This is the name of the Swig module.
In C++ this is actually a $code namespace$$, instead of a
Swig module.

$head module_ref$$
We use $icode module_ref$$ to denote the source code used to reference
the Cppad Py module for a particular language.
It has the following value (depending on the language):
$table
Language     $cnext Module Name        $cnext module_ref            $rnext
C++          $cnext $code cppad_py$$ $cnext $code cppad_py::$$  $rnext
Octave       $cnext $code m_cppad$$    $cnext $code m_cppad.$$      $rnext
Perl         $cnext $code pm_cppad$$   $cnext $code pm_cppad::$$    $rnext
Python       $cnext $code cppad_py$$   $cnext $code m_cppad.$$
$tend

$end
*/
# ifdef SWIGPYTHON
%module cppad_py
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
%include "exception.i"

%exception {
     try { $action }
     catch (std::runtime_error e) {
            SWIG_exception(SWIG_RuntimeError, const_cast<char*>( e.what() ) );
     }
}

%include <cppad/py/a_double.hpp>
%include <cppad/py/sparse.hpp>
%include <cppad/py/a_fun.hpp>
%include <cppad/py/error.hpp>

%template(vec_bool)      std::vector<bool>;
%template(vec_int)       std::vector<int>;
%template(vec_double)    std::vector<double>;
%template(vec_a_double)  std::vector<cppad_py::a_double>;

/*
-------------------------------------------------------------------------------
$begin a_double$$
$spell
	Cppad
	Py
$$

$section Cppad Py AD Scalars$$

$childtable%lib/a_double.cpp%$$

$end
-------------------------------------------------------------------------------
$begin vector$$
$spell
	Cppad
	Py
$$

$section Cppad Py Vectors$$

$childtable%lib/vector.omh%$$

$end
-------------------------------------------------------------------------------
$begin a_fun$$
$spell
	Cppad
	Py
$$

$section Cppad Py AD Functions$$

$childtable%lib/a_fun.cpp%$$

$end
-------------------------------------------------------------------------------
$begin sparse$$
$spell
	Cppad
	Py
$$

$section Cppad Py Sparse Calculation$$

$childtable%lib/sparse.cpp%$$

$end
-------------------------------------------------------------------------------
$begin error$$
$spell
	messaging
	Cppad
	Py
$$

$section Cppad Py Error Messaging$$

$childtable%lib/error.cpp%$$

$end
-------------------------------------------------------------------------------
*/
