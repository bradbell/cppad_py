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
#	seirwd
#	Covariates
#	Covariate
#	cv
#	sim
#	rel
#	std
#	optimizer
# $$
#
# $section Example Fitting an SEIRWD Model for Covid-19$$
#
# $head Model$$
# We use the $cref/seirwd/numeric_seirwd_model/$$ model and notation.
#
# $head Covariates$$
# In this example there are two covariates that
# affect the infectious rate $latex \beta$$:
# social mobility $latex c_0 (t)$$, and Covid-19 testing $latex c_1 (t)$$.
# The covariates are known functions of time.
# The mobility covariate has been shifted and scaled
# so it is in the interval [-1, 0].
# The testing covariate has been shifted and scaled
# so it is in the interval [0, 1].
# Note that the maximum mobility and the minimum testing corresponds to the
# normal (baseline) condition.
#
# $head beta(t)$$
# Our model for the infectious rate is
# $latex \[
#	\beta(t) = \bar{\beta} \left( 1 + m_0 c_0 (t) + m_1 c_1 (t) \right)
# \] $$
# where $latex \bar{\beta}$$ is the baseline value for the infectious rate,
# $latex m_0$$ is the social covariate multiplier, and
# $latex m_1$$ is the Covid-19 testing covariate multiplier.
# The baseline value $latex \bar{\beta}$$ is the infectious rate corresponding
# to all the covariates being zero.
# The covariate multipliers, and the baseline infectious rate, are unknown.
#
# $subhead Constraint$$
# The rate $latex \beta(t)$$ cannot be negative; i.e.,
# $latex \[
#	0 \leq \bar{\beta} \left( 1 + m_0 c_0 (t) + m_1 c_1 (t) \right)
# \] $$
# We are using piecewise linear interpolation of the covariates,
# it is sufficient to enforce this constraint at each of the knots.
# This could lead to huge number of constraints.
# We instead take a refinement approach.
# We start by solving the optimization problem with no $latex \beta(t)$$
# constraints.
# If the minimum value of $latex \beta(t)$$
# corresponding to the optimal solution is negative,
# add a constraint at the time where the minimum occurs,
# repeat the optimization,  and
# check the new minimum value of $latex \beta(t)$$.
#
# $head Other Rates$$
# The other rates
# $latex \sigma(t)$$,
# $latex \gamma(t)$$,
# $latex \xi(t)$$,
# $latex \chi(t)$$,
# $latex \delta(t)$$,
# constant functions with known values:
# $srccode%py%
sigma_known  = 0.2
gamma_known  = 0.05
chi_known    = 0.01
xi_known     = 0.00
delta_known  = 0.1
# %$$
#
# $head Initial Values$$
# The initial size of the Recovered group $latex R(0)$$
# and of the Death group $latex D(0)$$ is zero.
# We use fraction of the total population for sizes, so the sum of the
# other initial values is one.
# We treat the initial
# Infected group $latex I(0)$$, and
# Will die group $latex W(0)$$,
# as unknown parameters in the model.
# We would like to also solve for the initial exposed population but
# that model has identifiability problems, so
# we use the following approximation for the initial exposed group
# $latex \[
#	E(0) = I(0) \gamma / \sigma
# \]$$
# The initial Susceptible group $latex S(0)$$ is
# expressed as a function of the other initial conditions:
# $latex \[
#	S(0) = 1 - E(0) - I(0) - W(0)
# \] $$
#
# $head Unknown Parameters$$
# In summary, the unknown parameter vector in this model is
# $latex \[
#	x = [ m_0, m_1, I(0), W(0), \bar{\beta} ]
# \] $$
# $srccode%py%
x_name = [ 'm_mobility', 'm_testing', 'I(0)', 'W(0)', 'beta_bar' ]
# %$$
#
# $head Bounds$$
# The infection rate $latex \beta(t)$$ must be non-negative; i.e.,
# $latex \[
#	0 \leq \bar{\beta} \left( 1 + m_0 c_0 (t) + m_1 c_1 (t) \right)
# \] $$
# is true for all $latex t$$.
# Recalling that $latex -1 \leq c_0 (t) \leq 0$$ and
# $latex 0 \leq c_1 (t) \leq 1$$ for all $latex t$$.
# The function constraint above is approximation by the following bounds:
# $latex \[
#	\begin{array}{lcr}
#	0   &  \leq & \bar{\beta }   \\
#	m_0 &  \leq & 1              \\
#	-1  & \leq  & m_1
#	\end{array}
# \] $$
# We also include the following bounds to help the optimizer:
# $latex I(0), W(0), m_0$$ are all non-negative and $latex m_1 \leq 0$$.
#
# $head Data$$
# The data in this model is the cumulative number of deaths,
# as a fraction of the total population and as a function of time.
# We assume that new deaths are recorded for time intervals
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
# $head Display Fit Results$$
# If you set this variable to True,
# a printout and a plot of the fit results is generated.
# $srccode%py%
display_fit = False
# %$$
#
# $subhead Plot$$
# There are three plots all with time on the x-axis.
# The first contains the size for all the compartments, except S,
# as a fraction of the total population.
# The second contains the model and data for the death difference values.
# The third contains the weighted residuals corresponding to the death
# difference data.
#
# $subhead Printout$$
# If $icode data_file$$ is not empty,
# the fit result for the unknown parameters are printed.
# If $icode data_file$$ is empty,
# a table is printed with the following columns:
# $table
# $icode x_sim$$     $cnext known parameter value used during simulation $rnext
# $icode x_fit$$     $cnext fit result for the unknown parameter         $rnext
# $icode rel_error$$ $cnext relative error for fit versus simulation     $rnext
# $icode std_error$$ $cnext asymptotic standard error for the parameter  $rnext
# $icode residual$$  $cnext
#	$icode std_error$$ weighted residual for fit versus simulation
# $tend
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
# If $icode death_data_cv$$ is zero, $latex \lambda = 1$$, otherwise
# $latex \lambda$$ is equal to $icode death_data_cv$$.
# Let $latex y_i$$ be the i-th value for the cumulative death data.
# The weighted residuals (some times referred to as just the residuals) are
# $latex \[
#	r_i = \frac{ ( y_{i+1} - y_i ) - [ D( t_{i+1} ) - D( t_i ) ] }{
#	\lambda ( y_{i+1} - y_i ) }
# \] $$
# where # $latex D(t)$$ is the model for the cumulative data
# given the fit results.
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
# $head Data File$$
# If the data file name is the empty string, the cumulative death data,
# and corresponding covariates, are created by the program.
# Otherwise, the data file must be a CSV file with the following columns:
# $icode day$$, $icode death$$, $icode mobility$$, $icode testing$$.
# In this case the data file is used for the
# cumulative death and corresponding covariates.
# $srccode%py%
data_file = '/home/bradbell/trash/covid_19/seirwd.csv' # example file name
data_file = ''                                         # empty string
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
from matplotlib import gridspec
import scipy.optimize
import numpy
import random
import time
import csv
import copy
#
import cppad_py
from optimize_fun_class import optimize_fun_class
from seirwd_model import seirwd_model
#
# t_all, covariates
if data_file != '' :
	# getting cumulative death and covariates from data_file
	file_in   = open(data_file, 'r')
	file_data = list()
	reader    = csv.DictReader(file_in)
	for row in reader :
		file_data.append(row)
	file_in.close()
	n_time       = len(file_data)
	t_all        = numpy.empty(n_time, dtype=float)
	covariates   = numpy.empty( (n_time, 2) )
	for i in range(n_time) :
		t_all[i]        = float( file_data[i]['day'] )
		covariates[i,0] = float( file_data[i]['mobility'] )
		covariates[i,1] = float( file_data[i]['testing'] )
