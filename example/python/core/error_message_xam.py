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
    #
    # initialize return variable
    ok = True
    # ---------------------------------------------------------------------
    ok = False
    try :
        cppad_py.error_message("test message")
    except : # catch
        stored_message = cppad_py.error_message("")
        ok = (stored_message == "test message")
    #
    return( ok  )
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
