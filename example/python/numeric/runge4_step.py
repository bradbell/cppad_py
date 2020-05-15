# -----------------------------------------------------------------------------
#         cppad_py: A C++ Object Library and Python Interface to Cppad
#          Copyright (C) 2017-20 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# -----------------------------------------------------------------------------
# BEGIN_RUNGE4_STEP
def runge4_step(fun, ti, yi, h) :
	k1     = h * fun.f(ti,           yi)
	k2     = h * fun.f(ti + h / 2.0, yi + k1 / 2.0)
	k3     = h * fun.f(ti + h / 2.0, yi + k2 / 2.0)
	k4     = h * fun.f(ti + h,       yi + k3 )
	yf     = yi + (k1 + 2.0 * k2 + 2.0 * k3 + k4) / 6.0
	return yf
# END_RUNGE4_STEP
#
# $begin numeric_ode_runge4_step$$ $newlinech #$$
# $spell
#	Runge-Kutta
#	yf
#	yi
#	yp
#	numpy
# $$
#
#
# $section One Fourth Order Runge-Kutta ODE Step$$
#
# $head Syntax$$
# $icode%yf% = runge4_step(%fun%, %ti%, %yi%, %h%)%$$
#
# $head Purpose$$
# The routine can be used with $code ad_double$$
# to solve the initial value ODE
# $latex \[
#   y^{(1)} (t)  = f( t , y )
# \] $$
#
# $head fun$$
# This is a function that evaluates the ordinary differential equation
# using the syntax
# $codei%
#	%yp% = %fun%.f( %t% , %y% )%$$
# where $icode t$$ # is the current time,
# $icode y$$ is the current value of $latex y(t)$$, and
# $icode yp$$ is the current derivative $latex y^{(1)} (t)$$.
# The type of the elements of $icode t$$ and $icode y$$
# can be $code float$$ or $code ad_double$$.
#
# $head ti$$
# This is the initial time for the Runge-Kutta step.
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
# This solution is 4-th order accurate in time $latex t$$; e.g., if
# $latex y(t)$$ is a polynomial in $latex t$$ of order four or lower,
# the solution has no truncation error, only round off error.
#
# $children%
#	example/python/numeric/runge4_step_xam.py
# %$$
# $head Example$$
# $cref numeric_runge4_step_xam.py$$
#
# $head Source Code$$
# $srcthisfile%
#	0%# BEGIN_RUNGE4_STEP%# END_RUNGE4_STEP%0
# %$$
#
# $end
