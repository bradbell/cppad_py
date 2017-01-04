header_(a_double_xam)
c_ -----------------------------------------------------------------------------
c_         cppad_swig: A C++ Object Library and Swig Interface to CppAD
c_          Copyright (C) 2017-17 Bradley M. Bell (bradbell@seanet.com)
c_              This program is distributed under the terms of the
c_          GNU Affero General Public License version 3.0 or later see
c_                     http://www.gnu.org/licenses/agpl.txt
c_ -----------------------------------------------------------------------------
c_ a_double
c_ -----------------------------------------------------------------------------
begin_bool_fun_0_(ok, a_double_xam)
	new_var_new_(two,   module_fun_1_(a_double, 2.0))
	new_var_new_(three,  module_fun_1_(a_double, 3.0))
	c_
	new_var_(five,       var_(two) + var_(three))
	new_var_(six,        var_(two) * var_(three))
	new_var_(neg_one,    var_(two) - var_(three))
	new_var_(two_thirds, var_(two) / var_(three))
	c_
	and_assign_(ok, member_fun_0_(five,     value) == 5.0)
	and_assign_(ok, member_fun_0_(six,      value) == 6.0)
	and_assign_(ok, member_fun_0_(neg_one,  value) == -1.0)
	and_assign_(ok, member_fun_0_(neg_one,  value) == -1.0)
	and_assign_(ok, 0.5 < member_fun_0_(two_thirds,  value))
	and_assign_(ok, member_fun_0_(two_thirds,  value) < 1.0)
	and_assign_(ok, five < six)
	c_
	return_(var_(ok))
end_
