# vim: set expandtab:
# -----------------------------------------------------------------------------
#         cppad_py: A C++ Object Library and Python Interface to Cppad
#          Copyright (C) 2017-20 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# ----------------------------------------------------------------------------
"""
{begin_sphinxrst code_block_py}

Code Block Example / Test
=========================
{code_sphinxrst python}"""
def factorial(n) :
    if n == 1 :
        return 1
    return n * factorial(n-1)
"""{code_sphinxrst}
{end_sphinxrst code_block_py}
"""
