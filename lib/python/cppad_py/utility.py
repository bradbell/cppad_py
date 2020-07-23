# -----------------------------------------------------------------------------
#         cppad_py: A C++ Object Library and Python Interface to Cppad
#          Copyright (C) 2017-20 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# -----------------------------------------------------------------------------
import numpy
import cppad_py
# -----------------------------------------------------------------------------
# $begin numpy2vec$$ $newlinech #$$
# $spell
#   Numpy
#   cppad_py
#   vec
#   dtype
#   tuple
#   str
#   bool
# $$
#
# $section Convert a Numpy Array to a cppad_py Vector$$
#
# $head Syntax$$
# $icode%vec% = cppad_py.utility.numpy2vec(
#   %array%, %dtype%, %shape%, %context%, %name%
# )%$$
#
# $head array$$
# This is either a vector (only one index) or a matrix
# (has two indices) that we are converting to a vector.
# If this array does not match the conditions below,
# an exception is raised with an appropriate error message.
#
# $head dtype$$
# This is the expected data type for the elements of the array.
# It must be one of the following:
# $code bool$$, $code int$$, $code float$$ or $code cppad_py.a_double$$.
#
# $head shape$$
# This either a $code int$$ or a tuple of $code int$$ with length one or two.
# If it is an $code int$$, $icode array$$ is expected to be a vector.
# If it is a tuple with length one, $icode array$$ is expected to be a vector.
# Otherwise a matrix is expected.
#
# $head context$$
# This is the context that $icode array$$ appears in
# (often to syntax for some other operation).
# It is a $code str$$ that is used for error reporting.
#
# $head name$$
# This is the name used for $icode array$$ in $icode context$$.
# It is a $code str$$ that is used for error reporting.
#
# $head vec$$
# This is the values of $icode array$$
# as a vector is row major order.
# It has type $code vec_double$$ if $icode dtype$$ is $code float$$,
# and $code vec_a_double$$ if $icode dtype$$ is $code a_double$$.
#
# $end
# -----------------------------------------------------------------------------
def numpy2vec(array, dtype, shape, context, name) :
    #
    # dtype
    assert dtype in [bool, int, float, cppad_py.a_double]
    # -------------------------------------------------------------------------
    #
    if not isinstance(array, numpy.ndarray) :
        msg = context + ': ' + name + ' is not an numpy.ndarray'
        raise NotImplementedError(msg)
    if not array.dtype == dtype :
        msg = context + ': ' + name + '.dtype is not ' + str(dtype)
        raise NotImplementedError(msg)
    #
    # vector, nr, nc
    if isinstance(shape, int) :
        vector = True
        nr     = shape
        nc     = 1
    elif len(shape) == 1 :
        vector = True
        nr     = shape[0]
        nc     = 1
    else :
        assert len(shape) == 2
        vector = False
        nr     = shape[0]
        nc     = shape[1]
    #
    if vector and len(array.shape) != 1 :
        msg = context + ': ' + name + ' is not a vector'
    elif len(array.shape) != 2 :
        msg = context + ': ' + name + ' is not a matrix'
    #
    if array.shape[0] != nr :
        msg = context + ': ' + name + '.shape[0] is not ' + str(nr)
    #
    if dtype == bool :
        vec = cppad_py.vec_bool(nr * nc)
    if dtype == int :
        vec = cppad_py.vec_int(nr * nc)
    if dtype == float :
        vec = cppad_py.vec_double(nr * nc)
    if dtype == cppad_py.a_double :
        vec = cppad_py.vec_a_double(nr * nc)
    #
    if vector :
        for i in range(nr) :
            # must copy data so vec can manage its own memory
            vec[i] = dtype( array[i] )
    else :
        if array.shape[1] != nc :
            msg = context + ': ' + name + '.shape[1] is not ' + str(nc)
        #
        for i in range(nr) :
            for j in range(nc):
                # must copy data so vec can manage its own memory
                vec[i * nc + j] = dtype( array[i, j] )
    #
    return vec
# -----------------------------------------------------------------------------
# $begin vec2numpy$$ $newlinech #$$
#
# $spell
#   cppad_py
#   numpy
#   vec
#   nr
#   nc
#   len
# $$
#
# $section Convert a cppad_py Vector to a Numpy Array$$
#
# $head Syntax$$
# $icode%array% = cppad_py.utility.vec2numpy(%vec%, %nr%)
# %$$
# $icode%array% = cppad_py.utility.vec2numpy(%vec%, %nr%, %nc%)
# %$$
#
# $head vec$$
# This must have one of the following types:
# $code cppad_py.vec_int$$,
# $code cppad_py.vec_double$$,
# $code vec_py.vec_a_double$$.
# with size equal to $icode%nr%*%nc%$$.
#
# $head nr$$
# This is an $code int$$ equal to the number of rows in the array.
# If the argument $icode nc$$ is not present, the array is a vector; i.e.,
# $codei%len( %array%.shape ) == 1%$$.
#
# $head nc$$
# If this argument is present,
# it is an $code int$$ equal to the number of columns in the array.
# In this case the array is a matrix; i.e.,
# $codei%len( %array%.shape ) == 2%$$.
#
# $head array$$
# This is the array corresponding to $icode vec$$ in row major order.
# Note that this array can be used after the vector $icode vec$$ drops
# out of scope (is deleted).
#
# $end
# -----------------------------------------------------------------------------
def vec2numpy(vec, nr, nc = None) :
    # dtype
    if type(vec) == cppad_py.vec_int :
        dtype = int
    elif type(vec) == cppad_py.vec_double :
        dtype = float
    else :
        assert type(vec) == cppad_py.vec_a_double
        dtype = cppad_py.a_double
    #
    if nc == None :
        assert vec.size() == nr
        array = numpy.empty(nr, dtype)
        for i in range(nr) :
            # when dtype is cppad_py.a_double we need a copy of vec[i]
            # so that is does not get deleted when vec is deleted
            array[i] = dtype( vec[i] )
    else :
        assert vec.size() == nr * nc
        array = numpy.empty( (nr, nc), dtype)
        for i in range(nr) :
            for j in range(nc) :
                # when dtype is cppad_py.a_double we need a copy of vec[i]
                # so that is does not get deleted when vec is deleted
                array[i, j] = dtype( vec[i * nc + j] )
    #
    return array
