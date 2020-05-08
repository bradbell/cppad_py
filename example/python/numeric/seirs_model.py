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
def seirs_model(t_all, p_fun, initial) :
	# private member fuction (not part of class API)
	def ode(t, seir) :
		S      = seir[0]
		E      = seir[1]
		I      = seir[2]
		R      = seir[3]
		N      = S + E + I + R
		p      = p_fun(t)
		Sdot   = - p['beta'] * S * I / N + p['xi'] * R
		Edot   = + p['beta'] * S * I / N - p['sigma'] * E
		Idot   = + p['sigma'] * E        - (p['gamma'] + p['chi']) * I
		Rdot   = + p['gamma'] * I        - p['xi'] * R
		return numpy.array([ Sdot, Edot, Idot, Rdot])
	#
	seir_all  = runge4.multi_step(ode, t_all, initial)
	return seir_all
# END_PYTHON
#
# $begin numeric_seirs_model$$ $newlinech #$$
# $spell
#	seirs
#	seir
#	numpy
#	cppad
#	py
#	xi
#	interpolant
# $$
#
# $section A Susceptible Exposed Infectious Recovered Model$$
#
# $head Syntax$$
# $icode%seirs_all% = seirs_model(%t_all%, %p_fun%, %initial%)
# %$$
#
# $head ODE$$
# The ordinary differential equation for this model is:
# $latex \[
# \begin{array}{rcll}
# \dot{S} & = & - \beta S I / N   & + \xi R                \\
# \dot{E} & = & + \beta S I / N   & - \sigma E             \\
# \dot{I} & = & + \sigma E        & - ( \gamma + \chi )  I \\
# \dot{R} & = & + \gamma I        & - \xi R
# \end{array}
# \] $$
# where $latex N = S + E + I + R$$.
# We dropped the time dependence for all the terms in the equations above;
# e.g., $latex \beta$$ is actually $latex \beta(t)$$.
#
# $head set_t_all$$
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
# between the times in $icode t_all$$ it could be a piecewise linear
# interpolant.
#
# $head initial$$
# is a vector of length four containing the initial values for
# S, E, I, R in that order.
#
# $head seirs$$
# The return value $icode seir_all$$ is a numpy matrix with row dimension
# equal to the number of elements in $icode t_all$$ and column dimension
# equal to four. The value $icode%seir_all%[%i%, %j%]%$$ is the
# approximate solution for the j-th compartment at time $icode%t_all%[%i%]%$$.
# The compartments have the same order as in $icode initial$$ and
# $codei%%seir%[0,:]%$$ is equal to $icode initial$$.
# The sequence of floating point operations only depends on $icode t_all$$
# and the operations used to compute $icode p_fun$$.
#
# $children%
#	example/python/numeric/seirs_model_xam.py
# %$$
# $head Example$$
# $cref numeric_seirs_model_xam.py$$
#
# $head Source Code$$
# $srcthisfile%
#	0%# BEGIN_PYTHON%# END_PYTHON%0
# %$$
#
# $end
