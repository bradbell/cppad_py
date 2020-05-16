# -----------------------------------------------------------------------------
#         cppad_py: A C++ Object Library and Python Interface to Cppad
#          Copyright (C) 2017-20 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# -----------------------------------------------------------------------------
# $begin numeric_seirwd_model_xam.py$$ $newlinech #$$
# $spell
#	seris
# $$
#
# $section Example Using seris_model$$
#
# $srcthisfile%
#	0%# BEGIN_PYTHON%# END_PYTHON%1
# %$$
#
# $end
# BEGIN_PYTHON
import numpy
from seirwd_model import seirwd_model
from seirwd_model import check_seirwd_model
#
def seirwd_model_xam() :
	ok    = True
	#
	sigma = 1.0 / 5.0     # average 5 days between exposure and infectious
	gamma = 1.0 / 20.0    # average 20 days between infectious and recovered
	xi    = 1.0 / 365.0   # average 1 year of immunity
	chi   = gamma / 10.0  # probabiliy of death is 1/10 that of recovery
	delta = 1.0 / 10.0    # to days between no-longer infectious and death
	#
	# t_all
	t_all    = numpy.array( [ 0.0, 0.1, 0.2 ] )
	beta_all =  [ 0.30, 0.20, 0.10 ]
	#
	# p_all
	p_all    = list()
	for i in range(t_all.size) :
		p = {
			'beta'  : beta_all[i],
			'sigma' : sigma ,
			'gamma' : gamma ,
			'xi'    : xi ,
			'chi'   : chi ,
			'delta' : delta ,
		}
		p_all.append(p)
	#
	# initial
	I0  = 0.02
	E0  = 0.02
	R0  = 0.02
	S0  = 1.0 - I0 - E0 - R0
	W0  = 0.0
	D0  = 0.0
	initial  = numpy.array( [ S0, E0, I0, R0, W0, D0 ] )
	#
	# check derivatives for ODE needed for rosen3
	ok = ok and check_seirwd_model(t_all, p_all, initial)
	#
	# solve the ODE
	seirwd_all = seirwd_model(t_all, p_all, initial)
	#
	# check solution using midpoint values
	for i in range( len(t_all) - 1 ) :
		# midpoint values
		t_mid      = (t_all[i+1] + t_all[i]) / 2.0
		seirwd_mid = (seirwd_all[i,:] + seirwd_all[i+1,:]) / 2.0
		S, E, I, R, W, D = seirwd_mid
		#
		# differential equation
		p       = dict()
		for key in [ 'beta', 'sigma', 'gamma', 'xi', 'chi', 'delta' ] :
			p[key] = (p_all[i][key] + p_all[i+1][key]) / 2.0
		#
		dot     = numpy.empty( 6, dtype = float)
		dot[0]  = - p['beta'] *  S * I  + p['xi']   * R
		dot[1]  = + p['beta'] *  S * I - p['sigma'] * E
		dot[2]  = + p['sigma'] * E     - (p['gamma'] + p['chi']) * I
		dot[3]  = + p['gamma'] * I     - p['xi']    * R
		dot[4]  = + p['chi']   * I     - p['delta'] * W
		dot[5]  = + p['delta'] * W
		#
		# difference over interval
		seirwd_delta = seirwd_all[i+1,:] - seirwd_all[i,:]
		t_delta      = t_all[i+1]      - t_all[i]
		#
		check  = seirwd_delta / t_delta
		rel_error = dot / check - 1.0
		# print(rel_error)
		ok        = ok and all( abs(rel_error) < 1e-2 )
	#
	# now check solution using twice as many Runge-Kutta steps
	n_step      = 2
	seirwd_check = seirwd_model(t_all, p_all, initial, n_step)
	error       = seirwd_all - seirwd_check
	# print(error)
	ok          = ok and numpy.all( abs(error) < 1e-7 )
	#
	return ok
# END_PYTHON
