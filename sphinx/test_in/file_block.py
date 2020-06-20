# -----------------------------------------------------------------------------
#         cppad_py: A C++ Object Library and Python Interface to Cppad
#          Copyright (C) 2017-20 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# --------------------------------------------------------------------------
"""
{begin_sphinxrst file_block_example}

==================
File Block Example
==================

{file_sphinxrst%%# BEGIN_SRC%# END_SRC%}


{end_sphinxrst file_block_example}
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
{begin_sphinxrst file_block_result}

=================
File Block Result
=================

Text before file block.
{file_sphinxrst%%# BEGIN_FACTORIAL%# END_FACTORIAL%}
Text after file block.

:ref:`file_block_example`

{end_sphinxrst file_block_result}
"""
# END_SRC
