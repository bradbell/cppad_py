# -----------------------------------------------------------------------------
#         cppad_py: A C++ Object Library and Python Interface to Cppad
#          Copyright (C) 2017-20 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# -----------------------------------------------------------------------------
# $begin py_sparse_rc$$ $newlinech #$$
# $spell
#	rc
#	nr
#	nc
#	nnz
#	resize
#	const
#	Cppad
#	Py
#	vec
#	cppad_py
#	numpy
# $$
#
# $section Sparsity Patterns$$
#
# $head Syntax$$
# $icode%pattern%   = cppad_py.sparse_rc()
# %$$
# $icode%pattern%.resize(%nr%, %nc%, %nnz%)
# %$$
# $icode%nr%        = %pattern%.nr()
# %$$
# $icode%nc%        = %pattern%.nc()
# %$$
# $icode%nnz%       = %pattern%.nnz()
# %$$
# $icode%pattern%.put(%k%, %r%, %c%)
# %$$
# $icode%row%       = %pattern%.row()
# %$$
# $icode%col%       = %pattern%.col()
# %$$
# $icode%row_major% = %pattern%.row_major()
# %$$
# $icode%col_major% = %pattern%.col_major()
# %$$
#
# $head pattern$$
# This result is used to hold a sparsity pattern for a matrix.
# It is constant
# except during the $code resize$$ and $code put$$ operations.
#
# $head nr$$
# This argument is a non-negative $code int$$
# and is the number of rows in the sparsity pattern.
# The function $code nr()$$ returns the value of
# $icode nr$$ in the previous $code resize$$ operation.
#
# $head nc$$
# This argument is a non-negative $code int$$
# and is the number of columns in the sparsity pattern.
# The function $code nc()$$ returns the value of
# $icode nc$$ in the previous $code resize$$ operation.
#
# $head nnz$$
# This argument is a non-negative $code int$$
# and is the number of possibly non-zero
# index pairs in the sparsity pattern.
# The function $code nnz()$$ returns the value of
# $icode nnz$$ in the previous $code resize$$ operation.
#
# $head resize$$
# The current sparsity pattern is lost and a new one is started
# with the specified parameters.
# After each $code resize$$, the elements in the $icode row$$
# and $icode col$$ vectors should be assigned using $code put$$.
#
# $head put$$
# This function sets the values
# $codei%
#	%row%[%k%] = %r%
#	%col%[%k%] = %c%
# %$$
# (The name $code set$$ is used by Cppad, but not used here,
# because $code set$$ it is a built-in name in Python.)
#
# $subhead k$$
# This argument is a non-negative $code int$$
# and must be less than $icode nnz$$.
#
# $subhead r$$
# This argument is a non-negative $code int$$
# and must be less than $icode nr$$.
# It specifies the value assigned to $icode%row%[%k%]%$$.
#
# $subhead c$$
# This argument is a non-negative $code int$$
# and must be less than $icode nc$$.
# It specifies the value assigned to $icode%col%[%k%]%$$.
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
#	example/python/core/sparse_rc_xam.py
# %$$
# $head Example$$
# $cref sparse_rc_xam.py$$
#
# $end
# -----------------------------------------------------------------------------
import cppad_py
import numpy
class sparse_rc :
	"""Python interface to CppAD::sparse_rc"""
	#
	def __init__(self) :
		self.rc = cppad_py.swig.sparse_rc()
	#
	# resize
	def resize(self, nr, nc, nnz) :
		self.rc.resize(nr, nc, nnz)
	#
	# nr
	def nr(self) :
		return self.rc.nr()
	#
	# nc
	def nc(self) :
		return self.rc.nc()
	#
	# nnz
	def nnz(self) :
		return self.rc.nnz()
	#
	# put
	def put(self, k, r, c) :
		self.rc.put(k, r, c)
	#
	# row
	def row(self) :
		vec   = self.rc.row()
		assert vec.size() == self.rc.nnz()
		array = cppad_py.utility.vec2numpy(vec, vec.size() )
		return array
	#
	# col
	def col(self) :
		vec   = self.rc.col()
		assert vec.size() == self.rc.nnz()
		array = cppad_py.utility.vec2numpy(vec, vec.size() )
		return array
	#
	# row_major
	def row_major(self) :
		vec   = self.rc.row_major()
		assert vec.size() == self.rc.nnz()
		array = cppad_py.utility.vec2numpy(vec, vec.size() )
		return array
	#
	# col_major
	def col_major(self) :
		vec   = self.rc.col_major()
		assert vec.size() == self.rc.nnz()
		array = cppad_py.utility.vec2numpy(vec, vec.size() )
		return array
