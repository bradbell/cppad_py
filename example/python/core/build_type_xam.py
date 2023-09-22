# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileCopyrightText: Bradley M. Bell <bradbell@seanet.com>
# SPDX-FileContributor: 2017-23 Bradley M. Bell
# ----------------------------------------------------------------------------
# build_type
# -----------------------------------------------------------------------------
# BEGIN SOURCE
def build_type_xam() :
   import cppad_py
   #
   # build_type
   build_type = cppad_py.build_type()
   #
   # ok
   ok = build_type in [ 'debug', 'release' ]
   #
   return ok
#
# END SOURCE
# -----------------------------------------------------------------------------
#
# {xrst_begin build_type_xam.py}
# {xrst_comment_ch #}
#
# Python: CppAD Py build_type: Example and Test
# #############################################
# {xrst_literal
#  # BEGIN SOURCE
#  # END SOURCE
# }
# {xrst_end build_type_xam.py}
#
