/* -----------------------------------------------------------------------------
           cppad_py: A C++ Object Library and Python Interface to Cppad
            Copyright (C) 2017-20 Bradley M. Bell (bradbell@seanet.com)
                This program is distributed under the terms of the
                GNU General Public License version 3.0 or later see
                      https://www.gnu.org/licenses/gpl-3.0.txt
----------------------------------------------------------------------------- */
/* cppad_py_swig.i */
# ifdef SWIG
# define CPPAD_PY_LIB_PUBLIC
# else
# include <cppad_py_lib_export.h>
# endif


%{
# include <cppad/py/a_double.hpp>
# include <cppad/py/sparse.hpp>
# include <cppad/py/fun.hpp>
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
%module swig
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
%include <cppad/py/fun.hpp>
%include <cppad/py/error.hpp>

%extend cppad_py::a_double {
        cppad_py::a_double __radd__(const double& d) const
        {       cppad_py::a_double result;
                return radd(d, *($self));
        }
        cppad_py::a_double __rsub__(const double& d) const
        {       cppad_py::a_double result;
                return rsub(d, *($self));
        }
        cppad_py::a_double __rmul__(const double& d) const
        {       cppad_py::a_double result;
                return rmul(d, *($self));
        }
        cppad_py::a_double __rtruediv__(const double& d) const
        {       cppad_py::a_double result;
                return rdiv(d, *($self));
        }
}

namespace std {
     %template(vec_bool)      vector<bool>;
     %template(vec_int)       vector<int>;
     %template(vec_double)    vector<double>;
     %template(vec_a_double)  vector<cppad_py::a_double>;
}