else :
	# simulating cumulative death and covariates
	t_start = 0.0
	t_stop  = 60.0
	t_step  = 0.5
	t_all = numpy.arange(t_start, t_stop, t_step)
	#
	n_time = t_all.size
	covariates   = numpy.empty( (n_time, 2) )
	for i in range(n_time) :
		t               = t_all[i]
		mobility        = 0.0 if t < 10.0 else -1.0
		testing         = t / t_stop
		covariates[i,:] = [ mobility, testing ]
#
# mobility in [-1, 0]
assert numpy.all( covariates[:,0] <= 0.0 )
assert numpy.all( -1.0 <= covariates[:,0] )
#
# testing in [0, 1]
assert numpy.all( 0.0 <= covariates[:,1] )
assert numpy.all( covariates[:,0] <= 1.0 )
#
# beta_bar_sim
beta_bar_sim = 1.0
#
# covariate multipliers used in simulation
m_mobility_sim    =   0.5
m_testing_sim     = - 0.4
#
# initial conditions used to simulate data
I0_sim     = 0.00002
W0_sim     = 0.00002
E0_sim     = I0_sim * gamma_known / sigma_known
S0_sim     = 1.0 - E0_sim - I0_sim - W0_sim
R0_sim     = 0.0
D0_sim     = 0.0
#
# x_sim
x_sim = numpy.array( [
	m_mobility_sim, m_testing_sim, I0_sim, W0_sim, beta_bar_sim
] )
#
#
# actual_seed
# see begining of covid_19_xam function.
actual_seed = [ random_seed ]
#
# p_fun_class
# Returns the parameters in the ODE (not the unknown parameters)
class p_fun_class :
	def __init__(self, beta_all, other_rate) :
		self.beta_all   = beta_all
		self.other_rate = other_rate
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
		beta      = left * self.beta_all[i] + right * self.beta_all[ip]
		p         = copy.copy(self.other_rate)
		p['beta'] = beta
		return p
