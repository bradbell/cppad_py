# ifndef CPPAD_PY_MIXED_HPP
# define CPPAD_PY_MIXED_HPP
# if INCLUDE_MIXED
/* -----------------------------------------------------------------------------
           cppad_py: A C++ Object Library and Python Interface to Cppad
            Copyright (C) 2017-20 Bradley M. Bell (bradbell@seanet.com)
                This program is distributed under the terms of the
                GNU General Public License version 3.0 or later see
                      https://www.gnu.org/licenses/gpl-3.0.txt
----------------------------------------------------------------------------- */
# include <vector>
# include <Python.h>
# ifndef SWIG
# include <cppad/mixed/cppad_mixed.hpp>
# endif
# include <cppad/py/sparse.hpp>
# include <cppad/py/public_lib.hpp>

// ---------------------------------------------------------------------------
// cppad_derived class
// ---------------------------------------------------------------------------
# ifndef SWIG
// class derived from CppAD::mixed::cppad_mixed and not in SWIG interface
class CPPAD_PY_LIB_PUBLIC mixed_derived : public cppad_mixed {
    PyObject*  fatal_error_;
    PyObject*  warning_;
public:
    // ctor
    mixed_derived(
        size_t                             n_fixed       ,
        size_t                             n_random      ,
        bool                               quasi_fixed   ,
        bool                               bool_sparsity ,
        const  CppAD::mixed::d_sparse_rcv& A_rcv         ,
        PyObject*                          fatal_error   ,
        PyObject*                          warning
    );
    // warning
    void fatal_error(const std::string& message);
    // warning
    void warning(const std::string& message);
};
# endif


// ----------------------------------------------------------------------------
// mixed class
// ----------------------------------------------------------------------------
// version of cppad_derived that is in the SWIG interface
class CPPAD_PY_LIB_PUBLIC mixed {
private:
    // pointer to corresponding mixed_derived class
    mixed_derived* ptr_;
public:
    // ctor
    mixed(
        size_t                         n_fixed       ,
        size_t                         n_random      ,
        bool                           quasi_fixed   ,
        bool                           bool_sparsity ,
        const  cppad_py::sparse_rcv&   A_rcv         ,
        PyObject*                      fatal_error   ,
        PyObject*                      warning
    );
    // destructor
    ~mixed(void);
    // test_fatal_error
    void test_fatal_error(const char* message);
    // test_warning
    void test_warning(const char* message);
};

# endif
# endif
