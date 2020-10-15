# -----------------------------------------------------------------------------
#         cppad_py: A C++ Object Library and Python Interface to Cppad
#          Copyright (C) 2017-20 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# -----------------------------------------------------------------------------
# mixed ctor
# -----------------------------------------------------------------------------
# BEGIN SOURCE
def ctor_xam() :
    import cppad_py
    import numpy
    ok         = True
    #
    fixed_init = numpy.array( [ 1 ], dtype=float )
    mixed_obj  = cppad_py.mixed(fixed_init = fixed_init)
    return ok
#
# END SOURCE
'''
{xsrst_begin mixed_ctor_xam_py}

.. include:: ../preamble.rst

Python: Mixed Class Constructor: Example and Test
#################################################
{xsrst_file
  # BEGIN SOURCE
  # END SOURCE
}
{xsrst_end mixed_ctor_xam_py}
'''
