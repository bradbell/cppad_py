/* -----------------------------------------------------------------------------
           cppad_swig: A C++ Object Library and Swig Interface to Cppad
            Copyright (C) 2017-17 Bradley M. Bell (bradbell@seanet.com)
                This program is distributed under the terms of the
            GNU Affero General Public License version 3.0 or later see
                       http://www.gnu.org/licenses/agpl.txt
----------------------------------------------------------------------------- */
# include <cppad/cppad.hpp>
# include <cppad/swig/cppad_swig.hpp>

// ---------------------------------------------------------------------------
// Macros
// ---------------------------------------------------------------------------

// binary operators with ad results
# define BINARY_OP_AD_RESULT(op) \
a_double a_double::operator op(const a_double& ad) const \
{	a_double result; \
	*result.ptr() = *ptr() op *ad.ptr(); \
	return result; \
}
// comparison operators
# define COMPARISON_OP(op) \
bool a_double::operator op(const a_double& ad) const \
{	bool result =  *ptr() op *ad.ptr(); \
	return result; \
}
// compound assignment operators
# define COMPOUND_ASSIGNMENT_OP(op) \
a_double a_double::operator op(const a_double& ad)\
{	*ptr() op *ad.ptr(); \
	return *this; \
}
// unary functions with ad results
# define UNARY_FUN_AD_RESULT(fun) \
a_double a_double::fun(void) const \
{	a_double result; \
	*result.ptr() = CppAD::fun( *ptr() ); \
	return result; \
}
// ---------------------------------------------------------------------------

