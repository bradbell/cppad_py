header_(vector_double_xam)
c_ -----------------------------------------------------------------------------
c_         cppad_swig: A C++ Object Library and SWIG Interface to CppAD
c_          Copyright (C) 2017-17 Bradley M. Bell (bradbell@seanet.com)
c_              This program is distributed under the terms of the
c_          GNU Affero General Public License version 3.0 or later see
c_                     http://www.gnu.org/licenses/agpl.txt
c_ -----------------------------------------------------------------------------
c_ std::vector<double>
c_ -----------------------------------------------------------------------------
begin_bool_fun_0_(ok, vector_double_xam)
	new_var_(n, 4)
	new_var_new_(vec, module_fun_1_(vector_double, n))
	c_
	c_ check size
	and_assign_(ok, member_fun_0_(vec, size) == n)
	c_
	c_ setting elements
	begin_for_(i, var_(n) )
		vec_set_(vec, var_(i), 2.0 * var_(i))
	end_
	c_ getting elements
	begin_for_(i, var_(n) )
		new_var_(element, vec_get_(vec, var_(i)))
		and_assign_(ok, var_(element) == 2.0 * var_(i))
	end_
	return_(var_(ok))
end_
