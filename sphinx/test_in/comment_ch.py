# vim: set expandtab:
# -----------------------------------------------------------------------------
#         cppad_py: A C++ Object Library and Python Interface to Cppad
#          Copyright (C) 2017-20 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# ----------------------------------------------------------------------------
# {xsrst_comment_ch #}
#
# {xsrst_begin_parent comment_ch_exam}
#
# ===============================
# Begin Special Character Example
# ===============================
#
# {xsrst_file
#     # BEGIN_SRC
#     # END_SRC
# }
#
# {xsrst_end comment_ch_exam}
# ----------------------------------------------------------------------------
#
# BEGIN_SRC
# {xsrst_begin comment_ch_res}
#
# ==============================
# Begin Special Character Result
# ==============================
# In the original source, the leading characters '#' and ' ' get removed
# and the remaining text lines up with the ``def`` below:
#
# {xsrst_code py}
def factorial(n) :
    if n == 1 :
        return 1
    return n * factorial(n-1)
# {xsrst_code}
#
# :ref:`comment_ch_exam`
#
# {xsrst_end comment_ch_res}
# END_SRC
