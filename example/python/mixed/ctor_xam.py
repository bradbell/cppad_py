# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileCopyrightText: Bradley M. Bell <bradbell@seanet.com>
# SPDX-FileContributor: 2017-22 Bradley M. Bell
# ----------------------------------------------------------------------------
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
# END SOURCE
'''
{xrst_begin mixed_ctor_xam_py}

Mixed Class Constructor: Example and Test
#########################################
{xrst_literal
  # BEGIN SOURCE
  # END SOURCE
}
{xrst_end mixed_ctor_xam_py}
'''
