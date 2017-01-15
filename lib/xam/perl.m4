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
define(Ext_, pm)
define(True_, 1)
define(False_, 0)
define(And_, &&)
define(Not_, !)
define(End_, })
define(C_, `#')
define(Eos_, `;')
define(Try_, `eval { C_ try')
define(Catch_, `}; if( `$'@ ) { C_ catch')
define(Eof_, 1;)
# -----------------------------------------------------------------------------
# module

# Module_ or Module_(name)
define(Module_, `ifelse($#, 0, pm_cppad, pm_cppad::$1)')

# ModuleCtor_(name)
define(ModuleCtor_, new pm_cppad::$1)

# -----------------------------------------------------------------------------
# non-statements with arguments

# Var_(variable)
define(Var_, `$'$1)

# Member_(variable, name)
define(Member_, `$'$1->$2)

# StringEqual_(left, right)
define(StringEqual_, $1 eq $2)

# -----------------------------------------------------------------------------
# Assignment

# NewVar_(type, variable, value)
define(NewVar_, my `$'$2 = $3;)

# Assign_(variable, value)
define(Assign_, `$'$1 = $2;)

# AndAssign_(variable, value)
define(AndAssign_, `$'$1 = `$'$1 And_ $2;)

# -----------------------------------------------------------------------------
# Vector Operations
# 2DO: ask swig mailing list why cannot use [] or () operators for this.

# VecSet_(vector, index, value)
define(VecSet_, `$'$1->set($2, $3);)

# VecGet_(vector, index)
define(VecGet_, `$'$1->get($2))

# -----------------------------------------------------------------------------
# Function Statements

# BeginBoolFun__(return_variable, fun_name)
define(BeginBoolFun__,
package $2;
sub $2() {
	C_ check for standard perl programming conventions
	use strict;
	use warnings;
	C_
	C_ load the Cppad Swig library
	use Module_;
	C_
	C_ initilaize return variable
	my `$'$1 = True_;
	`C_' ---------------------------------------------------------------------)

# Return_(return_variable)
define(Return_, return( `$'$1 );)

# -----------------------------------------------------------------------------
# Other

# BeginFor_(variable, upper)
define(BeginFor_, for(my `$'$1 = 0; `$'$1 < $2; `$'$1++) {)

# print_tExt_(text)
define(print_tExt_, print "$1\n";)
