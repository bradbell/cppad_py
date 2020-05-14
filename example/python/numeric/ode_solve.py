# -----------------------------------------------------------------------------
#         cppad_py: A C++ Object Library and Python Interface to Cppad
#          Copyright (C) 2017-20 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# -----------------------------------------------------------------------------
# BEGIN_MULTI_STEP
from runge4_step import runge4_step
def multi_step(f, t_all, y_init ) :
	import numpy
	import copy
	dtype      = type(y_init[0])
	n_var      = y_init.size
	n_step     = t_all.size - 1
	y_all      = numpy.empty( (n_step+1, n_var), dtype = dtype  )
	y1         = y_init
	t1         = t_all[0]
	y_all[0,:] = y1
	for i in range(n_step) :
		y0            = y1
		t0            = t1
		t1            = t_all[i+1]
		t_step        = t1 - t0
		y1            = runge4_step(f, t0, y0, t_step)
		y_all[i+1,:]  = copy.copy(y1)
	return y_all
# END_MULTI_STEP
#
# $begin numeric_ode_multi_step$$ $newlinech #$$
# $spell
#	Runge-Kutta
#	init
#	yp
#	numpy
# $$
#
#
# $section Multiple Fourth Order Runge-Kutta ODE Steps$$
#
# $head Syntax$$
# $icode%y_all% = ode_solve.multi_step(%f%, %t_all%, %y_init%)%$$
#
# $head Purpose$$
# The routine can be used with $code ad_double$$
#
# $head f$$
# This is a function that evaluates the ordinary differential equation
# using the syntax
# $codei%
#	%yp% = %f%( %t% , %y% )
# %$$
# where $icode t$$ is the current time,
# $icode y$$ is the current value of $latex y(t)$$, and
# $icode yp$$ is the current derivative $latex y^{(1)} (t)$$.
#
# $head t_all$$
# This is a numpy vector of time values at which the solution is calculated.
# The type of its elements can be $code float$$ or $code ad_double$$.
# It must be either monotone increasing or decreasing.
# A single Runge-Kutta step is used to calculate the value at the next time
# given the value at the current time.
#
# $head y_init$$
# This is the value of $latex y(t)$$ at the initial time
# $icode%t_all%[%0%]%$$ as a numpy vector.
# The type of its elements can be $code float$$ or $code ad_double$$.
#
# $head y_all$$
# This is the approximate solution for $latex y(t)$$ at all of the
# times specified by $icode t_all$$ as a numpy array.
# The value $icode%y_all%[%i%, %j%]%$$ is the value of the j-th
# component of $latex y(t)$$ at time $icode%t_all%[%i%]%$$.
# This solution is 4-th order accurate in time $latex t$$; e.g., if
# $latex y(t)$$ is a polynomial in $latex t$$ of order four or lower,
# the solution has no truncation error, only round off error.
#
# $children%
#	example/python/numeric/ode_multi_step_xam.py
# %$$
# $head Example$$
# $cref numeric_ode_multi_step_xam.py$$
#
# $head Source Code$$
# $srcthisfile%
#	0%# BEGIN_MULTI_STEP%# END_MULTI_STEP%0
# %$$
#
# $end
