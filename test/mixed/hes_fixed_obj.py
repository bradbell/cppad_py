# -----------------------------------------------------------------------------
#         cppad_py: A C++ Object Library and Python Interface to Cppad
#          Copyright (C) 2017-20 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# -----------------------------------------------------------------------------
# hes_fixed_obj: check case where Hessian is sparse
# -----------------------------------------------------------------------------
def hes_fixed_obj() :
    import cppad_py
    import numpy
    ok         = True
    #
    n_fixed  = 5
    n_random = 0
    #
    # value of theta and we will record fix_likelihood( theta )
    theta = numpy.ones(n_fixed, dtype=float)
    #
    # independent variables during the recording
    atheta = cppad_py.independent(theta)
    #
    a_sum   = 0.0
    for i in range(n_fixed) :
        j      = (i + 1) % n_fixed
        a_sum += (i + j) * atheta[i] * atheta[j]
    #
    av   = numpy.array( [ a_sum ], dtype=cppad_py.a_double )
    f    = cppad_py.d_fun(atheta, av)
    #
    # mixed_obj
    empty = numpy.array( [ ], dtype=float )
    mixed_obj = cppad_py.mixed(
        fixed_init     = theta    ,
        random_init    = empty    ,
        fix_likelihood = f        ,
    )
    #
    # hes_fixed_obj_rcv
    hes_fixed_obj_rcv = cppad_py.sparse_rcv()
    mixed_obj.hes_fixed_obj(
        hes_fixed_obj_rcv        ,
        fixed_vec  = theta       ,
        random_opt = empty       ,
    )
    # check lower triangle of the Hessian
    ok  = ok and hes_fixed_obj_rcv.nr()  == n_fixed
    ok  = ok and hes_fixed_obj_rcv.nc()  == n_fixed
    ok  = ok and hes_fixed_obj_rcv.nnz() == n_fixed
    row = hes_fixed_obj_rcv.row()
    col = hes_fixed_obj_rcv.col()
    val = hes_fixed_obj_rcv.val()
    for k in range( hes_fixed_obj_rcv.nnz() ) :
        i  = row[k]
        j  = col[k]
        ok = ok and j < i
        ok = ok and ( (j+1 == i) or (j==0 and i == n_fixed-1) )
        ok = ok and val[k] == (i + j)
    return ok
# END SOURCE
