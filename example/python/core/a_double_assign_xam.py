# -----------------------------------------------------------------------------
#         cppad_py: A C++ Object Library and Python Interface to Cppad
#          Copyright (C) 2017-20 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# -----------------------------------------------------------------------------
# a_double assignment
# -----------------------------------------------------------------------------
# BEGIN SOURCE
def a_double_assign_xam() :
    #
    import numpy
    import cppad_py
    #
    # initialize return variable
    ok = True
    # ---------------------------------------------------------------------
    #
    ax = cppad_py.a_double(3.0);
    ok = ok and ax == 3.0
    #
    ax += cppad_py.a_double(2.0);
    ok = ok and ax == 5.0
    #
    ax -= 1.0;
    ok = ok and ax == cppad_py.a_double(4.0)
    #
    ax *= cppad_py.a_double(3.0);
    ok = ok and ax == 12.0
    #
    ax /= 4.0;
    ok = ok and ax == cppad_py.a_double(3.0)
    #
    return( ok )
#
# END SOURCE
#
# {xsrst_comment_ch #}
#
# {xsrst_begin a_double_assign_xam_py}
#
# .. include:: ../preamble.rst
#
# {xsrst_spell
# }
# Python: a_double Assignment Operators: Example and Test
# #######################################################
# {xsrst_file
#   # BEGIN SOURCE
#   # END SOURCE
# }
# {xsrst_end a_double_assign_xam_py}
#
