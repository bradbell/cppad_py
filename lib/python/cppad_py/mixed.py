# -----------------------------------------------------------------------------
#         cppad_py: A C++ Object Library and Python Interface to Cppad
#          Copyright (C) 2017-20 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# -----------------------------------------------------------------------------
"""
{xsrst_begin_parent mixed}
.. include:: ../preamble.rst

Python: Laplace Approximation of Mixed Effects Models
#####################################################

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

Children
********
{xsrst_child_list
}

{xsrst_end mixed}
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
    {xsrst_begin mixed_ctor}
    .. include:: ../preamble.rst
    {xsrst_spell
        init
        obj
        bool
        rcv
        \hat
        \cdots
    }

    Mixed Class Constructor
    #######################

    Syntax
    ******
    {xsrst_file
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
    The default value for this argument ``None`` corresponds
    to the empty vector and is not valid.

    random_vec
    **********
    is a numpy vector with ``float`` elements.
    It specifies a value of the random effects for which the
    likelihood and prior functions can be evaluated and is used to
    initialize *mixed_obj*.
    The default value for this argument ``None`` corresponds
    to the empty vector; i.e., no random effects.

    n_fixed
    *******
    is the length of the vector *fixed_init* and must not be zero.

    n_random
    ********
    is the length of the vector *random_init* and can be zero.

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
    Is a :ref:`sparse_rcv<py_sparse_rcv>` representation of the
    random constraint matrix :math:`A`; i.e.
    :math:`A \cdot \hat{u} ( \theta ) = 0`
    where :math:`\hat{u} ( \theta )` is the
    optimal random effects as a function of the fixed effects.
    The value ``None`` corresponds to no random constraints.

    warning
    *******
    is a python function that gets called when *mixed_obj*
    has a warning to report; see :ref:`mixed_warning`.
    The value ``None`` corresponds to ignoring all warning messages.

    fix_likelihood (ran_likelihood)
    *******************************
    is a :ref:`d_fun<py_fun_ctor.syntax.d_fun>` representation
    of the fixed (random) part of the likelihood.

    Syntax
    ======
    | *fix_like* = *fix_likelihood* . ``forward`` (0, *theta* )
    | *ran_like* = *ran_likelihood* . ``forward`` (0, *theta_u* )

    theta
    ======
    is a numpy vector with ``float`` elements and size
    :ref:`n_fixed<mixed_ctor.n_fixed>`.

    u
    =
    is a numpy vector with ``float`` elements and size
    :ref:`n_random<mixed_ctor.n_random>`.

    theta_u
    =======
    is a numpy vector with ``float`` elements and size
    *n_fixed* + *n_random*.
    The first *n_fixed* elements are the fixed effects *theta*
    and the last *n_random* elements are the random effect *u*.

    fix_like (ran_like)
    ===================
    is a numpy vector with ``float`` elements and size *s* (size 1).
    We use :math:`f` ( :math:`r` ) for the vector *fix_like* ( *ran_like* ),
    :math:`z` for the data that is independent of the random effects,
    :math:`y`' for the other data,

    Negative Log-Likelihood
    +++++++++++++++++++++++
    The fixed effects negative log likelihood is

    .. math::

        - \log [ \B{p} ( z | \theta ) \B{p} ( \theta ) ]
        =
        f_0 + | f_1 | + \cdots + | f_{s-1} |

    The random effects negative log likelihood is

    .. math::

        - \log [ \B{p} ( y | \theta , u ) \B{p} ( u | \theta ) ]
        =
        r_0


    The vectors :math:`f` and :math:`r` are assumed to be a smooth
    functions w.r.t the vectors :math:`\theta` and :math:`u` .

    Default
    =======
    The value *fix_likelihood* ( *ran_likelihood*) equal ``None``.
    corresponds to the fixed effect likelihood (random effect likelihood)
    being constant w.r.t. :math:`\theta` ( w.r.t :math:`\theta , u` ).

    {xsrst_children
      example/python/mixed/ctor_xam.py
    }
    Example
    *******
    :ref:`mixed_ctor_xam_py<mixed_ctor_xam_py>`

    {xsrst_end mixed_ctor}
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
        ran_likelihood   = None,
    # )
    # END_MIXED_CTOR
    ) :
        def numpy2std(vec, name) :
            # numpy2vec will check the length and report errors
            dtype = float
            shape = len(vec)
            context = 'cppad_mixed: ctor: ' + name
            vec = cppad_py.utility.numpy2vec(vec, dtype, shape, context, name)
            return vec
        #
        if fixed_init is None :
            raise RuntimeError('cppad_py.mixed: fixed_init is None')
        else :
            fixed_init = numpy2std(fixed_init, 'fixed_init')
        #
        if random_init is None :
            random_init = cppad_py.vec_double(0)
        else :
            random_init = numpy2std(random_init, 'random_init')
        #
        self.n_fixed        = len(fixed_init)
        self.n_random       = len(random_init)
        self.n_fix_con      = 0 # 2DO: fix when fix conratint function added
        self.A_rcv          = A_rcv
        #
        def ignore_warning ():
            return
        #
        if self.n_fixed == 0 :
            raise RuntimeError('cppad_py.mixed: n_fixed is zero')
        if self.n_random < 0 :
            raise RuntimeError('cppad_py.mixed: n_random is less than zero')
        if A_rcv is None :
            empty_pattern = cppad_py.sparse_rc()
            A_rcv         = cppad_py.sparse_rcv( empty_pattern )
            self.A_rcv    = A_rcv
        if warning is None :
            warning = ignore_warning
        if fix_likelihood is None :
            fix_likelihood = cppad_py.d_fun()
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
            ran_likelihood.f,
        )
    """
    -------------------------------------------------------------------------
    {xsrst_begin mixed_warning}
    .. include:: ../preamble.rst
    {xsrst_spell
        obj
    }

    Mixed Class Warnings
    ####################

    Syntax
    ******
    | *warning* ( *message* )
    | *mixed_obj* . ``post_warning`` ( *message* )

    warning
    *******
    This is the :ref:`mixed_ctor.warning` argument to the  mixed class
    constructor.
    It's *message* argument is an `str` describing the warning.

    post_warning
    ************
    is a mixed class member function that posts a warning.
    It's *message* argument is an `str` describing the warning.
    It's main purpose is for testing.

    {xsrst_children
      example/python/mixed/warning_xam.py
    }
    Example
    *******
    :ref:`mixed_warning_xam_py<mixed_warning_xam_py>`

    {xsrst_end mixed_warning}
    """
    def warning(self, message) :
        self.obj.warning(message)
    def post_warning(self, message) :
        self.obj.post_warning(message)
    """
    -------------------------------------------------------------------------
    {xsrst_begin mixed_fatal_error}
    .. include:: ../preamble.rst
    {xsrst_spell
        obj
    }

    Mixed Class Fatal Errors
    ########################

    Syntax
    ******
    | *mixed_obj* . ``post_fatal_error`` ( *message* )

    post_fatal_error
    ****************
    is a mixed class member function that posts a fatal error.
    It's *message* argument is an `str` describing the error.
    A call to this function will raise a python ``RuntimeError`` with
    the specified message.  It's main purpose is for testing.

    {xsrst_children
      example/python/mixed/fatal_error_xam.py
    }
    Example
    *******
    :ref:`mixed_fatal_error_xam_py<mixed_fatal_error_xam_py>`

    {xsrst_end mixed_fatal_error}
    """
    def post_fatal_error(self, message) :
        self.obj.post_fatal_error(message)
    """
    -------------------------------------------------------------------------
    {xsrst_begin mixed_fix_likelihood}
    {xsrst_spell
        \cdots
    }

    Fixed Effects Likelihood
    ########################

    Syntax
    ******
    *v* = *fix_likelihood* . ``forward`` (0, *theta* )


    fix_likelihood
    ***************
    is a :ref:`d_fun<py_fun_ctor.syntax.d_fun>` representation
    of the fixed effect likelihood.
    The negative log of the fixed effects likelihood is

    .. math::

        g( \theta )
        =
        v_0 ( \theta ) + | v_1 ( \theta)  | + \cdots + | v_{m-1} ( \theta ) |
        =
        - \log [ \B{p} ( z | \theta ) \B{p} ( \theta ) ]

    The functions :math:`v_i ( \theta )` for :math:`i = 0 , \ldots , m-1`
    are assumed to be a smooth w.r.t the vector :math:`\theta`.

    theta
    *****
    is a numpy vector with ``float`` elements and size
    :ref:`n_fixed<mixed_ctor.n_fixed>`
    containing a value for the fixed effects.

    v
    *
    is a numpy vector with ``float`` elements and size *m*.

    None
    ****
    The value *fix_likelihood* = ``None``
    corresponds to the fixed effect likelihood
    being constant w.r.t. :math:`\theta`.

    {xsrst_children
        example/python/mixed/fix_likelihood_xam.py
    }
    Example
    *******
    :ref:`mixed_fix_likelihood_xam_py<mixed_fix_likelihood_xam_py>`

    {xsrst_end mixed_fix_likelihood}
    -------------------------------------------------------------------------
    {xsrst_begin mixed_optimize_fixed}
    .. include:: ../preamble.rst
    {xsrst_spell
        ipopt
        \n
        iter
        cppad
        rcv
        \infty
    }

    Optimize Fixed Effects
    ######################

    Syntax
    ******
    {xsrst_file
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
    see :ref:`fix_likelihood<mixed_ctor.fix_likelihood_(ran_likelihood)>`.


    Argument Types
    **************
    The arguments *fixed_ipopt_options* and *random_ipopt_options*
    have type ``str``.  All the other arguments are
    numpy vectors with elements of type ``float``.

    Limits
    *******
    As a lower (upper) limit, the value ``None`` is minus (plus) infinity;
    i.e., no lower (upper) limit.

    fixed_lower (fixed_upper)
    =========================
    has length *n_fixed* and is the lower (upper) limit for the fixed effects.

    fix_constraint_lower (fix_constraint_upper)
    ===========================================
    has length equal to the return value for the fixed effects constraint
    function and is the corresponding lower (upper) limit.

    random_lower (random_upper)
    ===========================
    has length *n_random* and is the lower (upper) limit for the random effects.
    (The Laplace approximation assumes these constraints are not active.)

    fixed_in (random_in)
    ********************
    has length *n_fixed* (*n_random*) and is the initial value used during
    optimization of the fixed (random) effects.
    The value ``None`` corresponds to a vector of zeros.

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

    String
    ======
    An Ipopt string option is specifies with the following syntax:
    `String`` *name* *value*

    Integer
    =======
    An Ipopt integer option is specifies with the following syntax:
    `Integer`` *name* *value*

    Numeric
    =======
    An Ipopt numeric option is specifies with the following syntax:
    `Numeric`` *name* *value*

    derivative_test
    ===============
    If the string option is ``derivative_test``, *value* can be
    ``none``, ``first-order``, ``second-order``, ``only-second-order``.
    If second order derivatives are tested,
    :ref:`quasi_fixed<mixed_ctor.quasi_fixed>` must be false.
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
    THe objective and constraint functions are automatically scaled by
    cppad_mixed and it is an error to specify this option.

    random_ipopt_options
    ********************
    This contains the options for optimizing the fixed effects.
    It has the same format as *fixed_ipopt_options*, but does
    not have the special exceptions to the normal Ipopt options; e.g.,
    ``adaptive`` is not available as a ``derivative_test`` *value*.

    solution
    ********
    The return value *solution* has the following fields:

    fixed_opt
    =========
    The value *solution* . ``fixed_opt`` is a numpy vector with length
    *n_fixed* containing the final value of the fixed effects
    (after optimization).
    If the *max_iter* is -1, it is equal to *fixed_in*.

    fixed_lag
    =========
    The value *solution* . ``fixed_lag`` is a numpy vector with length
    *n_fixed* containing the Lagrange multipliers for
    the fixed effects lower (upper) bounds if it is greater than (less than)
    zero.

    fix_con_lag
    ===========
    The value *solution* . ``fix_con_lag`` is a Lagrange multipliers for
    the fixed effects lower (upper) bounds if it is greater than (less than).
    Its length is the same as the return value for the fixed effects constraint
    function.

    ran_con_lag
    ===========
    The value *solution* . ``ran_con_lag`` is a Lagrange multipliers for the
    rand effects constraint function.
    Its length is the same as the random constrain matrix :math"`A` ; see
    :ref:`A_rcv<mixed_ctor.A_rcv>`.

    {xsrst_children
        example/python/mixed/optimize_fixed_xam.py
    }
    Example
    *******
    :ref:`mixed_optimize_fixed_xam_py<mixed_optimize_fixed_xam_py>`

    {xsrst_end mixed_optimize_fixed}
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
            fixed_in = numpy.zeros(n_fixed, dtype=float)
        if random_in is None :
            random_in = numpy.zeros(n_random, dtype=float)
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
