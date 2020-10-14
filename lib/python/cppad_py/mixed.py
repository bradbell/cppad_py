# -----------------------------------------------------------------------------
#         cppad_py: A C++ Object Library and Python Interface to Cppad
#          Copyright (C) 2017-20 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# -----------------------------------------------------------------------------
"""
{xsrst_begin_parent py_mixed}
.. include:: ../preamble.rst

Python: Laplace Approximation of Mixed Effects Models
#####################################################

Children
********
{xsrst_child_list
}

{xsrst_end py_mixed}
"""
import cppad_py
import numpy
class mixed :
    """
    {xsrst_begin py_mixed_ctor}
    .. include:: ../preamble.rst
    {xsrst_spell
        obj
        cppad
        bool
        rcv
        \hat
        \cdots
    }

    Mixed Class Constructor
    #######################

    Syntax
    ******
    | *mixed_obj* =  ``cppad_py.mixed`` (
    | |tab| *n_fixed* ,
    | |tab| *n_random* ,
    | |tab| *quasi_fixed* ,
    | |tab| *bool_sparsity* ,
    | |tab| *A_rcv* ,
    | |tab| *warning* ,
    | |tab| *fix_likelihood*
    | )

    mixed_obj
    *********
    If the class object created by this syntax.

    n_fixed
    *******
    is a positive integer specifying the number of fixed effects in the model.

    n_random
    ********
    is a non-negative integer specifying the number of random effects
    in the model (zero is OK).

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

    warning
    *******
    is a python function that gets called when *mixed_obj*
    has a warning to report; see :ref:`py_mixed_warning`.

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
    :ref:`n_fixed<py_mixed_ctor.n_fixed>`.

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

    Empty Function
    ==============
    If all the data depends on the random effect
    and there is no prior for :math:`\theta`, you can use the default
    constructor for *fix_likelihood*; i.e.,
    *fix_likelihood* = ``cppad_py.d_fun()``.

    {xsrst_children
      example/python/mixed/ctor_xam.py
    }
    Example
    *******
    :ref:`mixed_ctor_xam_py<mixed_ctor_xam_py>`

    {xsrst_end py_mixed_ctor}
    -------------------------------------------------------------------------
    """
    #
    def __init__(
        self,
        n_fixed,
        n_random,
        quasi_newton,
        bool_sparsity,
        A_rcv,
        warning,
        fix_likelihood,
    ) :
        self.obj = cppad_py.cppad_swig.mixed(
            n_fixed,
            n_random,
            quasi_newton,
            bool_sparsity,
            A_rcv.rcv,
            warning,
            fix_likelihood.f,
        )
    """
    -------------------------------------------------------------------------
    {xsrst_begin py_mixed_warning}
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
    This is the :ref:`py_mixed_ctor.warning` argument to the  mixed class
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

    {xsrst_end py_mixed_warning}
    -------------------------------------------------------------------------
    """
    def warning(self, message) :
        self.obj.warning(message)
    def post_warning(self, message) :
        self.obj.post_warning(message)
    """
    {xsrst_begin py_mixed_fatal_error}
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

    {xsrst_end py_mixed_fatal_error}
    """
    def post_fatal_error(self, message) :
        self.obj.post_fatal_error(message)
