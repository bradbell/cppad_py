# -----------------------------------------------------------------------------
#         cppad_py: A C++ Object Library and Python Interface to Cppad
#          Copyright (C) 2017-20 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# -----------------------------------------------------------------------------
# BEGIN_ROSEN3_STEP
import numpy
from simple_inv import simple_inv
def rosen3_step(fun, ti, yi, h) :
	#
	r1_2     = 1.0   / 2.0
	r3_2     = 3.0   / 2.0
	r3_5     = 3.0   / 5.0
	r24_25   = 24.0  / 25.0
	r3_25    = 3.0   / 25.0
	r121_50  = 121.0 / 50.0
	r186_25  = 186.0 / 25.0
	r6_5     = 6.0   / 5.0
	r97_108  = 97.0  / 108.0
	r11_72   = 11.0  / 72.0
	r25_216  = 25.0  / 216.0
	#
	# Einv
	ny   = yi.size
	I    = numpy.identity(ny, dtype=float)
	E    = I - r1_2 * h * fun.f_y(ti, yi)
	Einv = simple_inv(E)
	#
	# f_t
	f_t  = fun.f_t(ti, yi)
	#
	# k1
	k1   = fun.f(ti, yi)
	k1  += r1_2 * h * f_t
	k1   = numpy.matmul(Einv , k1)
	#
	# k2
	k2   = fun.f(ti + h, yi + h * k1)
	k2  -= r3_2 * h * f_t
	k2  -= 4.0 * k1
	k2   = numpy.matmul(Einv , k2)
	#
	# k3
	t    = ti + r3_5 * h
	y    = yi + r24_25 * h * k1 + r3_25 * h * k2
	k3   = fun.f(t, y)
	k3  += r121_50 * h * f_t
	k3  += r186_25 * k1 + r6_5 * k2
	k3   = numpy.matmul(Einv , k3)
	#
	yf   = yi + h * ( r97_108 * k1 + r11_72 * k2 + r25_216 * k3)
	#
	return yf
# END_ROSEN3_STEP
#
# $begin numeric_rosen3_step$$ $newlinech #$$
# $spell
#	Rosenbrock
#	rosen
#	yf
#	yi
#	yp
#	numpy
#	Shampine
#	Rosenbrock
# $$
#
#
# $section One Third Order Rosenbrock ODE Step$$
#
# $head Syntax$$
# $icode%yf% = rosen3_step(%fun%, %ti%, %yi%, %h%)%$$
#
# $head Purpose$$
# The routine can be used with $code ad_double$$ to solve the initial
# value problem
# $latex \[
#	y^{(1)} (t)  = f( t , y )
# \] $$
#
# $head Reference$$
# The formulas in this method are taken from page 100 of the following
# reference (except that 98/108 was correct to 97/108):
# Shampine, L.F.,
# $italic Implementation of Rosenbrock Methods$$,
# ACM Transactions on Mathematical Software, Vol. 8, No. 2, June 1982.
#
# $head fun$$
# This is a function that evaluates the ordinary differential equation,
# and its partial derivatives,
#
# $subhead t$$
# The argument $icode t$$ below is the current time.
# It can be a $code float$$ or $code a_double$$.
#
# $subhead y$$
# The argument $icode y$$ below is the current value of $latex y(t)$$.
# The type of the elements of $icode y$$
# can be $code float$$ or $code ad_double$$.
#
# $subhead fun.f$$
# The syntax $codei%yp% = %fun%.f( %t% , %y% )%$$ returns $icode yp$$,
# the current function value $latex f(t, y)$$.
#
# $subhead fun.f_t$$
# The syntax $codei%yp_t% = %fun%.f_t( %t% , %y% )%$$ returns $icode yp_t$$,
# the current partial value $latex \partial_t f(t, y)$$.
#
# $subhead fun.f_y$$
# The syntax $codei%yp_y% = %fun%.f_y( %t% , %y% )%$$ returns $icode yp_y$$,
# the current partial value $latex \partial_y f(t, y)$$.
#
# $head ti$$
# This is the initial time for the Rosenbrock step.
# It can have type $code float$$ or $code a_double$$.
#
# $head yi$$
# This is the numpy vector containing the
# value of $latex y(t)$$ at the initial time.
# The type of its elements can be $code float$$ or $code a_double$$.
#
# $head h$$
# This is the step size in time; i.e., the time at the end of the step
# minus the initial time.
# It can have type $code float$$ or $code a_double$$.
#
# $head yf$$
# This is the approximate solution for $latex y(t)$$ at the final time
# as a numpy vector.
# This solution is 3-th order accurate in time $latex t$$; e.g., if
# $latex y(t)$$ is a polynomial in $latex t$$ of order three or lower,
# the solution has no truncation error, only round off error.
#
# $children%
#	example/python/numeric/rosen3_step_xam.py
# %$$
# $head Example$$
# $cref numeric_rosen3_step_xam.py$$
#
# $head Source Code$$
# $srcthisfile%
#	0%# BEGIN_ROSEN3_STEP%# END_ROSEN3_STEP%0
# %$$
#
# $end
