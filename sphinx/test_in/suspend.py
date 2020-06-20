# vim: set expandtab:
# -----------------------------------------------------------------------------
#         cppad_py: A C++ Object Library and Python Interface to Cppad
#          Copyright (C) 2017-20 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# ----------------------------------------------------------------------------
"""
{begin_sphinxrst suspend_exam}

===============
Suspend Example
===============

{file_sphinxrst%%# BEGIN_SRC%# END_SRC%}

{end_sphinxrst suspend_exam}
"""
# ----------------------------------------------------------------------------
# BEGIN_SRC
"""
{begin_sphinxrst suspend_res}
{spell_sphinxrst
    iterable
}

==============
Suspend Result
==============

Factorial
---------
*f* = ``factorial(`` *positive_integer* ``)``
{suspend_sphinxrst}
"""
def factorial(n) :
    if n == 1 :
        return 1
    return n * factorial(n-1)
"""
{resume_sphinxrst}

Product
-------
*p* = ``product(`` *iterable* ``)``
{suspend_sphinxrst}
"""
def product(itr) :
    p = 1.0
    for v in itr :
        p *= v
    return p
"""
{resume_sphinxrst}

:ref:`suspend_exam`

{end_sphinxrst suspend_res}
"""
# END_SRC
