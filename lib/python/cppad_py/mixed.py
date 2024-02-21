# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileCopyrightText: Bradley M. Bell <bradbell@seanet.com>
# SPDX-FileContributor: 2017-23 Bradley M. Bell
# ----------------------------------------------------------------------------
"""
{xrst_begin_parent mixed}
{xrst_spell
   laplace
}
Laplace Approximation of Mixed Effects Models
#############################################

Notation
********

theta
=====
We use :math:`\theta` to denote a value for the fixed effects vector.

u
=
We use :math:`u` to denote a value for the random effects vector.

z
=
We use :math:`z` to denote
the data that does not depend on the random effects.

y
=
We use :math:`y` to denote
the data that depends on the random effects.

p(theta)
========
We use :math:`\B{p} ( \theta )` to denote the prior density for :math:`\theta`.

p(z|theta)
==========
We use :math:`\B{p} (z | \theta )` to denote the density of :math:`z`
given :math:`\theta`.

p(u|theta)
==========
We use :math:`\B{p} (u | \theta )` to denote the density of :math:`u`
given :math:`\theta`.

p(y|theta,u)
============
We use :math:`\B{p} (y | \theta , u)` to denote the density of :math:`y`
given :math:`\theta` and :math:`u`.

Fixed Effects Likelihood
========================
We refer to :math:`\B{p} (z | \theta ) \B{p} ( \theta )`
as the fixed effects likelihood.
The negative log of this, as function of :math:`\theta`, is computed by
:ref:`mixed_ctor@fix_likelihood` .

Random Effects Likelihood
=========================
We refer to :math:`\B{p} (y | \theta , u ) \B{p} ( u | \theta )`
as the random effects likelihood.
The negative log of this, as function of :math:`\theta, u`, is computed by
:ref:`mixed_ctor@ran_likelihood` .

Children
********
{xrst_toc_table
}

{xrst_end mixed}
"""
import cppad_py
import numpy
class fixed_solution :
   def __init__(self, n_fixed, n_random, n_fix_con, n_ran_con,
      fixed_opt, fixed_lag, fix_con_lag, ran_con_lag ):
      self.fixed_opt   = cppad_py.utility.vec2numpy( fixed_opt , n_fixed )
      self.fixed_lag   = cppad_py.utility.vec2numpy( fixed_lag , n_fixed )
      self.fix_con_lag = cppad_py.utility.vec2numpy( fix_con_lag , n_fix_con )
      self.ran_con_lag = cppad_py.utility.vec2numpy( ran_con_lag , n_ran_con )

