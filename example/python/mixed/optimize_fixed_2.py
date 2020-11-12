# -----------------------------------------------------------------------------
#         cppad_py: A C++ Object Library and Python Interface to Cppad
#          Copyright (C) 2017-20 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# -----------------------------------------------------------------------------
# mixed optimize_fixed
# -----------------------------------------------------------------------------
'''
{xsrst_begin mixed_optimize_fixed_2_py}
{xsrst_spell
    ipopt
}

.. include:: ../preamble.rst

The Ipopt Example Problem: Example and Test
###########################################

Problem
*******
This optimization problem is take from the
`ipopt interfaces <https://coin-or.github.io/Ipopt/INTERFACES.html>`_
documentation.

.. math::

    \begin{align}
    \R{minimize} \;
        & x_0 x_3 ( x_0 + x_1 + x_2) + x_2
        & & \R{w.r.t \;} x \in \B{R}^4
    \\
    \R{subject \; to}  \;
        & 25 \leq  x_0 x_1 x_2 x_3 \\
        & 40 =  x_0^2 + x_1^2 + x_2^2 + x_3^2 \\
        & 1 \leq x \leq 5
    \end{align}

The starting point for the optimization is :math:`(1,5,5,1)`
and the optimal solution is

.. math:

    (1.00000000, 4.74299963, 3.82114998, 1.37940829)

{xsrst_file
  # BEGIN SOURCE
  # END SOURCE
}
{xsrst_end mixed_optimize_fixed_2_py}
'''
# BEGIN SOURCE
def optimize_fixed_2() :
    import cppad_py
    import numpy
    ok         = True
    inf        = numpy.inf
    #
    # define f(x) = x_0 x_3 ( x_0 + x_1 + x_2) + x_2
    x_start = numpy.array([ 1, 5, 5, 1 ], dtype=float )
    ax      = cppad_py.independent(x_start)
    av_0    = ax[0] * ax[3] * ( ax[0] + ax[1] + ax[2] ) + ax[2]
    av      = numpy.array( [ av_0 ] )
    f       = cppad_py.d_fun(ax, av)
    #
    # define g_0 (x) = x_0 * x_1 * x_2 * x_3
    #        g_1 (x) = x_0^2 + x_1^2 + x_2^2 + x_3^2
    ax       = cppad_py.independent(x_start)
    av_0     = ax[0] * ax[1] * ax[2] * ax[3]
    av_1     = ax[0]*ax[0] + ax[1]*ax[1] + ax[2]*ax[2] + ax[3]*ax[3]
    av       = numpy.array( [av_0, av_1] )
    g        = cppad_py.d_fun(ax, av)
    #
    x_lower  = numpy.array( [1, 1, 1, 1], dtype=float )
    x_upper  = numpy.array( [5, 5, 5, 5], dtype=float )
    g_lower  = numpy.array( [  25, 40], dtype=float )
    g_upper  = numpy.array( [ inf, 40], dtype=float )
    #
    mixed_obj = cppad_py.mixed(
        fixed_init     = x_start,
        fix_likelihood = f,
        fix_constraint = g,
    )
    #
    options  = 'String  sb    yes\n'     # suppress optimizer banner
    options += 'Integer print_level 0\n' # suppress optimizer trace
    solution  = mixed_obj.optimize_fixed(
        fixed_ipopt_options   = options,
        fixed_lower           = x_lower,
        fixed_upper           = x_upper,
        fixed_in              = x_start,
        fix_constraint_lower  = g_lower,
        fix_constraint_upper  = g_upper,
    )
    x_opt   = solution.fixed_opt
    x_check =  numpy.array( [1.00000000, 4.74299963, 3.82114998, 1.37940829] )
    ok      = ok and numpy.all( numpy.abs( x_opt - x_check ) < 1e-7 )
    return ok
# END SOURCE
