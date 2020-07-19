# -----------------------------------------------------------------------------
#         cppad_py: A C++ Object Library and Python Interface to Cppad
#          Copyright (C) 2017-20 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# ----------------------------------------------------------------------------
"""
{xsrst_begin_parent suspend_exam}

Suspend Example
###############

{xsrst_file
    # BEGIN_SRC
    # END_SRC
}

{xsrst_end suspend_exam}
"""
# ----------------------------------------------------------------------------
# BEGIN_SRC
"""
{xsrst_begin suspend_res}
{xsrst_spell
    iterable
}

Suspend Result
##############

Factorial
*********
*f* = ``factorial(`` *positive_integer* ``)``
{xsrst_suspend}
"""
def factorial(n) :
    if n == 1 :
        return 1
    return n * factorial(n-1)
"""
{xsrst_resume}

Product
*******
*p* = ``product(`` *iterable* ``)``
{xsrst_suspend}
"""
def product(itr) :
    p = 1.0
    for v in itr :
        p *= v
    return p
"""
{xsrst_resume}

:ref:`suspend_exam`

{xsrst_end suspend_res}
"""
# END_SRC
