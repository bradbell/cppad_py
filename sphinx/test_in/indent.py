# -----------------------------------------------------------------------------
#         cppad_py: A C++ Object Library and Python Interface to Cppad
#          Copyright (C) 2017-20 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# ----------------------------------------------------------------------------
"""
{xsrst_begin_parent indent_exam}

Indent Example
##############

{xsrst_file
    # BEGIN_SRC
    # END_SRC
}

{xsrst_end indent_exam}
"""
# ----------------------------------------------------------------------------
# BEGIN_SRC
"""
    {xsrst_begin indent_res}

    =============
    Indent Result
    =============
    {xsrst_code py}"""
    def factorial(n) :
        if n == 1 :
            return 1
        return n * factorial(n-1)
    """{xsrst_code}

    :ref:`indent_exam`

    {xsrst_end indent_res}
"""
# END_SRC
