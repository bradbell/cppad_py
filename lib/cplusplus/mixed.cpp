# ifdef INCLUDE_MIXED
/* -----------------------------------------------------------------------------
           cppad_py: A C++ Object Library and Python Interface to Cppad
            Copyright (C) 2017-20 Bradley M. Bell (bradbell@seanet.com)
                This program is distributed under the terms of the
                GNU General Public License version 3.0 or later see
                      https://www.gnu.org/licenses/gpl-3.0.txt
----------------------------------------------------------------------------- */
# include <cppad/py/mixed.hpp>
# include <cppad/py/cpp_convert.hpp>
# include <cppad/mixed/exception.hpp>

namespace cppad_py { // BEGIN_CPPAD_PY_NAMESPACE

// ---------------------------------------------------------------------------
// mixed_derived class
// ---------------------------------------------------------------------------
// ctor
mixed_derived::mixed_derived(
    size_t                                n_fixed          ,
    size_t                                n_random         ,
    bool                                  quasi_fixed      ,
    bool                                  bool_sparsity    ,
    const  CppAD::mixed::d_sparse_rcv&    A_rcv            ,
    PyObject*                             warning          ,
    d_fun&                                d_fix_likelihood ,
    d_fun&                                d_fix_constraint ,
    d_fun&                                d_ran_likelihood )
:
cppad_mixed( n_fixed, n_random, quasi_fixed, bool_sparsity, A_rcv ) ,
warning_(warning)                                                   ,
a_fix_likelihood_(d_fix_likelihood)                                 ,
a_fix_constraint_(d_fix_constraint)                                 ,
a_ran_likelihood_(d_ran_likelihood)
{ }
//
// warning
void mixed_derived::warning(const std::string& message)
{   PyObject* arglist = Py_BuildValue("(s)", message.c_str() );
    PyObject* result  = PyObject_CallObject(warning_, arglist);
    Py_DECREF(arglist);
    Py_DECREF(result);
}
//
// fatal_error
void mixed_derived::fatal_error(const std::string& message)
{   // swig exceptions are set up to catch std::runtime_error
    throw std::runtime_error(message);
}
//
// fix_likelihood
CppAD::vector< CppAD::AD<double> > mixed_derived::fix_likelihood(
    const CppAD::vector< CppAD::AD<double> >& fixed_vec )
{   CppAD::vector< CppAD::AD<double> > result;
    size_t n_result = a_fix_likelihood_.size_range();
    if( n_result == 0 )
        return result;
    result = a_fix_likelihood_.a_ptr_->Forward(0, fixed_vec);
    return result;
}
//
// fix_constraint
CppAD::vector< CppAD::AD<double> > mixed_derived::fix_constraint(
    const CppAD::vector< CppAD::AD<double> >& fixed_vec )
{   CppAD::vector< CppAD::AD<double> > result;
    size_t n_result = a_fix_constraint_.size_range();
    if( n_result == 0 )
        return result;
    result = a_fix_constraint_.a_ptr_->Forward(0, fixed_vec);
    return result;
}
//
// ran_likelihood
CppAD::vector< CppAD::AD<double> > mixed_derived::ran_likelihood(
    const CppAD::vector< CppAD::AD<double> >& fixed_vec ,
    const CppAD::vector< CppAD::AD<double> >& random_vec )
{   CppAD::vector< CppAD::AD<double> > result;
    size_t n_result = a_ran_likelihood_.size_range();
    if( n_result == 0 )
        return result;
    size_t n_fixed  = fixed_vec.size();
    size_t n_random = random_vec.size();
    CppAD::vector< CppAD::AD<double> > both(n_fixed + n_random);
    for(size_t j = 0; j < n_fixed; ++j)
        both[j] = fixed_vec[j];
    for(size_t j = 0; j < n_random; ++j)
        both[j + n_fixed] = random_vec[j];
    result = a_ran_likelihood_.a_ptr_->Forward(0, both);
    return result;
}

// ---------------------------------------------------------------------------
// mixed class
// ---------------------------------------------------------------------------
// ctor
mixed::mixed(
    const std::vector<double>&     fixed_init       ,
    const std::vector<double>&     random_init      ,
    bool                           quasi_fixed      ,
    bool                           bool_sparsity    ,
    sparse_rcv&                    A_rcv            ,
    PyObject*                      warning          ,
    d_fun&                         fix_likelihood   ,
    d_fun&                         fix_constraint   ,
    d_fun&                         ran_likelihood   )
{   size_t n_fixed  = fixed_init.size();
    size_t n_random = random_init.size();
    // --------------------------------------------------
    // copy_A_rc as CppAD::mixed::sparse_rc
    size_t nr  = A_rcv.nr();
    size_t nc  = A_rcv.nc();
    size_t nnz = A_rcv.nnz();
    CppAD::mixed::sparse_rc copy_A_rc(nr, nc, nnz);
    for(size_t k = 0; k < nnz; ++k)
        copy_A_rc.set(k, A_rcv.row()[k], A_rcv.col()[k]);
    // --------------------------------------------------
    // copy_A_rcv as CppAD::mixed::d_sparse_rcv
    CppAD::mixed::d_sparse_rcv copy_A_rcv( copy_A_rc );
    for(size_t k = 0; k < nnz; ++k)
        copy_A_rcv.set(k, A_rcv.val()[k]);
    // --------------------------------------------------
    // ptr_
    try
    {   ptr_ = new mixed_derived(
            n_fixed,
            n_random,
            quasi_fixed,
            bool_sparsity,
            copy_A_rcv,
            warning,
            fix_likelihood,
            fix_constraint,
            ran_likelihood
        );
        assert( ptr_ != CPPAD_NULL );
    }
    catch( CppAD::mixed::exception& e )
    {   std::string message = e.message("mixed_ctor before initialize");
        throw std::runtime_error(message);
    }
    try
    {   CppAD::vector<double> fixed_vec  = d_vec_std2cppad(fixed_init);
        CppAD::vector<double> random_vec = d_vec_std2cppad(random_init);
        //
        ptr_->initialize(fixed_vec, random_vec);
    }
    catch( CppAD::mixed::exception& e )
    {   std::string message = e.message("mixed_ctor during initialize");
        throw std::runtime_error(message);
    }
}
// destructor
mixed::~mixed(void)
{   // destructor should not throw exception
    assert( ptr_ != CPPAD_NULL );
    delete ptr_;
    ptr_ = CPPAD_NULL;
}
// post_warning
void mixed::post_warning(const char* message)
{   ptr_->warning( std::string(message) );
}
// post_fatal_error
void mixed::post_fatal_error(const char* message)
{   ptr_->fatal_error( std::string(message) );
}
// optimize_fixed
fixed_solution mixed::optimize_fixed(
    const char*                fixed_ipopt_options    ,
    const char*                random_ipopt_options   ,
    const std::vector<double>& fixed_lower            ,
    const std::vector<double>& fixed_upper            ,
    const std::vector<double>& fix_constraint_lower   ,
    const std::vector<double>& fix_constraint_upper   ,
    const std::vector<double>& fixed_scale            ,
    const std::vector<double>& fixed_in               ,
    const std::vector<double>& random_lower           ,
    const std::vector<double>& random_upper           ,
    const std::vector<double>& random_in              )
{   typedef CppAD::vector<double>        c_vector;
    typedef CppAD::mixed::fixed_solution c_fixed_solution;
    //
    std::string c_fixed_ipopt_options  = fixed_ipopt_options;
    std::string c_random_ipopt_options = random_ipopt_options;
    //
    c_vector c_fixed_lower          = d_vec_std2cppad(fixed_lower);
    c_vector c_fixed_upper          = d_vec_std2cppad(fixed_upper);
    c_vector c_fix_constraint_lower = d_vec_std2cppad(fix_constraint_lower);
    c_vector c_fix_constraint_upper = d_vec_std2cppad(fix_constraint_upper);
    c_vector c_fixed_scale          = d_vec_std2cppad(fixed_scale);
    c_vector c_fixed_in             = d_vec_std2cppad(fixed_in);
    c_vector c_random_lower         = d_vec_std2cppad(random_lower);
    c_vector c_random_upper         = d_vec_std2cppad(random_upper);
    c_vector c_random_in            = d_vec_std2cppad(random_in);
    //
    c_fixed_solution c_solution= ptr_->optimize_fixed(
        c_fixed_ipopt_options  ,
        c_random_ipopt_options ,
        c_fixed_lower          ,
        c_fixed_upper          ,
        c_fix_constraint_lower ,
        c_fix_constraint_upper ,
        c_fixed_scale          ,
        c_fixed_in             ,
        c_random_lower         ,
        c_random_upper         ,
        c_random_in
    );
    //
    fixed_solution solution;
    solution.fixed_opt   = d_vec_cppad2std( c_solution.fixed_opt );
    solution.fixed_lag   = d_vec_cppad2std( c_solution.fixed_lag );
    solution.fix_con_lag = d_vec_cppad2std( c_solution.fix_con_lag );
    solution.ran_con_lag = d_vec_cppad2std( c_solution.ran_con_lag );
    //
    return solution;
}
// optimize_random
std::vector<double> mixed::optimize_random(
    const char*                random_ipopt_options   ,
    const std::vector<double>& fixed_vec              ,
    const std::vector<double>& random_lower           ,
    const std::vector<double>& random_upper           ,
    const std::vector<double>& random_in              )
{   typedef CppAD::vector<double>        c_vector;
    //
    std::string c_random_ipopt_options = random_ipopt_options;
    //
    c_vector c_fixed_vec            = d_vec_std2cppad(fixed_vec);
    c_vector c_random_lower         = d_vec_std2cppad(random_lower);
    c_vector c_random_upper         = d_vec_std2cppad(random_upper);
    c_vector c_random_in            = d_vec_std2cppad(random_in);
    //
    c_vector c_random_out= ptr_->optimize_random(
        c_random_ipopt_options ,
        c_fixed_vec            ,
        c_random_lower         ,
        c_random_upper         ,
        c_random_in
    );
    std::vector<double> random_out = d_vec_cppad2std(c_random_out);
    //
    return random_out;
}
// hes_fixed_obj
sparse_rcv mixed::hes_fixed_obj(
    const std::vector<double>& fixed_vec  ,
    const std::vector<double>& random_opt )
{   typedef CppAD::vector<double>        c_vector;
    //
    c_vector c_fixed_vec  = d_vec_std2cppad(fixed_vec);
    c_vector c_random_opt = d_vec_std2cppad(random_opt);
    //
    CppAD::mixed::d_sparse_rcv c_result_rcv = ptr_->hes_fixed_obj(
        c_fixed_vec  ,
        c_random_opt
    );
    cppad_py::sparse_rcv result_rcv( mixed2sparse_rcv( c_result_rcv ) );
    //
    return result_rcv;
}
// hes_random_obj
sparse_rcv mixed::hes_random_obj(
    const std::vector<double>& fixed_vec  ,
    const std::vector<double>& random_vec )
{   typedef CppAD::vector<double>        c_vector;
    //
    c_vector c_fixed_vec  = d_vec_std2cppad(fixed_vec);
    c_vector c_random_vec = d_vec_std2cppad(random_vec);
    //
    CppAD::mixed::d_sparse_rcv c_result_rcv = ptr_->hes_random_obj(
        c_fixed_vec  ,
        c_random_vec
    );
    cppad_py::sparse_rcv result_rcv( mixed2sparse_rcv( c_result_rcv ) );
    //
    return result_rcv;
}


} // END_CPPAD_PY_NAMESPACE

# endif // INCLUDE_MIXED
