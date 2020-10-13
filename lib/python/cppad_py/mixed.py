# -----------------------------------------------------------------------------
#         cppad_py: A C++ Object Library and Python Interface to Cppad
#          Copyright (C) 2017-20 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# -----------------------------------------------------------------------------
"""
{xsrst_begin_parent py_mixed}

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
    | |tab| *warning*
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
        self, n_fixed, n_random, quasi_newton, bool_sparsity, A_rcv, warning
    ) :
        self.obj = cppad_py.cppad_swig.mixed(
            n_fixed, n_random, quasi_newton, bool_sparsity, A_rcv.rcv, warning
        )
    """
    -------------------------------------------------------------------------
    {xsrst_begin py_mixed_warning}
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
