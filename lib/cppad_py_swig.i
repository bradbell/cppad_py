/* -----------------------------------------------------------------------------
           cppad_py: A C++ Object Library and Python Interface to Cppad
            Copyright (C) 2017-18 Bradley M. Bell (bradbell@seanet.com)
                This program is distributed under the terms of the
                GNU General Public License version 3.0 or later see
                      https://www.gnu.org/licenses/gpl-3.0.txt
----------------------------------------------------------------------------- */
/* cppad_py_swig.i */
# ifdef SWIG
# define CPPAD_SWIG_LIB_PUBLIC
# else
# include <cppad_swig_lib_export.h>
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
	py
	namespace
$$

$section C++ and Python Modules$$

$head Language$$
Is a source code language.
Note that in C++, the library functions are in
the $code cppad_py$$ namespace,
while in the Python language is accessed through the
Swig $code cppad_py$$ module.

$end
*/
# ifdef SWIGPYTHON
%module cppad_py_swig
# endif
/* ------------------------------------------------------------------------- */


%ignore  ptr;
%include "std_vector.i"
%include "exception.i"

%exception {
     try { $action }
     catch (std::runtime_error& e) {
            SWIG_exception(SWIG_RuntimeError, const_cast<char*>( e.what() ) );
     }
}

%include <cppad/py/a_double.hpp>
%include <cppad/py/sparse.hpp>
%include <cppad/py/a_fun.hpp>
%include <cppad/py/error.hpp>

namespace std {
     %template(vec_bool)      vector<bool>;
     %template(vec_int)       vector<int>;
     %template(vec_double)    vector<double>;
     %template(vec_a_double)  vector<cppad_py::a_double>;
}
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