#
def x2seirwd_all(x) :
	#
	# unpack x
	cov_mul            = x[0 : 2]
	[I0, W0, beta_bar] = x[2 : 5]
	#
	# beta_all
	beta_all = beta_bar * (1.0 + numpy.matmul(covariates, cov_mul))
	#
	# other_rate
	other_rate = {
		'sigma' : sigma_known,
		'gamma' : gamma_known,
		'chi'   : chi_known,
		'xi'    : xi_known,
		'delta' : delta_known,
	}
	#
	# initial
	E0 = I0 * gamma_known / sigma_known
	S0 = 1.0 - E0 - I0 - W0
	R0 = 0.0
	D0 = 0.0
	initial  = numpy.array( [S0, E0, I0, R0, W0, D0] )
	#
	# p_fun
	p_fun_obj = p_fun_class(beta_all, other_rate)
	p_fun     = p_fun_obj.p_fun
	#
	# seirwd_all
	n_step = 2
	seirwd_all = seirwd_model(t_all, p_fun, initial, n_step)
	#
	return seirwd_all
#
def weighted_residual(D_data, D_model) :
	Ddiff_data   = numpy.diff(D_data)
	Ddiff_model  = numpy.diff(D_model)
	residual     = (Ddiff_data - Ddiff_model) / Ddiff_data
	if death_data_cv > 0.0 :
		residual = residual / death_data_cv
	return residual
#
# objective_d_fun
# t_all and D_data, are constants relative to the objective function
def objective_d_fun(t_all, D_data) :
	#
	n_x = len(x_name)
	x   = 0.1 * numpy.ones(n_x)
	ax  = cppad_py.independent(x)
	#
	# compute model for data
	aseirwd_all = x2seirwd_all(ax)
	#
	# Model for the cumulative death as function of time
	aD_model   = aseirwd_all[:,5] # column order is S, E, I, R, W, D
	#
	# compute negative log Gaussian likelihood dropping variance terms
	# because they are constaint w.r.t the unknown parameters
	aresidual = weighted_residual(D_data, aD_model)
	aloss     = 0.5 * numpy.sum( aresidual * aresidual)
	aloss     = numpy.array( [ aloss ] )
	#
	objective_ad = cppad_py.d_fun(ax, aloss)
	return objective_ad
