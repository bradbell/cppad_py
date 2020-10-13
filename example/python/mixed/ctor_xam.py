# -----------------------------------------------------------------------------
#         cppad_py: A C++ Object Library and Python Interface to Cppad
#          Copyright (C) 2017-20 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# -----------------------------------------------------------------------------
# mixed ctor
# -----------------------------------------------------------------------------
# BEGIN SOURCE
def ctor_xam() :
    import cppad_py
    #
    ok_list       = list()
    #
    n_fixed       = 1
    n_random      = 2
    quasi_fixed   = True
    bool_sparsity = False
    empty_pattern = cppad_py.sparse_rc()
    A_rcv         = cppad_py.sparse_rcv(empty_pattern)
    def warning(message) :
        if message == 'Testing warning' :
            ok_list.append(True)
    mixed_obj = cppad_py.mixed(
        n_fixed,
        n_random,
        quasi_fixed,
        bool_sparsity,
        A_rcv,
        warning
    )
    mixed_obj.post_warning('Testing warning')
    #
    ok = len(ok_list) == 1
    if ok :
        ok = ok and ok_list[0] == True
    return ok
#
# END SOURCE
'''
{xsrst_begin mixed_ctor_xam_py}

.. include:: ../preamble.rst

Python: Mixed Class Constructor: Example and Test
#################################################
{xsrst_file
  # BEGIN SOURCE
  # END SOURCE
}
{xsrst_end mixed_ctor_xam_py}
'''
