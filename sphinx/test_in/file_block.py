# vim: set expandtab:
# -----------------------------------------------------------------------------
#         cppad_py: A C++ Object Library and Python Interface to Cppad
#          Copyright (C) 2017-20 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# ----------------------------------------------------------------------------
# BEGIN_FACTORIAL
def factorial(n) :
    if n == 1 :
        return 1
    return n * factorial(n-1)
# END
"""
    {begin_sphinxrst file_block_py}

    File Code Block Example / Test
    ==============================

    Text before file block.
    {file_sphinxrst%%# BEGIN_FACTORIAL%# END%}
    Text after file block.

    {end_sphinxrst file_block_py}
"""
