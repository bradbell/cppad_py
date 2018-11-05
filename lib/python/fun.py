# -----------------------------------------------------------------------------
#         cppad_py: A C++ Object Library and Python Interface to Cppad
#          Copyright (C) 2017-18 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# -----------------------------------------------------------------------------
# $begin py_d_fun$$ $newlinech #$$
# $spell
#	Cppad
#	Py
# $$
#
# $section Cppad Py AD Functions$$
#
# $comment Files that have Python specific Implementation and Documention$$
# $childtable%lib/python/independent.py
#	%lib/python/abort_recording.omh
#	%lib/python/fun_ctor.py
#	%lib/python/fun_property.omh
#	%lib/python/fun_jacobian.py
#	%lib/python/fun_hessian.py
#	%lib/python/fun_forward.py
#	%lib/python/fun_reverse.py
#	%lib/python/fun_optimize.omh
# %$$
#
# $end
# ----------------------------------------------------------------------------
import cppad_py
class d_fun :
	"""Python interface to CppAD::ADFun<double>"""
	#
	# __init__: see fun_ctor.py
	def __init__(self, ax, ay) :
		self.f = cppad_py.d_fun_ctor(ax, ay)
	#
	# size_domain
	def size_domain(self) :
		return self.f.size_domain()
	#
	# size_range
	def size_range(self) :
		return self.f.size_range()
	#
	# size_var
	def size_var(self) :
		return self.f.size_var()
	#
	# size_op
	def size_op(self) :
		return self.f.size_op()
	#
	# size_order
	def size_order(self) :
		return self.f.size_order()
	#
	# jacobian: see fun_jacobian.py
	def jacobian(self, x) :
		return cppad_py.d_fun_jacobian(self.f, x)
	#
	# hessian: see fun_hessian.py
	def hessian(self, x, w) :
		return cppad_py.d_fun_hessian(self.f, x, w)
	#
	# forward
	def forward(self, p, xp) :
		return cppad_py.d_fun_forward(self.f, p, xp)
	#
	# reverse
	def reverse(self, q, yq) :
		return cppad_py.d_fun_reverse(self.f, q, yq)
	#
	# optimize
	def optimize(self) :
		return self.f.optimize()
	#
	# undocumented fact: pattern.rc is vec_int version of sparsity pattern
	#
	# for_jac_sparsity
	def for_jac_sparsity(self, pattern_in, pattern_out) :
		self.f.for_jac_sparsity(pattern_in.rc, pattern_out.rc)
	#
	# rev_jac_sparsity
	def rev_jac_sparsity(self, pattern_in, pattern_out) :
		self.f.rev_jac_sparsity(pattern_in.rc, pattern_out.rc)
	#
	# for_hes_sparsity
	def for_hes_sparsity(self, select_domain, select_range, pattern_out) :
		cppad_py.d_fun_for_hes_sparsity( \
			self.f, select_domain, select_range, pattern_out)
	#
	# rev_hes_sparsity
	def rev_hes_sparsity(self, select_domain, select_range, pattern_out) :
		cppad_py.d_fun_rev_hes_sparsity( \
			self.f, select_domain, select_range, pattern_out)
	#
	# sparse_jac_for
	def sparse_jac_for(self, subset, x, pattern, work) :
		cppad_py.d_fun_sparse_jac_for(self.f, subset, x, pattern, work)
	#
	# sparse_jac_rev
	def sparse_jac_rev(self, subset, x, pattern, work) :
		cppad_py.d_fun_sparse_jac_rev(self.f, subset, x, pattern, work)
	#
	# sparse_hes
	def sparse_hes(self, subset, x, r, pattern, work) :
		cppad_py.d_fun_sparse_hes(self.f, subset, x, r, pattern, work)
