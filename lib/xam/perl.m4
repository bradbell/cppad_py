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
define(ext_, pm)
define(true_, 1)
define(false_, 0)
define(and_, &&)
define(not_, !)
define(end_, })
define(c_, `#')
define(eos_, `;')
define(try_, `eval { c_ try')
define(catch_, `}; if( `$'@ ) { c_ catch')
define(eof_, 1;)
# -----------------------------------------------------------------------------
# module

# module_ or module_(name)
define(module_, `ifelse($#, 0, pm_cppad, pm_cppad::$1)')

# module_ctor_(name)
define(module_ctor_, new pm_cppad::$1)

# -----------------------------------------------------------------------------
# non-statements with arguments

# var_(variable)
define(var_, `$'$1)

# member_(variable, name)
define(member_, `$'$1->$2)

# string_equal_(left, right)
define(string_equal_, $1 eq $2)

# -----------------------------------------------------------------------------
# Assignment

# new_var_(type, variable, value)
define(new_var_, my `$'$2 = $3;)

# assign_(variable, value)
define(assign_, `$'$1 = $2;)

# and_assign_(variable, value)
define(and_assign_, `$'$1 = `$'$1 and_ $2;)

# -----------------------------------------------------------------------------
# Vector Operations

# vec_set_(vector, index, value)
define(vec_set_, `$'$1->set($2, $3);)

# vec_get_(vector, index)
define(vec_get_, `$'$1->get($2))

# -----------------------------------------------------------------------------
# Function Statements

# begin_bool_fun_0_(return_variable, fun_name)
define(begin_bool_fun_0_,
package $2;
sub $2() {
	c_ check for standard perl programming conventions
	use strict;
	use warnings;
	c_
	c_ load the Cppad Swig library
	use module_;
	c_
	c_ initilaize return variable
	my `$'$1 = true_;
	`c_' ---------------------------------------------------------------------)

# return_(return_variable)
define(return_, return( `$'$1 );)

# -----------------------------------------------------------------------------
# Other

# begin_for_(variable, upper)
define(begin_for_, for(my `$'$1 = 0; `$'$1 < $2; `$'$1++) {)

# print_text_(text)
define(print_text_, print "$1\n";)
