# -----------------------------------------------------------------------------
#         cppad_py: A C++ Object Library and Python Interface to Cppad
#          Copyright (C) 2017-20 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# -----------------------------------------------------------------------------
# $begin seirs$$
#
# $section A Covid-19 SEIRS Model$$
#
# $latex \[
# \begin{array}{rcl}
# \dot{S}(t) & = & - \beta(t) S(t) I(t) + \xi R(t)    \\
# \dot{E}(t) & = & + \beta(t) S(t) I(t) - \sigma E(t) \\
# \dot{I}(t) & = & + \sigma E(t) - \gamma  I(t) \\
# \dot{R}(t) & = & + \gamma I(t)
# \end{array}
# \] $$
#
#
# \end{array}
# \] $$
#
# $end

from pdb import set_trace
from matplotlib import pyplot
import scipy.optimize
import numpy
import copy
import cppad_py

def runge4(fun, y0, t, h) :
	k1     = h * fun(t,           y0)
	k2     = h * fun(t + h / 2.0, y0 + k1 / 2.0)
	k3     = h * fun(t + h / 2.0, y0 + k2 / 2.0)
	k4     = h * fun(t + h,       y0 + k3 )
	y1     = y0 + (k1 + 2.0 * k2 + 2.0 * k3 + k4) / 6.0
	return y1

def solve_ode(fun, t_all, y_init ) :
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
		y1            = runge4(fun, y0, t0, t_step)
		y_all[i+1,:]  = copy.copy(y1)
	return y_all

class seirs :
	def set_ode_p(self, ode_p) :
		self.ode_p = ode_p

	def set_t_all(self, t_all) :
		self.t_all = t_all

	def set_y_init(self, y_init) :
		self.y_init = y_init

	def ode(self, t, c_vec) :
		S      = c_vec[0]
		E      = c_vec[1]
		I      = c_vec[2]
		R      = c_vec[3]
		beta   = self.ode_p[0]
		sigma  = self.ode_p[1]
		gamma  = self.ode_p[2]
		xi     = self.ode_p[3]
		Sdot   = - beta * S * I - xi * R
		Edot   = + beta * S * I - sigma * E
		Idot   = + sigma * E - gamma * I
		Rdot   = + gamma * I - xi * R
		return numpy.array([ Sdot, Edot, Idot, Rdot])

	def model(self) :
		y_all     = solve_ode(self.ode, self.t_all, self.y_init)
		return y_all

def objective_d_fun(t_all, I_data) :
	#
	# 8 variables, 4 in ode_p, 4 in y_init
	x  = numpy.ones(8)
	ax = cppad_py.independent(x)
	#
	# x = concatenate( ode_p , y_init )
	aode_p   = ax[0:4]
	ay_init  = ax[4:8]
	#
	# set up seirs model
	seirs_obj = seirs()
	seirs_obj.set_t_all(t_all)
	seirs_obj.set_ode_p(aode_p)
	seirs_obj.set_y_init(ay_init)
	#
	# compute model for data
	ay_model = seirs_obj.model()
	#
	# model for the data
	aI_model  = ay_model[:,2] # S=0, E=1, I=2, R=3
	#
	# compute loss function
	aresidual = I_data - aI_model
	aloss     = numpy.sum( aresidual * aresidual)
	aloss     = numpy.array( [ aloss ] )
	#
	objective_ad = cppad_py.d_fun(ax, aloss)
	return objective_ad

def seirs_fit_xam() :
	ok = True
	#
	# parameter values used to simulate data
	seirs_obj = seirs()
	ode_p_true = [
		0.3,          # beta:  exposure rate
		1.0 / 5.0,    # sigma: on average 5 days from exposure to infectious
		1.0 / 20.0,   # gamma: on average 20 days from infectors to recovered
		0.0,          # xi: immunity is permanent
	]
	seirs_obj.set_ode_p(ode_p_true)
	t_init    = 0.0
	t_final   = 50.0
	n_step    = 40
	t_all     = numpy.linspace(t_init, t_final, n_step)
	seirs_obj.set_t_all(t_all)
	#
	I_start      = 0.01
	E_start      = I_start * ode_p_true[0] / ode_p_true[1]
	S_start      = 1.0 - E_start - I_start
	y_init_true  = numpy.array( [ S_start, E_start, I_start, 0.0 ] )
	seirs_obj.set_y_init(y_init_true)
	#
	# noiseless simulated data
	y_model    = seirs_obj.model()
	if False :
		ax = pyplot.subplot(111)
		ax.plot(t_all, y_model[:,0], 'b-', label='S')
		ax.plot(t_all, y_model[:,1], 'g-', label='E')
		ax.plot(t_all, y_model[:,2], 'r-', label='I')
		ax.plot(t_all, y_model[:,3], 'k-', label='R')
		ax.legend()
		pyplot.show()
	#
	# objective function for fitting y_init and ode_p to data
	I_data = y_model[:,2]
	objective_ad = objective_d_fun(t_all, I_data)
	#
	# objective: fun, jac, hes
	def objective_fun(x) :
		res = objective_ad.forward(0, x)
		return res[0]
	def objective_grad(x) :
		J = objective_ad.jacobian(x)
		return J.flatten()
	def objective_hess(x) :
		w = numpy.array( [ 1.0 ] )
		H = objective_ad.hessian(x, w)
		return H
	#
	# bounds
	x_true      = numpy.concatenate( (ode_p_true, y_init_true) )
	lower_bound = x_true / 5.0
	upper_bound = x_true * 5.0
	bounds = scipy.optimize.Bounds(
		lower_bound,
		upper_bound,
		keep_feasible = True
	)
	options = {
		'gtol'    : 1e-8,
		'xtol'    : 1e-8,
		'maxiter' : 300,
		'verbose' : 0,
	}
	start_point = x_true / 2.0
	result = scipy.optimize.minimize(
		objective_fun,
		start_point,
		method  = 'trust-constr',
		jac     = objective_grad,
		hess    = objective_hess,
		options = options,
		bounds  = bounds,
	)
	ok      = ok and result.success
	x_hat   = result.x
	for i in range(8) :
		if x_true[i] == 0.0 :
			rel_error = x_hat[i]
		else :
			rel_error = x_hat[i] / x_true[i] - 1.0
		ok = ok and abs(rel_error) < 1e-2
	#
	return ok
