# vim: set expandtab:
# -----------------------------------------------------------------------------
#         cppad_py: A C++ Object Library and Python Interface to Cppad
#          Copyright (C) 2017-20 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# ----------------------------------------------------------------------------
# BEGIN_SRC
# BEGIN_FACTORIAL
def factorial(n) :
    if n == 1 :
        return 1
    return n * factorial(n-1)
# END_FACTORIAL
"""
{begin_sphinxrst file_block_py}

.. _file_block_py:

File Block Example
==================

Text before file block.
{file_sphinxrst%%# BEGIN_FACTORIAL%# END_FACTORIAL%}
Text after file block.

Source
------
:ref:`file_block_src`

{end_sphinxrst file_block_py}
"""
# END_SRC
# --------------------------------------------------------------------------
"""
{begin_sphinxrst file_block_src}

.. _file_block_src:

File Block Source
=================

{file_sphinxrst%%# BEGIN_SRC%# END_SRC%}

Example
-------
:ref:`file_block_py`

{end_sphinxrst file_block_src}
"""
