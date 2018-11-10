# -----------------------------------------------------------------------------
#         cppad_py: A C++ Object Library and Python Interface to Cppad
#          Copyright (C) 2017-18 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# -----------------------------------------------------------------------------
# initialize cppad_py
# -----------------------------------------------------------------------------

# Function that work as is using swig interface to  c++
# BEGIN_SORT_THIS_LINE_PLUS_1
from cppad_py.swig import abort_recording
from cppad_py.swig import a_double
from cppad_py.swig import error_message
from cppad_py.swig import sparse_hes_work
from cppad_py.swig import sparse_jac_work
from cppad_py.swig import vec_a_double
from cppad_py.swig import vec_bool
from cppad_py.swig import vec_double
from cppad_py.swig import vec_int
# END_SORT_THIS_LINE_MINUS_1


# BEGIN_SORT_THIS_LINE_PLUS_1
from cppad_py.fun_ctor        import d_fun_ctor
from cppad_py.fun_forward     import a_fun_forward
from cppad_py.fun_forward     import d_fun_forward
from cppad_py.fun_hessian     import a_fun_hessian
from cppad_py.fun_hessian     import d_fun_hessian
from cppad_py.fun             import a_fun
from cppad_py.fun             import d_fun
from cppad_py.fun_jacobian    import a_fun_jacobian
from cppad_py.fun_jacobian    import d_fun_jacobian
from cppad_py.fun_new_dynamic import a_fun_new_dynamic
from cppad_py.fun_new_dynamic import d_fun_new_dynamic
from cppad_py.fun_reverse     import a_fun_reverse
from cppad_py.fun_reverse     import d_fun_reverse
from cppad_py.hes_sparsity    import d_fun_for_hes_sparsity
from cppad_py.hes_sparsity    import d_fun_rev_hes_sparsity
from cppad_py.independent     import independent
from cppad_py.sparse_hes      import d_fun_sparse_hes
from cppad_py.sparse_jac      import d_fun_sparse_jac_for
from cppad_py.sparse_jac      import d_fun_sparse_jac_rev
from cppad_py.sparse_rc       import sparse_rc
from cppad_py.sparse_rcv      import sparse_rcv
# END_SORT_THIS_LINE_MINUS_1
