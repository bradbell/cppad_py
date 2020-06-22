# vim: set expandtab:
# -----------------------------------------------------------------------------
#         cppad_py: A C++ Object Library and Python Interface to Cppad
#          Copyright (C) 2017-20 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# ----------------------------------------------------------------------------
"""
{sphinxrst_begin suspend_exam}

===============
Suspend Example
===============

{sphinxrst_file%%# BEGIN_SRC%# END_SRC%}

{sphinxrst_end suspend_exam}
"""
# ----------------------------------------------------------------------------
# BEGIN_SRC
"""
{sphinxrst_begin suspend_res}
{sphinxrst_spell
    iterable
}

==============
Suspend Result
==============

Factorial
---------
*f* = ``factorial(`` *positive_integer* ``)``
{sphinxrst_suspend}
"""
def factorial(n) :
    if n == 1 :
        return 1
    return n * factorial(n-1)
"""
{sphinxrst_resume}

Product
-------
*p* = ``product(`` *iterable* ``)``
{sphinxrst_suspend}
"""
def product(itr) :
    p = 1.0
    for v in itr :
        p *= v
    return p
"""
{sphinxrst_resume}

:ref:`suspend_exam`

{sphinxrst_end suspend_res}
"""
# END_SRC
