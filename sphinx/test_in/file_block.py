# -----------------------------------------------------------------------------
#         cppad_py: A C++ Object Library and Python Interface to Cppad
#          Copyright (C) 2017-20 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# --------------------------------------------------------------------------
"""
{sphinxrst_begin file_block_exam}

==================
File Block Example
==================

{sphinxrst_file%%# BEGIN_SRC%# END_SRC%}


{sphinxrst_end file_block_exam}
"""
# ----------------------------------------------------------------------------
# BEGIN_SRC
# BEGIN_FACTORIAL
def factorial(n) :
    if n == 1 :
        return 1
    return n * factorial(n-1)
# END_FACTORIAL
"""
{sphinxrst_begin file_block_res}

=================
File Block Result
=================

Text before file block.
{sphinxrst_file%%# BEGIN_FACTORIAL%# END_FACTORIAL%}
Text after file block.

:ref:`file_block_exam`

{sphinxrst_end file_block_res}
"""
# END_SRC
