# -----------------------------------------------------------------------------
#         cppad_py: A C++ Object Library and Python Interface to Cppad
#          Copyright (C) 2017-20 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# -----------------------------------------------------------------------------
# $begin numeric_covid_19_xam.py$$ $newlinech #$$
# $spell
#	Covid
#	seird
#	Covariates
#	Covariate
#	cv
# $$
#
# $section Example Fitting an SEIRD Model for Covid-19$$
#
# $head Model$$
# We use the $cref/seird/numeric_seird_model/$$ model and notation.
#
# $head Covariates$$
# In this example there are three covariates that
# affect the infectious rate $latex \beta$$:
# social mobility, outdoor temperature, and Covid-19 testing.
#
# $head beta(t)$$
# Our model for the infectious rate is
# $latex \[
#	\beta(t) = \beta_b \left( 1 + \sum_{j=0}^2 m_j c_j (t) \right)
# \] $$
# where $latex \beta_b$$ is the baseline value for the infectious rate,
# $latex c_j (t)$$ is the j-th covariate as a function of time,
# and $latex m_j$$ is the j-th covariate multiplier.
# The covariates are known functions of time.
# The baseline value $latex \beta_b$$ is the infectious rate corresponding
# to all the covariates being zero.
# The covariate multipliers, and the baseline infectious rate, are unknown.
#
# $head Other Rates$$
# The other rates
# $latex \sigma(t)$$,
# $latex \gamma(t)$$,
# $latex \xi(t)$$,
# $latex \chi(t)$$,
# constant functions with a known value.
#
# $head Initial Values$$
# The initial size of the Recovered group $latex R(0)$$
# and of the Death group $latex D(0)$$ is zero.
# We use fraction of the total population for sizes, so the sum of the
# other initial values is one.
# We treat the initial Exposed group $latex E(0)$$ and the initial
# infected group $latex I(0)$$ as unknown parameters in the model
# and use the relation
# $latex \[
#	S(0) = 1 - E(0) - I(0)
# \] $$
# to express the initial Susceptible group as a function
# of the unknown parameters.
#
# $head Unknown Parameters$$
# In summary, the unknown parameter vector in this model is
# $latex \[
#	x = [ E(0), I(0), \beta_b , m_0 , m_1, m_2 ]
# \] $$
#
# $head Data$$
# The data in this model is cumulative number of deaths,
# as a fraction of the total population and as a function of time.
# We assume that new deaths are recorded at regular time intervals
# and the cumulative deaths is the sum of these recordings.
# For this reason, we model the difference of the cumulative deaths
# between time points as independent.
#
# $head Maximum Likelihood$$
# We use a Gaussian likelihood for each of the differences in the
# cumulative deaths. The unknown parameters are estimated by maximizing the
# product of these likelihoods; i.e., the differences are modeled as being
# independent. The covariance of the estimates is approximated
# by the inverse of the observed information matrix.
# AD is used to compute first and second derivatives of the likelihood
# w.r.t. the unknown parameters $latex x$$.
# These derivatives are used during optimization as well as for
# computing the observed information matrix.
#
# $head Plot Fit$$
# If you set this variable to True, you will get a plot of the fit results.
# $srccode%py%
plot_fit = True
# %$$
# There are two plots. One contains the size for all the compartments
# as a function of time and as a fraction of the total population.
# The other plot is the weighted residuals for the death difference
# data as a function of time.
#
# $head Coefficient of Variation$$
# This is the coefficient of variation for the differences
# in the cumulative death data as a fraction, not a percent.
# If this value is zero, a CV of  zero is used for data simulation
# and a CV of one in the definition of the likelihood.
# This enables checking that the unknown parameters can be accurately
# identified using perfect data.
# $srccode%py%
death_data_cv = 0.1
# %$$
#
# $head Data Residuals$$
# The weighted residuals (some times referred to as just the residuals) are
# $latex \[
#	r_i = \frac{ ( y_{i+1} - y_i ) - [ D( t_{i+1} ) - D( t_i ) ] }{
#	\lambda ( y_{i+1} - y_i) }
# \] $$
# where $latex y_i$$ is the i-th value for the cumulative death data,
# $latex D(t)$$ is the model for the cumulative date given the fit results,
# and $latex \lambda$$ is the $icode death_data_cv$$.
# (The value $latex \lambda = 1$$ is used in the special case where
# $icode death_data_cv$$ is zero.)
# The time corresponding to $latex r_i$$ is $latex ( t_{i+1} + t_i ) / 2$$.
# We put the data difference in the denominator,
# instead of the model difference,
# because it is constant with respect to the unknown parameters.
#
# $head Random Seed$$
# This is the random seed used to simulate noise in the data.
# If this value is zero, the system clock is used to choose the random seed.
# $srccode%py%
random_seed = 0
# %$$
#
# $head Source Code$$
# $srcthisfile%
#	0%# BEGIN_PYTHON%# END_PYTHON%1
# %$$
#
# $end
# BEGIN_PYTHON
from pdb import set_trace
from matplotlib import pyplot
import scipy.optimize
import numpy
import random
import time
#
import cppad_py
import runge4
from optimize_fun_class import optimize_fun_class
from seird_model import seird_model
#
# t_all
t_start = 0.0
t_stop  = 60.0
t_step  = 0.5
t_all = numpy.arange(t_start, t_stop, t_step)
#
# covariates
# Note that we scale and shift our covariates so zero corresponds to the
# baseline infectious rate and so that their variation is order one.
n_time = t_all.size
covariates   = numpy.empty( (n_time, 3) )
for i in range(n_time) :
	t               = t_all[i]
	mobility        = 0.0 if t < 10.0 else -1.0
	temperature     = numpy.sin(2.0 * numpy.pi * t / t_stop )
	testing         = t / t_stop
	covariates[i,:] = [ mobility, temperature, testing ]
