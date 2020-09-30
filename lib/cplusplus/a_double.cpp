/* -----------------------------------------------------------------------------
           cppad_py: A C++ Object Library and Python Interface to Cppad
            Copyright (C) 2017-20 Bradley M. Bell (bradbell@seanet.com)
                This program is distributed under the terms of the
                GNU General Public License version 3.0 or later see
                      https://www.gnu.org/licenses/gpl-3.0.txt
----------------------------------------------------------------------------- */
# include <cppad/cppad.hpp>
# include <cppad/py/error.hpp>
# include <cppad/py/a_double.hpp>

// ---------------------------------------------------------------------------
// Macros
// ---------------------------------------------------------------------------

// binary operators with ad results
# define BINARY_OP_AD_RESULT(op) \
a_double a_double::operator op(const a_double& ad) const \
{   a_double result; \
    *result.ptr() = *ptr() op *ad.ptr(); \
    return result; \
}\
a_double a_double::operator op(const double& d) const \
{   a_double result; \
    *result.ptr() = *ptr() op d; \
    return result; \
}

// comparison operators
# define COMPARISON_OP(op) \
bool a_double::operator op(const a_double& ad) const \
{   bool result =  *ptr() op *ad.ptr(); \
    return result; \
}\
bool a_double::operator op(const double& d) const \
{   bool result =  *ptr() op d; \
    return result; \
}

// compound assignment operators
# define ASSIGNMENT_OP(op) \
a_double a_double::operator op(const a_double& ad)\
{   *ptr() op *ad.ptr(); \
    return *this; \
}\
a_double a_double::operator op(const double& d)\
{   *ptr() op d; \
    return *this; \
}

// unary functions with ad results
# define UNARY_FUN_AD_RESULT(fun) \
a_double a_double::fun(void) const \
{   a_double result; \
    *result.ptr() = CppAD::fun( *ptr() ); \
    return result; \
}
// ---------------------------------------------------------------------------