#
def simulate_data() :
	#
	# noiseless simulated data
	seirwd_all_sim = x2seirwd_all(x_sim)
	#
	# rng: numpy random number generator
	rng = numpy.random.default_rng(seed = actual_seed[0])
	#
	# D_data
	D_sim       = seirwd_all_sim[:,5]
	Ddiff_sim   = numpy.diff( D_sim )
	std         = death_data_cv * Ddiff_sim
	noise       = std * rng.standard_normal(size = t_all.size - 1)
	Ddiff_data  = Ddiff_sim + noise
	D_data      = numpy.cumsum(Ddiff_data)
	D_data      = numpy.concatenate( ([0.0], D_data) )
	#
	return D_data

def random_start(n_random, x_lower, x_upper, log_scale, objective, A) :
	# check beta constraints
	def feasible(x) :
		nr, nc = A.shape
		if nr == 0 :
			return True
		return all( -1.0 <= numpy.matmul(A, x) )
	#
	n_x      = len(x_lower)
	#
	x_best   = (x_lower + x_upper) / 2.0
	obj_best = objective(x_best)
	#
	x_low    = copy.copy(x_lower)
	x_up     = copy.copy(x_upper)
	for j in range(n_x) :
		if log_scale[j] :
			x_low[j] = numpy.log(x_lower[j])
			x_up[j]  = numpy.log(x_upper[j])
	#
	# rng: numpy random number generator
	rng = numpy.random.default_rng(seed = actual_seed[0])
	#
	for i in range(n_random) :
		x_current   = rng.uniform(x_low, x_up)
		for j in range(n_x) :
			if log_scale[j] :
				x_current[j] = numpy.exp(x_current[j])
		if feasible(x_current) :
			obj_current = objective(x_current)
			if obj_current < obj_best :
				# print( 'sample # =', i, ', objective = ', obj_current)
				x_best = x_current
				obj_best = obj_current
	#
	return x_best

