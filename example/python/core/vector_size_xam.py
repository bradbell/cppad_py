# -----------------------------------------------------------------------------
#         cppad_py: A C++ Object Library and Python Interface to Cppad
#          Copyright (C) 2017-22 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# -----------------------------------------------------------------------------
# vector size()
# -----------------------------------------------------------------------------
# BEGIN SOURCE
def vector_size_xam() :
    #
    import numpy
    import cppad_py
    #
    # initialize return variable
    ok = True
    # ---------------------------------------------------------------------
    # create vectors
    bv = cppad_py.vec_bool()
    iv = cppad_py.vec_int(1)
    dv = cppad_py.vec_double(2)
    av = cppad_py.vec_a_double(3)
    #
    # check size of vectors
    ok = ok and bv.size() == 0
    ok = ok and iv.size() == 1
    ok = ok and dv.size() == 2
    ok = ok and av.size() == 3
    #
    return( ok )
#
# END SOURCE
#
# {xrst_comment_ch #}
#
# {xrst_begin vector_size_xam_py}
#
# {xrst_spell
# }
# Python: Size of Vectors: Example and Test
# #########################################
# {xrst_literal
#   # BEGIN SOURCE
#   # END SOURCE
# }
# {xrst_end vector_size_xam_py}
#