namespace cppad_py { // BEGIN_CPPAD_PY_NAMESPACE

// ---------------------------------------------------------------------------
// public member functions not in Swig interface
// ---------------------------------------------------------------------------
// pointer to this as an AD<double> object
CppAD::AD<double>* a_double::ptr(void)
{   return reinterpret_cast< CppAD::AD<double>* >( & data_ );
}
// const version of pointer to this as an AD<double> object
const CppAD::AD<double>* a_double::ptr(void) const
{   return reinterpret_cast< const CppAD::AD<double>* >( & data_ );
}
// ctor from CppAD::AD<double>
a_double::a_double(const CppAD::AD<double>* a_ptr)
{   CPPAD_PY_ASSERT_UNKNOWN( sizeof(data_) == sizeof( CppAD::AD<double> ) );
    new ( & data_ ) CppAD::AD<double>(*a_ptr);
}
/*
-------------------------------------------------------------------------------
{xsrst_begin a_double_ctor}

.. include:: ../preamble.rst

{xsrst_spell
    cppad
}

The a_double Constructor
########################

Syntax
******

| *ad* =  ``cppad_py.a_double`` ()
| *ad* =  ``cppad_py.a_double`` ( *d* )
| *ad* =  ``cppad_py.a_double`` ( *a_other* )

Purpose
*******
Creates a ``cppad_py::a_double`` object that can be use
to track floating point operations and perform algorithmic differentiation.

d
*
This argument has prototype

| |tab| ``const double&`` *d*

The resulting *ad* variable represents
a constant function equal to *d* .

a_other
*******
This argument has prototype

| |tab| ``const a_double&`` *a_other*

The resulting *ad* variable is the same function
of the independent variables as *a_other* .

ad
**
is the ``a_double`` object that is constructed.

Example
*******
All of the other ``a_double`` examples use an ``a_double``
constructor.

{xsrst_end a_double_ctor}
-------------------------------------------------------------------------------
*/
// default a_double ctor
a_double::a_double(void)
{   // placement version of new operator uses this->data_ for memory
    CPPAD_PY_ASSERT_UNKNOWN( sizeof(data_) == sizeof( CppAD::AD<double> ) );
    new ( & data_ ) CppAD::AD<double>();
}
// a_double ctor from double
a_double::a_double(const double& d)
{   CPPAD_PY_ASSERT_UNKNOWN( sizeof(data_) == sizeof( CppAD::AD<double> ) );
    new ( & data_ ) CppAD::AD<double>(d);
}
// ctor from a_double
a_double::a_double(const a_double& ad)
{   CPPAD_PY_ASSERT_UNKNOWN( sizeof(data_) == sizeof( CppAD::AD<double> ) );
    new ( & data_ ) CppAD::AD<double>(*ad.ptr());
}
// a_double destructor
a_double::~a_double(void)
{ }
/*
{xsrst_begin a_double_unary_op}

.. include:: ../preamble.rst

a_double Unary Plus and Minus
#############################

{xsrst_spell
}

Syntax
******

| *ay* = + *ax*
| *ay* = - *ax*

ax
**
This object has prototype

| |tab| ``const a_double&`` *ax*

ay
**
If the operator is ``+`` , the result is equal to *ax* .
If it is ``-`` , the result is the negative of *ax* .

{xsrst_children
    example/cplusplus/a_double_unary_op_xam.cpp
    example/python/core/a_double_unary_op_xam.py
}
Example
*******
:ref:`c++<a_double_unary_op_xam_cpp>`,
:ref:`python<a_double_unary_op_xam_py>`.

{xsrst_end a_double_unary_op}
*/
const a_double& a_double::operator+(void) const
{   return *this; }
a_double a_double::operator-(void) const
{   a_double result;
    *result.ptr() = - *ptr();
    return result;
}
/*
-------------------------------------------------------------------------------
{xsrst_begin a_double_property}

.. include:: ../preamble.rst

{xsrst_spell
    bool
    aother
    ap
}

Properties of an a_double Object
################################

Syntax
******

| *d* = *ad* . ``value`` ()
| *p* = *ad* . ``parameter`` ()
| *v* = *ad* . ``variable`` ()
| *e* = *ad* . ``near_equal`` ( *aother* )
| *ap* = *ad* . ``var2par`` ()

ad
**
This object has prototype

| |tab| ``const a_double&`` *ad*

value
*****
The result *d* has prototype

| |tab| ``double`` *d*

It is the value of *ad* , as a constant function.

Restriction
===========
The object *ad* must not depend on the
:ref:`independent<cpp_independent>`
variables when *ad* . ``value`` () is called.
If it does depend on the independent variables,
you will have to wait until the current recording is terminated
before you can access its value; see
:ref:`var2par<a_double_property.var2par>` below.

parameter
*********
The result *p* has prototype

| |tab| ``bool`` *p*

It is true if *ad* represent a constant functions; i.e.,
*ad* not depend on the independent variables.

variable
********
The result *v* has prototype

| |tab| ``bool`` *v*

It is true if *ad* is not a constant function; i.e.,
*ad* depends on the independent variables.

near_equal
**********
The argument *aother* ,
and the result *e* , have prototype

| |tab| ``const a_double&`` *aother*
| |tab| ``bool`` *e*

The result is true if *ad* is nearly equal to *aother* .
To be specific, the result is

.. math::

    | d - o | \leq 100 \; \varepsilon \; ( |d| + |o| )

where *d* and *o* are the value corresponding to
*ad* and *aother* and
:math:`\varepsilon` is machine epsilon corresponding
to the type ``double`` .

var2par
*******
The result has prototype

| |tab| ``a_double`` *ap*

It has the same value as *ad* and is sure to be a parameter
( *ad* may or may not be a variable).
This can be useful when you want to access the value of *ad*
while is a variable; :ref:`value<a_double_property.value>` above.

{xsrst_children
    example/cplusplus/a_double_property_xam.cpp
    example/python/core/a_double_property_xam.py
}
Example
*******
:ref:`c++<a_double_property_xam_cpp>`,
:ref:`python<a_double_property_xam_py>`.

{xsrst_end a_double_property}
*/
double a_double::value(void) const
{   double result = CppAD::Value( *ptr() );
    return result;
}
bool a_double::parameter(void) const
{   bool result = CppAD::Parameter( *ptr() );
    return result;
}
bool a_double::variable(void) const
{   bool result = CppAD::Variable( *ptr() );
    return result;
}
bool a_double::near_equal(const a_double& aother)
{   double d       = CppAD::Value( CppAD::Var2Par( *ptr() ) );
    double o       = CppAD::Value( CppAD::Var2Par( *aother.ptr() ) );
    double diff    = std::fabs( d - o );
    double eps     = std::numeric_limits<double>::epsilon();
    double sum_abs = std::fabs(d) + std::fabs(o);
    return diff <= 100.0 * eps * sum_abs;
}
a_double a_double::var2par() const
{   a_double result;
    *result.ptr() = CppAD::Var2Par( *ptr() );
    return result;
}
/*
-------------------------------------------------------------------------------
{xsrst_begin a_double_binary}

.. include:: ../preamble.rst

a_double Binary Operators with an AD Result
###########################################

{xsrst_spell
    az
}

Syntax
******

| *az* = *ax* *op* *ay*
| *az* = *ax* *op* *y*
| *az* = *y* *op* *ax*

op
**
The binary operator *op* is one of the following:
addition ``+`` ,
subtraction ``-`` ,
multiplication ``*`` ,
division ``/`` , or
exponentiation ``**`` .
Note that exponentiation is a function is c++ and an operator in python.

ax
**
This object has prototype

| |tab| ``const a_double&`` *ax*

ay
**
This object has prototype

| |tab| ``const a_double&`` *ay*

y
*
This object has prototype

| |tab| ``const double&`` *y*

az
**
The result has prototype

| |tab| ``a_double`` *az*

{xsrst_children
    example/cplusplus/a_double_binary_xam.cpp
    example/python/core/a_double_binary_xam.py
}
Example
*******
:ref:`c++<a_double_binary_xam_cpp>`,
:ref:`python<a_double_binary_xam_py>`.

{xsrst_end a_double_binary}
*/
BINARY_OP_AD_RESULT(+)
BINARY_OP_AD_RESULT(-)
BINARY_OP_AD_RESULT(*)
BINARY_OP_AD_RESULT(/)
//
// binary operators when right operand is a double
a_double radd(const double& d, const a_double& ad)
{   a_double result;
    *result.ptr() = d + *ad.ptr();
    return result;
}
a_double rsub(const double& d, const a_double& ad)
{   a_double result;
    *result.ptr() = d - *ad.ptr();
    return result;
}
a_double rmul(const double& d, const a_double& ad)
{   a_double result;
    *result.ptr() = d * *ad.ptr();
    return result;
}
a_double rdiv(const double& d, const a_double& ad)
{   a_double result;
    *result.ptr() = d / *ad.ptr();
    return result;
}
//
// pow (operator in python but not c++)
a_double pow(const a_double& ax, const a_double& ay)
{   a_double result;
    *result.ptr() = CppAD::pow( *ax.ptr(), *ay.ptr() );
    return result;
}
a_double pow(const a_double& ad, const double& d)
{   a_double result;
    *result.ptr() = CppAD::pow( *ad.ptr(), d );
    return result;
}
a_double pow(const double& d, const a_double& ad)
{   a_double result;
    *result.ptr() = CppAD::pow( d, *ad.ptr() );
    return result;
}
/*
-------------------------------------------------------------------------------
{xsrst_begin a_double_compare}

.. include:: ../preamble.rst

a_double Comparison Operators
#############################

{xsrst_spell
    bool
}

Syntax
******

| *b* = *ax* *op* *ay*
| *b* = *ax* *op* *y*

op
**
The binary operator *op* is one of the following:
``<`` (less than),
``<=`` (less than or equal),
``>`` (greater than),
``>=`` (greater than or equal),
``==`` (equal),
``!=`` (not equal).

ax
**
This object has prototype

| |tab| ``const a_double&`` *ax*

ay
**
This object has prototype

| |tab| ``const a_double&`` *ay*

y
*
This object has prototype

| |tab| ``const double&`` *y*

b
*
The result has prototype

| |tab| ``bool`` *b*

{xsrst_children
    example/cplusplus/a_double_compare_xam.cpp
    example/python/core/a_double_compare_xam.py
}
Example
*******
:ref:`c++<a_double_compare_xam_cpp>`,
:ref:`python<a_double_compare_xam_py>`.

{xsrst_end a_double_compare}
*/
COMPARISON_OP(<)
COMPARISON_OP(<=)
COMPARISON_OP(>)
COMPARISON_OP(>=)
COMPARISON_OP(==)
COMPARISON_OP(!=)
/*
-------------------------------------------------------------------------------
{xsrst_begin a_double_assign}

.. include:: ../preamble.rst

a_double Assignment Operators
#############################

{xsrst_spell
}

Syntax
******

| *ax* *op* *ay*
| *aw* *op* *y*

op
**
The assignment operator *op* is one of the following:

.. csv-table::
    :widths: 2, 30

    *op* , Meaning
    ``=`` , simple assignment
    ``+=`` , *ax* = *ax* + ( *ay* ``or`` *y* )
    ``-=`` , *ax* = *ax* - ( *ay* ``or`` *y* )
    ``*=`` , *ax* = *ax* ``*`` *ay* ``or`` *y* )
    ``/=`` , *ax* = *ax* ``/`` *ay* ``or`` *y* )

ax
**
This object has prototype

| |tab| ``const a_double&`` *ax*

ay
**
This object has prototype

| |tab| ``a_double&`` *ay*

y
*
This object has prototype

| |tab| ``const double&`` *y*

{xsrst_children
    example/cplusplus/a_double_assign_xam.cpp
    example/python/core/a_double_assign_xam.py
}
Example
*******
:ref:`c++<a_double_assign_xam_cpp>`,
:ref:`python<a_double_assign_xam_py>`.

{xsrst_end a_double_assign}
*/
ASSIGNMENT_OP(=)
ASSIGNMENT_OP(+=)
ASSIGNMENT_OP(-=)
ASSIGNMENT_OP(*=)
ASSIGNMENT_OP(/=)
/*
-------------------------------------------------------------------------------
{xsrst_begin a_double_unary_fun}

.. include:: ../preamble.rst

{xsrst_spell
    acos
    asin
    atan
    exp
    fabs
    sqrt
    tanh
    asinh
    acosh
    atanh
    expm
    erf
}

Unary Functions with AD Result
##############################

Syntax
******

| *ay* = *ax* . *fun* ()

ax
**
This object has prototype

| |tab| ``const a_double&`` *ax*

This is the argument for the function evaluation.

fun
***
This specifies which function is being evaluated and is one
of  following value:
``abs`` ,
``acos`` ,
``asin`` ,
``atan`` ,
``cos`` ,
``cosh`` ,
``erf`` ,
``exp`` ,
``fabs`` ,
``log`` ,
``sin`` ,
``sinh`` ,
``sqrt`` ,
``tan`` ,
``tanh`` .
2DO: Add the C++11 functions
asinh, acosh, atanh, expm1, and log1p to this list.

ay
**
The result object has prototype

| |tab| ``a_double`` *ay*

and is the specified function evaluated at the specified argument; i.e.,

| |tab| *ay* = *fun* ( *ax* )

{xsrst_children
    example/cplusplus/a_double_unary_fun_xam.cpp
    example/python/core/a_double_unary_fun_xam.py
}
Example
*******
:ref:`c++<a_double_unary_fun_xam_cpp>`,
:ref:`python<a_double_unary_fun_xam_py>`.

{xsrst_end a_double_unary_fun}
*/
UNARY_FUN_AD_RESULT(abs)
UNARY_FUN_AD_RESULT(acos)
UNARY_FUN_AD_RESULT(asin)
UNARY_FUN_AD_RESULT(atan)
UNARY_FUN_AD_RESULT(cos)
UNARY_FUN_AD_RESULT(cosh)
UNARY_FUN_AD_RESULT(erf)
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
{xsrst_begin a_double_cond_assign}

.. include:: ../preamble.rst

{xsrst_spell
    cond
}

AD Conditional Assignment
#########################

Syntax
******

| *target* . ``cond_assign`` ( *cop* , *left* , *right* , *if_true* , *if_false* )

Purpose
*******
The code

| |tab| ``if`` ( *left* *cop* *right* )
| |tab| |tab| *target* = *if_true*
| |tab| ``else``
| |tab| |tab| *target* = *if_false*

records either the true or false case depending on the value
of *left* and *right* ; see :ref:`cpp_fun_ctor<cpp_fun_ctor>`.
If *left* or *right* is a
:ref:`variable<a_double_property.variable>`,
it may be desirable to switch between *if_true* and *if_false*
depending of the value of the independent variable during
calls to order zero :ref:`cpp_fun_forward<cpp_fun_forward>`.
The ``cond_assign`` does this.

target
******
This object has prototype

| |tab| ``a_double&`` *target*

cop
***
This argument has prototype

| |tab| ``const char *cop``

The comparison is

| |tab| *left* *cop* *right*

where *cop* is one of the following:

.. csv-table::
    :widths: 3, 21

