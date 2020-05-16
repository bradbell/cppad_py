# -----------------------------------------------------------------------------
#         cppad_py: A C++ Object Library and Python Interface to Cppad
#          Copyright (C) 2017-20 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# -----------------------------------------------------------------------------
# BEGIN_PYTHON
import numpy
from ode_multi_step import ode_multi_step
from runge4_step import runge4_step
# -----------------------------------------------------------------------------
class fun_class :
	def __init__(self, t_all, p_all, n_step) :
		self.t_all  = t_all
		self.p_all  = p_all
		self.n_step = n_step
		self.index  = None
	#
	def set_t_all_index(self, refine_index) :
		t_all_index  = int( numpy.floor( refine_index / self.n_step ) )
		self.index   = t_all_index
	#
	def f(self, t, seirwd) :
		assert self.index != None
		t_all = self.t_all
		p_all = self.p_all
		index = self.index
		#
		# linearly interpolate the parameter values
		p      = dict()
		t_diff = t_all[index + 1] - t_all[index]
		left   = (t_all[index + 1] - t) / t_diff
		right  = (t - t_all[index + 0]) / t_diff
		for key in [ 'beta', 'sigma', 'gamma', 'xi', 'chi', 'delta' ] :
			p[key] = left * p_all[index][key] + right * p_all[index+1][key]
		#
		# unpack the comparements
		S, E, I, R, W, D = seirwd
		#
		# compute f(t, y)
		Sdot   = - p['beta']  *  S * I  + p['xi']    * R
		Edot   = + p['beta']  *  S * I  - p['sigma'] * E
		Idot   = + p['sigma'] * E       - (p['gamma'] + p['chi']) * I
		Rdot   = + p['gamma'] * I       - p['xi']    * R
		Wdot   = + p['chi']   * I       - p['delta'] * W
		Ddot   = + p['delta'] * W
		#
		return numpy.array([ Sdot, Edot, Idot, Rdot, Wdot, Ddot])
	#
# -----------------------------------------------------------------------------
def seirwd_model(t_all, p_all, initial, n_step = 1) :
	# private member fuction (not part of class API)
	fun      = fun_class(t_all, p_all, n_step)
	one_step = runge4_step
	if n_step == 1 :
		seirwd_all  = ode_multi_step(one_step, fun, t_all, initial)
	else :
		# t_refine
		t_refine = list()
		for i in range( len(t_all) - 1 ) :
			step = (t_all[i+1] - t_all[i]) / n_step
			for j in range(n_step) :
				t_refine.append( t_all[i] + j * step )
		t_refine.append( t_all[-1] )
		t_refine = numpy.array( t_refine )
		#
		seirwd_refine   = ode_multi_step(one_step, fun, t_refine, initial)
		index_all   = [ i * n_step for i in range(len(t_all)) ]
		seirwd_all   = seirwd_refine[ index_all ]
	#
	return seirwd_all