def display_fit_results(x_fit, std_error, D_data) :
	n_x = len(x_fit)
	# -----------------------------------------------------------------------
	# printout
	if data_file != '' :
		for j in range( n_x ) :
			print( '{:<15s}={:>+11.7f}'.format( x_name[j], x_fit[j] ) )
	else :
		fmt = '{:<15s}{:>11s}{:>11s}{:>11s}{:>11s}{:>11s}'
		line = fmt.format(
			'', 'x_sim','x_fit','rel_error','std_error','residual'
		)
		print(line)
		for i in range( n_x ) :
			if x_sim[i] == 0.0 :
				rel_error = 0.0
			else :
				rel_error = x_fit[i] / x_sim[i] - 1.0
			residual  = (x_fit[i] - x_sim[i]) / std_error[i]
			fmt = '{:<15s}{:+11.7f}{:+11.7f}{:+11.7f}{:+11.7f}{:+11.7f}'
			line = fmt.format(x_name[i],
				x_sim[i], x_fit[i], rel_error, std_error[i], residual
			)
			print(line)
	# -----------------------------------------------------------------------
	# plot
	# -----------------------------------------------------------------------
	#
	# seirwd_all_fit
	seirwd_all_fit = x2seirwd_all(x_fit)
	#
	# D_fit
	D_fit = seirwd_all_fit[:,5]
	#
	# residual_fit
	residual_fit = weighted_residual(D_data, D_fit)
	#
	fig  = pyplot.figure(tight_layout = True)
	gs   = gridspec.GridSpec(3, 2)
	ax1  = fig.add_subplot(gs[:,0])
	ax2  = fig.add_subplot(gs[0,1])
	ax3  = fig.add_subplot(gs[1,1])
	ax4  = fig.add_subplot(gs[2,1])
	#
	ax1.plot(t_all, seirwd_all_fit[:,1], 'g-', label='E')
	ax1.plot(t_all, seirwd_all_fit[:,2], 'r-', label='I')
	ax1.plot(t_all, seirwd_all_fit[:,3], 'k-', label='R')
	ax1.plot(t_all, seirwd_all_fit[:,4], 'y-', label='W')
	ax1.plot(t_all, seirwd_all_fit[:,5], 'b-', label='D')
	ax1.legend()
	ax1.set_xlabel('time')
	ax1.set_ylabel('population fraction')
	#
	Ddiff_data = numpy.diff(D_data)
	Ddiff_fit  = numpy.diff(D_fit)
	t_mid      = (t_all[0 : -1] + t_all[1 :]) / 2.0
	ax2.plot(t_mid, Ddiff_data, 'k+' , label='data')
	ax2.plot(t_mid, Ddiff_fit,  'k-' , label='fit')
	ax2.legend()
	ax2.set_ylabel('death differences')
	#
	ax3.plot( t_mid,                 residual_fit,   'k+' )
	ax3.plot( [t_all[0], t_all[-1]], [0.0, 0.0], 'k-' )
	ax3.set_ylabel('weighted residuals')
	#
	cov_mul  = x_fit[0 : 2]
	beta_bar = x_fit[4]
	beta_all = beta_bar * (1.0 + numpy.matmul(covariates, cov_mul))
	ax4.plot(t_all, beta_all, 'k-')
	ax4.set_xlabel('time')
	ax4.set_ylabel('beta(t)')
	#
	pyplot.show()

def new_beta_positive_constraint(x_fit, A_fit) :
	nr, nc = A_fit.shape
	assert nc == len(x_fit)
	#
	cov_mul  = x_fit[0 : 2]
	beta_bar = x_fit[4]
	beta_all = beta_bar * (1.0 + numpy.matmul(covariates, cov_mul))
	#
	i_min    = numpy.argmin(beta_all)
	beta_min = beta_all[i_min]
	if 0.0 <= beta_min :
		return A_fit
	#
	# covariates at time of minimum
	c0_min = covariates[i_min,0]
	c1_min = covariates[i_min,1]
	#
	# new row to add to A
	new_row  = [ c0_min, c1_min, *( (nc-2) * [ 0.0 ] ) ]
	#
	A_new    = numpy.empty( (nr+1,nc), dtype=float )
	if nr > 0 :
		A_new[0:nr,:] = A_fit
	A_new[nr, :]  = new_row
	#
	return A_new

