# -----------------------------------------------------------------------------
#         cppad_py: A C++ Object Library and Python Interface to Cppad
#          Copyright (C) 2017-20 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# -----------------------------------------------------------------------------
# a_double unary operators
# -----------------------------------------------------------------------------
# BEGIN SOURCE
def a_double_unary_op_xam() :
    #
    import numpy
    import cppad_py
    #
    # initialize return variable
    ok = True
    # ---------------------------------------------------------------------
    a2 = cppad_py.a_double(2.0)
    aplus2 = + a2
    a2_minus = - a2
    #
    ok = ok and aplus2 == 2.0
    ok = ok and a2_minus == -2.0
    #
    return( ok )
#
# END SOURCE
#
# {xsrst_comment_ch #}
#
# {xsrst_begin a_double_unary_op_xam_py}
#
# .. include:: ../preamble.rst
#
# {xsrst_spell
# }
# Python: a_double Unary Plus and Minus: Example and Test
# #######################################################
# {xsrst_file
#   # BEGIN SOURCE
#   # END SOURCE
# }
# {xsrst_end a_double_unary_op_xam_py}
#