# END_PYTHON
#
# $begin numeric_seirwd_model$$ $newlinech #$$
# $spell
#	seirwd
#	numpy
#	cppad
#	py
#	xi
#	interpolant
# $$
#
# $section A Susceptible Exposed Infectious Recovered and Death Model$$
#
# $head Purpose$$
# This routine can be used with $code ad_double$$.
#
# $head Syntax$$
# $icode%seirwd_all% = seirwd_model(%t_all%, %p_all%, %initial%, %n_step% = 1)
# %$$
#
# $head Notation$$
# $table
# $latex S(t)$$      $cnext size of the Susceptible group     $rnext
# $latex E(t)$$      $cnext size of the Exposed group         $rnext
# $latex I(t)$$      $cnext size of the Infectious group      $rnext
# $latex R(t)$$      $cnext size Recovered group              $rnext
# $latex W(t)$$      $cnext size of the group that will die   $rnext
# $latex D(t)$$      $cnext size of the group that has died   $rnext
# $latex \beta(t)$$  $cnext infectious rate                   $rnext
# $latex \sigma(t)$$ $cnext incubation rate                   $rnext
# $latex \gamma(t)$$ $cnext recovery rate                     $rnext
# $latex \xi(t)$$    $cnext loss of immunity rate             $rnext
# $latex \chi(t)$$   $cnext excess mortality rate             $rnext
# $latex \delta(t)$$ $cnext delay between infectious and death
# $tend
#
# $head ODE$$
# The ordinary differential equation for this model is:
# $latex \[
# \begin{array}{rcll}
# \dot{S} & = & - \beta  S I      & + \xi    R             \\
# \dot{E} & = & + \beta  S I      & - \sigma E             \\
# \dot{I} & = & + \sigma E        & - ( \gamma + \chi )  I \\
# \dot{R} & = & + \gamma I        & - \xi    R             \\
# \dot{W} & = & + \chi   I        & - \delta W             \\
# \dot{D} & = & + \delta W        &
# \end{array}
# \] $$
# where we dropped the time dependence in the equations above.
# This model does not account for death by other causes.
# It is similar to the standard
# $href%https://www.idmod.org/docs/hiv/model-seir.html%SEIRS%$$ model
# with the following differences:
# $list number$$
# The total population $latex N$$ is not included in this model,
# so the units for $latex \beta$$ are different.
# $lnext
# This model tracks death due to the condition using the compartments W and D.
# $lend
#
# $head t_all$$
# The argument $icode t_all$$ is a vector that is monotone
# increasing or decreasing.
# The type of its elements can be $code float$$ or $code a_double$$.
# The smaller the spacing between time points, the more accurate
# the approximation is.
# We call $icode%t_all%[0]%$$ the initial time and
# $icode%t_all%[-1]%$$ the final time.
#
# $head p_all$$
# This argument is a list of dictionaries.
# The i-th element of the list has the following $icode key$$,
# $icode value$$ pairs:
# $table
# $icode key$$    $cnext $icode value$$     $rnext
# $code 'beta'$$  $cnext $latex \beta( t_i )$$  $rnext
# $code 'sigma'$$ $cnext $latex \sigma( t_i )$$ $rnext
# $code 'gamma'$$ $cnext $latex \gamma( t_i )$$ $rnext
# $code 'xi'$$    $cnext $latex \xi( t_i )$$    $rnext
# $code 'chi'$$   $cnext $latex \chi( t_i )$$   $rnext
# $code 'delta'$$ $cnext $latex \delta( t_i )$$
# $tend
# where $icode t_i$$ is the time $icode%t_all%[%i%]%$$.
# The type of $icode value$$ can be $code float$$ or $code a_double$$.
# Each of the these parameters will be linearly interpolated
# for times between the those in $icode t_all$$.
#
# $head initial$$
# is a vector of length four containing the initial values for
# S, E, I, R, W, D in that order.
# The type of its elements can be $code float$$ or $code a_double$$.
#
# $head n_step$$
# This is the number of numerical integration steps to use for each
# time interval in the $icode t_all$$ array.
# It must be an $code int$$ greater or equal one.
# The larger $icode n_step$$ the more computational effort and the more
# accurate the solution.  The default value is for $icode n_step$$ is one.
#
# $head seirwd_all$$
# The return value $icode seirwd_all$$ is a numpy matrix with row dimension
# equal to the number of elements in $icode t_all$$ and column dimension
# equal to six. The value $icode%seirwd_all%[%i%, %j%]%$$ is the
# approximate solution for the j-th compartment at time $icode%t_all%[%i%]%$$.
# The compartments have the same order as in $icode initial$$ and
# $codei%%seirwd%[0,:]%$$ is equal to $icode initial$$.
# The sequence of floating point operations only depends on $icode t_all$$
# and the operations used to compute $icode p_fun$$.
#
# $head Conservation of Mass$$
# Note that the sum of S, E, I, R, W, and D should be constant; i.e.,
# up to numerical accuracy, it not depend on time.
#
# $children%
#	example/python/numeric/seirwd_model_xam.py
# %$$
# $head Example$$
# $cref numeric_seirwd_model_xam.py$$
#
# $head Source Code$$
# $srcthisfile%
#	0%# BEGIN_PYTHON%# END_PYTHON%0
# %$$
#
# $end