def covid_19_xam(call_count = 0) :
	ok = True
	#
	# if random seed is zero, seed of the cloce
	if random_seed == 0 :
		actual_seed = [ int( 13 * time.time() ) ]
	#
	# D_data
	if data_file == '' :
		D_data = simulate_data()
	else :
		D_data = list()
		for row in file_data :
			D_data.append( float( row['death'] ) )
		D_data = numpy.array(D_data)
	#
	# objective_ad
	objective_ad = objective_d_fun(t_all, D_data)
	#
	# objective: fun, grad, hess
	optimize_fun = optimize_fun_class(objective_ad)
	#
	# options
	options = {
		'gtol'    : 1e-10,
		'xtol'    : 1e-8,
		'maxiter' : 300,
		'verbose' : 0,
	}
	# -----------------------------------------------------------------------
	# bounds
	n_x = len(x_name)
	x_lower    = numpy.zeros( n_x, dtype=float)
	x_upper    = x_sim * 10.0
	#
	# 0 <= m_0 <= 1
	x_upper[0] = 1.0
	#
	# -1 <= m_1 <= 0
	x_lower[1] = -1.0
	x_upper[1] = 0.0
	#
	# currently not using log-scaling
	log_scale    = numpy.array( n_x * [ False ] )
	#
	assert numpy.all( x_lower <= x_sim )
	assert numpy.all( x_sim <= x_upper )
	#
	bounds = scipy.optimize.Bounds(
		x_lower,
		x_upper,
		keep_feasible = True
	)
	# ------------------------------------------------------------------------
	# optimizer loop over beta constraints
	constraints  = list()
	optimal      = False
	A_fit        = numpy.empty( (0, n_x), dtype = float )
	x_fit        = None
	while ok and not optimal :
		# start_point
		n_random    = 2000
		start_point = random_start(
			n_random,
			x_lower,
			x_upper,
			log_scale,
			optimize_fun.objective_fun,
			A_fit,
		);
		# run optimizer
		result = scipy.optimize.minimize(
			optimize_fun.objective_fun,
			start_point,
			method        = 'trust-constr',
			jac           = optimize_fun.objective_grad,
			hess          = optimize_fun.objective_hess,
			constraints   = constraints,
			options       = options,
			bounds        = bounds,
		)
		# check optimizer status
		ok = ok and result.success
		# print('objective = ', result.fun )
		if ok :
			# check beta(t) >= 0
			x_fit   = result.x
			A_new   = new_beta_positive_constraint(x_fit, A_fit)
			optimal = A_new.shape == A_fit.shape
			if not optimal :
				# add a new constraint and repeat
				nr, nc   = A_new.shape
				c_lower  = numpy.array( nr * [ -1.0 ] )
				c_upper  = numpy.array( nr * [ numpy.inf ] )
				linear_constraint = scipy.optimize.LinearConstraint(
					A_new, c_lower, c_upper, keep_feasible = True
				)
				constraints = [linear_constraint]
				A_fit       = A_new
	#
	# H: the observed infromation matrix
	H = optimize_fun.objective_hess(x_fit)
	#
	# Hinv: approxiamtion for covariance of the estimate x_fit
	Hinv = numpy.linalg.inv(H)
	#
	# standard devaition for each component of x_fit
	std_error = numpy.sqrt( numpy.diag(Hinv) )
	#
	# seirwd_all_fit
	seirwd_all_fit = x2seirwd_all(x_fit)
	#
	# D_fit
	D_fit = seirwd_all_fit[:,5]
	#
	# residual_fit
	residual_fit = weighted_residual(D_data, D_fit)
	#
	# check that all the data residuals an less than 3.0
	ok  = ok and numpy.all( numpy.abs( residual_fit ) < 3.0 )
	#
	# compare fit to simulation truth
	if data_file == '' :
		for i in range( n_x ) :
			if x_sim[i] == 0.0 :
				rel_error = 0.0
			else :
				rel_error = x_fit[i] / x_sim[i] - 1.0
			residual  = (x_fit[i] - x_sim[i]) / std_error[i]
			if death_data_cv > 0.0 :
				# check that all the weighted residuals are less than two
				ok = ok and abs(residual) < 2.0
			else :
				# check for perfect fit
				ok = ok and abs(rel_error) < 1e-5
		#
		if not ok :
			msg  = 'covid_19_xam: Correctness test failed, '
			msg += 'actual random seed = ' + str(actual_seed[0])
			print( msg )
			call_count += 1
			if call_count < 2 and random_seed == 0 :
				print( 're-trying with a differenent random seed')
				ok = covid_19_xam(call_count)
	#
	# check conservation of mass in the compartmental model
	sum_all_fit = numpy.sum(seirwd_all_fit, axis=1)
	eps99       = 99.0 * numpy.finfo(float).eps
	ok          = ok and max( abs(sum_all_fit - 1.0) ) < eps99
	#
	# display_fit_results
	if display_fit :
		display_fit_results(x_fit, std_error, D_data)
	#
	return ok
# END_PYTHON
