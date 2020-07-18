# -----------------------------------------------------------------------------
#         cppad_py: A C++ Object Library and Python Interface to Cppad
#          Copyright (C) 2017-20 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# -----------------------------------------------------------------------------
# sparse_rc
# -----------------------------------------------------------------------------
# BEGIN SOURCE
def sparse_rc_xam() :
    #
    import numpy
    import cppad_py
    #
    # initialize return variable
    ok = True
    # ---------------------------------------------------------------------
    #
    # create a sparsity pattern
    pattern = cppad_py.sparse_rc()
    #
    nr = 6
    nc = 5
    nnz = 4
    #
    # resize
    pattern.resize(nr, nc, nnz)
    #
    ok = ok and pattern.nr()  == nr
    ok = ok and pattern.nc()  == nc
    ok = ok and pattern.nnz() == nnz
    #
    # indices corresponding to upper-diagonal
    for k in range( nnz ) :
        pattern.put(k, k, k+1)
    #
    #
    # row and column indices
    row = pattern.row()
    col = pattern.col()
    #
    # check row and column indices
    for k in range( nnz ) :
        ok = ok and row[k] == k
        ok = ok and col[k] == k+1
    #
    #
    # For this case, row_major and col_major order are same as original order
    row_major = pattern.row_major()
    col_major = pattern.col_major()
    for k in range( nnz ) :
        ok = ok and row_major[k] == k
        ok = ok and col_major[k] == k
    #
    #
    return( ok )
#
# END SOURCE
#
# $begin sparse_rc_xam.py$$ $newlinech #$$
# $spell
#   py
#   perl
#   cppad
#   py
#   xam
#   Jacobian
#   Jacobians
# $$
# $section Python: Sparsity Patterns: Example and Test$$
# $srcthisfile|0|# BEGIN SOURCE|# END SOURCE|$$
# $end
#
