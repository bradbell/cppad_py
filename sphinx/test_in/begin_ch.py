# vim: set expandtab:
# -----------------------------------------------------------------------------
#         cppad_py: A C++ Object Library and Python Interface to Cppad
#          Copyright (C) 2017-20 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# ----------------------------------------------------------------------------
"""
{xsrst_begin begin_ch_exam}

===============================
Begin Special Character Example
===============================

{xsrst_file # BEGIN_SRC
    # END_SRC
}

{xsrst_end begin_ch_exam}
"""
# ----------------------------------------------------------------------------
# BEGIN_SRC
# {xsrst_begin begin_ch_res #}
#
# ==============================
# Begin Special Character Result
# ==============================
# {xsrst_code}
def factorial(n) :
    if n == 1 :
        return 1
    return n * factorial(n-1)
# {xsrst_code}
#
#:ref:`begin_ch_exam`
#
# {xsrst_end begin_ch_res}
# END_SRC
