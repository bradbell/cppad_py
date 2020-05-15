# -----------------------------------------------------------------------------
#         cppad_py: A C++ Object Library and Python Interface to Cppad
#          Copyright (C) 2017-20 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# -----------------------------------------------------------------------------
# BEGIN_ODE_MULTI_STEP
import numpy
import copy
def ode_multi_step(one_step, f, t_all, y_init ) :
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
		y1            = one_step(f, t0, y0, t_step)
		y_all[i+1,:]  = copy.copy(y1)
	return y_all
# END_ODE_MULTI_STEP
#
# $begin numeric_ode_multi_step$$ $newlinech #$$
# $spell
#	init
#	yp
#	numpy
# $$
#
#
# $section Multiple Ode Steps$$
#
# $head Syntax$$
# $icode%y_all% = ode_multi_step(%one_step%, %f%, %t_all%, %y_init%)%$$
#
# $head Purpose$$
# The routine can be used with $code ad_double$$.
#
# $head one_step$$
# This routine executes one step of an ODE approximation method with the
# following syntax:
# $codei%
#	%y1% = %one_step%(%f%, %t0%, %y0%, %t_step%)
# %$$
# The elements of $icode y0$$ and the scalars above can be
# $code float$$ or $code a_double$$.
#
# $subhead t0$$
# is the initial time value for the step.
#
# $subhead y0$$
# is the initial value of $latex y(t)$$ for the step.
#
# $subhead t_step$$
# is the is the size of the step (in time).
#
# $subhead y1$$
# is the approximation for the ODE solution at time $icode%t0% + %t_step%$$.
#
# $head f$$
# This is a function that evaluates the ordinary differential equation
# $latex \[
#	y^{(1)} (t) = f [ t , y(t) ]
# \] $$
# The specification for this function depend on the $icode one_step$$
# routine.
#
# $head t_all$$
# This is a numpy vector of time values at which the solution is calculated.
# The type of its elements can be $code float$$ or $code ad_double$$.
# It must be either monotone increasing or decreasing.
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
#
# $children%
#	example/python/numeric/ode_multi_step_xam.py
# %$$
# $head Example$$
# $cref numeric_ode_multi_step_xam.py$$
#
# $head Source Code$$
# $srcthisfile%
#	0%# BEGIN_ODE_MULTI_STEP%# END_ODE_MULTI_STEP%0
# %$$
#
# $end