class mixed :
   """
   -------------------------------------------------------------------------
   {xrst_begin mixed_ctor}
   {xrst_spell
      bool
      boolean
      obj
      rcv
   }

   Mixed Class Constructor
   #######################

   Syntax
   ******
   {xrst_literal
      # BEGIN_MIXED_CTOR
      # END_MIXED_CTOR
   }

   mixed_obj
   *********
   We refer to the value returned by this constructor as *mixed_obj*.

   fixed_init
   **********
   is a numpy vector with ``float`` elements.
   It specifies a value of the fixed effects for which the
   likelihood and prior functions can be evaluated and is used to
   initialize *mixed_obj*.
   This vector must be non-empty and the default value ``None`` is not valid.

   n_fixed
   =======
   We use the notation *n_fixed* for the length of *fixed_init* .

   random_init
   ***********
   is a numpy vector with ``float`` elements.
   It specifies a value of the random effects for which the
   likelihood and prior functions can be evaluated and is used to
   initialize *mixed_obj*.
   The default value for this argument ``None`` corresponds
   to the empty vector.

   n_random
   ========
   We use the notation *n_random* for the length of *random_init* .


   quasi_fixed
   ***********
   is True (False) if a quasi-Newton method (Newton method) is used to
   optimize the fixed effects. The Newton method requires computation
   of second derivatives.

   bool_sparsity
   *************
   is True (False) if CppAD should use boolean sparsity patterns
   (set sparsity patterns) for its internal calculations

   A_rcv
   *****
   Is a :ref:`sparse_rcv<py_sparse_rcv-name>` representation of the
   random constraint matrix :math:`A`; i.e.
   :math:`A \cdot \hat{u} ( \theta ) = 0`
   where :math:`\hat{u} ( \theta )` is the
   optimal random effects as a function of the fixed effects.
   The value ``None`` corresponds to no random constraint.

   warning
   *******
   is a python function that gets called when *mixed_obj*
   has a warning to report; see :ref:`mixed_warning-title`.
   The value ``None`` corresponds to ignoring all warning messages.

   fix_likelihood
   **************
   see :ref:`mixed_fix_likelihood-title` .
   The value ``None`` corresponds to no fixed effects likelihood.

   fix_constraint
   **************
   see :ref:`mixed_fix_constraint-title` .
   The value ``None`` corresponds to no constraint function
   for the fixed effects (one can still have bound constraints).

   ran_likelihood
   **************
   see :ref:`mixed_ran_likelihood-title` .
   The value ``None`` corresponds to no random effects likelihood.

   {xrst_toc_hidden
      example/python/mixed/ctor_xam.py
   }
   Example
   *******
   :ref:`mixed_ctor_xam.py-name`

   {xrst_end mixed_ctor}
   """
   #
   def __init__(
      self,
   # BEGIN_MIXED_CTOR
   # mixed_obj = cppad_py.mixed(
      fixed_init       = None,
      random_init      = None,
      quasi_fixed      = False,
      bool_sparsity    = False,
      A_rcv            = None,
      warning          = None,
      fix_likelihood   = None,
      fix_constraint   = None,
      ran_likelihood   = None,
   # )
   # END_MIXED_CTOR
   ) :
      def numpy2std(vec, name) :
         # numpy2vec will check the length and report errors
         dtype = float
         shape = len(vec)
         context = 'cppad_py.mixed: ' + name
         vec = cppad_py.utility.numpy2vec(vec, dtype, shape, context, name)
         return vec
      #
      def ignore_warning ():
         return
      #
      if fixed_init is None :
         raise RuntimeError('cppad_py.mixed: fixed_init is None')
      if random_init is None :
         random_init = numpy.array( [], dtype='float' )
      #
      self.n_fixed        = len(fixed_init)
      self.n_random       = len(random_init)
      self.fixed_init     = fixed_init
      self.random_init    = random_init
      self.A_rcv          = A_rcv
      if fix_constraint is None :
         self.n_fix_con  = 0
      else :
         self.n_fix_con  = fix_constraint.size_range()
      #
      fixed_init  = numpy2std(fixed_init, 'fixed_init')
      random_init = numpy2std(random_init, 'random_init')
      #
      if self.n_fixed == 0 :
         raise RuntimeError('cppad_py.mixed: n_fixed is zero')
      if self.n_random < 0 :
         raise RuntimeError('cppad_py.mixed: n_random is less than zero')
      if A_rcv is None :
         A_rcv         = cppad_py.sparse_rcv()
         self.A_rcv    = A_rcv
      if warning is None :
         warning = ignore_warning
      if fix_likelihood is None :
         fix_likelihood = cppad_py.d_fun()
      if fix_constraint is None :
         fix_constraint = cppad_py.d_fun()
      if ran_likelihood is None :
         ran_likelihood = cppad_py.d_fun()
      #
      self.obj = cppad_py.cppad_swig.mixed(
         fixed_init,
         random_init,
         quasi_fixed,
         bool_sparsity,
         A_rcv.rcv,
         warning,
         fix_likelihood.f,
         fix_constraint.f,
         ran_likelihood.f,
      )
   """
   -------------------------------------------------------------------------
   {xrst_begin mixed_warning}
   {xrst_spell
      obj
   }

   Mixed Class Warnings
   ####################

   Syntax
   ******
   | *warning* ( *message* )
   | *mixed_obj*\ ``.post_warning`` ( *message* )

   warning
   *******
   This is the :ref:`mixed_ctor@warning` argument to the  mixed class
   constructor.
   It's *message* argument is an `str` describing the warning.

   post_warning
   ************
   is a mixed class member function that posts a warning.
   It's *message* argument is an `str` describing the warning.
   It's main purpose is for testing.

   {xrst_toc_hidden
      example/python/mixed/warning_xam.py
   }
   Example
   *******
   :ref:`mixed_warning_xam.py-name`

   {xrst_end mixed_warning}
   """
   def warning(self, message) :
      self.obj.warning(message)
   def post_warning(self, message) :
      self.obj.post_warning(message)
   """
   -------------------------------------------------------------------------
   {xrst_begin mixed_fatal_error}
   {xrst_spell
      obj
      runtime
   }

   Mixed Class Fatal Errors
   ########################

   Syntax
   ******
   | *mixed_obj*\ ``.post_fatal_error`` ( *message* )

   post_fatal_error
   ****************
   is a mixed class member function that posts a fatal error.
   It's *message* argument is an `str` describing the error.
   A call to this function will raise a python ``RuntimeError`` with
   the specified message.  It's main purpose is for testing.

   {xrst_toc_hidden
      example/python/mixed/fatal_error_xam.py
   }
   Example
   *******
   :ref:`mixed_fatal_error_xam.py-name`

   {xrst_end mixed_fatal_error}
   """
   def post_fatal_error(self, message) :
      self.obj.post_fatal_error(message)
   """
   -------------------------------------------------------------------------
   {xrst_begin mixed_fix_likelihood}

   Fixed Effects Likelihood
   ########################

   Syntax
   ******
   *v* = *fix_likelihood*\ ``.forward`` (0, *theta* )


   fix_likelihood
   **************
   is a :ref:`d_fun<py_fun_ctor@Syntax@d_fun>` representation
   of the negative log of the
   :ref:`fixed effects likelihood <mixed@Notation@Fixed Effects Likelihood>`

   .. math::

      f( \theta )
      =
      v_0 ( \theta ) + | v_1 ( \theta)  | + \cdots + | v_{m-1} ( \theta ) |
      =
      - \log [ \B{p} ( z | \theta ) \B{p} ( \theta ) ]

   The functions :math:`v_i ( \theta )` for :math:`i = 0 , \ldots , m-1`
   are assumed to be a smooth w.r.t the vector :math:`\theta`.

   theta
   *****
   is a numpy vector with ``float`` elements and size
   :ref:`mixed_ctor@fixed_init@n_fixed`
   containing a value for the fixed effects.

   v
   *
   is a numpy vector with ``float`` elements and size *m*.

   None
   ****
   The value *fix_likelihood* = ``None``
   corresponds to the fixed effects likelihood
   being constant w.r.t. :math:`\theta`.

   {xrst_toc_hidden
      example/python/mixed/fix_likelihood_xam.py
   }
   Example
   *******
   :ref:`mixed_fix_likelihood_xam.py-name`

   {xrst_end mixed_fix_likelihood}
   -------------------------------------------------------------------------
   {xrst_begin mixed_fix_constraint}
   Fixed Effects Constraint Function
   #################################

   Syntax
   ******
   *v* = *fix_constraint*\ ``.forward`` (0, *theta* )


   fix_constraint
   **************
   is a :ref:`d_fun<py_fun_ctor@Syntax@d_fun>` representation
   of the fixed effects constraint function

   .. math::
      g( \theta )
      =
      [ v_0 ( \theta ) , \cdots , v_{m-1} ( \theta ) ]^\R{T}

   The functions :math:`v_i ( \theta )` for :math:`i = 0 , \ldots , m-1`
   are assumed to be a smooth w.r.t the vector :math:`\theta`.
   The bounds for :math:`g( \theta )` are specified by
   :ref:`mixed_optimize_fixed@fix_constraint_lower (fix_constraint_upper)` .

   theta
   *****
   is a numpy vector with ``float`` elements and size
   :ref:`mixed_ctor@fixed_init@n_fixed`
   containing a value for the fixed effects.

   v
   *
   is a numpy vector with ``float`` elements and size *m*.

   None
   ****
   The value *fix_constraint* = ``None``
   corresponds to not fixed effects constraint function; i.e.,
   :math:`m = 0`.

   {xrst_toc_hidden
      example/python/mixed/fix_constraint_xam.py
   }
   Example
   *******
   :ref:`mixed_fix_constraint_xam.py-name`

   {xrst_end mixed_fix_constraint}
   -------------------------------------------------------------------------
   {xrst_begin mixed_ran_likelihood}
   Random Effects Likelihood
   #########################

   Syntax
   ******
   *v* = *ran_likelihood*\ ``.forward`` (0, *theta* , *u* )


   ran_likelihood
   **************
   is a :ref:`d_fun<py_fun_ctor@Syntax@d_fun>` representation
   of the negative log of the
   :ref:`random effects likelihood <mixed@Notation@Random Effects Likelihood>`

   .. math::

      r( \theta , u )
      =
      v_0 ( \theta , u )
      =
      - \log [ \B{p} ( y | \theta , u ) \B{p} ( u | \theta ) ]

   The function :math:`v_0 ( \theta , u )`
   is assumed to be a smooth w.r.t the vector :math:`( \theta , u )`.

   theta
   *****
   is a numpy vector with ``float`` elements and size
   :ref:`mixed_ctor@fixed_init@n_fixed`
   containing a value for the fixed effects.

   u
   *
   is a numpy vector with ``float`` elements and size
   :ref:`mixed_ctor@random_init@n_random`
   containing a value for the random effects.

   v
   *
   is a numpy vector with ``float`` elements and size 1.

   None
   ****
   The value *ran_likelihood* = ``None``
   corresponds to the random effects likelihood
   being constant w.r.t. :math:`( \theta , u )`.

   {xrst_toc_hidden
      example/python/mixed/ran_likelihood_xam.py
   }
   Example
   *******
   :ref:`mixed_ran_likelihood_xam.py-name`

   {xrst_end mixed_ran_likelihood}
   -------------------------------------------------------------------------
   {xrst_begin mixed_optimize_fixed}
   {xrst_spell
      ipopt
      iter
      lagrange
      laplace
      max
      nlp
      rcv
   }

   Optimize The Fixed Effects
   ##########################

   Syntax
   ******
   {xrst_literal
      # BEGIN_OPTIMIZE_FIXED
      # END_OPTIMIZE_FIXED
   }

   Purpose
   *******
   This routine maximizes, with respect to the fixed effect :math:`\theta`,
   the Laplace approximation for the likelihood of the data and fixed effects.

   .. math::
      \B{p} ( z | \theta ) \B{p} ( \theta ) \int_{-\infty}^{+\infty}
         \B{p} ( y | \theta , u ) \B{p}( u | \theta ) \B{d} u

   If there are no random effects,
   there is no Laplace approximation of the integral above, and
   this routine maximizes :math:`\B{p} ( z | \theta ) \B{p} ( \theta )` ;
   see :ref:`mixed_fix_likelihood-title`.
   It also is no data, this routine maximizes :math:`\B{p} ( \theta )`.


   Argument Types
   **************
   The arguments *fixed_ipopt_options* and *random_ipopt_options*
   have type ``str``.  All the other arguments are
   numpy vectors with elements of type ``float``.

   Limits
   ******
   As a lower (upper) limit, the value ``None`` is minus (plus) infinity;
   i.e., no lower (upper) limit.

   fixed_lower (fixed_upper)
   *************************
   has length *n_fixed* and is the lower (upper) limit for the fixed effects.

   fix_constraint_lower (fix_constraint_upper)
   *******************************************
   has length equal to the
   :ref:`py_fun_property@size_range` for the
   :ref:`mixed_fix_constraint-title`
   and is the corresponding lower (upper) limit.

   random_lower (random_upper)
   ***************************
   has length *n_random* and is the lower (upper) limit for the random effects.
   (The Laplace approximation assumes these bounds are not active.)

   fixed_in (random_in)
   ********************
   has length *n_fixed* (*n_random*) and is the initial value used during
   optimization of the fixed (random) effects.
   If *fixed_in* (*random_in*) is ``None``, the value
   *fixed_init* (*random_init*) is used; see
   :ref:`mixed_ctor@fixed_init`, :ref:`mixed_ctor@random_init` .

   fixed_scale
   ***********
   has length *n_fixed* and is the value of the fixed at which the
   fixed effect objective is scaled so its derivative is near one.
   The value ``None`` corresponds to *fixed_scale* equal to *fixed_in*.

   fixed_ipopt_options
   *******************
   This contains the options for optimizing the fixed effects.
   Each line of an options argument corresponds to an ipopt option
   and is terminated by a ``\n`` character.
   Each line has three non-empty tokens separated by one or more spaces.
   The first token in each line is ``String``, ``Integer``, or ``Numeric``;
   see below.

   ipopt options
   =============
   See the `ipopt options <https://coin-or.github.io/Ipopt/OPTIONS.html>`_
   documentation for a list of the options and how they affect the
   optimization.

   String
   ======
   An Ipopt string option is specified by a line containing
   the following syntax:

   | |tab| ``String`` *name* *value*

   Integer
   =======
   An Ipopt integer option specified specifies by a line containing
   the following syntax:

   | |tab| ``Integer`` *name* *value*

   Numeric
   =======
   An Ipopt numeric option specified specifies by a line containing
   the following syntax:

   | |tab| ``Numeric`` *name* *value*

   derivative_test
   ===============
   If the string option is ``derivative_test``, *value* can be
   ``none``, ``first-order``, ``second-order``, ``only-second-order``.
   If second order derivatives are tested,
   :ref:`quasi_fixed<mixed_ctor@quasi_fixed>` must be false.
   In addition to the standard ipopt options above, *value* can be
   ``adaptive`` or ``trace-adaptive`` which uses a special derivative
   tester that adapts its step sizes for each argument component.

   hessian_approximation
   =====================
   If *quasi_fixed* is true, this string option (if present) must have value
   ``limit_memory``.

   max_iter
   ========
   This integer option has a special *value* -1.
   In this case ipopt is run with ``max_iter`` equal to zero,
   and the return solution corresponds to the input value of the
   fixed effects.

   nlp_scaling_method
   ==================
   The objective and constraint function are automatically scaled by
   cppad_mixed and it is an error to specify this option.

   random_ipopt_options
   ********************
   This contains the options for optimizing the random effects.
   It has the same format as *fixed_ipopt_options*, but does
   not have the special exceptions to the normal Ipopt options; e.g.,
   ``adaptive`` is not available as a ``derivative_test`` *value*.

   solution
   ********
   All the fields in the return value *solution*
   are numpy vectors with elements of type ``float``.

   fixed_opt
   =========
   The value *solution*\ ``.fixed_opt`` has length
   *n_fixed* and is the final value of the fixed effects
   (after optimization).
   If the *max_iter* is -1, it is equal to *fixed_in*.

   fixed_lag
   =========
   The value *solution*\ ``.fixed_lag`` has length
   *n_fixed* and is the Lagrange multipliers for
   the fixed effects lower (upper) bounds if it is greater than (less than)
   zero.

   fix_con_lag
   ===========
   The value *solution*\ ``.fix_con_lag`` is a Lagrange multipliers for
   the fixed effects lower (upper) bounds if it is greater than (less than).
   Its length is the same as the return value for the fixed effects constraint
   function.

   ran_con_lag
   ===========
   The value *solution*\ ``.ran_con_lag`` is a Lagrange multipliers for the
   rand effects constraint function.
   Its length is the same as the random constrain matrix :math:`A` ; see
   :ref:`A_rcv<mixed_ctor@A_rcv>`.

   {xrst_toc_hidden
      example/python/mixed/optimize_fixed_1.py
      example/python/mixed/optimize_fixed_2.py
   }
   Examples
   ********

   - :ref:`mixed_optimize_fixed_1.py-title`
   - :ref:`mixed_optimize_fixed_2.py-title`

   {xrst_end mixed_optimize_fixed}
   """
   def optimize_fixed(
      self,
   # BEGIN_OPTIMIZE_FIXED
   # solution = mixed_obj.optimize_fixed(
      fixed_ipopt_options  = None ,
      random_ipopt_options = None ,
      fixed_lower          = None ,
      fixed_upper          = None ,
      fix_constraint_lower = None ,
      fix_constraint_upper = None ,
      fixed_scale          = None ,
      fixed_in             = None ,
      random_lower         = None ,
      random_upper         = None ,
      random_in            = None ,
   # )
   # END_OPTIMIZE_FIXED
   ) :
      def numpy_infinity(length) :
         return numpy.ones(length, dtype=float) * numpy.inf
      def numpy2std(vec, length, name) :
         # numpy2vec will check the length and report errors
         dtype = float
         shape = length
         context = 'optimize_fixed: ' + name
         return cppad_py.utility.numpy2vec(vec, dtype, shape, context, name)
      #
      n_fixed   = self.n_fixed
      n_random  = self.n_random
      n_fix_con = self.n_fix_con
      n_ran_con = self.A_rcv.nr()
      #
      # adjust limits that are None
      if fixed_lower is None :
         fixed_lower = - numpy_infinity( n_fixed )
      if fixed_upper is None :
         fixed_upper = +  numpy_infinity( n_fixed )
      if fix_constraint_lower is None :
         fix_constraint_lower = -  numpy_infinity( n_fix_con )
      if fix_constraint_upper is None :
         fix_constraint_upper = +  numpy_infinity( n_fix_con )
      if random_lower is None :
         random_lower = - numpy_infinity( n_random )
      if random_upper is None :
         random_upper = + numpy_infinity( n_random )
      #
      # adjust other arguments that are None
      if fixed_ipopt_options is None :
         fixed_ipopt_options = ''
      if random_ipopt_options is None :
         random_ipopt_options = ''
      if fixed_in is None :
         fixed_in = self.fixed_init
      if random_in is None :
         random_in = self.random_init
      if fixed_scale is None :
         fixed_scale = fixed_in
      #
      # convert vectors from numpy to std
      fixed_lower   = numpy2std(fixed_lower, n_fixed, 'fixed_lower')
      fixed_upper   = numpy2std(fixed_upper, n_fixed, 'fixed_upper')
      fixed_scale   = numpy2std(fixed_scale, n_fixed, 'fixed_scale')
      fixed_in      = numpy2std(fixed_in, n_fixed, 'fixed_in')
      random_lower  = numpy2std(random_lower, n_random, 'random_lower')
      random_upper  = numpy2std(random_upper, n_random, 'random_upper')
      random_in     = numpy2std(random_in, n_random, 'random_in')
      fix_constraint_lower = \
         numpy2std(fix_constraint_lower, n_fix_con, 'fix_constraint_lower')
      fix_constraint_upper = \
         numpy2std(fix_constraint_upper, n_fix_con, 'fix_constraint_upper')
      #
      # call the c++ object
      solution_tmp = self.obj.optimize_fixed(
         fixed_ipopt_options,
         random_ipopt_options,
         fixed_lower,
         fixed_upper,
         fix_constraint_lower,
         fix_constraint_upper,
         fixed_scale,
         fixed_in,
         random_lower,
         random_upper,
         random_in,
      )
      solution = fixed_solution(
         n_fixed,
         n_random,
         n_fix_con,
         n_ran_con,
         solution_tmp.fixed_opt,
         solution_tmp.fixed_lag,
         solution_tmp.fix_con_lag,
         solution_tmp.ran_con_lag
      )
      return solution
   """
   -------------------------------------------------------------------------
   {xrst_begin mixed_optimize_random}
   {xrst_spell
      ipopt
   }

   Optimize The Random Effects
   ###########################

   Syntax
   ******
   {xrst_literal
      # BEGIN_OPTIMIZE_RANDOM
      # END_OPTIMIZE_RANDOM
   }

   Purpose
   *******
   Given a value for the fixed effects :math:`\theta`,
   this routine maximizes the :ref:`mixed_ran_likelihood-title`
   with respect to the fixed effect :math:`u`; i.e.,

   .. math::

      \B{p} ( y | \theta , u ) \B{p}( u | \theta )

   If there is no data, this routine maximizes :math:`\B{p} ( u | \theta )`.


   Argument Types
   **************
   The argument *random_ipopt_options*
   has type ``str``.  All the other arguments are
   numpy vectors with elements of type ``float``.

   fixed_vec
   *********
   has length *n_fixed* and is the value of the fixed effects
   :math:`\theta` in the objective function.
   This vector can't be ``None``.

   random_lower (random_upper)
   ***************************
   has length *n_random* and is the lower (upper) limit for the random effects.
   As a lower (upper) limit, the value ``None`` is minus (plus) infinity;
   i.e., no lower (upper) limit.

   random_in
   *********
   has length *n_random* and is the initial value used during
   optimization of the random effects.
   If *random_in* is ``None`` the value *random_init* is used; see
   :ref:`mixed_ctor@random_init` .

   random_opt
   **********
   The return value *random_opt* is a numpy vector,
   with length *n_random* an elements of type ``float``,
   that maximizes the random likelihood with respect to the random effects.

   Examples
   ********
   {xrst_toc_list
      example/python/mixed/optimize_random_xam.py
   }

   {xrst_end mixed_optimize_random}
   """
   def optimize_random(
      self,
   # BEGIN_OPTIMIZE_RANDOM
   # random_opt = mixed_obj.optimize_random(
      random_ipopt_options = None ,
      fixed_vec            = None ,
      random_lower         = None ,
      random_upper         = None ,
      random_in            = None ,
   # )
   # END_OPTIMIZE_RANDOM
   ) :
      def numpy_infinity(length) :
         return numpy.ones(length, dtype=float) * numpy.inf
      def numpy2std(vec, length, name) :
         # numpy2vec will check the length and report errors
         dtype = float
         shape = length
         context = 'cppad_py.mixed.optimize_random: ' + name
         return cppad_py.utility.numpy2vec(vec, dtype, shape, context, name)
      #
      n_fixed   = self.n_fixed
      n_random  = self.n_random
      #
      # fixed_vec
      if fixed_vec is None :
         msg = 'cppad_py.mixed.optimzie_random: fixed_vec is None'
         raise RuntimeError(msg)
      #
      # adjust limits that are None
      if random_lower is None :
         random_lower = - numpy_infinity( n_random )
      if random_upper is None :
         random_upper = + numpy_infinity( n_random )
      #
      # adjust other arguments that are None
      if random_ipopt_options is None :
         random_ipopt_options = ''
      if random_in is None :
         random_in = self.random_init
      #
      # convert vectors from numpy to std
      fixed_vec     = numpy2std(fixed_vec, n_fixed, 'fixed_vec')
      random_lower  = numpy2std(random_lower, n_random, 'random_lower')
      random_upper  = numpy2std(random_upper, n_random, 'random_upper')
      random_in     = numpy2std(random_in, n_random, 'random_in')
      #
      # call the c++ object
      random_opt = self.obj.optimize_random(
         random_ipopt_options,
         fixed_vec,
         random_lower,
         random_upper,
         random_in,
      )
      #
      random_opt = cppad_py.utility.vec2numpy( random_opt , n_random )
      return random_opt
   """
   -------------------------------------------------------------------------
   {xrst_begin mixed_hes_fixed_obj}
   {xrst_spell
      laplace
      rcv
   }

   Hessian of Fixed Effects Objective
   ##################################

   Syntax
   ******
   {xrst_literal
      # BEGIN_HES_FIXED_OBJ
      # END_HES_FIXED_OBJ
   }

   Purpose
   *******
   We are given a value for the fixed effects :math:`\theta`
   and the corresponding optimal value for the random effects
   :math:`\hat{u} ( \theta )`.
   This routine computes the hessian, with respect to the fixed effects,
   of the negative log of the Laplace approximation for the
   fixed effects objective

   .. math::
      \B{p} ( z | \theta ) \B{p} ( \theta ) \int_{-\infty}^{+\infty}
         \B{p} ( y | \theta , u ) \B{p}( u | \theta ) \B{d} u

   If there is no data,  and not random effects,
   the return value is the Hessian of
   :math:`- \log [ \B{p} ( \theta ) ]` .

   hes_fixed_obj_rcv
   *****************
   The argument *hes_fixed_obj_rcv* is a
   :ref:`py_sparse_rcv <py_sparse_rcv-name>` matrix.
   The input value of this argument does not matter.
   Upon return it contains the lower triangle of the Hessian
   (the Hessian is symmetric).

   fixed_vec
   *********
   The argument *fixed_vec* is a numpy vector with ``float`` elements
   and length *n_fixed*. It contains the value of the fixed effects
   :math:`\theta` at which the Hessian is evaluated.
   This vector can't be ``None``.

   random_opt
   **********
   The argument *random_opt* is a numpy vector with ``float`` elements
   and length *n_random*.
   It contains the optional value for the random effects,
   which is a function of the fixed effects and denoted by
   :math:`\hat{u} ( \theta )` .
   This vector can't be ``None``.

   Examples
   ********
   {xrst_toc_list
      example/python/mixed/hes_fixed_obj_xam.py
   }

   {xrst_end mixed_hes_fixed_obj}
   """
   def hes_fixed_obj(
      self,
   # BEGIN_HES_FIXED_OBJ
   # mixed_obj.hes_fixed_obj(
      hes_fixed_obj_rcv    = None ,
      fixed_vec            = None ,
      random_opt           = None ,
   # )
   # END_HES_FIXED_OBJ
   ) :
      def numpy2std(vec, length, name) :
         # numpy2vec will check the length and report errors
         dtype = float
         shape = length
         context = 'cppad_py.hes_fixed_obj: ' + name
         vec = cppad_py.utility.numpy2vec(vec, dtype, shape, context, name)
         return vec
      #
      n_fixed   = self.n_fixed
      n_random  = self.n_random
      #
      # fixed_vec
      if fixed_vec is None :
         msg = 'cppad_py.mixed.hes_fixed_obj: fixed_vec is None'
         raise RuntimeError(msg)
      #
      # random_opt
      if random_opt is None :
         msg = 'cppad_py.mixed.hes_fixed_obj: random_opt is None'
         raise RuntimeError(msg)
      #
      # convert vectors from numpy to std
      fixed_vec     = numpy2std(fixed_vec, n_fixed, 'fixed_vec')
      random_opt    = numpy2std(random_opt, n_random, 'random_opt')
      #
      # call the c++ object
      hes_fixed_obj_rcv.rcv = self.obj.hes_fixed_obj(
         fixed_vec,
         random_opt,
      )
   """
   -------------------------------------------------------------------------
   {xrst_begin mixed_hes_random_obj}
   {xrst_spell
      rcv
   }

   Hessian of Random Effects Objective
   ###################################

   Syntax
   ******
   {xrst_literal
      # BEGIN_HES_RANDOM_OBJ
      # END_HES_RANDOM_OBJ
   }

   Purpose
   *******
   We are given a value for the fixed effects :math:`\theta`,
   and the corresponding random effects :math:`u` .
   This routine the hessian, with respect to the random effects,
   of the negative log of random effects objective; i.e.,
   :ref:`ran_likelihood <mixed_ran_likelihood@ran_likelihood>`

   .. math::
      \B{p} ( y | \theta , u ) \B{p}( u | \theta ) \B{d} u

   If there is no data, the return value is the Hessian of
   :math:`- \log [ \B{p} ( u | \theta ) ]` w.r.t :math:`u` .

   hes_random_obj_rcv
   ******************
   The argument *hes_random_obj_rcv* is a
   :ref:`py_sparse_rcv <py_sparse_rcv-name>` matrix.
   The input value of this argument does not matter.
   Upon return it contains the lower triangle of the Hessian
   (the Hessian is symmetric).

   fixed_vec
   *********
   The argument *fixed_vec* is a numpy vector with ``float`` elements
   and length *n_fixed*. It contains the value of the fixed effects
   :math:`\theta` at which the Hessian is evaluated.
   This vector can't be ``None``.

   random_vec
   **********
   The argument *random_vec* is a numpy vector with ``float`` elements
   and length *n_random*.
   It contains the value for the random effects at which the Hessian
   is evaluated.,
   This vector can't be ``None``.

   Examples
   ********
   {xrst_toc_list
      example/python/mixed/hes_random_obj_xam.py
   }

   {xrst_end mixed_hes_random_obj}
   """
   def hes_random_obj(
      self,
   # BEGIN_HES_RANDOM_OBJ
   # mixed_obj.hes_random_obj(
      hes_random_obj_rcv   = None ,
      fixed_vec            = None ,
      random_vec           = None ,
   # )
   # END_HES_RANDOM_OBJ
   ) :
      def numpy2std(vec, length, name) :
         # numpy2vec will check the length and report errors
         dtype = float
         shape = length
         context = 'cppad_py.hes_random_obj: ' + name
         vec = cppad_py.utility.numpy2vec(vec, dtype, shape, context, name)
         return vec
      #
      n_fixed   = self.n_fixed
      n_random  = self.n_random
      #
      # fixed_vec
      if fixed_vec is None :
         msg = 'cppad_py.mixed.hes_random_obj: fixed_vec is None'
         raise RuntimeError(msg)
      #
      # random_vec
      if random_vec is None :
         msg = 'cppad_py.mixed.hes_random_obj: random_vec is None'
         raise RuntimeError(msg)
      #
      # convert vectors from numpy to std
      fixed_vec     = numpy2std(fixed_vec, n_fixed, 'fixed_vec')
      random_vec    = numpy2std(random_vec, n_random, 'random_vec')
      #
      # call the c++ object
      hes_random_obj_rcv.rcv = self.obj.hes_random_obj(
         fixed_vec,
         random_vec,
      )
