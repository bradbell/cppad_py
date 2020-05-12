# -----------------------------------------------------------------------------
#         cppad_py: A C++ Object Library and Python Interface to Cppad
#          Copyright (C) 2017-20 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# -----------------------------------------------------------------------------
# BEGIN_PYTHON
import numpy
import runge4
def seird_model(t_all, p_fun, initial, n_step = 1) :
	# private member fuction (not part of class API)
	def ode(t, seird) :
		S      = seird[0]
		E      = seird[1]
		I      = seird[2]
		R      = seird[3]
		D      = seird[4]
		p      = p_fun(t)
		Sdot   = - p['beta'] *  S * I  + p['xi']    * R
		Edot   = + p['beta'] *  S * I  - p['sigma'] * E
		Idot   = + p['sigma'] * E      - (p['gamma'] + p['chi']) * I
		Rdot   = + p['gamma'] * I      - p['xi']    * R
		Ddot   = + p['chi']   * I
		return numpy.array([ Sdot, Edot, Idot, Rdot, Ddot])
	#
	if n_step == 1 :
		seird_all  = runge4.multi_step(ode, t_all, initial)
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
		seird_refine   = runge4.multi_step(ode, t_refine, initial)
		index_all   = [ i * n_step for i in range(len(t_all)) ]
		seird_all   = seird_refine[ index_all ]
	#
	return seird_all
# END_PYTHON
#
# $begin numeric_seird_model$$ $newlinech #$$
# $spell
#	seird
#	numpy
#	cppad
#	py
#	xi
#	interpolant
# $$
#
# $section A Susceptible Exposed Infectious Recovered and Death Model$$
#
# $head Syntax$$
# $icode%seird_all% = seird_model(%t_all%, %p_fun%, %initial%, %n_step% = 1)
# %$$
#
# $head Notation$$
# $table
# $latex S(t)$$      $cnext size of the Susceptible group     $rnext
# $latex E(t)$$      $cnext size of the Exposed group         $rnext
# $latex I(t)$$      $cnext size of the Infectious group      $rnext
# $latex R(t)$$      $cnext size Recovered group              $rnext
# $latex D(t)$$      $cnext size of the group that has died   $rnext
# $latex \beta(t)$$  $cnext infectious rate                   $rnext
# $latex \sigma(t)$$ $cnext incubation rate                   $rnext
# $latex \gamma(t)$$ $cnext recovery rate                     $rnext
# $latex \xi(t)$$    $cnext loss of immunity rate             $rnext
# $latex \chi(t)$$   $cnext excess mortality rate
# $tend
#
# $head ODE$$
# The ordinary differential equation for this model is:
# $latex \[
# \begin{array}{rcll}
# \dot{S} & = & - \beta S I       & + \xi R                \\
# \dot{E} & = & + \beta S I       & - \sigma E             \\
# \dot{I} & = & + \sigma E        & - ( \gamma + \chi )  I \\
# \dot{R} & = & + \gamma I        & - \xi R                \\
# \dot{D} & = & + \chi I          &
# \end{array}
# \] $$
# where we dropped the time dependence in the equations above.
# This model does not account for death by other causes.
# Some versions of this model use a $latex \beta$$
# that is scaled by the total population $latex N$$.
#
# $head t_all$$
# The argument $icode t_all$$ is a vector that is monotone
# increasing or decreasing.
# The smaller the spacing between time points, the more accurate
# the approximation is.
# We call $icode%t_all%[0]%$$ the initial time and
# $icode%t_all%[-1]%$$ the final time.
#
# $head p_fun$$
# This argument is a function and the syntax
# $codei%
#	%p% = %p_fun%(%t%)
# %$$
# sets $icode p$$ to a dictionary with the following keys and values:
# $table
# Key             $cnext Value $rnext
# $code 'beta'$$  $cnext $latex \beta(t)$$ $rnext
# $code 'sigma'$$ $cnext $latex \sigma(t)$$ $rnext
# $code 'gamma'$$ $cnext $latex \gamma(t)$$ $rnext
# $code 'chi'$$   $cnext $latex \chi(t)$$ $rnext
# $code 'xi'$$    $cnext $latex \xi(t)$$
# $tend
# The value $icode t$$ will be between the initial and final time.
# The parameter functions above are assumed to be smooth
# for all times between the initial and final time and
# not in $icode t_all$$.
# It is also assumed to be continuous at the times in $icode t_all$$; e.g,
# it could be a piecewise linear interpolant with knots at $icode t_all$$.
#
# $head initial$$
# is a vector of length four containing the initial values for
# S, E, I, R, D in that order.
#
# $head n_step$$
# This is the number of numerical integration steps to use for each
# time interval in the $icode t_all$$ array. It must be greater or equal one.
# The larger $icode n_step$$ the more computational effort and the more
# accurate the solution.  The default value is for $icode n_step$$ is one.
#
# $head seird_all$$
# The return value $icode seird_all$$ is a numpy matrix with row dimension
# equal to the number of elements in $icode t_all$$ and column dimension
# equal to five. The value $icode%seird_all%[%i%, %j%]%$$ is the
# approximate solution for the j-th compartment at time $icode%t_all%[%i%]%$$.
# The compartments have the same order as in $icode initial$$ and
# $codei%%seird%[0,:]%$$ is equal to $icode initial$$.
# The sequence of floating point operations only depends on $icode t_all$$
# and the operations used to compute $icode p_fun$$.
#
# $head Conservation of Mass$$
# Note that the sum of S, E, I, R, and D should be constant; i.e.,
# up to numerical accuracy, it not depend on time.
#
# $children%
#	example/python/numeric/seird_model_xam.py
# %$$
# $head Example$$
# $cref numeric_seird_model_xam.py$$
#
# $head Source Code$$
# $srcthisfile%
#	0%# BEGIN_PYTHON%# END_PYTHON%0
# %$$
#
# $end
