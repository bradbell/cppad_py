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

Children
********
{xsrst_child_list
}

{xsrst_end mixed}
"""
import cppad_py
import numpy
class fixed_solution :
   def __init__( self, fixed_opt, fixed_lag, fix_con_lag, ran_con_lag ):
        self.fixed_opt   = cppad_py.utility.vec2numpy( fixed_opt )
        self.fixed_lag   = cppad_py.utility.vec2numpy( fixed_lag )
        self.fix_con_lag = cppad_py.utility.vec2numpy( fix_con_lag )
        self.ran_con_lag = cppad_py.utility.vec2numpy( ran_con_lag )

class mixed :
    """
    -------------------------------------------------------------------------
    {xsrst_begin mixed_ctor}
    .. include:: ../preamble.rst
    {xsrst_spell
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

    n_fixed
    *******
    is a positive integer specifying the number of fixed effects in the model.
    The default value 0 is not valid
    (hence this parameter must be specified).

    n_random
    ********
    is a non-negative integer specifying the number of random effects
    in the model.

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

    fix_likelihood
    **************
    is a :ref:`d_fun<py_fun_ctor.syntax.d_fun>` representation
    of the part of the likelihood that does not depend on the
    random effects.

    Syntax
    ======
    *vec* = *fix_likelihood* . ``forward`` (0, *theta* )

    theta
    ======
    is a numpy vector with ``float`` elements and size
    :ref:`n_fixed<mixed_ctor.n_fixed>`.

    vec
    ===
    is a numpy vector with ``float`` elements and size *s*.
    Using :math:`v` for the vector *vec* and
    :math:`z` for the data that is independent of the random effects,
    the fixed effects negative log likelihood is

    .. math::

        - \log [ \B{p} ( z | \theta ) \B{p} ( \theta ) ]
        =
        v_0 + | v_1 | + \cdots + | v_{s-1} |

    Note tha :math:`v_0` is assumed to be a smooth w.r.t
    the vector of fixed effects :math:`\theta`.

    Default
    =======
    The value *fix_likelihood* equal ``None``.
    corresponds to all the data depending on the random effect
    no prior for the fixed effects :math:`\theta`.

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
        n_fixed          = 0,
        n_random         = 0,
        quasi_fixed      = False,
        bool_sparsity    = False,
        A_rcv            = None,
        warning          = None,
        fix_likelihood   = None,
    # )
    # END_MIXED_CTOR
    ) :
        self.n_fixed        = n_fixed
        self.n_random       = n_random
        self.A_rcv          = A_rcv
        #
        def ignore_warning ():
            return
        #
        if n_fixed == 0 :
            raise RuntimeError('cppad_py.mixed: n_fixed is zero')
        if n_random < 0 :
            raise RuntimeError('cppad_py.mixed: n_random is less than zero')
        if A_rcv is None :
            empty_pattern = cppad_py.sparse_rc()
            A_rcv         = cppad_py.sparse_rcv( empty_pattern )
        if warning is None :
            warning = ignore_warning
        if fix_likelihood is None :
            fix_likelihood = cppad_py.d_fun()
        #
        self.obj = cppad_py.cppad_swig.mixed(
            n_fixed,
            n_random,
            quasi_fixed,
            bool_sparsity,
            A_rcv.rcv,
            warning,
            fix_likelihood.f,
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
    {xsrst_begin optimize_fixed}
    .. include:: ../preamble.rst
    {xsrst_spell
        ipopt
        \n
        iter
        cppad
        rcv
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
    This routine maximizes the Laplace Approximation for the likelihood
    of the data and priors given the fixed effects.

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

    {xsrst_end optimize_fixed}
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
        # adjust limits that are None
        if fixed_lower is None :
            fixed_lower = - numpy_infinity( self.n_fixed )
        if fixed_upper is None :
            fixed_upper = +  numpy_infinity( self.n_fixed )
        if fix_constraint_lower is None :
            # 2DO: fix length once fixed constraint is added to constructor
            fix_constraint_lower = -  numpy_infinity( 0 )
        if fix_constraint_upper is None :
            # 2DO: fix length once fixed constraint is added to constructor
            fix_constraint_upper = +  numpy_infinity( 0 )
        if random_lower is None :
            random_lower = - numpy_infinity( self.n_random )
        if random_upper is None :
            random_upper = + numpy_infinity( self.n_random )
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
        fixed_lower = numpy2std(fixed_lower, self.n_fixed, 'fixed_lower')
        fixed_upper = numpy2std(fixed_upper, self.n_fixed, 'fixed_upper')
        fixed_scale   = numpy2std(fixed_scale, self.n_fixed, 'fixed_scale')
        fixed_in      = numpy2std(fixed_in, self.n_fixed, 'fixed_in')
        random_lower  = numpy2std(random_lower, self.n_random, 'random_lower')
        random_upper  = numpy2std(random_upper, self.n_random, 'random_upper')
        random_in     = numpy2std(random_in, self.n_random, 'random_in')
        # 2DO: fix length once fixed constraint is added to constructor
        fix_constraint_lower = \
            numpy2std(fix_constraint_lower, 0, 'fix_constraint_lower')
        fix_constraint_upper = \
            numpy2std(fix_constraint_upper, 0, 'fix_constraint_upper')
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
            solution_tmp.fixed_opt,
            solution_tmp.fixed_lag,
            solution_tmp.fix_con_lag,
            solution_tmp.ran_con_lag
        )
        return solution
