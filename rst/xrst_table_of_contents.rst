.. _xrst_table_of_contents-title:

Table of Contents
*****************
:ref:`cppad_py-title`

| :ref:`1<setup_py-title>` Configure and Build the cppad_py Python Module
|    :ref:`1.1<install_error-title>` Error Messages During Installation
|    :ref:`1.2<get_cppad_sh-title>` Get Cppad
|    :ref:`1.3<get_cppad_mixed_sh-title>` Get cppad_mixed
| :ref:`2<numeric_xam-title>` Numerical Examples
|    :ref:`2.1<numeric_simple_inv-title>` An AD Compatible Matrix Inverse Routine
|       :ref:`2.1.1<numeric_simple_inv_xam_py-title>` Example Computing Derivatives of Matrix Inversion
|    :ref:`2.2<numeric_runge4_step-title>` One Fourth Order Runge-Kutta ODE Step
|       :ref:`2.2.1<numeric_runge4_step_xam_py-title>` Example Computing Derivative A Runge-Kutta Ode Solution
|    :ref:`2.3<numeric_rosen3_step-title>` One Third Order Rosenbrock ODE Step
|       :ref:`2.3.1<numeric_rosen3_step_xam_py-title>` Example Computing Derivative A Rosenbrock Ode Solution
|    :ref:`2.4<numeric_ode_multi_step-title>` Multiple Ode Steps
|       :ref:`2.4.1<numeric_ode_multi_step_xam_py-title>` Example Computing Derivative A Runge-Kutta Ode Solution
|    :ref:`2.5<numeric_optimize_fun_class-title>` A Helper Class That Defines Functions Needed for Optimization
|       :ref:`2.5.1<numeric_optimize_fun_xam_py-title>` Example Using optimize_fun_class with Scipy Optimization
|    :ref:`2.6<numeric_seirwd_model-title>` A Susceptible Exposed Infectious Recovered and Death Model
|       :ref:`2.6.1<numeric_seirwd_model_xam_py-title>` Example Using seris_model
|    :ref:`2.7<numeric_covid_19_xam_py-title>` Example Fitting an SEIRWD Model for Covid-19
| :ref:`3<library-title>` The Cppad Py Libraries
|    :ref:`3.1<py_lib-title>` The Python Library
|       :ref:`3.1.1<py_fun-title>` Cppad Py AD Functions
|          :ref:`3.1.1.1<py_independent-title>` Declare Independent Variables and Start Recording
|             :ref:`3.1.1.1.1<fun_dynamic_xam_py-title>` Python: Using Dynamic Parameters: Example and Test
|          :ref:`3.1.1.2<py_abort_recording-title>` Abort Recording
|             :ref:`3.1.1.2.1<fun_abort_xam_py-title>` Python: Abort Recording a_double Operations: Example and Test
|          :ref:`3.1.1.3<py_fun_ctor-title>` Stop Current Recording and Store Function Object
|             :ref:`3.1.1.3.1<a_fun_xam_py-title>` Python: Purpose of a_fun Objects: Example and Test
|          :ref:`3.1.1.4<py_fun_property-title>` Properties of a Function Object
|             :ref:`3.1.1.4.1<fun_property_xam_py-title>` Python: d_fun Properties: Example and Test
|          :ref:`3.1.1.5<py_fun_check_for_nan-title>` Check for Nan in a Function Object
|             :ref:`3.1.1.5.1<check_for_nan_xam_py-title>` Python: Example Turning of Checking For Nan
|          :ref:`3.1.1.6<py_fun_new_dynamic-title>` New Dynamic Parameters
|          :ref:`3.1.1.7<py_fun_jacobian-title>` Jacobian of an AD Function
|             :ref:`3.1.1.7.1<fun_jacobian_xam_py-title>` Python: Dense Jacobian Using AD: Example and Test
|          :ref:`3.1.1.8<py_fun_hessian-title>` Hessian of an AD Function
|             :ref:`3.1.1.8.1<fun_hessian_xam_py-title>` Python: Dense Hessian Using AD: Example and Test
|          :ref:`3.1.1.9<py_fun_forward-title>` Forward Mode AD
|             :ref:`3.1.1.9.1<fun_forward_xam_py-title>` Python: Forward Mode AD: Example and Test
|          :ref:`3.1.1.10<py_fun_reverse-title>` Reverse Mode AD
|             :ref:`3.1.1.10.1<fun_reverse_xam_py-title>` Python: Reverse Mode AD: Example and Test
|          :ref:`3.1.1.11<py_fun_optimize-title>` Optimize an AD Function
|             :ref:`3.1.1.11.1<fun_optimize_xam_py-title>` Python: Optimize an d_fun: Example and Test
|          :ref:`3.1.1.12<py_fun_json-title>` Json Representation of AD Computation Graph
|             :ref:`3.1.1.12.1<fun_to_json_xam_py-title>` Python to_json: Example and Test
|             :ref:`3.1.1.12.2<fun_from_json_xam_py-title>` Python from_json: Example and Test
|       :ref:`3.1.2<py_sparse-title>` Python Sparsity Routines
|          :ref:`3.1.2.1<py_sparse_rc-title>` Sparsity Patterns
|             :ref:`3.1.2.1.1<sparse_rc_xam_py-title>` Python: Sparsity Patterns: Example and Test
|          :ref:`3.1.2.2<py_sparse_rcv-title>` Sparse Matrices
|             :ref:`3.1.2.2.1<sparse_rcv_xam_py-title>` Python: Sparsity Patterns: Example and Test
|          :ref:`3.1.2.3<py_jac_sparsity-title>` Jacobian Sparsity Patterns
|             :ref:`3.1.2.3.1<sparse_jac_pattern_xam_py-title>` Python: Jacobian Sparsity Patterns: Example and Test
|          :ref:`3.1.2.4<py_hes_sparsity-title>` Hessian Sparsity Patterns
|             :ref:`3.1.2.4.1<sparse_hes_pattern_xam_py-title>` Python: Hessian Sparsity Patterns: Example and Test
|          :ref:`3.1.2.5<py_sparse_jac-title>` Computing Sparse Jacobians
|             :ref:`3.1.2.5.1<sparse_jac_xam_py-title>` Python: Computing Sparse Jacobians: Example and Test
|          :ref:`3.1.2.6<py_sparse_hes-title>` Computing Sparse Hessians
|             :ref:`3.1.2.6.1<sparse_hes_xam_py-title>` Python: Hessian Sparsity Patterns: Example and Test
|       :ref:`3.1.3<py_utility-title>` Python Utilities
|          :ref:`3.1.3.1<numpy2vec-title>` Convert a Numpy Array to a cppad_py Vector
|          :ref:`3.1.3.2<vec2numpy-title>` Convert a cppad_py Vector to a Numpy Array
|       :ref:`3.1.4<mixed-title>` Laplace Approximation of Mixed Effects Models
|          :ref:`3.1.4.1<mixed_ctor-title>` Mixed Class Constructor
|             :ref:`3.1.4.1.1<mixed_ctor_xam_py-title>` Mixed Class Constructor: Example and Test
|          :ref:`3.1.4.2<mixed_warning-title>` Mixed Class Warnings
|             :ref:`3.1.4.2.1<mixed_warning_xam_py-title>` Warnings: Example and Test
|          :ref:`3.1.4.3<mixed_fatal_error-title>` Mixed Class Fatal Errors
|             :ref:`3.1.4.3.1<mixed_fatal_error_xam_py-title>` fatal_error: Example and Test
|          :ref:`3.1.4.4<mixed_fix_likelihood-title>` Fixed Effects Likelihood
|             :ref:`3.1.4.4.1<mixed_fix_likelihood_xam_py-title>` fix_likelihood: Example and Test
|          :ref:`3.1.4.5<mixed_fix_constraint-title>` Fixed Effects Constraint Function
|             :ref:`3.1.4.5.1<mixed_fix_constraint_xam_py-title>` fix_constraint: Example and Test
|          :ref:`3.1.4.6<mixed_ran_likelihood-title>` Random Effects Likelihood
|             :ref:`3.1.4.6.1<mixed_ran_likelihood_xam_py-title>` ran_likelihood: Example and Test
|          :ref:`3.1.4.7<mixed_optimize_fixed-title>` Optimize The Fixed Effects
|             :ref:`3.1.4.7.1<mixed_optimize_fixed_1_py-title>` A Very Simple Optimize Fixed Effects: Example and Test
|             :ref:`3.1.4.7.2<mixed_optimize_fixed_2_py-title>` The Ipopt Example Problem: Example and Test
|          :ref:`3.1.4.8<mixed_optimize_random-title>` Optimize The Random Effects
|             :ref:`3.1.4.8.1<mixed_optimize_random_xam_py-title>` optimize_random: Example and Test
|          :ref:`3.1.4.9<mixed_hes_fixed_obj-title>` Hessian of Fixed Effects Objective
|             :ref:`3.1.4.9.1<mixed_hes_fixed_obj_xam_py-title>` ran_likelihood: Example and Test
|          :ref:`3.1.4.10<mixed_hes_random_obj-title>` Hessian of Random Effects Objective
|             :ref:`3.1.4.10.1<mixed_hes_random_obj_xam_py-title>` ran_likelihood: Example and Test
|       :ref:`3.1.5<more_py-title>` Steps To Add More Python Functions
|    :ref:`3.2<cpp_lib-title>` The C++ Library
|       :ref:`3.2.1<cppad_error-title>` Converting CppAD Errors To Python Exceptions
|          :ref:`3.2.1.1<cppad_error_xam-title>` Python: Example CppAD Error Message
|       :ref:`3.2.2<cpp_fun-title>` Cppad Py AD Functions
|          :ref:`3.2.2.1<cpp_independent-title>` Declare Independent Variables and Start Recording
|             :ref:`3.2.2.1.1<fun_dynamic_xam_cpp-title>` C++: Using Dynamic Parameters: Example and Test
|          :ref:`3.2.2.2<cpp_abort_recording-title>` Abort Recording
|             :ref:`3.2.2.2.1<fun_abort_xam_cpp-title>` C++: Abort Recording a_double Operations: Example and Test
|          :ref:`3.2.2.3<cpp_fun_ctor-title>` Stop Current Recording and Store Function Object
|          :ref:`3.2.2.4<cpp_fun_property-title>` Properties of a Function Object
|             :ref:`3.2.2.4.1<fun_property_xam_cpp-title>` C++: function Properties: Example and Test
|          :ref:`3.2.2.5<cpp_fun_new_dynamic-title>` Change The Dynamic Parameters
|          :ref:`3.2.2.6<cpp_fun_jacobian-title>` Jacobian of an AD Function
|             :ref:`3.2.2.6.1<fun_jacobian_xam_cpp-title>` C++: Dense Jacobian Using AD: Example and Test
|          :ref:`3.2.2.7<cpp_fun_hessian-title>` Hessian of an AD Function
|             :ref:`3.2.2.7.1<fun_hessian_xam_cpp-title>` C++: Dense Hessian Using AD: Example and Test
|          :ref:`3.2.2.8<cpp_fun_forward-title>` Forward Mode AD
|             :ref:`3.2.2.8.1<fun_forward_xam_cpp-title>` C++: Forward Mode AD: Example and Test
|          :ref:`3.2.2.9<cpp_fun_reverse-title>` Reverse Mode AD
|             :ref:`3.2.2.9.1<fun_reverse_xam_cpp-title>` C++: Reverse Mode AD: Example and Test
|          :ref:`3.2.2.10<cpp_fun_optimize-title>` Optimize an AD Function
|             :ref:`3.2.2.10.1<fun_optimize_xam_cpp-title>` C++: Optimize an d_fun: Example and Test
|          :ref:`3.2.2.11<cpp_fun_json-title>` Json Representation of AD Computational Graph
|             :ref:`3.2.2.11.1<fun_to_json_xam_cpp-title>` C++: to_json: Example and Test
|             :ref:`3.2.2.11.2<fun_from_json_xam_cpp-title>` C++: from_json: Example and Test
|          :ref:`3.2.2.12<cpp_check_for_nan-title>` Check For Nan In Function or Derivative Results
|             :ref:`3.2.2.12.1<fun_check_for_nam_xam-title>` C++: Check For Nan in Function Result: Example and Test
|       :ref:`3.2.3<sparse-title>` Cppad Py Sparse Calculation
|          :ref:`3.2.3.1<cpp_sparse_rc-title>` Sparsity Patterns
|             :ref:`3.2.3.1.1<sparse_rc_xam_cpp-title>` C++: Sparsity Patterns: Example and Test
|          :ref:`3.2.3.2<cpp_sparse_rcv-title>` Sparse Matrices
|             :ref:`3.2.3.2.1<sparse_rcv_xam_cpp-title>` C++: Sparsity Patterns: Example and Test
|          :ref:`3.2.3.3<cpp_jac_sparsity-title>` Jacobian Sparsity Patterns
|             :ref:`3.2.3.3.1<sparse_jac_pattern_xam_cpp-title>` C++: Jacobian Sparsity Patterns: Example and Test
|          :ref:`3.2.3.4<cpp_sparsity-title>` Hessian Sparsity Patterns
|             :ref:`3.2.3.4.1<sparse_hes_pattern_xam_cpp-title>` C++: Hessian Sparsity Patterns: Example and Test
|          :ref:`3.2.3.5<cpp_sparse_jac-title>` Computing Sparse Jacobians
|             :ref:`3.2.3.5.1<sparse_jac_xam_cpp-title>` C++: Computing Sparse Jacobians: Example and Test
|          :ref:`3.2.3.6<cpp_sparse_hes-title>` Computing Sparse Hessians
|             :ref:`3.2.3.6.1<sparse_hes_xam_cpp-title>` C++: Hessian Sparsity Patterns: Example and Test
|       :ref:`3.2.4<cpp_utility-title>` C++ Utilities
|          :ref:`3.2.4.1<cpp_convert-title>` Convert Objects Between cppad_mixed and cppad_py
|             :ref:`3.2.4.1.1<ad_vec_std2cppad-title>` Convert AD Vector From Standard to CppAD
|             :ref:`3.2.4.1.2<ad_vec_cppad2std-title>` Convert AD Vector From CppAD to Standard
|             :ref:`3.2.4.1.3<d_vec_std2cppad-title>` Convert double Vector From Standard to CppAD
|             :ref:`3.2.4.1.4<d_vec_cppad2std-title>` Convert double Vector From CppAD to Standard
|             :ref:`3.2.4.1.5<mixed2sparse_rcv-title>` Convert Sparse Matrix from cppad_mixed to cppad_py
|          :ref:`3.2.4.2<exception-title>` Exception Handling
|             :ref:`3.2.4.2.1<exception_xam_cpp-title>` C++: Cppad Py Exception Handling: Example and Test
|             :ref:`3.2.4.2.2<exception_xam_py-title>` Python: Cppad Py Exception Handling: Example and Test
|       :ref:`3.2.5<more_cpp-title>` Steps To Add More C++ Functions
|    :ref:`3.3<a_double-title>` Cppad Py AD Scalars
|       :ref:`3.3.1<a_double_ctor-title>` The a_double Constructor
|       :ref:`3.3.2<a_double_unary_op-title>` a_double Unary Plus and Minus
|          :ref:`3.3.2.1<a_double_unary_op_xam_cpp-title>` C++: a_double Unary Plus and Minus: Example and Test
|          :ref:`3.3.2.2<a_double_unary_op_xam_py-title>` Python: a_double Unary Plus and Minus: Example and Test
|       :ref:`3.3.3<a_double_property-title>` Properties of an a_double Object
|          :ref:`3.3.3.1<a_double_property_xam_cpp-title>` C++: a_double Properties: Example and Test
|          :ref:`3.3.3.2<a_double_property_xam_py-title>` Python: a_double Properties: Example and Test
|       :ref:`3.3.4<a_double_binary-title>` a_double Binary Operators with an AD Result
|          :ref:`3.3.4.1<a_double_binary_xam_py-title>` Python: a_double Binary Operators With AD Result: Example and Test
|          :ref:`3.3.4.2<a_double_binary_xam_cpp-title>` C++: a_double Binary Operators With AD Result: Example and Test
|       :ref:`3.3.5<a_double_compare-title>` a_double Comparison Operators
|          :ref:`3.3.5.1<a_double_compare_xam_cpp-title>` C++: a_double Comparison Operators: Example and Test
|          :ref:`3.3.5.2<a_double_compare_xam_py-title>` Python: a_double Comparison Operators: Example and Test
|       :ref:`3.3.6<a_double_assign-title>` a_double Assignment Operators
|          :ref:`3.3.6.1<a_double_assign_xam_cpp-title>` C++: a_double Assignment Operators: Example and Test
|          :ref:`3.3.6.2<a_double_assign_xam_py-title>` Python: a_double Assignment Operators: Example and Test
|       :ref:`3.3.7<a_double_unary_fun-title>` Unary Functions with AD Result
|          :ref:`3.3.7.1<a_double_unary_fun_xam_cpp-title>` C++: a_double Unary Functions with AD Result: Example and Test
|          :ref:`3.3.7.2<a_double_unary_fun_xam_py-title>` Python: a_double Unary Functions with AD Result: Example and Test
|       :ref:`3.3.8<a_double_cond_assign-title>` AD Conditional Assignment
|          :ref:`3.3.8.1<a_double_cond_assign_xam_cpp-title>` C++: a_double Conditional Assignment: Example and Test
|          :ref:`3.3.8.2<a_double_cond_assign_xam_py-title>` Python: a_double Conditional Assignment: Example and Test
|    :ref:`3.4<vector-title>` Cppad Py Vectors
|       :ref:`3.4.1<vector_ctor-title>` Cppad Py Vector Constructors
|       :ref:`3.4.2<vector_size-title>` Size of a Vector
|          :ref:`3.4.2.1<vector_size_xam_cpp-title>` C++: Size of Vectors: Example and Test
|          :ref:`3.4.2.2<vector_size_xam_py-title>` Python: Size of Vectors: Example and Test
|       :ref:`3.4.3<vector_set_get-title>` Setting and Getting Vector Elements
|          :ref:`3.4.3.1<vector_set_get_xam_cpp-title>` C++: Setting and Getting Vector Elements: Example and Test
|          :ref:`3.4.3.2<vector_set_get_xam_py-title>` Python: Setting and Getting Vector Elements: Example and Test
| :ref:`4<release_notes-title>` CppAD Py Release Notes By Year
|    :ref:`4.1<whats_new_2022-title>` CppAD Py Changes During 2022
|    :ref:`4.2<whats_new_2021-title>` CppAD Py Changes During 2021
|    :ref:`4.3<whats_new_2020-title>` CppAD Py Changes During 2020
|    :ref:`4.4<whats_new_2018-title>` Cppad Py Changes During 2018
