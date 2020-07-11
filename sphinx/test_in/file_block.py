# -----------------------------------------------------------------------------
#         cppad_py: A C++ Object Library and Python Interface to Cppad
#          Copyright (C) 2017-20 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# --------------------------------------------------------------------------
"""
{xsrst_begin_parent file_block_exam}

File Block Example
##################

{xsrst_file
    # BEGIN_SRC
    # END_SRC
}

{xsrst_end file_block_exam}
"""
# ----------------------------------------------------------------------------
# BEGIN_SRC
#
# BEGIN_FACTORIAL
def factorial(n) :
    if n == 1 :
        return 1
    return n * factorial(n-1)
# END_FACTORIAL
#
# BEGIN_SQUARE
def square(x) :
	# END_SQUARE
	return x * x
#
"""
{xsrst_begin file_block_res}

File Block Result
#################

factorial
*********
{xsrst_file
    # BEGIN_FACTORIAL
    # END_FACTORIAL
}

square
******
{xsrst_file
    # BEGIN_SQUARE
    # END_SQUARE
}

{xsrst_end file_block_res}
"""
# END_SRC
