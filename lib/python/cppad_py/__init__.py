# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileCopyrightText: Bradley M. Bell <bradbell@seanet.com>
# SPDX-FileContributor: 2017-23 Bradley M. Bell
# ----------------------------------------------------------------------------
# initialize cppad_py
# -----------------------------------------------------------------------------

# Function that work as is using swig interface to  c++
# BEGIN_SORT_THIS_LINE_PLUS_1
from cppad_py.cppad_swig import abort_recording
from cppad_py.cppad_swig import a_double
from cppad_py.cppad_swig import sparse_hes_work
from cppad_py.cppad_swig import sparse_jac_work
from cppad_py.cppad_swig import vec_a_double
from cppad_py.cppad_swig import vec_bool
from cppad_py.cppad_swig import vec_double
from cppad_py.cppad_swig import vec_int
from cppad_py.cppad_swig import pow_int
from cppad_py.cppad_swig import build_type
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
from cppad_py.mixed           import mixed
# END_SORT_THIS_LINE_MINUS_1
