# -----------------------------------------------------------------------------
#         cppad_py: A C++ Object Library and Python Interface to Cppad
#          Copyright (C) 2017-20 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# -----------------------------------------------------------------------------
# mixed fatal_error
# -----------------------------------------------------------------------------
# BEGIN SOURCE
def fatal_error_xam() :
    import cppad_py
    import numpy
    #
    ok_list       = list()
    #
    fixed_init = numpy.array( [ 1 ], dtype=float )
    mixed_obj  = cppad_py.mixed(fixed_init = fixed_init)
    try :
        mixed_obj.post_fatal_error('Testing fatal error')
    except RuntimeError as error :
        if str(error) == 'Testing fatal error' :
            ok_list.append(True)
    #
    ok = len(ok_list) == 1
    for i in range( len(ok_list) ) :
        ok = ok and ok_list[i] == True
    return ok
#
# END SOURCE
'''
{xsrst_begin mixed_fatal_error_xam_py}

.. include:: ../preamble.rst

Python: Mixed Class fatal_error: Example and Test
#################################################

{xsrst_file
  # BEGIN SOURCE
  # END SOURCE
}
{xsrst_end mixed_fatal_error_xam_py}
'''