#
# baseline_true
baseline_true = 0.15
#
# cov_mul_true
cov_mul_true  = numpy.array( [ - 0.2, - 0.3, - 0.4 ] )
#
# true initial conditions used to simulate data
I0_true     = 0.02
E0_true     = 0.02
S0_true     = 1.0 - E0_true - I0_true
R0_true     = 0.0
D0_true     = 0.0
#
# actual_seed
if random_seed == 0 :
	actual_seed = int( 13 * time.time() )
else :
	actual_seed = random_seed
#
# p_fun_class
# Returns the parameters in the ODE (not the unknown parameters)
class p_fun_class :
	def __init__(self, beta_all) :
		self.beta_all = beta_all
	#
	# There are faster ways to search for interval; e.g., cache previous index
	def p_fun(self, t) :
		i = 0
		while i < len(t_all) - 1 and t_all[i + 1] < t :
			i += 1
		# linear interpolation coefficients
		ip     = i + 1
		t_diff = t_all[ip] - t_all[i]
		left   = ( t_all[ip] - t         ) / t_diff
		right  = ( t         - t_all[i]  ) / t_diff
		# beta changes with time are continuous at all points in t_all
		# and smooth for times not in t_all
		beta   = left * self.beta_all[i] + right * self.beta_all[ip]
		p      = {
			'beta'  : beta,
			'sigma' : 1.0 / 5.0,   # average Exposed is 5 days
			'gamma' : 1.0 / 20.0,  # average Infectious is 20 days
			'chi'   : 1.0 / 200.0, # rate of death is 1/10 recovery rate
			'xi'    : 1.0 / 365.0, # average immunity is 365 days
		}
		return p
#
def x2seird_all(x) :
	#
	# unpack x
	E0       = x[0]
	I0       = x[1]
	baseline = x[2]
	cov_mul  = x[3 :]
	#
	# beta_all
	beta_all = baseline * (1.0 + numpy.matmul(covariates, cov_mul))
	#
	# initial
	S0 = 1.0 - E0 - I0
	R0 = 0.0
	D0 = 0.0
	initial  = numpy.array( [S0, E0, I0, R0, D0] )
	#
	# p_fun
	p_fun_obj = p_fun_class(beta_all)
	p_fun     = p_fun_obj.p_fun
	#
	# seird_all
	seird_all = seird_model(t_all, p_fun, initial)
	#
	return seird_all
#
# objective_d_fun
# t_all and D_data, are constants relative in the objective function
def objective_d_fun(t_all, D_data) :
	#
	# x = ( E(0), I(0), baseline, m[0], m[1], m[2] )
	x  = 0.1 * numpy.ones(6)
	ax = cppad_py.independent(x)
	#
	# compute model for data
	aseird_all = x2seird_all(ax)
	#
	# Model for the cumulative death as function of time
	aD_model   = aseird_all[:,4] # column order is S, E, I, R, D
	#
	# Differences of the death over the time intervals
	Ddiff_data   = numpy.diff(D_data)
	aDdiff_model = numpy.diff(aD_model)
	#
	# compute negative log Gaussian likelihood dropping variance terms
	# because they are constaint w.r.t the unknown parameters
	aresidual = (Ddiff_data - aDdiff_model) / Ddiff_data
	if death_data_cv > 0.0 :
		aresidual = aresidual / death_data_cv
	aloss     = 0.5 * numpy.sum( aresidual * aresidual)
	aloss     = numpy.array( [ aloss ] )
	#
	objective_ad = cppad_py.d_fun(ax, aloss)
	return objective_ad
