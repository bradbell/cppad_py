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
define(ext_, m)
define(true_, true)
define(false_, false)
define(and_, &&)
define(end_, end)
define(c_, `%')

# -----------------------------------------------------------------------------
# module, var, and member

# module_ or module_(name)
define(module_, `ifelse($#, 0, m_cppad, m_cppad.$1)')

# var_(variable)
define(var_, $1)

# member_(variable, name)
define(member_, $1.$2)

# -----------------------------------------------------------------------------
# Assignment

# new_var_(type, variable, value)
define(new_var_, $2 = $3;)

# new_var_new_(type, variable, value)
define(new_var_new_, $2 = $3;)

# assign_(variable, value)
define(assign_, $1 = $2;)

# and_assign_(variable, value)
define(and_assign_, $1 = $1 and_ $2;)

# -----------------------------------------------------------------------------
# Vector Operations

# vec_set_(vector, index, value)
define(vec_set_, $1($2) = $3;)


# vec_get_(vector, index)
define(vec_get_, $1($2))

# -----------------------------------------------------------------------------
# Function Statements

# begin_bool_fun_0_(name, return_variable)
define(begin_bool_fun_0_,
function $1 = $2()
	c_
	c_ load the Cppad Swig library
	module_
	c_
	c_ initialize return variable
	$1 = true_;)

# return_(return_variable)
define(return_, return;)

# -----------------------------------------------------------------------------
# Other

# header_(example)
define(header_,
c_ This file can be automatically generated using the following command
c_ m4 ../octave.m4 ../../xam/$1.xam > $1.ext_)

# begin_for_(variable, upper)
define(begin_for_, for $1 = [ 0 :($2-1) ])

# print_text_(text)
define(print_text_, printf('$1\n'))
