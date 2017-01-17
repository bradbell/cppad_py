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
define(Ext_, m)
define(True_, true)
define(False_, false)
define(And_, &&)
define(Not_, ~)
define(End_, end)
define(C_, `%')
define(Eos_, `;')
define(Try_, try)
define(Catch_, catch)
define(Eof_, C_)
# -----------------------------------------------------------------------------
# module, var, and member

# Module_ or Module_(name)
define(Module_, `ifelse($#, 0, m_cppad, m_cppad.$1)')

# ModuleCtor_(name)
define(ModuleCtor_, m_cppad.$1)

# -----------------------------------------------------------------------------
# non-statements with arguments

# Var_(variable)
define(Var_, $1)

# Member_(variable, name)
define(Member_, $1.$2)

# StringEqual_(left, right)
define(StringEqual_, `strcmp($1, $2)')

# -----------------------------------------------------------------------------
# Assignment

# NewVar_(type, variable, value)
define(NewVar_, $2 = $3;)

# Assign_(variable, value)
define(Assign_, $1 = $2;)

# AndAssign_(variable, value)
define(AndAssign_, $1 = $1 And_ $2;)

# -----------------------------------------------------------------------------
# Vector Operations

# VecSet_(vector, index, value)
define(VecSet_, $1($2) = $3;)


# VecGet_(vector, index)
define(VecGet_, $1($2))

# -----------------------------------------------------------------------------
# Function Statements

# BeginBoolFun_(name, return_variable)
define(BeginBoolFun_,
function $1 = $2()
	C_
	C_ load the Cppad Swig library
	Module_
	C_
	C_ initialize return variable
	$1 = True_;
	C_ -----------------------------------------------------------------------)

# Return_(return_variable)
define(Return_, return;)

# -----------------------------------------------------------------------------
# Other

# For_(variable, upper)
define(For_, for $1 = [ 0 :($2-1) ])
