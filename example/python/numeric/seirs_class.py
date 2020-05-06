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
class seirs_class :
	#
	def set_t_all(self, t_all) :
		self.t_all = t_all
	#
	def set_ode_p(self, ode_p) :
		self.ode_p = ode_p
	#
	def set_initial(self, initial) :
		self.initial = initial
	#
	def model(self) :
		seir_all     = runge4.multi_step(self.ode, self.t_all, self.initial)
		return seir_all
	#
	# private member fuction (not part of class API)
	def ode(self, t, seir) :
		S      = seir[0]
		E      = seir[1]
		I      = seir[2]
		R      = seir[3]
		beta   = self.ode_p[0]
		sigma  = self.ode_p[1]
		gamma  = self.ode_p[2]
		xi     = self.ode_p[3]
		Sdot   = - beta * S * I + xi * R
		Edot   = + beta * S * I - sigma * E
		Idot   = + sigma * E    - gamma * I
		Rdot   = + gamma * I    - xi * R
		return numpy.array([ Sdot, Edot, Idot, Rdot])
# END_PYTHON
#
# $begin numeric_seirs_class$$ $newlinech #$$
# $spell
#	seirs
#	seir
#	numpy
#	cppad
#	py
# $$
#
# $section A Susceptible Exposed Infectious Recovered Model$$
#
# $head Syntax$$
# $icode%seirs% = seirs_class()
# %$$
# $icode%seirs%.set_t_all(%t_all%)
# %$$
# $icode%seirs%.set_ode_p(%ode_p%)
# %$$
# $icode%seirs%.set_initial(%initial%)
# %$$
# $icode%seir_all% = %seirs%.model()
# %$$
#
# $head ODE$$
# The ordinary differential equation for this model is:
# $latex \[
# \begin{array}{rcl}
# \dot{S}(t) & = & - \beta(t) S(t) I(t) + \xi R(t)    \\
# \dot{E}(t) & = & + \beta(t) S(t) I(t) - \sigma E(t) \\
# \dot{I}(t) & = & + \sigma E(t)        - \gamma  I(t) \\
# \dot{R}(t) & = & + \gamma I(t)        - \xi R(t)
# \end{array}
# \] $$
#
# $head set_t_all$$
# The argument $icode t_all$$ is a vector that is monotone
# increasing or decreasing.
# The smaller the spacing between time points, the more accurate
# the approximation is.
#
# $head set_ode_p$$
# The argument $icode ode_p$$ is a vector of length four
# containing the ODE parameters in the following order:
# $latex \beta, \sigma, \gamma, \xi$$.
#
# $head set_initial$$
# The argument $icode initial$$ is a vector of length four
# containing the initial compartment values in the following order:
# $latex S, E, I, R$$.
#
# $head model$$
# Given all of the settings above, this function computes an
# approximate solution of the ODE.
# The return value $icode seir_all$$ is a numpy matrix with row dimension
# equal to the number of elements in $icode t_all$$ and column dimension
# equal to four. The value $icode%seir_all%[%i%, %j%]%$$ is the
# approximate solution for the j-th compartment at time $icode%t_all%[%i%]%$$.
# The compartments have the same order as in $icode initial$$ and
# $codei%%seir%[0,:]%$$ is equal to $icode initial$$.
# The sequence of floating point operations only depends on $icode t_all$$;
# i.e., cppad_py functions that depend on the model results can be used
# for different values of $icode ode_p$$ and $icode initial$$.
#
# $children%
#	example/python/numeric/seirs_fit_xam.py
# %$$
# $head Example$$
# $cref numeric_seirs_fit_xam.py$$
#
# $head Source Code$$
# $srcthisfile%
#	0%# BEGIN_PYTHON%# END_PYTHON%0
# %$$
#
# $end