namespace cppad_swig { // BEGIN_CPPAD_SWIG_NAMESPACE

// ---------------------------------------------------------------------------
// public member functions not in Swig interface
// ---------------------------------------------------------------------------
// pointer to this as an AD<double> object
CppAD::AD<double>* a_double::ptr(void)
{	return reinterpret_cast< CppAD::AD<double>* >( & data_ );
}
// const version of pointer to this as an AD<double> object
const CppAD::AD<double>* a_double::ptr(void) const
{	return reinterpret_cast< const CppAD::AD<double>* >( & data_ );
}
// ctor from CppAD::AD<double>
a_double::a_double(const CppAD::AD<double>* ad_ptr)
{	CPPAD_ASSERT_UNKNOWN( sizeof(data_) == sizeof( CppAD::AD<double> ) );
	new ( & data_ ) CppAD::AD<double>(*ad_ptr);
}
/*
-------------------------------------------------------------------------------
$begin a_double_ctor$$
$spell
	cppad
	const
	perl
	py
$$

$section The a_double Constructor$$

$head Syntax$$
$icode%ad% = %module_ref% a_double()
%$$
$icode%ad% = %module_ref% a_double(%d%)
%$$
$icode%ad% = %module_ref% a_double(%ad_other%)
%$$

$head Purpose$$
Creates a $code cppad_swig::a_double$$ object that can be use
to track floating point operations and preform algorithmic differentiation.

$head module_ref$$
This is a $cref/module reference/module/Module Reference/$$
for the particular language.

$head d$$
This argument has prototype
$codei%
	const double& %d%
%$$
The resulting $icode ad$$ variable represents
a constant function equal to $icode d$$.

$head ad_other$$
This argument has prototype
$codei%
	const a_double& %ad_other%
%$$
The resulting $icode ad$$ variable is the same function
of the independent variables as $icode ad_other$$.

$head ad$$
is the $code a_double$$ object that is constructed.

$head Example$$
All of the other $code a_double$$ examples use an $code a_double$$
constructor.

$end
-------------------------------------------------------------------------------
*/
// default a_double ctor
a_double::a_double(void)
{	// placement version of new operator uses this->data_ for memory
	CPPAD_ASSERT_UNKNOWN( sizeof(data_) == sizeof( CppAD::AD<double> ) );
	new ( & data_ ) CppAD::AD<double>();
}
// a_double ctor from double
a_double::a_double(const double& d)
{	CPPAD_ASSERT_UNKNOWN( sizeof(data_) == sizeof( CppAD::AD<double> ) );
	new ( & data_ ) CppAD::AD<double>(d);
}
// ctor from a_double
a_double::a_double(const a_double& ad)
{	CPPAD_ASSERT_UNKNOWN( sizeof(data_) == sizeof( CppAD::AD<double> ) );
	new ( & data_ ) CppAD::AD<double>(*ad.ptr());
}
// a_double destructor
a_double::~a_double(void)
{ }
/*
$begin a_double_unary_op$$

$section a_double Unary Plus and Minus$$
$spell
	const
	perl
$$

$head Syntax$$
$icode%ay% = +%ax%
%$$
$icode%ay% = -%ax%
%$$

$head ax$$
This object has prototype
$codei%
	const a_double& %ax%
%$$

$head ay$$
If the operator is $code +$$, the result is equal to $icode ax$$.
If it is $code -$$, the result is the negative of $icode ax$$.

$head Octave$$
Note that Octave does not support these unary operators
(the reason why is unclear at this time).

$children%
	build/lib/example/cplusplus/a_double_unary_op_xam.cpp%
	build/lib/example/octave/a_double_unary_op_xam.m%
	build/lib/example/perl/a_double_unary_op_xam.pm%
	build/lib/example/python/a_double_unary_op_xam.py
%$$
$head Example$$
$cref/C++/a_double_unary_op_xam.cpp/$$,
$cref/Octave/a_double_unary_op_xam.m/$$,
$cref/Perl/a_double_unary_op_xam.pm/$$,
$cref/Python/a_double_unary_op_xam.py/$$.

$end
*/
const a_double& a_double::operator+(void) const
{	return *this; }
a_double a_double::operator-(void) const
{	a_double result;
	*result.ptr() = - *ptr();
	return result;
}
/*
-------------------------------------------------------------------------------
$begin a_double_property$$
$spell
	const
	perl
	bool
	ae
$$

$section Properties of an a_double Object$$

$head Syntax$$
$icode%d% = %ad%.value()
%$$
$icode%p% = %ad%.parameter()
%$$
$icode%v% = %ad%.variable()
%$$
$icode%n% = %ad%.near_equal(%ae%)
%$$


$head ad$$
This object has prototype
$codei%
	const a_double& %ad%
%$$

$head value$$
The result $icode d$$ has prototype
$codei%
	double %d%
%$$
It is the value of $icode ad$$, as a constant function.
In addition it must represent a constant functions; i.e.,
$icode ad$$ not depend on the
$cref independent$$ variables when $icode%ad%.value()%$$ is called.
If it does depend on the independent variables,
you will have to wait until the current recording is terminated
before you can access its value.

$head parameter$$
The result $icode p$$ has prototype
$codei%
	bool %p%
%$$
It is true if $icode ad$$ represent a constant functions; i.e.,
$icode ad$$ not depend on the $cref independent$$ variables.

$head variable$$
The result $icode v$$ has prototype
$codei%
	bool %v%
%$$
It is true if $icode ad$$ is not a constant function; i.e.,
$icode ad$$ depends on the $cref independent$$ variables.

$head near_equal$$
The argument $icode ae$$,
and the result $icode n$$, have prototype
$codei%
	const a_double& %ae%
	bool %n%
%$$
The result is true if $icode ae$$ is nearly equal to $icode ae$$.
To be specific, the result is
$latex \[
	| d - e | \leq 100 \; \varepsilon \; ( |d| + |e| )
\] $$
where $icode d$$ and $icode e$$ are the value corresponding to
$icode ad$$ and $icode ae$$ and
$latex \varepsilon$$ is machine epsilon corresponding
to the type $code double$$.

$children%
	build/lib/example/cplusplus/a_double_property_xam.cpp%
	build/lib/example/octave/a_double_property_xam.m%
	build/lib/example/perl/a_double_property_xam.pm%
	build/lib/example/python/a_double_property_xam.py
%$$
$head Example$$
$cref/C++/a_double_property_xam.cpp/$$,
$cref/Octave/a_double_property_xam.m/$$,
$cref/Perl/a_double_property_xam.pm/$$,
$cref/Python/a_double_property_xam.py/$$.

$end
*/
double a_double::value(void) const
{	double result = CppAD::Value( *ptr() );
	return result;
}
bool a_double::parameter(void) const
{	bool result = CppAD::Parameter( *ptr() );
	return result;
}
bool a_double::variable(void) const
{	bool result = CppAD::Variable( *ptr() );
	return result;
}
bool a_double::near_equal(const a_double& ae)
{	double d       = CppAD::Value( CppAD::Var2Par( *ptr() ) );
	double e       = CppAD::Value( CppAD::Var2Par( *ae.ptr() ) );
	double diff    = std::fabs( d - e );
	double eps     = std::numeric_limits<double>::epsilon();
	double sum_abs = std::fabs(d) + std::fabs(e);
	return diff <= 100.0 * eps * sum_abs;
}
/*
-------------------------------------------------------------------------------
$begin a_double_ad_binary$$

$section ad_double Binary Operators with an AD Result$$
$spell
	const
	az
	op
	perl
$$

$head Syntax$$
$icode%az% = %ax% %op% %ay%$$

$head op$$
The binary operator $icode op$$ is one of the following:
$code +$$ (addition),
$code -$$ (subtraction),
$code *$$ (multiplication),
$code /$$ (division).

$head ax$$
This object has prototype
$codei%
	const a_double& %ax%
%$$

$head ay$$
This object has prototype
$codei%
	const a_double& %ay%
%$$

$head az$$
The result has prototype
$codei%
	a_double %az%
%$$

$children%
	build/lib/example/cplusplus/a_double_ad_binary_xam.cpp%
	build/lib/example/octave/a_double_ad_binary_xam.m%
	build/lib/example/perl/a_double_ad_binary_xam.pm%
	build/lib/example/python/a_double_ad_binary_xam.py
%$$
$head Example$$
$cref/C++/a_double_ad_binary_xam.cpp/$$,
$cref/Octave/a_double_ad_binary_xam.m/$$,
$cref/Perl/a_double_ad_binary_xam.pm/$$,
$cref/Python/a_double_ad_binary_xam.py/$$.

$end
*/
BINARY_OP_AD_RESULT(+)
BINARY_OP_AD_RESULT(-)
BINARY_OP_AD_RESULT(*)
BINARY_OP_AD_RESULT(/)
/*
-------------------------------------------------------------------------------
$begin a_double_compare$$

$section ad_double Comparison Operators$$
$spell
	const
	az
	op
	perl
	bool
$$

$head Syntax$$
$icode%b% = %ax% %op% %ay%$$

$head op$$
The binary operator $icode op$$ is one of the following:
$code <$$ (less than),
$code <=$$ (less than or equal),
$code >$$ (greater than),
$code >=$$ (greater than or equal),
$code ==$$ (equal),
$code !=$$ (not equal).

$head ax$$
This object has prototype
$codei%
	const a_double& %ax%
%$$

$head ay$$
This object has prototype
$codei%
	const a_double& %ay%
%$$

$head b$$
The result has prototype
$codei%
	bool %b%
%$$

$children%
	build/lib/example/cplusplus/a_double_compare_xam.cpp%
	build/lib/example/octave/a_double_compare_xam.m%
	build/lib/example/perl/a_double_compare_xam.pm%
	build/lib/example/python/a_double_compare_xam.py
%$$
$head Example$$
$cref/C++/a_double_compare_xam.cpp/$$,
$cref/Octave/a_double_compare_xam.m/$$,
$cref/Perl/a_double_compare_xam.pm/$$,
$cref/Python/a_double_compare_xam.py/$$.

$end
*/
COMPARISON_OP(<)
COMPARISON_OP(<=)
COMPARISON_OP(>)
COMPARISON_OP(>=)
COMPARISON_OP(==)
COMPARISON_OP(!=)
/*
-------------------------------------------------------------------------------
$begin a_double_assign$$

$section ad_double Assignment Operators$$
$spell
	const
	az
	op
	perl
$$

$head Syntax$$
$icode%ay% %op% %ax%%$$

$head op$$
The assignment operator $icode op$$ is one of the following:
$table
$icode op$$ $pre  $$ $cnext Meaning            $rnext
$code =$$ $cnext  simple assignment            $rnext
$code +=$$ $cnext $icode%ay% = %ay% + %ax%$$   $rnext
$code -=$$ $cnext $icode%ay% = %ay% - %ax%$$   $rnext
$code *=$$ $cnext $icode%ay% = %ay% * %ax%$$   $rnext
$code /=$$ $cnext $icode%ay% = %ay% / %ax%$$
$tend

$head ax$$
This object has prototype
$codei%
	const a_double& %ax%
%$$

$head ay$$
This object has prototype
$codei%
	a_double& %ay%
%$$

$children%
	build/lib/example/cplusplus/a_double_assign_xam.cpp%
	build/lib/example/octave/a_double_assign_xam.m%
	build/lib/example/perl/a_double_assign_xam.pm%
	build/lib/example/python/a_double_assign_xam.py
%$$
$head Example$$
$cref/C++/a_double_assign_xam.cpp/$$,
$cref/Octave/a_double_assign_xam.m/$$,
$cref/Perl/a_double_assign_xam.pm/$$,
$cref/Python/a_double_assign_xam.py/$$.

$end
*/
COMPOUND_ASSIGNMENT_OP(+=)
COMPOUND_ASSIGNMENT_OP(-=)
COMPOUND_ASSIGNMENT_OP(*=)
COMPOUND_ASSIGNMENT_OP(/=)
/*
-------------------------------------------------------------------------------
$begin a_double_unary_fun$$
$spell
	const
	perl
	bool

	acos
	asin
	atan
	cos
	exp
	fabs
	sqrt
	tanh
	asinh
	acosh
	atanh
	expm
$$

$section Unary Functions with AD Result$$

$head Syntax$$
$icode%ay% = %ax%.%fun%()
%$$

$head ax$$
This object has prototype
$codei%
	const a_double& %ax%
%$$
This is the argument for the function evaluation.

$head fun$$
This specifies which function is being evaluated and is one
of  following value:
$code acos$$,
$code asin$$,
$code atan$$,
$code cos$$,
$code cosh$$,
$code exp$$,
$code fabs$$,
$code log$$,
$code sin$$,
$code sinh$$,
$code sqrt$$,
$code tan$$,
$code tanh$$.
2DO: Add the C++11 functions
asinh, acosh, atanh, expm1, and log1p to this list.

$head ay$$
The result object has prototype
$codei%
	a_double %ay%
%$$
and is the specified function evaluated at the specified argument; i.e.,
$codei%
	%ay% = %fun%( %ax% )
%$$

$children%
	build/lib/example/cplusplus/a_double_unary_fun_xam.cpp%
	build/lib/example/octave/a_double_unary_fun_xam.m%
	build/lib/example/perl/a_double_unary_fun_xam.pm%
	build/lib/example/python/a_double_unary_fun_xam.py
%$$
$head Example$$
$cref/C++/a_double_unary_fun_xam.cpp/$$,
$cref/Octave/a_double_unary_fun_xam.m/$$,
$cref/Perl/a_double_unary_fun_xam.pm/$$,
$cref/Python/a_double_unary_fun_xam.py/$$.

$end
*/
UNARY_FUN_AD_RESULT(acos)
UNARY_FUN_AD_RESULT(asin)
UNARY_FUN_AD_RESULT(atan)
UNARY_FUN_AD_RESULT(cos)
UNARY_FUN_AD_RESULT(cosh)
UNARY_FUN_AD_RESULT(exp)
UNARY_FUN_AD_RESULT(fabs)
UNARY_FUN_AD_RESULT(log)
UNARY_FUN_AD_RESULT(sin)
UNARY_FUN_AD_RESULT(sinh)
UNARY_FUN_AD_RESULT(sqrt)
UNARY_FUN_AD_RESULT(tan)
UNARY_FUN_AD_RESULT(tanh)
/*
-------------------------------------------------------------------------------
$begin a_double_cond_assign$$
$spell
	const
	perl
	cond
$$

$section AD Conditional Assignment$$

$head Syntax$$
$icode%target%.cond_assign(%cop%, %left%, %right%, %if_true%, %if_false%)
%$$

$head Purpose$$
The code
$codei%
	if( %left% %cop% %right% )
		%target% = %if_true%
	else
		%target% = %if_false%
%$$
records either the true or false case depending on the value
of $icode left$$ and $icode right$$; see $cref a_fun_ctor$$.
If $icode left$$ or $icode right$$ is a
$cref/variable/a_double_property/variable/$$,
it may be desirable to switch between $icode if_true$$ and $icode if_false$$
depending of the value of the independent variable during
calls to order zero $cref a_fun_forward$$.
The $code cond_assign$$ does this.

$head target$$
This object has prototype
$codei%
	a_double& %target%
%$$

$head cop$$
This argument has prototype
$codei%
	const char *cop
%$$
The comparison is
$codei%
	%left% %cop% %right%
%$$
where $icode cop$$ is one of the following:
$table
$icode cop$$  $cnext                       $rnext
$code <$$     $cnext less than             $rnext
$code <=$$    $cnext less than or equal    $rnext
$code ==$$    $cnext equal                 $rnext
$code >=$$    $cnext greater than or equal $rnext
$code >$$     $cnext greater than
$tend

$head left$$
This argument has prototype
$codei%
	const a_double& %left%
%$$
It specifies the left operand in the comparison.

$head right$$
This argument has prototype
$codei%
	const a_double& %right%
%$$
It specifies the right operand in the comparison.

$head if_true$$
This argument has prototype
$codei%
	const a_double& %if_true%
%$$
It specifies the value assigned to $icode ad$$ if the result
of the comparison is true.

$head if_false$$
This argument has prototype
$codei%
	const a_double& %if_false%
%$$
It specifies the value assigned to $icode ad$$ if the result
of the comparison is false.


$children%
	build/lib/example/cplusplus/a_double_cond_assign_xam.cpp%
	build/lib/example/octave/a_double_cond_assign_xam.m%
	build/lib/example/perl/a_double_cond_assign_xam.pm%
	build/lib/example/python/a_double_cond_assign_xam.py
%$$
$head Example$$
$cref/C++/a_double_cond_assign_xam.cpp/$$,
$cref/Octave/a_double_cond_assign_xam.m/$$,
$cref/Perl/a_double_cond_assign_xam.pm/$$,
$cref/Python/a_double_cond_assign_xam.py/$$.

$end
*/
void a_double::cond_assign(
	const char*     cop       ,
	const a_double& left      ,
	const a_double& right     ,
	const a_double& if_true   ,
	const a_double& if_false  )
{	std::string cop_string(cop);
	if( cop_string == "<" )
	{	*ptr() = CppAD::CondExpLt(
			*left.ptr(), *right.ptr(), *if_true.ptr(), *if_false.ptr()
		);
	}
	else if( cop_string == "<=" )
	{	*ptr() = CppAD::CondExpLe(
			*left.ptr(), *right.ptr(), *if_true.ptr(), *if_false.ptr()
		);
	}
	else if( cop_string == "==" )
	{	*ptr() = CppAD::CondExpEq(
			*left.ptr(), *right.ptr(), *if_true.ptr(), *if_false.ptr()
		);
	}
	else if( cop_string == ">=" )
	{	*ptr() = CppAD::CondExpGe(
			*left.ptr(), *right.ptr(), *if_true.ptr(), *if_false.ptr()
		);
	}
	else if( cop_string == ">" )
	{	*ptr() = CppAD::CondExpGt(
			*left.ptr(), *right.ptr(), *if_true.ptr(), *if_false.ptr()
		);
	}
	else
	{	std::string message = "a_double::cond_assing:: cop = '";
		message += cop;
		message += "' is not a valid comparison operator";
		error_message(message.c_str());
	}
}
// --------------------------------------------------------------------------
} // END_CPPAD_SWIG_NAMESPACE
