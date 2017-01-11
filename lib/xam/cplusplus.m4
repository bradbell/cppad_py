# -----------------------------------------------------------------------------
#         cppad_swig: A C++ Object Library and Swig Interface to Cppad
#          Copyright (C) 2017-17 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#          GNU Affero General Public License version 3.0 or later see
#                     http://www.gnu.org/licenses/agpl.txt
# -----------------------------------------------------------------------------
# NOTE: order of these macros is same as order of documentation in macro.omh
# -----------------------------------------------------------------------------
# No Arguments
define(ext_, cpp)
define(true_, true)
define(false_, false)
define(and_, &&)
define(not_, !)
define(end_, `}')
define(c_, `//')
define(eos_, `;')
define(try_, `try {')
define(catch_, `} catch (...) {')

# -----------------------------------------------------------------------------
# module, var, and member

# module_ or module_(name)
define(module_, `ifelse($#, 0, cppad_swig, cppad_swig::$1)')

# var_(variable)
define(var_, $1)

# member_(variable, name)
define(member_, $1.$2)

# string_equal_(left, right)
define(string_equal_, $1 == $2)

# -----------------------------------------------------------------------------
# Assignment

# new_var_(type, variable, value)
define(new_var_, $1 $2 = $3;)

# new_var_new_(type, variable, value)
define(new_var_new_, $1 $2 = $3;)

# assign_(variable, value)
define(assign_, $1 = $2;)

# and_assign_(variable, value)
define(and_assign_, $1 = $1 and_ $2;)

# -----------------------------------------------------------------------------
# Vector Operations

# vec_set_(vector, index, value)
define(vec_set_, $1[$2] = $3;)

# vec_get_(vector, index)
define(vec_get_, $1[$2])

# -----------------------------------------------------------------------------
# Function Statements

# begin_bool_fun_0_(return_variable, fun_name)
define(begin_bool_fun_0_,
`#' include <cstdio>
`#' include <string>
`#' include <cppad/swig/cppad_swig.hpp>

bool $2(void) {
	using cppad_swig::a_double;
	using cppad_swig::vector_double;
	using cppad_swig::vector_ad;
	using cppad_swig::a_fun;
	using std::string;
	c_
	c_ initialize return variable
	bool $1 = true_;
	c_------------------------------------------------------------------------)

# return_(return_variable)
define(return_, return( $1 );)

# -----------------------------------------------------------------------------
# Other

# begin_for_(variable, upper)
define(begin_for_, for(size_t $1 = 0; $1 < $2; $1++) {)

# print_text_(text)
define(print_text_, std::printf("$1\n"))
