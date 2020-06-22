# vim: set expandtab:
# -----------------------------------------------------------------------------
#         cppad_py: A C++ Object Library and Python Interface to Cppad
#          Copyright (C) 2017-20 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# ----------------------------------------------------------------------------
"""
{sphinxrst_begin code_block_exam}

==================
Code Block Example
==================

{sphinxrst_file%%# BEGIN_SRC%# END_SRC%}

{sphinxrst_end code_block_exam}
"""
# ----------------------------------------------------------------------------
# BEGIN_SRC
"""
{sphinxrst_begin code_block_res}

=================
Code Block Result
=================
{sphinxrst_code}"""
def factorial(n) :
    if n == 1 :
        return 1
    return n * factorial(n-1)
"""{sphinxrst_code}

:ref:`code_block_exam`

{sphinxrst_end code_block_res}
"""
# END_SRC
