// ------------------------------------------------------------ 
// Copyright (C) Bradley M. Bell 1998-2015, All rights reserved 
// ------------------------------------------------------------ 
Keyword = 
[
{ tag: 'cppad_py', title:'cppad_py-2020.5.8: A C++ Object Library and Python Interface to CppAD', other:' git repository purpose getting started numerical examples function speed license' },
{ tag: 'setup.py', title:'Configure and Build the cppad_py Python Module', other:' syntax external requirements install using pip errors download top source directory get test c++ import path' },
{ tag: 'install_error', title:'Error Messages During Installation', other:' solved swig permissions cppad library missing fortify source unsolved travis' },
{ tag: 'get_cppad.sh', title:'Get Cppad', other:' syntax top source directory settings cppad_prefix extra_cxx_flags build_type test_cppad caching' },
{ tag: 'numeric_xam', title:'Numerical Examples', other:'' },
{ tag: 'numeric_runge4_one_step', title:'One Fourth Order Runge-Kutta ODE Step', other:' syntax ti yi yf example source code' },
{ tag: 'numeric_runge4_multi_step', title:'Multiple Fourth Order Runge-Kutta ODE Steps', other:' syntax t_all y_init y_all example source code' },
{ tag: 'numeric_runge4_one_step_xam.py', title:'Example Computing Derivative A Runge-Kutta Ode Solution', other:' source code' },
{ tag: 'numeric_runge4_multi_step_xam.py', title:'Example Computing Derivative A Runge-Kutta Ode Solution', other:' source code' },
{ tag: 'numeric_optimize_fun_class', title:'A Helper Class That Defines Functions Needed for Optimization', other:' syntax purpose objective_ad constraint_ad objective_fun objective_grad objective_hess constraint_fun constraint_jac constraint_hess example source code' },
{ tag: 'numeric_optimize_fun_xam.py', title:'Example Using optimize_fun_class with Scipy Optimization', other:' reference problem trust_constr source code' },
{ tag: 'numeric_seird_model', title:'A Susceptible Exposed Infectious Recovered and Death Model', other:' syntax set_t_all p_fun initial seird_all example source code' },
{ tag: 'numeric_seird_model_xam.py', title:'Example Using seris_model', other:'' },
{ tag: 'numeric_covid_19_xam.py', title:'Example Fitting an SEIRD Model for Covid-19', other:' plot truth source code' },
{ tag: 'library', title:'The Cppad Py Libraries', other:'' },
{ tag: 'py_lib', title:'The Python Library', other:'' },
{ tag: 'py_fun', title:'Cppad Py AD Functions', other:'' },
{ tag: 'py_independent', title:'Declare Independent Variables and Start Recording', other:' syntax dynamic adynamic purpose example' },
{ tag: 'fun_dynamic_xam.py', title:'Python: Using Dynamic Parameters: Example and Test', other:'' },
{ tag: 'py_abort_recording', title:'Abort Recording', other:' syntax purpose example' },
{ tag: 'fun_abort_xam.py', title:'Python: Abort Recording a_double Operations: Example and Test', other:'' },
{ tag: 'py_fun_ctor', title:'Stop Current Recording and Store Function Object', other:' syntax d_fun a_fun ay empty af example' },
{ tag: 'a_fun_xam.py', title:'Python: Purpose of a_fun Objects: Example and Test', other:'' },
{ tag: 'py_fun_property', title:'Properties of a Function Object', other:' syntax size_domain size_range size_var size_op size_order example' },
{ tag: 'fun_property_xam.py', title:'Python: d_fun Properties: Example and Test', other:'' },
{ tag: 'py_fun_new_dynamic', title:'New Dynamic Parameters', other:' syntax size_order example' },
{ tag: 'py_fun_jacobian', title:'Jacobian of an AD Function', other:' syntax f(x) example' },
{ tag: 'fun_jacobian_xam.py', title:'Python: Dense Jacobian Using AD: Example and Test', other:'' },
{ tag: 'py_fun_hessian', title:'Hessian of an AD Function', other:' syntax f(x) g(x) w example' },
{ tag: 'fun_hessian_xam.py', title:'Python: Dense Hessian Using AD: Example and Test', other:'' },
{ tag: 'py_fun_forward', title:'Forward Mode AD', other:' syntax taylor coefficient f(x) x(t) y(t) size_order xp yp example' },
{ tag: 'fun_forward_xam.py', title:'Python: Forward Mode AD: Example and Test', other:'' },
{ tag: 'py_fun_reverse', title:'Reverse Mode AD', other:' syntax notation f(x) x(t) y(t) g(t) q yq xq example' },
{ tag: 'fun_reverse_xam.py', title:'Python: Reverse Mode AD: Example and Test', other:'' },
{ tag: 'py_fun_optimize', title:'Optimize an AD Function', other:' syntax purpose example' },
{ tag: 'fun_optimize_xam.py', title:'Python: Optimize an d_fun: Example and Test', other:'' },
{ tag: 'py_fun_json', title:'Json Representation of AD Computation Graph', other:' syntax to_json from_json examples' },
{ tag: 'fun_to_json_xam.py', title:'Python to_json: Example and Test', other:'' },
{ tag: 'fun_from_json_xam.py', title:'Python from_json: Example and Test', other:'' },
{ tag: 'py_sparse', title:'Python Sparsity Routines', other:'' },
{ tag: 'py_sparse_rc', title:'Sparsity Patterns', other:' syntax nr nc nnz resize put k row col row_major col_major example' },
{ tag: 'sparse_rc_xam.py', title:'Python: Sparsity Patterns: Example and Test', other:'' },
{ tag: 'py_sparse_rcv', title:'Sparse Matrices', other:' syntax pattern matrix nr nc nnz put k row col val row_major col_major example' },
{ tag: 'sparse_rcv_xam.py', title:'Python: Sparsity Patterns: Example and Test', other:'' },
{ tag: 'py_jac_sparsity', title:'Jacobian Sparsity Patterns', other:' syntax purpose for_jac_sparsity rev_jac_sparsity pattern_in pattern_out entire example' },
{ tag: 'sparse_jac_pattern_xam.py', title:'Python: Jacobian Sparsity Patterns: Example and Test', other:'' },
{ tag: 'py_hes_sparsity', title:'Hessian Sparsity Patterns', other:' syntax purpose f select_domain select_range pattern_out component wise example' },
{ tag: 'sparse_hes_pattern_xam.py', title:'Python: Hessian Sparsity Patterns: Example and Test', other:'' },
{ tag: 'py_sparse_jac', title:'Computing Sparse Jacobians', other:' syntax purpose sparse_jac_for sparse_jac_rev subset pattern work n_sweep uses forward example' },
{ tag: 'sparse_jac_xam.py', title:'Python: Computing Sparse Jacobians: Example and Test', other:'' },
{ tag: 'py_sparse_hes', title:'Computing Sparse Hessians', other:' syntax purpose f subset pattern work n_sweep uses forward example' },
{ tag: 'sparse_hes_xam.py', title:'Python: Hessian Sparsity Patterns: Example and Test', other:'' },
{ tag: 'py_utility', title:'Python Utilities', other:'' },
{ tag: 'numpy2vec', title:'Convert a Numpy Array to a cppad_py Vector', other:' syntax dtype shape name' },
{ tag: 'vec2numpy', title:'Convert a cppad_py Vector to a Numpy Array', other:' syntax nr nc' },
{ tag: 'more_py', title:'Steps To Add More Python Functions', other:' purpose documentation independent new_dynamic example implementation fun_new_dynamic.py __init__.py testing' },
{ tag: 'cpp_lib', title:'The C++ Library', other:'' },
{ tag: 'a_double', title:'Cppad Py AD Scalars', other:'' },
{ tag: 'vector', title:'Cppad Py Vectors', other:'' },
{ tag: 'cpp_fun', title:'Cppad Py AD Functions', other:'' },
{ tag: 'sparse', title:'Cppad Py Sparse Calculation', other:'' },
{ tag: 'cpp_utility', title:'C++ Utilities', other:'' },
{ tag: 'a_double_ctor', title:'The a_double Constructor', other:' syntax purpose a_other ad example' },
{ tag: 'a_double_unary_op', title:'a_double Unary Plus and Minus', other:' syntax ay example' },
{ tag: 'a_double_property', title:'Properties of an a_double Object', other:' syntax ad value restriction parameter variable near_equal var2par example' },
{ tag: 'a_double_binary', title:'a_double Binary Operators with an AD Result', other:' syntax ay az example' },
{ tag: 'a_double_compare', title:'a_double Comparison Operators', other:' syntax ay example' },
{ tag: 'a_double_assign', title:'a_double Assignment Operators', other:' syntax ay example' },
{ tag: 'a_double_unary_fun', title:'Unary Functions with AD Result', other:' syntax ay example' },
{ tag: 'a_double_cond_assign', title:'AD Conditional Assignment', other:' syntax purpose target cop left right if_true if_false example' },
{ tag: 'a_double_unary_op_xam.cpp', title:'C++: a_double Unary Plus and Minus: Example and Test', other:'' },
{ tag: 'a_double_unary_op_xam.py', title:'Python: a_double Unary Plus and Minus: Example and Test', other:'' },
{ tag: 'a_double_property_xam.cpp', title:'C++: a_double Properties: Example and Test', other:'' },
{ tag: 'a_double_property_xam.py', title:'Python: a_double Properties: Example and Test', other:'' },
{ tag: 'a_double_binary_xam.cpp', title:'C++: a_double Binary Operators With AD Result: Example and Test', other:'' },
{ tag: 'a_double_binary_xam.py', title:'Python: a_double Binary Operators With AD Result: Example and Test', other:'' },
{ tag: 'a_double_compare_xam.cpp', title:'C++: a_double Comparison Operators: Example and Test', other:'' },
{ tag: 'a_double_compare_xam.py', title:'Python: a_double Comparison Operators: Example and Test', other:'' },
{ tag: 'a_double_assign_xam.cpp', title:'C++: a_double Assignment Operators: Example and Test', other:'' },
{ tag: 'a_double_assign_xam.py', title:'Python: a_double Assignment Operators: Example and Test', other:'' },
{ tag: 'a_double_unary_fun_xam.cpp', title:'C++: a_double Unary Functions with AD Result: Example and Test', other:'' },
{ tag: 'a_double_unary_fun_xam.py', title:'Python: a_double Unary Functions with AD Result: Example and Test', other:'' },
{ tag: 'a_double_cond_assign_xam.cpp', title:'C++: a_double Conditional Assignment: Example and Test', other:'' },
{ tag: 'a_double_cond_assign_xam.py', title:'Python: a_double Conditional Assignment: Example and Test', other:'' },
{ tag: 'vector_ctor', title:'Cppad Py Vector Constructors', other:' syntax purpose vec_bool vec_int vec_double vec_a_double example' },
{ tag: 'vector_size', title:'Size of a Vector', other:' syntax example' },
{ tag: 'vector_set_get', title:'Setting and Getting Vector Elements', other:' syntax element_type u example' },
{ tag: 'vector_size_xam.cpp', title:'C++: Size of Vectors: Example and Test', other:'' },
{ tag: 'vector_size_xam.py', title:'Python: Size of Vectors: Example and Test', other:'' },
{ tag: 'vector_set_get_xam.cpp', title:'C++: Setting and Getting Vector Elements: Example and Test', other:'' },
{ tag: 'vector_set_get_xam.py', title:'Python: Setting and Getting Vector Elements: Example and Test', other:'' },
{ tag: 'cpp_independent', title:'Declare Independent Variables and Start Recording', other:' syntax purpose dynamic a_both example' },
{ tag: 'cpp_abort_recording', title:'Abort Recording', other:' syntax purpose example' },
{ tag: 'cpp_fun_ctor', title:'Stop Current Recording and Store Function Object', other:' syntax d_fun a_fun ay empty af example' },
{ tag: 'cpp_fun_property', title:'Properties of a Function Object', other:' syntax size_domain size_range size_var size_op size_order example' },
{ tag: 'cpp_fun_new_dynamic', title:'Change The Dynamic Parameters', other:' syntax size_order example' },
{ tag: 'cpp_fun_jacobian', title:'Jacobian of an AD Function', other:' syntax f(x) example' },
{ tag: 'cpp_fun_hessian', title:'Hessian of an AD Function', other:' syntax f(x) g(x) w example' },
{ tag: 'cpp_fun_forward', title:'Forward Mode AD', other:' syntax taylor coefficient f(x) x(t) y(t) size_order xp yp example' },
{ tag: 'cpp_fun_reverse', title:'Reverse Mode AD', other:' syntax notation f(x) x(t) y(t) g(t) q yq xq example' },
{ tag: 'cpp_fun_optimize', title:'Optimize an AD Function', other:' syntax purpose example' },
{ tag: 'cpp_fun_json', title:'Json Representation of AD Computational Graph', other:' syntax to_json from_json examples' },
{ tag: 'fun_dynamic_xam.cpp', title:'C++: Using Dynamic Parameters: Example and Test', other:'' },
{ tag: 'fun_abort_xam.cpp', title:'C++: Abort Recording a_double Operations: Example and Test', other:'' },
{ tag: 'fun_property_xam.cpp', title:'C++: function Properties: Example and Test', other:'' },
{ tag: 'fun_jacobian_xam.cpp', title:'C++: Dense Jacobian Using AD: Example and Test', other:'' },
{ tag: 'fun_hessian_xam.cpp', title:'C++: Dense Hessian Using AD: Example and Test', other:'' },
{ tag: 'fun_forward_xam.cpp', title:'C++: Forward Mode AD: Example and Test', other:'' },
{ tag: 'fun_reverse_xam.cpp', title:'C++: Reverse Mode AD: Example and Test', other:'' },
{ tag: 'fun_optimize_xam.cpp', title:'C++: Optimize an d_fun: Example and Test', other:'' },
{ tag: 'fun_to_json_xam.cpp', title:'C++: to_json: Example and Test', other:'' },
{ tag: 'fun_from_json_xam.cpp', title:'C++: to_json: Example and Test', other:'' },
{ tag: 'cpp_sparse_rc', title:'Sparsity Patterns', other:' syntax nr nc nnz resize put k row col row_major col_major example' },
{ tag: 'cpp_sparse_rcv', title:'Sparse Matrices', other:' syntax pattern matrix nr nc nnz put k row col val row_major col_major example' },
{ tag: 'cpp_jac_sparsity', title:'Jacobian Sparsity Patterns', other:' syntax purpose for_jac_sparsity rev_jac_sparsity pattern_in pattern_out entire example' },
{ tag: 'cpp_sparsity', title:'Hessian Sparsity Patterns', other:' syntax purpose f select_domain select_range pattern_out component wise example' },
{ tag: 'cpp_sparse_jac', title:'Computing Sparse Jacobians', other:' syntax purpose sparse_jac_for sparse_jac_rev subset pattern work n_sweep uses forward example' },
{ tag: 'cpp_sparse_hes', title:'Computing Sparse Hessians', other:' syntax purpose f subset pattern work n_sweep uses forward example' },
{ tag: 'sparse_rc_xam.cpp', title:'C++: Sparsity Patterns: Example and Test', other:'' },
{ tag: 'sparse_rcv_xam.cpp', title:'C++: Sparsity Patterns: Example and Test', other:'' },
{ tag: 'sparse_jac_pattern_xam.cpp', title:'C++: Jacobian Sparsity Patterns: Example and Test', other:'' },
{ tag: 'sparse_hes_pattern_xam.cpp', title:'C++: Hessian Sparsity Patterns: Example and Test', other:'' },
{ tag: 'sparse_jac_xam.cpp', title:'C++: Computing Sparse Jacobians: Example and Test', other:'' },
{ tag: 'sparse_hes_xam.cpp', title:'C++: Hessian Sparsity Patterns: Example and Test', other:'' },
{ tag: 'vec2cppad_double', title:'Convert an a_double Vector to a CppAD::AD<double> Vector', other:' syntax prototype' },
{ tag: 'vec2a_double', title:'Convert a CppAD::AD<double> Vector to an a_double Vector', other:' syntax prototype' },
{ tag: 'error_message', title:'Exception Handling', other:' syntax try block catch cppad errors not thread safe example' },
{ tag: 'error_message_xam.cpp', title:'C++: Cppad Py Exception Handling: Example and Test', other:'' },
{ tag: 'error_message_xam.py', title:'Python: Cppad Py Exception Handling: Example and Test', other:'' },
{ tag: 'more_cpp', title:'Steps To Add More C++ Functions', other:' purpose include file independent new_dynamic documentation example implementation testing' },
{ tag: 'whats_new_2020', title:'CppAD Py Changes During 2020', other:' previous years 05-08 05-07 05-06 05-05 05-04 04-28 04-27 04-26 04-25 04-24 04-23 04-22 04-20 04-19 04-18 04-13 04-12 04-10' },
{ tag: 'whats_new_2018', title:'Cppad Py Changes During 2018', other:' 11-10 11-09 11-07 11-05 08-13 07-31 07-26 07-19 07-15 07-14 07-13 07-12 07-10 07-08 07-07 07-03' }
]

