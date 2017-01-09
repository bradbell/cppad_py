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
// computed assignment operators
# define COMPUTED_ASSIGNMENT_OP(op) \
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
$icode%ad% = %module_ref_%a_double()
%$$
$icode%ad% = %module_ref_%a_double(%d%)
%$$
$icode%ad% = %module_ref_%a_double(%ad_other%)
%$$

$head Purpose$$
Creates a $code cppad_swig::a_double$$ object that can be use
to track floating point operations and preform algorithmic differentiation.

$head module_ref_$$
This is a reference to the Cppad Swig module which is
language dependent as follows:
$table
C++        $cnext $code cppad_swig::$$ $rnext
Octave     $cnext $code m_cppad.$$     $rnext
Perl       $cnext $code pm_cppad::$$   $rnext
Python     $cnext $code py_cppad.$$
$tend

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
-------------------------------------------------------------------------------
$begin a_double_value$$
$spell
	perl
$$

$section Conversion From a_double to double$$
$spell
	const
$$

$head Syntax$$
$icode%d% = ad%.value()%$$

$head ad$$
This object has prototype
$codei%
	const a_double& %ad%
%$$
In addition it must represent a constant functions; i.e.,
it must not depend on the independent variable.
If it does depend on the independent variables,
you will have to wait until the current recording is terminated
before you can access its value.

$head d$$
The result has prototype
$codei%
	double %d%
%$$
It is the value of $icode ad$$, as a constant function.

$children%
	build/lib/example/cplusplus/a_double_value_xam.cpp%
	build/lib/example/octave/a_double_value_xam.m%
	build/lib/example/perl/a_double_value_xam.pm%
	build/lib/example/python/a_double_value_xam.py
%$$
$head Example$$
$cref/C++/a_double_value_xam.cpp/$$,
$cref/octave/a_double_value_xam.m/$$,
$cref/perl/a_double_value_xam.pm/$$,
$cref/python/a_double_value_xam.py/$$.

$end
*/
/// conversion to double
double a_double::value(void) const
{	double result = Value( *ptr() );
	return result;
}
/*
-------------------------------------------------------------------------------
$begin a_double_ad_binary$$

$section Binary Operators with an a_double Result$$
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
addition $code +$$,
subtraction $code -$$,
multiplication $code *$$,
division $code /$$.

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
$cref/octave/a_double_ad_binary_xam.m/$$,
$cref/perl/a_double_ad_binary_xam.pm/$$,
$cref/python/a_double_ad_binary_xam.py/$$.

$end
*/
BINARY_OP_AD_RESULT(+)
BINARY_OP_AD_RESULT(-)
BINARY_OP_AD_RESULT(*)
BINARY_OP_AD_RESULT(/)
// comparison operators
COMPARISON_OP(<)
COMPARISON_OP(<=)
COMPARISON_OP(>)
COMPARISON_OP(>=)
COMPARISON_OP(==)
COMPARISON_OP(!=)
// computed assignment operators
COMPUTED_ASSIGNMENT_OP(+=)
COMPUTED_ASSIGNMENT_OP(-=)
COMPUTED_ASSIGNMENT_OP(*=)
COMPUTED_ASSIGNMENT_OP(/=)

} // END_CPPAD_SWIG_NAMESPACE
