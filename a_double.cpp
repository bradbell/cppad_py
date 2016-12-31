// $Id$
/* -----------------------------------------------------------------------------
           cppad_swig: A C++ Object Library and SWIG Interface to CppAD
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

// default ctor
a_double::a_double(void)
{	// placement version of new operator uses this->data_ for memory
	CPPAD_ASSERT_UNKNOWN( sizeof(data_) == sizeof( CppAD::AD<double> ) );
	new ( & data_ ) CppAD::AD<double>();
}
// destructor
a_double::~a_double(void)
{ }
// ctor from double
a_double::a_double(const double& base)
{	CPPAD_ASSERT_UNKNOWN( sizeof(data_) == sizeof( CppAD::AD<double> ) );
	new ( & data_ ) CppAD::AD<double>(base);
}
// ctor from a_double
a_double::a_double(const a_double& ad)
{	CPPAD_ASSERT_UNKNOWN( sizeof(data_) == sizeof( CppAD::AD<double> ) );
	new ( & data_ ) CppAD::AD<double>(*ad.ptr());
}
/// conversion to double
double a_double::value(void) const
{	double result = Value( *ptr() );
	return result;
}
// binary operators with an ad result
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