var MaxList = 100;
var Nstring = -1;
var Nkeyword = Keyword.length;
var Row2Tag  = [];
Initialize();

function Initialize()
{
	UpdateList();
	document.search.keywords.focus();
}
function UpdateList()
{
	var string  = document.search.keywords.value;
	if( Nstring == string.length )
		return;
	Nstring     = string.length;

	var word    = string.match(/\S+/g);
	var nword   = 0;
	if(word != null )
		nword   = word.length;

	var pattern = new Array(nword);
	for(var j = 0; j < nword; j++)
		pattern[j] = new RegExp(word[j], 'i');

	var nlist       = 0;
	var title_list  = '';
	var tag_list    = '';
	for(i = 0; (i < Nkeyword) && (nlist < MaxList) ; i++)
	{
		var match = true;
		for(j = 0; j < nword; j++)
		{	var flag = pattern[j].test(Keyword[i].tag);
			flag     = flag || pattern[j].test(Keyword[i].title);
			flag     = flag || pattern[j].test(Keyword[i].other);
			match    = match && flag;
		}
		if( match )
		{
			var tag    = Keyword[i].tag;
			var title  = Keyword[i].title
			title      = title.split(/\s+/);
			title      = title.join(' ');
			title_list = title_list + title + '\n';
			tag_list   = tag_list + tag + '\n'
			Row2Tag[nlist] = tag;
			nlist = nlist + 1;
		}
	}
	document.search.title_list.value = title_list;
	document.search.title_list.setAttribute('wrap', 'off');;
	document.search.title_list.readOnly = true;
	document.search.tag_list.value = tag_list;
	document.search.tag_list.setAttribute('wrap', 'off');;
	document.search.tag_list.readOnly = true;
}
function Choose(textarea)
{	var start_select = textarea.value.substring(0, textarea.selectionStart);
	var start_pos    = Math.max(0, start_select.lastIndexOf('\n') + 1);
	var length       = textarea.value.length;
	var end_select   = 
		textarea.value.substring(textarea.selectionEnd, length);
	var end_pos  = end_select.indexOf('\n');
	end_pos      = textarea.selectionEnd + end_pos;
	textarea.selectionStart = start_pos;
	textarea.selectionEnd   = end_pos;
	var row = start_select.split('\n').length - 1;
	var tag = Row2Tag[row];
	document.search.selection.value    = tag.toLowerCase();
	document.search.selection.readOnly = true;
	
	return true;
}
function Goto()
{  selection       = document.search.selection.value;
   if( selection != '' )
	    parent.location = selection + '.htm';
}
function CheckForReturn()
{
	var key = event.which;
	if( key == 13 ) Goto();
}
