# -----------------------------------------------------------------------------
#         cppad_py: A C++ Object Library and Python Interface to Cppad
#          Copyright (C) 2017-22 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# ----------------------------------------------------------------------------
# {xrst_comment_ch #}
#
# {xrst_begin_parent comment_ch_exam}
#
# =========================
# Comment Character Example
# =========================
#
# {xrst_literal
#     # BEGIN_SRC
#     # END_SRC
# }
#
# {xrst_end comment_ch_exam}
# ----------------------------------------------------------------------------
#
# BEGIN_SRC
# {xrst_begin comment_ch_res}
#
# ========================
# Comment Character Result
# ========================
# In the original source, the leading characters '#' and ' ' get removed
# and the remaining text lines up with the ``def`` below:
#
# {xrst_code py}
def factorial(n) :
    if n == 1 :
        return 1
    return n * factorial(n-1)
# {xrst_code}
#
# :ref:`@comment_ch_exam`
#
# {xrst_end comment_ch_res}
# END_SRC
