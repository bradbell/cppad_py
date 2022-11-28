# -----------------------------------------------------------------------------
#         cppad_py: A C++ Object Library and Python Interface to Cppad
#          Copyright (C) 2017-22 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# -----------------------------------------------------------------------------
# BEGIN_PYTHON
import numpy
from ode_multi_step import ode_multi_step
from rosen3_step import rosen3_step
from runge4_step import runge4_step
from rosen3_step import check_rosen3_step
# -----------------------------------------------------------------------------
class fun_class :
   # ------------------------------------------------------------------------
   # init
   def __init__(self, t_all, p_all, n_step) :
      self.t_all  = t_all
      self.p_all  = p_all
      self.n_step = n_step
      self.index  = None
      self.p      = None
   # -----------------------------------------------------------------------
   # set_t_all_index
   def set_t_all_index(self, refine_index) :
      t_all_index  = int( numpy.floor( refine_index / self.n_step ) )
      self.index   = t_all_index
   # -----------------------------------------------------------------------
   # get_p
   def get_p(self, t, seirwd) :
      assert self.index != None
      t_all = self.t_all
      p_all = self.p_all
      index = self.index
      #
      # linearly interpolate the parameter values
      p      = dict()
      t_left = t_all[index]
      t_diff = t_all[index + 1] - t_left
      for key in ['alpha', 'beta', 'sigma', 'gamma', 'xi', 'chi', 'delta'] :
         p_left = p_all[index][key]
         p_diff = p_all[index + 1][key] - p_left
         p[key] = p_left + (t - t_left) * p_diff / t_diff
      #
      return p
   # -----------------------------------------------------------------------
   # get_p_t
   def get_p_t(self) :
      assert self.index != None
      t_all = self.t_all
      p_all = self.p_all
      index = self.index
      #
      # linearly interpolate the parameter values
      p_t    = dict()
      t_diff = t_all[index + 1] - t_all[index]
      for key in ['alpha', 'beta', 'sigma', 'gamma', 'xi', 'chi', 'delta'] :
         p_diff   = p_all[index + 1][key] - p_all[index][key]
         p_t[key] = p_diff / t_diff
      #
      return p_t
   # -----------------------------------------------------------------------
   # f
   def f(self, t, seirwd) :
      p                = self.get_p(t, seirwd)
      S, E, I, R, W, D = seirwd
      #
      Ia     = pow(I, p['alpha'])
      #
      # compute f(t, y)
      Sdot   = - p['beta']  *  S * Ia  + p['xi']    * R
      Edot   = + p['beta']  *  S * Ia  - p['sigma'] * E
      Idot   = + p['sigma'] * E        - (p['gamma'] + p['chi']) * I
      Rdot   = + p['gamma'] * I        - p['xi']    * R
      Wdot   = + p['chi']   * I        - p['delta'] * W
      Ddot   = + p['delta'] * W
      #
      return numpy.array([ Sdot, Edot, Idot, Rdot, Wdot, Ddot])
   # -----------------------------------------------------------------------
   # f_t
   def f_t(self, t, seirwd) :
      p                = self.get_p(t, seirwd)
      p_t              = self.get_p_t()
      S, E, I, R, W, D = seirwd
      #
      Ia     = pow(I, p['alpha'])
      #
      #
      Sdot_t   = - p_t['beta']  *  S * Ia  + p_t['xi']    * R
      Edot_t   = + p_t['beta']  *  S * Ia  - p_t['sigma'] * E
      Idot_t   = + p_t['sigma'] * E        - (p_t['gamma'] + p_t['chi']) * I
      Rdot_t   = + p_t['gamma'] * I        - p_t['xi']    * R
      Wdot_t   = + p_t['chi']   * I        - p_t['delta'] * W
      Ddot_t   = + p_t['delta'] * W
      return numpy.array([ Sdot_t, Edot_t, Idot_t, Rdot_t, Wdot_t, Ddot_t])
   # -----------------------------------------------------------------------
   # f_y
   def f_y(self, t, seirwd) :
      p                = self.get_p(t, seirwd)
      S, E, I, R, W, D = seirwd
      #
      Ia     = pow(I, p['alpha'])
      if p['alpha'] == 1.0 :
         Ia_I = 1.0
      else :
         Ia_I = p['alpha'] * pow(I, p['alpha'] - 1.0 )
      #
      ny     = 6
      type_y = type( seirwd[0] )
      zero   = type_y( 0.0 )
      J      = numpy.empty( (ny,ny), dtype = type_y )
      #
      # partials of Sdot(t, y) w.r.t. y
      Sdot_S   = - p['beta']  *  Ia
      Sdot_I   = - p['beta']  *  S * Ia_I
      Sdot_R   = + p['xi']
      J[0,:]   = [ Sdot_S, zero, Sdot_I, Sdot_R, zero, zero ]
      #
      # partial of Edot(t, y) w.r.t y
      Edot_S   = + p['beta']  *  Ia
      Edot_I   = + p['beta']  *  S * Ia_I
      Edot_E   =  - p['sigma']
      J[1,:]   = [ Edot_S, Edot_E, Edot_I, zero, zero, zero ]
      #
      # partial of Idot(t, y) w.r.t y
      Idot_E   = + p['sigma']
      Idot_I   = - (p['gamma'] + p['chi'])
      J[2,:]   = [ zero, Idot_E, Idot_I, zero, zero, zero ]
      #
      # partial Rdot(t, y) w.r.t y
      Rdot_I   = + p['gamma']
      Rdot_R   = - p['xi']
      J[3,:]   = [ zero, zero, Rdot_I, Rdot_R, zero, zero ]
      #
      # partial Wdot(t, y) w.r.t. y
      Wdot_I   = + p['chi']
      Wdot_W   = - p['delta']
      J[4,:]   = [ zero, zero, Wdot_I, zero, Wdot_W, zero ]
      #
      # partial Ddot(t, y) w.r.t y
      Ddot_W   = + p['delta']
      J[5,:]   = [ zero, zero, zero, zero, Ddot_W, zero ]
      #
      return J
