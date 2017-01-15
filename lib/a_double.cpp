/* -----------------------------------------------------------------------------
           cppad_swig: A C++ Object Library and Swig Interface to Cppad
            Copyright (C) 2017-17 Bradley M. Bell (bradbell@seanet.com)
                This program is distributed under the terms of the
            GNU Affero General Public License version 3.0 or later see
                       http://www.gnu.org/licenses/agpl.txt
----------------------------------------------------------------------------- */
# include <cppad/cppad.hpp>
# include <cppad/swig/a_double.hpp>

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
$begin a_double_unary$$

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
$$

$section Properties of an a_double Object$$

$head Syntax$$
$icode%d% = %ad%.value()
%$$
$icode%p% = %ad%.parameter()
%$$
$icode%v% = %ad%.variable()
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
{	double result = Value( *ptr() );
	return result;
}
bool a_double::parameter(void) const
{	bool result = Parameter( *ptr() );
	return result;
}
bool a_double::variable(void) const
{	bool result = Variable( *ptr() );
	return result;
}
/*
-------------------------------------------------------------------------------
$begin a_double_ad_binary$$

$section ad_double Binary Operators with an a_double Result$$
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
// --------------------------------------------------------------------------
} // END_CPPAD_SWIG_NAMESPACE
