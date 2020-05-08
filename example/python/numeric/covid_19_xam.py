# -----------------------------------------------------------------------------
#         cppad_py: A C++ Object Library and Python Interface to Cppad
#          Copyright (C) 2017-20 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# -----------------------------------------------------------------------------
# $begin numeric_covid_19_xam.py$$ $newlinech #$$
#
# $section Example Fitting an SEIRS Model$$
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
import copy
import cppad_py
import runge4
from optimize_fun_class import optimize_fun_class
from seirs_model import seirs_model
#
# t_all
t_init    = 0.0
t_final   = 50.0
n_point   = 40
t_all     = numpy.linspace(t_init, t_final, n_point)
#
#
# p_fun_class
class p_fun_class :
	def __init__(self, beta_all) :
		self.beta_all = beta_all
	#
	def p_fun(self, t) :
		i = 0
		while i < len(t_all) - 1 and t_all[i + 1] < t :
			i += 1
		# linear interpolation coefficients
		ip     = i + 1
		t_diff = t_all[ip] - t_all[i]
		left   = ( t_all[ip] - t ) / t_diff
		right  = ( t - t_all[i]  ) / t_diff
		# only beta changes with time not continuous at all points in t_all
		# and smooth for times not in t_all
		beta   = left * self.beta_all[i] + right * self.beta_all[ip]
		p      = {
			'beta'  : beta,
			'sigma' : 1.0 / 5.0,
			'gamma' : 1.0 / 20.0,
			'chi'   : 1.0 / 365.0,
			'xi'    : 0.0
		}
		return p
#
# beta_all
def beta_all_fun(beta_vec) :
	n_point  = t_all.size;
	beta_all = numpy.empty( n_point, dtype=type( beta_vec[0] ) )
	for i in range(n_point) :
		if t_all[i] <= 15 :
			beta_all[i] = beta_vec[0]
		elif t_all[i] <= 30 :
			beta_all[i] = beta_vec[1]
		else :
			beta_all[i] = beta_vec[2]
	return beta_all
#
# objective_d_fun
def objective_d_fun(t_all, I_data) :
	#
	# x = ( beta[0], beta[1]. beta[2], S[0], E[0], I[0], R[0] )
	x  = numpy.ones(7)
	ax = cppad_py.independent(x)
	#
	# abeta_all
	abeta_all  = beta_all_fun( ax[0:3] )
	#
	# ainitial
	ainitial  = ax[3:7]
	#
	# p_fun
	ap_fun_obj = p_fun_class(abeta_all)
	ap_fun    = ap_fun_obj.p_fun
	#
	# compute model for data
	aseir_all = seirs_model(t_all, ap_fun, ainitial)
	#
	# Only have I(t) data.
	aI_model  = aseir_all[:,2] # S=0, E=1, I=2, R=3
	#
	# compute Gaussian loss function
	aresidual = I_data - aI_model
	aloss     = numpy.sum( aresidual * aresidual)
	aloss     = numpy.array( [ aloss ] )
	#
	objective_ad = cppad_py.d_fun(ax, aloss)
	return objective_ad

def covid_19_xam() :
	ok = True
	#
	# beta_all_true
	beta_vec_true = numpy.array( [ 0.1, 0.2, 0.3 ] )
	beta_all_true = beta_all_fun( beta_vec_true )
	#
	# p_fun_true
	p_fun_obj   = p_fun_class(beta_all_true)
	p_fun_true  = p_fun_obj.p_fun
	#
	# compute model for data
	#
	# initial_true
	I_start      = 0.02
	E_start      = 0.02
	R_start      = 0.10
	S_start      = 1.0 - E_start - I_start - R_start
	initial_true = numpy.array( [ S_start, E_start, I_start, R_start ] )
	#
	# noiseless simulated data
	seir_all_true = seirs_model(t_all, p_fun_true, initial_true)
	if False :
		ax = pyplot.subplot(111)
		ax.plot(t_all, seir_all_true[:,0], 'b-', label='S')
		ax.plot(t_all, seir_all_true[:,1], 'g-', label='E')
		ax.plot(t_all, seir_all_true[:,2], 'r-', label='I')
		ax.plot(t_all, seir_all_true[:,3], 'k-', label='R')
		ax.legend()
		pyplot.show()
	#
	# objective function for fitting y_init and ode_p to data
	I_data = seir_all_true[:,2]
	objective_ad = objective_d_fun(t_all, I_data)
	#
	# objective: fun, grad, hess
	optimize_fun = optimize_fun_class(objective_ad)
	#
	# bounds
	x_true      = numpy.concatenate( (beta_vec_true, initial_true) )
	lower_bound = x_true / 5.0
	upper_bound = x_true * 5.0
	lower_bound[-1] = x_true[-1] # Constrain initial R because data
	upper_bound[-1] = x_true[-1] # is not sensitive to it
	bounds = scipy.optimize.Bounds(
		lower_bound,
		upper_bound,
		keep_feasible = True
	)
	options = {
		'gtol'    : 1e-9,
		'xtol'    : 1e-8,
		'maxiter' : 300,
		'verbose' : 0,
	}
	start_point = x_true / 2.0
	result = scipy.optimize.minimize(
		optimize_fun.objective_fun,
		start_point,
		method  = 'trust-constr',
		jac     = optimize_fun.objective_grad,
		hess    = optimize_fun.objective_hess,
		options = options,
		bounds  = bounds,
	)
	ok      = ok and result.success
	x_hat   = result.x
	for i in range(7) :
		rel_error = x_hat[i] / x_true[i] - 1.0
		ok        = ok and abs(rel_error) < 1e-5
	#
	return ok
# END_PYTHON
