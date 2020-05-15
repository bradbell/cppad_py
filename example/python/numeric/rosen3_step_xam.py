# -----------------------------------------------------------------------------
#         cppad_py: A C++ Object Library and Python Interface to Cppad
#          Copyright (C) 2017-20 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# -----------------------------------------------------------------------------
# $begin numeric_rosen3_step_xam.py$$ $newlinech #$$
# $spell
#	Rosenbrock
# $$
#
# $section Example Computing Derivative A Rosenbrock Ode Solution$$
#
# $head y(t, x)$$
# The two initial value problems below have the following solution:
# $latex \[
#	y_i (t, x) = ( t^{i+1} / (i+1) ! ) \prod_{j=0}^i x_j
# \]$$
#
# $head First ODE$$
# $latex \[
# f(t, y, x)  =
# \left\{ \begin{array}{rl}
#		x_0               & {\rm if} \; i = 0 \\
#		x_i y_{i-1} (t)   & {\rm otherwise}
# \end{array} \right. \]$$
# with the initial condition $latex y(0) = 0$$
#
# $head Second ODE$$
# $latex \[
#	f(t, y, x)  = ( t^i / i ! ) \prod_{j=0}^i x_j
# \]$$
# with the initial condition $latex y(0) = 0$$
#
#
# $head Derivative of Solution$$
# For this special case, the partial derivative of the solution with respect
# to the j-th component of the vector $latex x$$ is
# $latex \[
#	\partial_{x(j)} y_i (t, x) =  \left\{ \begin{array}{rl}
#		y_i (t, x) / x_j      & {\rm if} \; j \leq i \\
#		0                     & {\rm otherwise}
# \end{array} \right. \]$$
#
#
# $head Source Code$$
# $srcthisfile%
#	0%# BEGIN_PYTHON%# END_PYTHON%1
# %$$
#
# $end
# BEGIN_PYTHON
import numpy
from  scipy.special import factorial
import cppad_py
from rosen3_step import rosen3_step
# ---------------------------------------------------------------------------
class first_fun_class :
	def __init__(self, x) :
		self.x = x

	# fun.f
	def f(self, t, y) :
		y_shift = numpy.concatenate( ( [1.0] , y[0:-1] ) )
		return self.x * y_shift
	#
	# fun.f_t
	def f_t(self, t, y) :
		ny = y.size
		return numpy.zeros( ny, dtype=type(y[0]) )
	#
	# fun.f_y
	def f_y(self, t, y) :
		ny = y.size
		J  = numpy.zeros( (ny, ny), dtype=type(y[0]) )
		for i in range(ny - 1) :
			J[i+1, i] = self.x[i+1]
		return J
# ---------------------------------------------------------------------------
class second_fun_class :
	def __init__(self, x) :
		self.x  = x

	# fun.f
	def f(self, t, y) :
		ny        = y.size
		type_y    = type(y[0])
		result    = numpy.empty(ny, dtype=type(y[0]) )
		result[0] = type_y( self.x[0] )
		for i in range(ny - 1) :
			result[i+1] = result[i] * self.x[i + 1] * t / float(i+1)
		return result
	#
	# fun.f_t
	def f_t(self, t, y) :
		ny = y.size
		type_y    = type(y[0])
		result    = numpy.empty(ny, dtype=type(y[0]) )
		result[0] = type_y( 0.0 )
		prod      = type_y( self.x[0] )
		for i in range(ny - 1) :
			prod        = prod * self.x[i+1]
			result[i+1] = prod
			prod        = prod * t / (i + 1)
	# fun.f_y
	def f_y(self, t, y) :
		ny = y.size
		return numpy.zeros( ny, dtype=type(y[0]) )
# ---------------------------------------------------------------------------
def test_case(case) :
	ok    = True
	nx    = 3
	eps99 = 99.0 * numpy.finfo(float).eps
	#
	# independent variables for this g(x) = y(1, x)
	x  = numpy.array( nx * [ 1.0 ] )
	ax = cppad_py.independent(x)
	#
	if case == 1 :
		fun = first_fun_class(ax)
	elif case == 2 :
		fun = first_fun_class(ax)
	else :
		assert(False)
	#
	#
	# function to pass to rosen3_step
	#
	# initiali value for the ODE
	ay_start =  numpy.array( nx * [ cppad_py.a_double(0.0) ] )
	t_start  = 0.0
	t_step   = 0.75
	#
	# take one step
	ay = rosen3_step(fun, t_start, ay_start, t_step)
	#
	# g(x) = y(t_step, x)
	g = cppad_py.d_fun(ax, ay)
	#
	# Check g_i (x) = prod_{j=0}^i x[j] t^(i+1) / (i+1) !
	# 3th order method should be very accutate for functions
	# or order 3 or less in t.
	x  = numpy.arange(0, nx) + 1.0
	gx = g.forward(0, x)
	prod = 1.0
	for i in range(nx) :
		prod      = prod * x[i]
		check     = prod * numpy.power(t_step, i+1) / factorial(i+1)
		rel_error = gx[i] / check - 1.0
		ok       &= abs(rel_error) < eps99
	#
	# Check derivative of g_i (x) w.r.t x_j
	# is zero for i < j and  g_i(x) / x_j otherwise
	J = g.jacobian(x)
	for j in range(nx) :
		for i in range(nx) :
			if i < j :
				ok &= J[i,j] == 0.0
			else :
				check     = gx[i] / x[j]
				rel_error = J[i,j] / check - 1.0
				ok       &= abs(rel_error) < eps99

	return ok
# ---------------------------------------------------------------------------
def rosen3_step_xam() :
	ok = True
	ok = ok and test_case(1)
	ok = ok and test_case(2)
	return ok

# END_PYTHON
