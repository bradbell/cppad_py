# -----------------------------------------------------------------------------
#         cppad_py: A C++ Object Library and Python Interface to Cppad
#          Copyright (C) 2017-20 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# -----------------------------------------------------------------------------
# BEGIN_PYTHON
def runge4_step(f, ti, yi, h) :
	k1     = h * f(ti,           yi)
	k2     = h * f(ti + h / 2.0, yi + k1 / 2.0)
	k3     = h * f(ti + h / 2.0, yi + k2 / 2.0)
	k4     = h * f(ti + h,       yi + k3 )
	yf     = yi + (k1 + 2.0 * k2 + 2.0 * k3 + k4) / 6.0
	return yf
# END_PYTHON
#
# $begin numeric_runge4_step$$ $newlinech #$$
# $spell
#	Runge-Kutta
#	yf
#	yi
#	yp
# $$
#
#
# $section One Fourth Order Runge-Kutta ODE Step$$
#
# $head Syntax$$
# $icode%yf% = runge4_step(%f%, %ti%, %yi%, %h%)%$$
#
# $head f$$
# This is a function that evaluates the ordinary differential equation
# using the syntax $codei%yp% = %f%( %t% , %y% )%$$ where
# $icode t$$ # is the current time,
# $icode y$$ is the current value of $latex y(t)$$, and
# $icode yp$$ is the current derivative $latex y^{(1)} (t)$$.
#
# $head ti$$
# This is the initial time for the Runge-Kutta step.
#
# $head yi$$
# This is the value of $latex y(t)$$ at the initial time.
#
# $head h$$
# This is the step size in time; i.e., the time at the end of the step
# minus the initial time.
#
# $head yf$$
# This is the approximate solution for $latex y(t)$$ at the final time.
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
#	0%# BEGIN_PYTHON%# END_PYTHON%0
# %$$
#
# $end