    *cop* ,
    ``<`` , less than
    ``<=`` , less than or equal
    ``==`` , equal
    ``>=`` , greater than or equal
    ``>`` , greater than

left
****
This argument has prototype

| |tab| ``const a_double&`` *left*

It specifies the left operand in the comparison.

right
*****
This argument has prototype

| |tab| ``const a_double&`` *right*

It specifies the right operand in the comparison.

if_true
*******
This argument has prototype

| |tab| ``const a_double&`` *if_true*

It specifies the value assigned to *ad* if the result
of the comparison is true.

if_false
********
This argument has prototype

| |tab| ``const a_double&`` *if_false*

It specifies the value assigned to *ad* if the result
of the comparison is false.

{xsrst_children
    example/cplusplus/a_double_cond_assign_xam.cpp
    example/python/core/a_double_cond_assign_xam.py
}
Example
*******
:ref:`c++<a_double_cond_assign_xam_cpp>`,
:ref:`python<a_double_cond_assign_xam_py>`.

{xsrst_end a_double_cond_assign}
*/
void a_double::cond_assign(
    const char*     cop       ,
    const a_double& left      ,
    const a_double& right     ,
    const a_double& if_true   ,
    const a_double& if_false  )
{   std::string cop_string(cop);
    if( cop_string == "<" )
    {   *ptr() = CppAD::CondExpLt(
            *left.ptr(), *right.ptr(), *if_true.ptr(), *if_false.ptr()
        );
    }
    else if( cop_string == "<=" )
    {   *ptr() = CppAD::CondExpLe(
            *left.ptr(), *right.ptr(), *if_true.ptr(), *if_false.ptr()
        );
    }
    else if( cop_string == "==" )
    {   *ptr() = CppAD::CondExpEq(
            *left.ptr(), *right.ptr(), *if_true.ptr(), *if_false.ptr()
        );
    }
    else if( cop_string == ">=" )
    {   *ptr() = CppAD::CondExpGe(
            *left.ptr(), *right.ptr(), *if_true.ptr(), *if_false.ptr()
        );
    }
    else if( cop_string == ">" )
    {   *ptr() = CppAD::CondExpGt(
            *left.ptr(), *right.ptr(), *if_true.ptr(), *if_false.ptr()
        );
    }
    else
    {   std::string message = "a_double::cond_assing:: cop = '";
        message += cop;
        message += "' is not a valid comparison operator";
        CPPAD_PY_ASSERT_KNOWN(false, message.c_str());
    }
}
// --------------------------------------------------------------------------
} // END_CPPAD_PY_NAMESPACE