#
def simulate_data() :
	#
	x_true = numpy.empty(6, dtype=float)
	x_true[0:3] = [ E0_true, I0_true, baseline_true ]
	x_true[3 :] = cov_mul_true
	#
	# noiseless simulated data
	seird_all_true = x2seird_all(x_true)
	#
	# rng: numpy random number generator
	rng = numpy.random.default_rng(seed = actual_seed)
	#
	# D_data
	D_true       = seird_all_true[:,4]
	Ddiff_true   = numpy.diff( D_true )
	std          = death_data_cv * Ddiff_true
	noise        = std * rng.standard_normal(size = t_all.size - 1)
	Ddiff_data   = Ddiff_true + noise
	D_data       = numpy.cumsum(Ddiff_data)
	D_data       = numpy.concatenate( ([0.0], D_data) )
	#
	return D_data

def covid_19_xam(call_count = 0) :
	ok = True
	#
	# D_data
	D_data = simulate_data()
	#
	# objective_ad
	objective_ad = objective_d_fun(t_all, D_data)
	#
	# objective: fun, grad, hess
	optimize_fun = optimize_fun_class(objective_ad)
	#
	# x_true
	x_true      = numpy.empty( 6, dtype=float)
	x_true[0:3] = [ E0_true, I0_true, baseline_true ]
	x_true[3:]  = cov_mul_true
	#
	# bounds
	lower_bound = numpy.empty(x_true.size, dtype=float)
	upper_bound = numpy.empty(x_true.size, dtype=float)
	for i in range(x_true.size) :
		if x_true[i] > 0.0 :
			lower_bound[i] = x_true[i] / 5.0
			upper_bound[i] = x_true[i] * 5.0
		else :
			lower_bound[i] = x_true[i] * 5.0
			upper_bound[i] = x_true[i] / 5.0
	bounds = scipy.optimize.Bounds(
		lower_bound,
		upper_bound,
		keep_feasible = True
	)
	options = {
		'gtol'    : 1e-10,
		'xtol'    : 1e-8,
		'maxiter' : 300,
		'verbose' : 0,
	}
	start_point     = x_true / 2.0
	result = scipy.optimize.minimize(
		optimize_fun.objective_fun,
		start_point,
		method      = 'trust-constr',
		jac         = optimize_fun.objective_grad,
		hess        = optimize_fun.objective_hess,
		options     = options,
		bounds      = bounds,
	)
	ok      = ok and result.success
	x_fit   = result.x
	#
	# compute the observed infromation matrix
	H = optimize_fun.objective_hess(x_fit)
	#
	# approxiamtion for covariance of the estimate x_fit
	Hinv = numpy.linalg.inv(H)
	#
	# standard devaition for each component of x_fit
	std_error = numpy.sqrt( numpy.diag(Hinv) )
	#
	# check that all the weighted residuals are less than two
	for i in range(x_true.size) :
		rel_error = x_fit[i] / x_true[i] - 1.0
		residual  = (x_fit[i] - x_true[i]) / std_error[i]
		print( x_true[i], x_fit[i], rel_error, std_error[i], residual )
		if death_data_cv > 0.0 :
			ok = ok and abs(residual) < 2.0
		else :
			ok = ok and abs(rel_error) < 1e-5
	#
	if not ok :
		msg  = 'covid_19_xam: Correctness test failed, '
		msg += 'actual random seed = ' + str(actual_seed)
		print( msg )
		call_count += 1
		if call_count < 2 and random_seed == 0 :
			print( 're-trying with a differenent random seed')
			ok = covid_19_xam(call_count)
	#
	# plot_fit
	seird_all_fit = x2seird_all(x_fit)
	if plot_fit and ok :
		fig1, ax1 = pyplot.subplots()
		ax1.plot(t_all, seird_all_fit[:,0], 'b-', label='S')
		ax1.plot(t_all, seird_all_fit[:,1], 'g-', label='E')
		ax1.plot(t_all, seird_all_fit[:,2], 'r-', label='I')
		ax1.plot(t_all, seird_all_fit[:,3], 'k-', label='R')
		ax1.plot(t_all, seird_all_fit[:,4], 'y-', label='D')
		ax1.legend()
		ax1.set_xlabel('time')
		ax1.set_ylabel('population fraction')
		#
		t_mid      = (t_all[0 : -1] + t_all[1 :]) / 2.0
		D_fit      = seird_all_fit[:,4]
		Ddiff_data = numpy.diff(D_data)
		Ddiff_fit  = numpy.diff(D_fit)
		residual   = (Ddiff_data - Ddiff_fit) / Ddiff_data
		if death_data_cv > 0.0 :
			residual = residual / death_data_cv
		fig2, ax2 = pyplot.subplots()
		ax2.plot( t_mid,                 residual,   'k+' )
		ax2.plot( [t_all[0], t_all[-1]], [0.0, 0.0], 'k-' )
		ax2.set_xlabel('time')
		ax2.set_ylabel('data weighted residuals')

		#
		pyplot.show()
	#
	# check conservation of masss in the compartmental model
	sum_all_fit = numpy.sum(seird_all_fit, axis=1)
	eps99       = 99.0 * numpy.finfo(float).eps
	ok          = ok and max( abs(sum_all_fit - 1.0) ) < eps99
	#
	return ok
# END_PYTHON
