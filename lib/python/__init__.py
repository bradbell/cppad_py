# -----------------------------------------------------------------------------
#         cppad_py: A C++ Object Library and Python Interface to Cppad
#          Copyright (C) 2017-18 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# -----------------------------------------------------------------------------
# initialize cppad_py
# -----------------------------------------------------------------------------

# Function that work as in c++
# BEGIN_SORT_THIS_LINE_PLUS_1
from cppad_py.cppad_py_swig import abort_recording
from cppad_py.cppad_py_swig import a_double
from cppad_py.cppad_py_swig import error_message
from cppad_py.cppad_py_swig import sparse_hes_work
from cppad_py.cppad_py_swig import sparse_jac_work
from cppad_py.cppad_py_swig import sparse_rc
from cppad_py.cppad_py_swig import sparse_rcv
from cppad_py.cppad_py_swig import vec_a_double
from cppad_py.cppad_py_swig import vec_bool
from cppad_py.cppad_py_swig import vec_double
from cppad_py.cppad_py_swig import vec_int
# END_SORT_THIS_LINE_MINUS_1

# functions that require a python wraper
from cppad_py.a_fun           import a_fun
from cppad_py.a_fun_ctor      import a_fun_ctor
from cppad_py.a_fun_forward   import a_fun_forward
from cppad_py.a_fun_hessian   import a_fun_hessian
from cppad_py.a_fun_jacobian  import a_fun_jacobian
from cppad_py.independent     import independent
