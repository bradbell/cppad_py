# -----------------------------------------------------------------------------
#         cppad_py: A C++ Object Library and Python Interface to Cppad
#          Copyright (C) 2017-20 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# -----------------------------------------------------------------------------
# mixed warning
# -----------------------------------------------------------------------------
# BEGIN SOURCE
def warning_xam() :
    import cppad_py
    #
    ok_list       = list()
    def my_warning(message) :
        if message == 'Testing warning' :
            ok_list.append(True)
    #
    mixed_obj = cppad_py.mixed(n_fixed = 1, warning = my_warning)
    mixed_obj.post_warning('Testing warning')
    #
    ok = len(ok_list) == 1
    for i in range( len(ok_list) ) :
        ok = ok and ok_list[i] == True
    return ok
#
# END SOURCE
'''
{xsrst_begin mixed_warning_xam_py}

.. include:: ../preamble.rst

Python: Mixed Class Warnings: Example and Test
##############################################
{xsrst_file
  # BEGIN SOURCE
  # END SOURCE
}
{xsrst_end mixed_warning_xam_py}
'''
