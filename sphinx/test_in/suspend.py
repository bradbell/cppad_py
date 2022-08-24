# -----------------------------------------------------------------------------
#         cppad_py: A C++ Object Library and Python Interface to Cppad
#          Copyright (C) 2017-22 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# ----------------------------------------------------------------------------
"""
{xrst_begin_parent suspend_exam}

Suspend Example
###############

{xrst_literal
    # BEGIN_SRC
    # END_SRC
}

{xrst_end suspend_exam}
"""
# ----------------------------------------------------------------------------
# BEGIN_SRC
"""
{xrst_begin suspend_res}
{xrst_spell
    iterable
}

Suspend Result
##############

Factorial
*********
*f* = ``factorial(`` *positive_integer* ``)``
{xrst_suspend}
"""
def factorial(n) :
    if n == 1 :
        return 1
    return n * factorial(n-1)
"""
{xrst_resume}

Product
*******
*p* = ``product(`` *iterable* ``)``
{xrst_suspend}
"""
def product(itr) :
    p = 1.0
    for v in itr :
        p *= v
    return p
"""
{xrst_resume}

:ref:`@suspend_exam`

{xrst_end suspend_res}
"""
# END_SRC
