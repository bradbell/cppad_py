# -----------------------------------------------------------------------------
#         cppad_py: A C++ Object Library and Python Interface to Cppad
#          Copyright (C) 2017-20 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# -----------------------------------------------------------------------------
# BEGIN_PYTHON
import numpy
import cppad_py

class optimize_fun_class :
    def __init__(self, objective_ad, constraint_ad=None) :
        self.objective_ad  = objective_ad
        self.constraint_ad = constraint_ad
    #
    def objective_fun(self, x) :
        # objective as a vector
        y = self.objective_ad.forward(0, x)
        return y[0]
    #
    def objective_grad(self, x) :
        # Jacobian as a matrix
        J = self.objective_ad.jacobian(x)
        # change to a vector
        return J.flatten()
    #
    def objective_hess(self, x) :
        w = numpy.array( [ 1.0 ] )
        H = self.objective_ad.hessian(x, w)
        return H
    #
    def constraint_fun(self, x) :
        return self.constraint_ad.forward(0, x)
    #
    def constraint_jac(self, x) :
        # Jacobian as a matrix
        J = self.constraint_ad.jacobian(x)
        return J
    #
    def constraint_hess(self, x, v) :
        H = self.constraint_ad.hessian(x, v)
        return H
# END_PYTHON
"""
$begin numeric_optimize_fun_class$$
$spell
    numpy
    hess
    jac
$$

$section A Helper Class That Defines Functions Needed for Optimization$$

$head Syntax$$
$icode%optimize_fun% = optimize_fun_class(%objective_ad%, %constraint_ad%)%$$

$head Purpose$$
This class is an aid solving optimization problems of the form
$latex \[
    \begin{array}{rl}
    {\rm minimize}       & f(x) \; {\rm w.r.t} \; x \\
    {\rm subject \; to}  & a \leq g(x) \leq b \\
    \end{array}
\] $$
where $latex x$$ is a vector,
$latex f(x)$$ is a scalar, and
$latex a, g(x), b$$ are all vectors with the same length.
We use $latex n$$, $latex m$$ for the length of the vectors
$latex x$$ and $latex g(x)$$ respectively.

$head objective_ad$$
This is a $cref/d_fun/py_fun_ctor/Syntax/d_fun/$$
representation of the function $latex f(x)$$.

$head constraint_ad$$
This is a $code d_fun$$ representation of the function $latex g(x)$$.

$head optimize_fun$$
This class object has the following functions defined:

$subhead objective_fun$$
The syntax
$codei%
    %y% = %optimize_fun%.objective_fun(%x%)
%$$
sets $latex y = f(x)$$ where
$icode x$$ is a numpy vector with length $icode n$$
and $icode y$$ is a scalar.

$subhead objective_grad$$
The syntax
$codei%
    %z% = %optimize_fun%.objective_grad(%x%)
%$$
sets $latex z = f^{(1)} (x)$$ where
$icode x$$ and $icode z$$ are numpy vectors with length $icode n$$.

$subhead objective_hess$$
The syntax
$codei%
    %h% = %optimize_fun%.objective_hess(%x%)
%$$
sets $latex h = f^{(2)} (x)$$ where
$icode x$$ is a numpy vector with length $icode n$$
and $icode h$$ is a numpy $icode n$$ by $icode n$$  matrix.

$subhead constraint_fun$$
The syntax
$codei%
    %y% = %optimize_fun%.constraint_fun(%x%)
%$$
sets $latex y = g(x)$$ where
$icode x$$ ($icode y$$) is a numpy vector with length
$icode n$$ ($icode m$$).

$subhead constraint_jac$$
The syntax
$codei%
    %J% = %optimize_fun%.constraint_jac(%x%)
%$$
sets $latex J = g^{(1)} (x)$$ where
$icode x$$ is a numpy vector with length $icode n$$
and $icode J$$ is a numpy $icode m$$ by $icode n$$  matrix.

$subhead constraint_hess$$
The syntax
$codei%
    %H% = %optimize_fun%.constraint_hess(%x%, %v%)
%$$
sets
$latex \[
    H = \sum_{i=0}^{m-1} v_k g_i^{(2)} (x)
\]$$
where $icode x$$ is a numpy vector with length $icode n$$
and $icode H$$ is a numpy $icode n$$ by $icode n$$  matrix.

$children%
    example/python/numeric/optimize_fun_xam.py
%$$
$head Example$$
$cref numeric_optimize_fun_xam.py$$

$head Source Code$$
$srcthisfile%
    0%# BEGIN_PYTHON%# END_PYTHON%0
%$$

$end
"""
