# -----------------------------------------------------------------------------
#         cppad_py: A C++ Object Library and Python Interface to Cppad
#          Copyright (C) 2017-20 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# -----------------------------------------------------------------------------
# $begin numeric_simple_inv_xam.py$$ $newlinech #$$
#
# $section Example Computing Derivatives of Matrix Inversion$$
#
# $head Problem$$
# We define
# $latex \[
#   A(x) = \left( \begin{array}{cc}
#   x_0 & x_1 \\
#   x_2 & x_3
#   \end{array} \right)
# \] $$
# It follows that
# $latex \[
#   A^{-1}(x) =
#   \frac{1}{x_3 * x_0 - x_1 * x_2}
#   \left( \begin{array}{cc}
#   x_3 & - x_1 \\
#   - x_2 & x_0
#   \end{array} \right)
# \] $$
# We define
# $latex \[
#   f(x) = (x_3 * x_0 - x_1 * x_2) [
#   A_{0,0}^{-1} (x),
#   A_{0,1}^{-1} (x),
#   A_{1,0}^{-1} (x),
#   A_{1,1}^{-1} (x)
#   ]
# = [ x_3, -x_1, -x_2, x_0]
# \] $$
# The following example below check the derivative of $latex f(x)$$
#
# $head Source Code$$
# $srcthisfile%
#   0%# BEGIN_PYTHON%# END_PYTHON%1
# %$$
# $end
#
# BEGIN_PYTHON
import numpy
import cppad_py
from simple_inv import simple_inv
def simple_inv_xam() :
    ok = True
    x  = numpy.array( [1.0, 2.0, 3.0, 4.0] )
    ax = cppad_py.independent(x)
    #
    # create the matrix [ [x_0, x_1], [x_2, x_3] ]
    aA = numpy.reshape(ax, (2,2), order='C' )
    #
    # compute inverse of A
    aAinv = simple_inv(aA)
    #
    # create f(x)
    ay = numpy.reshape(aAinv, 4, order='C' )
    ay = (ax[3] * ax[0] - ax[1] * ax[2]) * ay
    f  = cppad_py.d_fun(ax, ay)
    #
    # evaluate the derivative f'(x)
    J      = f.jacobian(x)
    #
    # Check the derivative
    check      = numpy.zeros( (4, 4) )
    check[0,3] =  1.0
    check[1,1] = -1.0
    check[2,2] = -1.0
    check[3,0] =  1.0
    #
    eps99 = 99.0 * numpy.finfo(float).eps
    ok   &= numpy.all( numpy.fabs(J - check) < eps99 )
    return ok

# END_PYTHON
