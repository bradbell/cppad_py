# -----------------------------------------------------------------------------
#         cppad_py: A C++ Object Library and Python Interface to Cppad
#          Copyright (C) 2017-20 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# -----------------------------------------------------------------------------
# mixed fix_likelihood
# -----------------------------------------------------------------------------
# BEGIN SOURCE
def fix_likelihood_xam() :
    import cppad_py
    import numpy
    ok         = True
    #
    mean_theta = 1.0 # mean of prior for theta
    z          = 2.0 # data that does not depend on random effects
    std        = 1.0 # standard deviation of both data and prior
    #
    # value of theta at which we will record fix_likelihood( theta )
    theta      = numpy.array([ mean_theta ], dtype=float )
    #
    # indpeendent variables during the recording
    atheta     = cppad_py.independent(theta)
    #
    # - log[ p(theta) ]
    ares     = ( atheta[0] - mean_theta ) / std
    ap_theta = 0.5 * ares * ares
    #
    # - log[ p(z|theta)
    ares       = ( z  - atheta[0] ) / std
    ap_z_theta = 0.5 * ares * ares
    #
    # - log[ p(z|theta) p(theta) ]
    av_0 = ap_z_theta + ap_theta
    #
    # function mapping theta -> v
    av   = numpy.array( [ av_0 ] )
    fun  = cppad_py.d_fun(atheta, av)
    #
    # mixed_obj
    mixed_obj = cppad_py.mixed(
        fixed_init     = theta ,
        fix_likelihood = fun,
    )
    #
    # optimize_fixed
    options  = 'String  sb    yes\n'     # suppress optimizer banner
    options += 'Integer print_level 0\n' # suppress optimizer trace
    solution  = mixed_obj.optimize_fixed(
        fixed_ipopt_options = options
    )
    #
    # optimal value for theta
    theta_opt = solution.fixed_opt
    #
    # check solution
    ok        = ok and abs( (mean_theta + z) / 2.0 - theta_opt[0] ) < 1e-10
    return ok
#
# END SOURCE
'''
{xsrst_begin mixed_fix_likelihood_xam_py}

.. include:: ../preamble.rst

Mixed Class fix_likelihood: Example and Test
############################################
{xsrst_file
  # BEGIN SOURCE
  # END SOURCE
}
{xsrst_end mixed_fix_likelihood_xam_py}
'''
