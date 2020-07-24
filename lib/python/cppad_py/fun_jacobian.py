# -----------------------------------------------------------------------------
#         cppad_py: A C++ Object Library and Python Interface to Cppad
#          Copyright (C) 2017-20 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# -----------------------------------------------------------------------------
# {xsrst_comment_ch #}
#
# {xsrst_begin py_fun_jacobian}
#
# .. include:: ../preamble.rst
#
# Jacobian of an AD Function
# ##########################
#
# Syntax
# ******
# *J* = *f* . ``jacobian`` ( *x* )
#
# f
# *
# This is either a
# :ref:`d_fun<py_fun_ctor.syntax.d_fun>` or
# :ref:`a_fun<py_fun_ctor.syntax.a_fun>` function object.
# Upon return, the zero order
# :ref:`taylor_coefficients<py_fun_forward.taylor_coefficient>`
# in *f* correspond to the value of *x* .
# The other Taylor coefficients in *f* are unspecified.
#
# f(x)
# ****
# We use the notation :math:`f: \B{R}^n \rightarrow \B{R}^m`
# for the function corresponding to *f* .
# Note that *n* is the size of :ref:`ax<py_fun_ctor.ax>`
# and *m* is the size of :ref:`ay<py_fun_ctor.ay>`
# in to the constructor for *f* .
#
# x
# *
# If *f* is a ``d_fun`` or ``a_fun`` ,
# *x* is a numpy vector with ``float`` ( ``a_double`` ) elements
# and size *n* .
# It specifies the argument value at we are computing the Jacobian
# :math:`f'(x)`.
#
# J
# *
# The result is a numpy matrix with ``float`` ( ``a_double`` ) elements,
# *m* rows, and ``n`` columns.
# For *i* between zero and *m* -1
# and *j* between zero and *n* -1 ,
#
# .. math::
#
#    J [ i,  j ] = \frac{ \partial f_i }{ \partial x_j } (x)
#
# {xsrst_children
#   example/python/core/fun_jacobian_xam.py
# }
# Example
# *******
# :ref:`fun_jacobian_xam_py<fun_jacobian_xam_py>`
#
# {xsrst_end py_fun_jacobian}
# -----------------------------------------------------------------------------
import cppad_py
import numpy
# ----------------------------------------------------------------------------
# This function is used by jacobian in d_fun class to implement syntax above
def d_fun_jacobian(f, x) :
    """
    J = f.jacobian(x)
    computes the Jacobian of the function corresponding to f
    """
    #
    n = f.size_domain()
    m = f.size_range()
    #
    # convert x -> u
    dtype    = float
    syntax   = 'f.jacobian(x)'
    u = cppad_py.utility.numpy2vec(x, dtype, n, syntax, 'x')
    #
    # call jacobian
    v =  f.jacobian(u)
    #
    # convert v -> J
    J = cppad_py.utility.vec2numpy(v, m, n)
    #
    return J
# ----------------------------------------------------------------------------
# This function is used by jacobian in a_fun class to implement syntax above
def a_fun_jacobian(af, ax) :
    """
    aJ = af.jacobian(ax)
    computes the Jacobian of the function corresponding to af
    """
    #
    n = af.size_domain()
    m = af.size_range()
    #
    # convert x -> u
    dtype    = cppad_py.a_double
    syntax   = 'af.jacobian(ax)'
    au = cppad_py.utility.numpy2vec(ax, dtype, n, syntax, 'ax')
    #
    # call jacobian
    av =  af.jacobian(au)
    #
    # convert v -> J
    aJ = cppad_py.utility.vec2numpy(av, m, n)
    #
    return aJ
