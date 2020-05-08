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
# $$
#
# $section Example Fitting an SEIRD Model for Covid-19$$
#
# $head Plot Truth$$
# If you set this variable to True, you will get a plot of the
# values used to simulate the data:
# $srccode%py%
plot_truth = False
# %$$
#
# $head Coefficient of Variation$$
# This is the coefficient of variation for the differences
# in the cumulative death data.
# It is a fraction, not a percent value and
# the value zero corresponds to no noise:
# $srccode%py%
death_data_cv = 0.2
# %$$
#
# $head Random Seed$$
# This is the random seed used to simulate noise in the data.
# The value zero instructs says to us the system clock to seed the data.
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
t_stop  = 50.0
t_step  = 2.0
t_all = numpy.arange(t_start, t_stop, t_step)
#
# covariates
n_time = t_all.size
base_line     = [ 1.0              for t in t_all ]
close_school  = [ float(5.0  < t)  for t in t_all ]
stay_home     = [ float(10.0 < t)  for t in t_all ]
essential     = [ float(15.0 < t)  for t in t_all ]
covariates     = numpy.array( [
	[ base_line[i],  close_school[i], stay_home[i], essential[i] ]
	for i in range(n_time)
] )
#
# p_fun_class
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
		left   = ( t_all[ip] - t ) / t_diff
		right  = ( t - t_all[i]  ) / t_diff
		# beta changes with time are continuous at all points in t_all
		# and smooth for times not in t_all
		beta   = left * self.beta_all[i] + right * self.beta_all[ip]
		p      = {
			'beta'  : beta,
			'sigma' : 1.0 / 5.0,   # The other rates are fixed constants
			'gamma' : 1.0 / 20.0,
			'chi'   : 1.0 / 200.0,
			'xi'    : 1.0 / 365.0,
		}
		return p
#
# objective_d_fun
# t_all and D_data, are constants relative in the objective function
def objective_d_fun(t_all, D_data) :
	#
	# number of covariates
	n_time, n_cov = covariates.shape
	#
	# number of independent variables in objective function
	n_x = n_cov + 2
	#
	# x = ( cov_mul, E(0), I(0) )
	# Note that R(0) = D(0) = 0 and S(0) = 1 - E(0) - I(0)
	x  = 0.1 * numpy.ones(n_x)
	ax = cppad_py.independent(x)
	#
	# abeta_all
	cov_mul    = ax[0 : n_cov]
	abeta_all  = numpy.matmul(covariates, cov_mul)
	#
	# ainitial
	aE_0      = ax[n_cov + 0]
	aI_0      = ax[n_cov + 1]
	aR_0      = 0.0
	aD_0      = 0.0
	aS_0      = 1.0 - aE_0 - aI_0
	ainitial  = numpy.array( [aS_0, aE_0, aI_0, aR_0, aD_0] )
	#
	# p_fun
	ap_fun_obj = p_fun_class(abeta_all)
	ap_fun    = ap_fun_obj.p_fun
	#
	# compute model for data
	aseird_all = seird_model(t_all, ap_fun, ainitial)
	#
	# Model for the derivative of the death data
	aD_model   = aseird_all[:,4] # column order is S, E, I, R, D
	#
	# Differences of the death data
	Ddiff_data   = numpy.diff(D_data)
	aDdiff_model = numpy.diff(aD_model)
	#
	# compute negative log Gaussian likelihood dropping variance terms
	# because they are constaint w.r.t the parameters we optimize.
	aresidual = (Ddiff_data - aDdiff_model) / (death_data_cv * Ddiff_data)
	aloss     = 0.5 * numpy.sum( aresidual * aresidual)
	aloss     = numpy.array( [ aloss ] )
	#
	objective_ad = cppad_py.d_fun(ax, aloss)
	return objective_ad

def covid_19_xam(call_count = 0) :
	ok = True
	#
	# cov_mul_true
	cov_mul_true  = numpy.array( [ 0.35, - 0.1, - 0.1, - 0.1 ] )
	#
	# beta_all_true
	beta_all_true = numpy.matmul(covariates, cov_mul_true)
	#
	# p_fun_true
	p_fun_obj   = p_fun_class(beta_all_true)
	p_fun_true  = p_fun_obj.p_fun
	#
	# compute model for data
	#
	# initial_true: (must satisfy S + E + I = 1, R = D = 0)
	I_start      = 0.02
	E_start      = 0.02
	S_start      = 1.0 - E_start - I_start
	R_start      = 0.0
	D_start      = 0.0
	initial_true = numpy.array(
		[ S_start, E_start, I_start, R_start, D_start ]
	)
	#
	# noiseless simulated data
	seird_all_true = seird_model(t_all, p_fun_true, initial_true)
	if plot_truth :
		ax = pyplot.subplot(111)
		ax.plot(t_all, seird_all_true[:,0], 'b-', label='S')
		ax.plot(t_all, seird_all_true[:,1], 'g-', label='E')
		ax.plot(t_all, seird_all_true[:,2], 'r-', label='I')
		ax.plot(t_all, seird_all_true[:,3], 'k-', label='R')
		ax.plot(t_all, seird_all_true[:,4], 'y-', label='D')
		ax.legend()
		pyplot.show()
	#
	# actual_seed
	if random_seed == 0 :
		actual_seed = int( 13 * time.time() )
	else :
		actual_seed = random_seed
	random.seed(actual_seed)
	#
	# D_data
	D_true       = seird_all_true[:,4]
	Ddiff_true   = numpy.diff( D_true )
	mu           = Ddiff_true
	sigma        = death_data_cv * Ddiff_true
	Ddiff_data   = random.normalvariate(mu, sigma)
	D_data       = numpy.cumsum(Ddiff_data)
	D_data       = numpy.concatenate( ([0.0], D_data) )
	#
	# objective_ad
	objective_ad = objective_d_fun(t_all, D_data)
	#
	# objective: fun, grad, hess
	optimize_fun = optimize_fun_class(objective_ad)
	#
	# x_true
	E_0_true = initial_true[1]
	I_0_true = initial_true[2]
	x_true   = numpy.concatenate( (cov_mul_true, [ E_0_true, I_0_true ]) )
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
	x_hat   = result.x
	for i in range(x_true.size) :
		rel_error = x_hat[i] / x_true[i] - 1.0
		# print( x_true[i], x_hat[i], rel_error)
		ok        = ok and abs(rel_error) < (1e-5 + death_data_cv )
	#
	if not ok :
		msg  = 'covid_19_xam: Correctness test failed, '
		msg += 'actual random seed = ' + str(actual_seed)
		print( msg )
		call_count += 1
		if call_count < 2 and random_seed == 0 :
			ok = covid_19_xam(call_count)
	return ok
# END_PYTHON
