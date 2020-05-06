# -----------------------------------------------------------------------------
#         cppad_py: A C++ Object Library and Python Interface to Cppad
#          Copyright (C) 2017-20 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# -----------------------------------------------------------------------------
# $begin py_sparse_rcv$$ $newlinech #$$
# $spell
#	rc
#	rcv
#	nr
#	nc
#	nnz
#	resize
#	const
#	Cppad
#	vec
#	cppad_py
#	numpy
# $$
#
# $section Sparse Matrices$$
#
# $head Syntax$$
# $icode%matrix%    = cppad_py::sparse_rcv(%pattern%)
# %$$
# $icode%nr%        = %matrix%.nr()
# %$$
# $icode%nc%        = %matrix%.nc()
# %$$
# $icode%nnz%       = matrix%.nnz()
# %$$
# $icode%matrix%.put(%k%, %v%)
# %$$
# $icode%row%       = %matrix%.row()
# %$$
# $icode%col%       = %matrix%.col()
# %$$
# $icode%val%       = %matrix%.val()
# %$$
# $icode%row_major% = %matrix%.row_major()
# %$$
# $icode%col_major% = %matrix%.col_major()
# %$$
#
# $head pattern$$
# This argument has prototype
# $codei%
#	const sparse_rc& %pattern%
# %$$
# It specifies the number of rows, number of columns and
# the possibly non-zero entries in the $icode matrix$$.
#
# $head matrix$$
# This is a sparse matrix object with the sparsity specified by $icode pattern$$.
# Only the $icode val$$ vector can be changed. All other values returned by
# $icode matrix$$ are fixed during the constructor and constant there after.
# The $icode val$$ vector is only changed by the constructor
# and the $code set$$ function.
#
# $head nr$$
# This return value is an $code int$$
# and is the number of rows in the matrix.
#
# $head nc$$
# This return value is an $code int$$
# and is the number of columns in the matrix.
#
# $head nnz$$
# This return value is an $code int$$
# and is the number of possibly non-zero values in the matrix.
#
# $head put$$
# This function sets the value
# $codei%
#	%val%[%k%] = %v%
# %$$
# (The name $code set$$ is used by Cppad, but not used here,
# because $code set$$ it is a built-in name in Python.)
#
# $subhead k$$
# This is a non-negative $code int$$ and must be less than $icode nnz$$.
#
# $subhead v$$
# This argument has type $code float$$ and
# specifies the value assigned to $icode%val%[%k%]%$$.
#
# $head row$$
# This result is a numpy vector with $code int$$ elements
# and its size is $icode nnz$$.
# For $icode%k% = 0, %...%, %nnz%-1%$$,
# $icode%row%[%k%]%$$ is the row index for the $th k$$ possibly non-zero
# entry in the matrix.
#
# $head col$$
# This result is a numpy vector with $code int$$ elements
# and its size is $icode nnz$$.
# For $icode%k% = 0, %...%, %nnz%-1%$$,
# $icode%col%[%k%]%$$ is the column index for the $th k$$ possibly non-zero
# entry in the matrix.
#
# $head val$$
# This result is a numpy vector with $code float$$ elements
# and its size is $icode nnz$$.
# For $icode%k% = 0, %...%, %nnz%-1%$$,
# $icode%val%[%k%]%$$ is the value of the $th k$$ possibly non-zero
# entry in the matrix (the value may be zero).
#
# $head row_major$$
# This result is a numpy vector with $code int$$ elements
# and its size $icode nnz$$.
# It sorts the sparsity pattern in row-major order.
# To be specific,
# $codei%
#	%col%[ %row_major%[%k%] ] <= %col%[ %row_major%[%k%+1] ]
# %$$
# and if $icode%col%[ %row_major%[%k%] ] == %col%[ %row_major%[%k%+1] ]%$$,
# $codei%
#	%row%[ %row_major%[%k%] ] < %row%[ %row_major%[%k%+1] ]
# %$$
# This routine generates an assert if there are two entries with the same
# row and column values (if $code NDEBUG$$ is not defined).
#
# $head col_major$$
# This result is a numpy vector with $code int$$ elements
# and its size $icode nnz$$.
# It sorts the sparsity pattern in column-major order.
# To be specific,
# $codei%
#	%row%[ %col_major%[%k%] ] <= %row%[ %col_major%[%k%+1] ]
# %$$
# and if $icode%row%[ %col_major%[%k%] ] == %row%[ %col_major%[%k%+1] ]%$$,
# $codei%
#	%col%[ %col_major%[%k%] ] < %col%[ %col_major%[%k%+1] ]
# %$$
# This routine generates an assert if there are two entries with the same
# row and column values (if $code NDEBUG$$ is not defined).
#
# $children%
#	example/python/core/sparse_rcv_xam.py
# %$$
# $head Example$$
# $cref sparse_rcv_xam.py$$
#
# $end
# -----------------------------------------------------------------------------
import cppad_py
import numpy
class sparse_rcv :
	"""Python interface to CppAD::sparse_rc"""
	#
	def __init__(self, pattern) :
		# use undocumented fact that pattern.rc is vec_int version of sparsity
		self.rcv = cppad_py.swig.sparse_rcv(pattern.rc)
	#
	# nr
	def nr(self) :
		return self.rcv.nr()
	#
	# nc
	def nc(self) :
		return self.rcv.nc()
	#
	# nnz
	def nnz(self) :
		return self.rcv.nnz()
	#
	# put
	def put(self, k, v) :
		self.rcv.put(k, v)
	#
	# row
	def row(self) :
		vec   = self.rcv.row()
		assert vec.size() == self.rcv.nnz()
		array = cppad_py.utility.vec2numpy(vec, vec.size() )
		return array
	#
	# col
	def col(self) :
		vec   = self.rcv.col()
		assert vec.size() == self.rcv.nnz()
		array = cppad_py.utility.vec2numpy(vec, vec.size() )
		return array
	#
	# val
	def val(self) :
		vec   = self.rcv.val()
		assert vec.size() == self.rcv.nnz()
		array = cppad_py.utility.vec2numpy(vec, vec.size() )
		return array
	#
	# row_major
	def row_major(self) :
		vec   = self.rcv.row_major()
		assert vec.size() == self.rcv.nnz()
		array = cppad_py.utility.vec2numpy(vec, vec.size() )
		return array
	#
	# col_major
	def col_major(self) :
		vec   = self.rcv.col_major()
		assert vec.size() == self.rcv.nnz()
		array = cppad_py.utility.vec2numpy(vec, vec.size() )
		return array