# -----------------------------------------------------------------------------
# check the fun derivatives required by rosen3_step
def test_fun_derivatives(t_all, p_all, initial) :
   ok     = True
   n_step = 1
   fun  = fun_class(t_all, p_all, n_step)
   index  = 0
   fun.set_t_all_index(index)
   ti   = t_all[index]
   yi   = initial
   h    = t_all[index + 1] - t_all[index]
   ok   = ok and check_rosen3_step(fun, ti, yi, h)
   return ok
# -----------------------------------------------------------------------------
# seriwd_model
def seirwd_model(method, t_all, p_all, initial, n_step = 1) :
   for i in range( len(t_all) - 1 ) :
      assert p_all[i+1]['alpha'] == p_all[0]['alpha']
   #
   fun      = fun_class(t_all, p_all, n_step)
   if method == 'runge4' :
      one_step = runge4_step
   elif method == 'rosen3' :
      one_step = rosen3_step
   else :
      assert False
   if n_step == 1 :
      seirwd_all  = ode_multi_step(one_step, fun, t_all, initial)
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
      seirwd_refine   = ode_multi_step(one_step, fun, t_refine, initial)
      index_all   = [ i * n_step for i in range(len(t_all)) ]
      seirwd_all   = seirwd_refine[ index_all ]
   #
   return seirwd_all
# END_PYTHON
#
#
# {xrst_begin numeric_seirwd_model}
# {xrst_spell
#     interpolated
#     linearly
#     rcll
#     runge
#     seirwd
# }
# {xrst_comment_ch #}
#
#
# A Susceptible Exposed Infectious Recovered and Death Model
# ##########################################################
#
# Purpose
# *******
# This routine can be used with ``ad_double`` .
#
# Syntax
# ******
#
# | *seirwd_all* =  ``seirwd_model`` (
# | |tab| *method* , *t_all* , *p_all* , *initial* , *n_step* = 1
# | )
#
# Notation
# ********
#
# .. csv-table::
#  :widths: 4, 34
#
#  :math:`S(t)`, size of the Susceptible group
#  :math:`E(t)`, size of the Exposed group
#  :math:`I(t)`, size of the Infectious group
#  :math:`R(t)`, size Recovered group
#  :math:`W(t)`, size of the group that will die
#  :math:`D(t)`, size of the group that has died
#  :math:`\alpha(t)`, infectious group size exponent
#  :math:`\beta(t)`, infectious rate
#  :math:`\sigma(t)`, incubation rate
#  :math:`\gamma(t)`, recovery rate
#  :math:`\xi(t)`, loss of immunity rate
#  :math:`\chi(t)`, excess mortality rate
#  :math:`\delta(t)`, delay between infectious and death
#
# ODE
# ***
# The ordinary differential equation for this model is:
#
# .. math::
#
#    \begin{array}{rcll}
#    \dot{S} & = & - \beta  S I^\alpha  & + \xi    R             \\
#    \dot{E} & = & + \beta  S I^\alpha  & - \sigma E             \\
#    \dot{I} & = & + \sigma E           & - ( \gamma + \chi )  I \\
#    \dot{R} & = & + \gamma I           & - \xi    R             \\
#    \dot{W} & = & + \chi   I           & - \delta W             \\
#    \dot{D} & = & + \delta W           &
#    \end{array}
#
# where we dropped the time dependence in the equations above.
# This model does not account for death by other causes.
# It is similar to the standard
# `SEIRS <https://www.idmod.org/docs/hiv/model-seir.html>`_ model
# with the following differences:

# #. The total population :math:`N` is not included in this model,
#    so the units for :math:`\beta` are different.
# #. This model tracks death due to the condition using the compartments W and D.
#
# method
# ******
# This ``str`` must be either ``runge4`` or ``rosen3`` .
# It determines if :ref:`runge4_step<numeric_runge4_step-name>` or
# :ref:`rosen3_step<numeric_rosen3_step-name>` is used to solve the ODE.
#
# t_all
# *****
# The argument *t_all* is a vector that is monotone
# increasing or decreasing.
# The type of its elements can be ``float`` or ``a_double`` .
# The smaller the spacing between time points, the more accurate
# the approximation is.
# Note two points can be equal; i.e., no zero spacing.
# We call *t_all* [0] the initial time and
# *t_all* [-1] the final time.
#
# p_all
# *****
# This argument is a list of dictionaries.
# The i-th element of the list has the following *key* ,
# *value* pairs:
#
# .. csv-table::
#  :widths: 7, 8
#
#  *key* , *value*
#  ``'alpha'`` , :math:`\alpha( t_i )`
#  ``'beta'`` , :math:`\beta( t_i )`
#  ``'sigma'`` , :math:`\sigma( t_i )`
#  ``'gamma'`` , :math:`\gamma( t_i )`
#  ``'xi'`` , :math:`\xi( t_i )`
#  ``'chi'`` , :math:`\chi( t_i )`
#  ``'delta'`` , :math:`\delta( t_i )`
#
# where *t_i* is the time *t_all* [ *i* ] .
# The type of *value* can be ``float`` or ``a_double`` .
# Each of the these parameters will be linearly interpolated
# for times between the those in *t_all* .
#
# alpha
# =====
# There is a special restriction that :math:`\alpha(t)` must be
# constant; i.e. :math:`\alpha( t_i ) = \alpha( t_0 )` for
# all :math:`i`.
# This is because talking the derivative of :math:`I^\alpha`
# respect to :math:`I` has a special representation when :math:`\alpha = 1`.
# Using a special representation for that case would not work with AD
# unless :math:`\alpha` is constant.
#
# initial
# *******
# is a vector of length four containing the initial values for
# S, E, I, R, W, D in that order.
# The type of its elements can be ``float`` or ``a_double`` .
#
# n_step
# ******
# This is the number of numerical integration steps to use for each
# time interval in the *t_all* array.
# It must be an ``int`` greater or equal one.
# The larger *n_step* the more computational effort and the more
# accurate the solution.  The default value is for *n_step* is one.
#
# seirwd_all
# **********
# The return value *seirwd_all* is a numpy matrix with row dimension
# equal to the number of elements in *t_all* and column dimension
# equal to six. The value *seirwd_all* [ *i* , *j* ] is the
# approximate solution for the j-th compartment at time *t_all* [ *i* ] .
# The compartments have the same order as in *initial* and
# ``seirwd`` [0, *:* is equal to *initial* .
# The sequence of floating point operations only depends on *t_all*
# and the operations used to compute *p_fun* .
#
# Conservation of Mass
# ********************
# Note that the sum of S, E, I, R, W, and D should be constant; i.e.,
# up to numerical accuracy, it not depend on time.
#
# {xrst_toc_hidden
#  example/python/numeric/seirwd_model_xam.py
# }
# Example
# *******
# :ref:`numeric_seirwd_model_xam_py-name`
#
# Source Code
# ***********
# {xrst_literal
#  # BEGIN_PYTHON
#  # END_PYTHON
# }
#
# {xrst_end numeric_seirwd_model}
