# -----------------------------------------------------------------------------
#         cppad_py: A C++ Object Library and Python Interface to Cppad
#          Copyright (C) 2017-22 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# -----------------------------------------------------------------------------
import numpy
import cppad_py
# -----------------------------------------------------------------------------
#
# {xrst_begin numpy2vec}
# {xrst_comment_ch #}
#
# {xrst_spell
#  cppad
#  bool
# }
#
# Convert a Numpy Array to a cppad_py Vector
# ##########################################
#
# Syntax
# ******
#
# | *vec* =  ``cppad_py.utility.numpy2vec`` (
# | |tab| *array* , *dtype* , *shape* , *context* , *name*
# | )
#
# array
# *****
# This is either a vector (only one index) or a matrix
# (has two indices) that we are converting to a vector.
# If this array does not match the conditions below,
# an exception is raised with an appropriate error message.
#
# dtype
# *****
# This is the expected data type for the elements of the array.
# It must be one of the following:
# ``bool`` , ``int`` , ``float`` or ``cppad_py.a_double`` .
#
# shape
# *****
# This either a ``int`` or a tuple of ``int`` with length one or two.
# If it is an ``int`` , *array* is expected to be a vector.
# If it is a tuple with length one, *array* is expected to be a vector.
# Otherwise a matrix is expected.
#
# context
# *******
# This is the context that *array* appears in
# (often to syntax for some other operation).
# It is a ``str`` that is used for error reporting.
#
# name
# ****
# This is the name used for *array* in *context* .
# It is a ``str`` that is used for error reporting.
#
# vec
# ***
# This is the values of *array*
# as a vector is row major order.
# It has type ``vec_double`` if *dtype* is ``float`` ,
# and ``vec_a_double`` if *dtype* is ``a_double`` .
#
# {xrst_end numpy2vec}
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
   if array.shape[0] != nr :
      msg = context + ': ' + name + '.shape[0] is not ' + str(nr)
      raise RuntimeError(msg)
   #
   if vector :
      if  len(array.shape) != 1 :
         msg = context + ': ' + name + ' is not a vector'
         raise RuntimeError(msg)
   else :
      if len(array.shape) != 2 :
         msg = context + ': ' + name + ' is not a matrix'
         raise RuntimeError(msg)
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
         raise RuntimeError(msg)
      #
      for i in range(nr) :
         for j in range(nc):
            # must copy data so vec can manage its own memory
            vec[i * nc + j] = dtype( array[i, j] )
   #
   return vec
# -----------------------------------------------------------------------------
# {xrst_begin vec2numpy}
# {xrst_comment_ch #}
#
# {xrst_spell
#  cppad
# }
#
# Convert a cppad_py Vector to a Numpy Array
# ##########################################
#
# Syntax
# ******
#
# | *array* =  ``cppad_py.utility.vec2numpy`` ( *vec* , *nr* )
# | *array* =  ``cppad_py.utility.vec2numpy`` ( *vec* , *nr* , *nc* )
#
# vec
# ***
# This must have one of the following types:
# ``cppad_py.vec_int`` ,
# ``cppad_py.vec_double`` ,
# ``vec_py.vec_a_double`` .
# with size equal to *nr* ``*`` *nc* .
#
# nr
# **
# This is an ``int`` equal to the number of rows in the array.
# If the argument *nc* is not present, the array is a vector; i.e.,
# ``len`` ( *array*\ ``.shape ) == 1`` .
#
# nc
# **
# If this argument is present,
# it is an ``int`` equal to the number of columns in the array.
# In this case the array is a matrix; i.e.,
# ``len`` ( *array*\ ``.shape ) == 2`` .
#
# array
# *****
# This is the array corresponding to *vec* in row major order.
# Note that this array can be used after the vector *vec* drops
# out of scope (is deleted).
#
# {xrst_end vec2numpy}
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
