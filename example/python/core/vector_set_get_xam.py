# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileCopyrightText: Bradley M. Bell <bradbell@seanet.com>
# SPDX-FileContributor: 2017-22 Bradley M. Bell
# ----------------------------------------------------------------------------
# std::vector<double>
# -----------------------------------------------------------------------------
# BEGIN SOURCE
def vector_set_get_xam() :
   #
   import numpy
   import cppad_py
   #
   # initialize return variable
   ok = True
   # ---------------------------------------------------------------------
   n = 4
   bv = cppad_py.vec_bool(n)
   iv = cppad_py.vec_int(n)
   dv = numpy.empty(n, dtype=float)
   av = numpy.empty(n, dtype=cppad_py.a_double)
   #
   # setting elements
   for i in range( n  ) :
      bv[i] = i > n / 2
      iv[i] = 2 * i
      dv[i] = 3.0 * i
      av[i] = cppad_py.a_double(4.0 * i)
   #
   #
   for i in range( n  ) :
      be = bv[i]
      ok = ok and be == (i > n / 2)
      #
      ie = iv[i]
      ok = ok and ie == 2 * i
      #
      de = dv[i]
      ok = ok and de == 3.0 * i
      #
      ae = av[i]
      ok = ok and ae == 4.0 * i
   #
   #
   return( ok )
#
# END SOURCE
#
#
# {xrst_begin vector_set_get_xam_py}
# {xrst_comment_ch #}
#
# Python: Setting and Getting Vector Elements: Example and Test
# #############################################################
# {xrst_literal
#  # BEGIN SOURCE
#  # END SOURCE
# }
# {xrst_end vector_set_get_xam_py}
#
