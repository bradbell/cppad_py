# -----------------------------------------------------------------------------
#         cppad_py: A C++ Object Library and Python Interface to Cppad
#          Copyright (C) 2017-20 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# -----------------------------------------------------------------------------
# error_message
# -----------------------------------------------------------------------------
# BEGIN SOURCE
def error_message_xam() :
    #
    import numpy
    import cppad_py
    import sys
    #
    ok_list = list()
    try :
        left     = cppad_py.a_double(1.0)
        right    = cppad_py.a_double(2.0)
        if_true  = cppad_py.a_double(3.0)
        if_false = cppad_py.a_double(4.0)
        target   = cppad_py.a_double()
        target.cond_assign(
            '<>', left, right, if_true, if_false
        )
    except RuntimeError as e: # catch
        message = str(e)
        index   = message.find("'<>' is not a valid comparison operator")
        ok      = 0 <= index
        ok_list.append( ok )
    #
    if len( ok_list ) == 0 :
        ok_list.append(False)
    return( ok_list[0]  )
#
# END SOURCE
# -----------------------------------------------------------------------------
# {xsrst_comment_ch #}
#
# {xsrst_begin error_message_xam_py}
#
# .. include:: ../preamble.rst
#
# {xsrst_spell
#   cppad
# }
# Python: Cppad Py Exception Handling: Example and Test
# #####################################################
# {xsrst_file
#   # BEGIN SOURCE
#   # END SOURCE
# }
# {xsrst_end error_message_xam_py}
#
