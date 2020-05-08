# -----------------------------------------------------------------------------
#         cppad_py: A C++ Object Library and Python Interface to Cppad
#          Copyright (C) 2017-20 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# -----------------------------------------------------------------------------
# $begin numeric_seirs_model_xam.py$$ $newlinech #$$
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
import seirs_model
from pdb import set_trace
#
def seirs_model_xam() :
	ok    = True
	#
	sigma = 1.0 / 5.0     # average 5 days between exposure and infectious
	gamma = 1.0 / 20.0    # average 20 days between infectious and recovered
	chi   = gamma / 50.0  # probabiliy of death is 1/50 that of recovery
	xi    = 1.0 / 365.0   # average 1 year of immunity
	#
	# t_all
	t_all = numpy.array( [ 0.0, 0.1, 0.2 ] )
	#
	# p_all
	p_all = {
		'beta'  :  [ 0.30, 0.20, 0.10 ],
		'sigma' : 3 * [ sigma ],
		'gamma' : 3 * [ gamma ],
		'chi'   : 3 * [ chi ],
		'xi'    : 3 * [ xi ],
	}
	#
	# p_fun
	def p_fun(t) :
		i = 0
		while i < len(t_all) - 1 and t_all[i + 1] < t :
			i += 1
		# linear interpolation coefficients
		ip     = i + 1
		t_diff = t_all[ip] - t_all[i]
		left   = ( t_all[ip] - t ) / t_diff
		right  = ( t - t_all[i]  ) / t_diff
		p      = dict()
		for key in [ 'beta', 'sigma', 'gamma', 'chi', 'xi' ] :
			p[key] = left * p_all[key][i] + right * p_all[key][ip]
		return p
	#
	# initial
	I_start  = 0.02
	E_start  = 0.02
	R_start  = 0.02
	S_start  = 1.0 - I_start - E_start - R_start
	initial  = numpy.array( [ S_start, E_start, I_start, R_start ] )
	#
	# solve the ODE
	seir_all = seirs_model.seirs_model(t_all, p_fun, initial)
	#
	# check solution using midpoint values
	for i in range( len(t_all) - 1 ) :
		# midpoint values
		t     = (t_all[i] + t_all[i+1]) / 2.0
		S     = (seir_all[i,0] + seir_all[i+1,0]) / 2.0
		E     = (seir_all[i,1] + seir_all[i+1,1]) / 2.0
		I     = (seir_all[i,2] + seir_all[i+1,2]) / 2.0
		R     = (seir_all[i,3] + seir_all[i+1,3]) / 2.0
		N     = S + E + I + R
		p     = p_fun(t)
		dot       = dict()
		dot['S']  = - p['beta'] * S * I / N + p['xi'] * R
		dot['E']  = + p['beta'] * S * I / N - p['sigma'] * E
		dot['I']  = + p['sigma'] * E        - (p['gamma'] + p['chi']) * I
		dot['R']  = + p['gamma'] * I        - p['xi'] * R
		#
		# difference over interval
		delta         = dict()
		delta['t']    = t_all[i+1]      - t_all[i]
		delta['S']    = seir_all[i+1,0] - seir_all[i,0]
		delta['E']    = seir_all[i+1,1] - seir_all[i,1]
		delta['I']    = seir_all[i+1,2] - seir_all[i,2]
		delta['R']    = seir_all[i+1,3] - seir_all[i,3]
		#
		for key in [ 'S', 'E', 'I', 'R' ] :
			check     = delta[key] / delta['t']
			rel_error = dot[key] / check - 1.0
			ok        = ok and abs(rel_error) < 1e-2
	return ok
# END_PYTHON
