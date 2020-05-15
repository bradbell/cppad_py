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
import cppad_py
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
# BEGIN_CHECK_ROSEN3_STEP
def check_rosen3_step(fun, ti, yi, h) :
	ok    = True
	eps99 = 99.0 * numpy.finfo(float).eps
	#
	ny    = yi.size
	both  = numpy.concatenate( (yi, [ti]) )
	aboth = cppad_py.independent(both)
	az    = fun.f(aboth[ny], aboth[0:ny] )
	fun_d = cppad_py.d_fun(aboth, az)
	#
	J     = fun_d.jacobian(both)
	#
	# check fun.f_t(t, y)
	fun_t = fun.f_t(ti, yi)
	for i in range(ny) :
		if J[i, ny] == 0.0 :
			ok = ok and fun_t[i] == 0.0
		else :
			rel_error = fun_t[i] / J[i,ny] - 1.0
			ok = ok and abs( rel_error ) < eps99
	#
	# check fun.f_y(t, y)
	fun_y = fun.f_y(ti, yi)
	for i in range(ny) :
		for j in range(ny) :
			if J[i, j] == 0.0 :
				ok = ok and fun_y[i, j] == 0.0
			else :
				rel_error = fun_y[i, j] / J[i, j] - 1.0
				ok = ok and abs( rel_error ) < eps99
	#
	return ok
# END_CHECK_ROSEN3_STEP
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
# $icode%yf% = rosen3_step(%fun%, %ti%, %yi%, %h%)
# %$$
# $icode%ok% = check_rosen3_step(%fun%, %ti%, %yi%, %h%)
# %$$
#
# $head Purpose$$
# The routine $code rosen3_step$$ can be used with
# $code ad_double$$ to solve the initial
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
# (For $code check_rosen3_step$$ only $code float$$ is allowed.)
#
# $head yi$$
# This is the numpy vector containing the
# value of $latex y(t)$$ at the initial time.
# The type of its elements can be $code float$$ or $code a_double$$.
# (For $code check_rosen3_step$$ only $code float$$ is allowed.)
#
# $head h$$
# This is the step size in time; i.e., the time at the end of the step
# minus the initial time.
# It can have type $code float$$ or $code a_double$$.
# (This is not used by $code check_rosen3_step$$.)
#
# $head yf$$
# This is the approximate solution for $latex y(t)$$ at the final time
# as a numpy vector.
# This solution is 3-th order accurate in time $latex t$$; e.g., if
# $latex y(t)$$ is a polynomial in $latex t$$ of order three or lower,
# the solution has no truncation error, only round off error.
#
# $head ok$$
# This is true if the function $icode%fun%.f(%t%,%y%)%$$
# and the partials $icode%fun%.f_t(%t%, %y%)%$$,
# $icode%fun%.f_y(%t%, %y%)%$$ agree.
# Otherwise AD has detected an error in these functions.
#
# $children%
#	example/python/numeric/rosen3_step_xam.py
# %$$
# $head Example$$
# $cref numeric_rosen3_step_xam.py$$
#
# $head Source Code$$
#
# $subhead rosen3_step$$
# $srcthisfile%
#	0%# BEGIN_ROSEN3_STEP%# END_ROSEN3_STEP%0
# %$$
#
# $subhead check_rosen3_step$$
# $srcthisfile%
#	0%# BEGIN_CHECK_ROSEN3_STEP%# END_CHECK_ROSEN3_STEP%0
# %$$
#
# $end
