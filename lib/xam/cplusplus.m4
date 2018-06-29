# -----------------------------------------------------------------------------
#         cppad_py: A C++ Object Library and Python Interface to Cppad
#          Copyright (C) 2017-18 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# -----------------------------------------------------------------------------
# NOTE: order of these macros is same as order of documentation in macro.omh
# -----------------------------------------------------------------------------
# No Arguments
define(Ext_, cpp)
define(True_, true)
define(False_, false)
define(And_, &&)
define(Not_, !)
define(End_, `}')
define(C_, `//')
define(Eos_, `;')
define(Try_, `try {')
define(Catch_, `} catch (...) {')
define(Eof_, C_)
# -----------------------------------------------------------------------------
# module, var, and member

# Module_ or Module_(name)
define(Module_, `ifelse($#, 0, cppad_py, cppad_py::$1)')

# ModuleCtor_(name)
define(ModuleCtor_, cppad_py::$1)

# -----------------------------------------------------------------------------
# non-statements with arguments

# Var_(variable)
define(Var_, $1)

# Member_(variable, name)
define(Member_, $1.$2)

# StringEqual_(left, right)
define(StringEqual_, $1 == $2)

# -----------------------------------------------------------------------------
# Assignment

# NewVar_(type, variable, value)
define(NewVar_, $1 $2 = $3;)

# Assign_(variable, value)
define(Assign_, $1 = $2;)

# AndAssign_(variable, value)
define(AndAssign_, $1 = $1 And_ $2;)

# -----------------------------------------------------------------------------
# Vector Operations

# VecSet_(vector, index, value)
define(VecSet_, $1[$2] = $3;)

# VecGet_(vector, index)
define(VecGet_, $1[$2])

# -----------------------------------------------------------------------------
# Function Statements

# BeginBoolFun_(return_variable, fun_name)
define(BeginBoolFun_,
`#' include <cstdio>
`#' include <string>
`#' include <cppad/swig/cppad_py.hpp>

bool $2(void) {
	using cppad_py::a_double;
	using cppad_py::vec_bool;
	using cppad_py::vec_int;
	using cppad_py::vec_double;
	using cppad_py::vec_a_double;
	using cppad_py::a_fun;
	using cppad_py::sparse_rc;
	using cppad_py::sparse_rcv;
	using cppad_py::sparse_jac_work;
	using cppad_py::sparse_hes_work;
	using std::string;
	C_
	C_ initialize return variable
	bool $1 = True_;
	C_------------------------------------------------------------------------)

# Return_(return_variable)
define(Return_, return( $1 );)

# -----------------------------------------------------------------------------
# Control Flow

# For_(variable, upper)
define(For_, for(int $1 = 0; $1 < $2; $1++) {)

# If_(expression)
define(If_, if( $1 ) {)
