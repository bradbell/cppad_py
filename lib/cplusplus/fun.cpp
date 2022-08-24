/* -----------------------------------------------------------------------------
           cppad_py: A C++ Object Library and Python Interface to Cppad
            Copyright (C) 2017-22 Bradley M. Bell (bradbell@seanet.com)
                This program is distributed under the terms of the
                GNU General Public License version 3.0 or later see
                      https://www.gnu.org/licenses/gpl-3.0.txt
----------------------------------------------------------------------------- */
# include <cppad/cppad.hpp>
# include <cppad/py/fun.hpp>
# include <cppad/py/assert.hpp>
# include <cppad/py/cpp_convert.hpp>

namespace cppad_py { // BEGIN_CPPAD_PY_NAMESPACE

/*
-------------------------------------------------------------------------------
{xrst_begin cpp_independent}

{xrst_spell
    cppad
    nx
    nd
}

Declare Independent Variables and Start Recording
#################################################

Syntax
******

| *ax* =  ``cppad_py::independent`` ( *x* )
| *a_both* =  ``cppad_py::independent`` ( *x* , *dynamic* )

Purpose
*******
This starts recording :ref:`a_double` operations.
This recording is terminated, and the information is stored,
by calling the :ref:`d_fun_constructor<cpp_fun_ctor>`.
It can be terminated, and the information is lost,
by calling :ref:`abort_recording<cpp_abort_recording>`.

x
*
This argument has prototype

| |tab| ``const vec_double&`` *x*

Its specifies the number of independent variables
and their values during the recording.
We use the notation *nx* = *x*\ ``.size`` ()
to denote the number of independent variables.

dynamic
*******
This argument has prototype

| |tab| ``const vec_double&`` *dynamic*

Its specifies the number of independent dynamic parameters
and their values during the recording.
We use the notation *nd* = *dynamic*\ ``.size`` ()
to denote the number of independent variables.

ax
**
This result has prototype

| |tab| ``vec_a_double&`` *ax*

and is the vector of independent variables.
It has size *nx* and for
*i* = 0 to *n* -1

| |tab| *ax* [ *i* ] == *x* [ *i* ]

a_both
******
this result has prototype

| |tab| ``vec_a_double&`` *a_both*

and is the vector of both the independent variables
and independent dynamic parameters.
It has size *nx* + *nd* .
For *i* = 0 to *nx* -1

| |tab| *a_both* [ *i* ] == *x* [ *i* ]

is the *i*-th independent variable.
For *i* = 0 to *nd* -1

| |tab| *a_both* [ *nx* + *i* ] == *dynamic* [ *i* ]

is the *i*-th independent dynamic parameter.

{xrst_toc_hidden
    example/cplusplus/fun_dynamic_xam.cpp
}
Example
*******
Most of the c++ ``d_fun`` examples use the *ax*
return syntax.
The :ref:`fun_dynamic_xam_cpp` example uses the *a_both*
return syntax.

{xrst_end cpp_independent}
*/
std::vector<a_double> independent(const std::vector<double>& x)
{   using CppAD::AD;
    size_t n = x.size();
    CppAD::vector< AD<double> > ax(n);
    for(size_t j = 0; j < n; j++)
        ax[j] = x[j];
    CppAD::Independent(ax);
    std::vector<a_double> result(n);
    // use a_double( *AD<double> ) constructor in this assignment loop
    for(size_t j = 0; j < n; j++)
        result[j] =  &ax[j] ;
    return result;
}
// BEGIN_A_BOTH_INDEPENDENT_SOURCE
std::vector<a_double> independent(
    const std::vector<double>& x       ,
    const std::vector<double>& dynamic )
{   using CppAD::AD;
    size_t nx = x.size();
    size_t nd = dynamic.size();
    CppAD::vector< AD<double> > ax(nx), adynamic(nd);
    for(size_t j = 0; j < nx; j++)
        ax[j] = x[j];
    for(size_t j = 0; j < nd; j++)
        adynamic[j] = dynamic[j];
    size_t abort_op_index = 0;
    size_t record_compare = false;
    CppAD::Independent(ax, abort_op_index, record_compare, adynamic);
    std::vector<a_double> a_both(nx + nd);
    // use a_double( *AD<double> ) constructor in these assignment loops
    for(size_t j = 0; j < nx; j++)
        a_both[j] =  &ax[j] ;
    for(size_t j = 0; j < nd; j++)
        a_both[nx + j] =  &adynamic[j] ;
    return a_both;
}
// END_A_BOTH_INDEPENDENT_SOURCE
/*
-------------------------------------------------------------------------------
{xrst_begin cpp_abort_recording}

{xrst_spell
    cppad
}

Abort Recording
###############

Syntax
******
``cppad_py::abort_recording`` ()

Purpose
*******
This aborts the current recording (if it exists)
started by the most recent call to :ref:`independent<cpp_independent>`.

{xrst_toc_hidden
    example/cplusplus/fun_abort_xam.cpp
}
Example
*******
:ref:`c++<fun_abort_xam_cpp>`.

{xrst_end cpp_abort_recording}
*/
void abort_recording(void)
{   CppAD::AD<double>::abort_recording();
}
/*
-------------------------------------------------------------------------------
{xrst_begin cpp_fun_ctor}

{xrst_spell
    af
    cppad
}

Stop Current Recording and Store Function Object
################################################

Syntax
******

d_fun
=====

| *f* =  ``cppad_py::d_fun`` ( *ax* , *ay* )

a_fun
=====

| *af* =  ``cppad_py::a_fun`` ( *f* )

ax
**
This argument has prototype

| |tab| ``const vec_a_double&`` *ax*

and must be the same as
:ref:`ax<cpp_independent@ax>`
returned by the previous call to ``independent`` ; i.e.,
it must be the independent variable vector.
We use the notation *n* = *ax*\ ``.size`` ()
to denote the number of independent variables.

ay
**
This argument has prototype

| |tab| ``const vec_a_double&`` *ax*

It specifies the dependent variables.
We use the notation *m* = *ay*\ ``.size`` ()
to denote the number of dependent variables.

f
*
This result has prototype

| |tab| ``cppad_py::d_fun`` *f*

It has a representation for the floating point operations
that mapped the independent variables *ax*
to the dependent variables *ay* .
This object computes function and derivative values using ``double`` .

Empty Function
==============
In the case where *ax* and *ay* have size zero,
the function is 'empty' and all its sizes are zero; see
:ref:`cpp_fun_property`.

af
**
This result has prototype

| |tab| ``cppad_py::a_fun`` *af*

It has a representation of the same function as *f* .
This object computes function and derivative values using ``a_double`` .
Initially, there are not Taylor coefficient stored in *af* ; i.e.,
:ref:`af_size_order()<cpp_fun_property@size_order>` is zero.

Example
*******
All of the examples use these constructors.

{xrst_end cpp_fun_ctor}
*/
// d_fun(ax, ay)
d_fun::d_fun(
    const std::vector<a_double>& ax ,
    const std::vector<a_double>& ay )
{   ptr_ = new CppAD::ADFun<double>();
    size_t n = ax.size();
    size_t m = ay.size();
    CPPAD_PY_ASSERT_UNKNOWN(
        ( (n == 0 ) && (m == 0) ) || ( (n != 0) && (m != 0) )
    );
    // check for default constructor
    if( n == 0 )
        return;

    // copy and convert from Swig vector to Cppad vectors
    CppAD::vector< CppAD::AD<double> > ax_copy(n), ay_copy(m);
    for(size_t j = 0; j < n; j++)
        ax_copy[j] = *( ax[j].ptr() );
    for(size_t i = 0; i < m; i++)
        ay_copy[i] = *( ay[i].ptr() );
    // store the recording
    ptr_->Dependent(ax_copy, ay_copy);
}
// destructor
d_fun::~d_fun(void)
{   // desructor should not throw exception
    assert( ptr_ != CPPAD_NULL );
    delete ptr_;
    ptr_ = CPPAD_NULL;
}
// --------------------------------------------------------------------------
// constructor
a_fun::a_fun(const d_fun& f)
{   a_ptr_ = new CppAD::ADFun< CppAD::AD<double>, double>();
    CPPAD_PY_ASSERT_UNKNOWN( a_ptr_ != CPPAD_NULL );
    *a_ptr_ = f.ptr_->base2ad();
}
// destructor
a_fun::~a_fun(void)
{   // desructor should not throw exception
    assert( a_ptr_ != CPPAD_NULL );
    delete a_ptr_;
    a_ptr_ = CPPAD_NULL;
}
/*
------------------------------------------------------------------------------
{xrst_begin cpp_fun_property}

{xrst_spell
    af
}

Properties of a Function Object
###############################

Syntax
******

| ``a_fun`` *f* ( *f* )
| *n* = *f*\ ``.size_domain`` ()
| *m* = *f*\ ``.size_range`` ()
| *v* = *f*\ ``.size_var`` ()
| *p* = *f*\ ``.size_op`` ()
| *q* = *f*\ ``.size_order`` ()

f
*
This is either a
:ref:`d_fun<cpp_fun_ctor@syntax@d_fun>` or
:ref:`a_fun<cpp_fun_ctor@syntax@a_fun>` function object
and is ``const`` .

size_domain
***********
The return value has prototype

| |tab| ``int`` *n*

and is the size of the vector
:ref:`ax<cpp_fun_ctor@ax>` in the function constructor; i.e.,
the number of independent variables.

size_range
**********
The return value has prototype

| |tab| ``int`` *m*

and is the size of the vector
:ref:`ay<cpp_fun_ctor@ay>` in the function constructor; i.e.,
the number of dependent variables.

size_var
********
The return value has prototype

| |tab| ``int`` *v*

and is the number of variables in the function.
This includes the independent variables, dependent variables,
and any variables that are used to compute the dependent variables
from the independent variables.

size_op
*******
The return value has prototype

| |tab| ``int`` *p*

and is the number of atomic operations that are used to express
the dependent variables as a function of the independent variables.

size_order
**********
The return value has prototype

| |tab| ``int`` *q*

and is the number of Taylor coefficients currently stored in *f* ,
for every variable in the operation sequence corresponding to *f* .
These coefficients are computed by :ref:`cpp_fun_forward`.
This is different from the other function properties in that it can change
after each call to *f*\ ``.forward`` ; see
:ref:`size_order<cpp_fun_forward@p@size_order>` in the forward mode section.
The initial value for this property, when the object *f*
or *af* is created, is zero.

{xrst_toc_hidden
    example/cplusplus/fun_property_xam.cpp
}
Example
*******
:ref:`fun_property_xam_cpp`

{xrst_end cpp_fun_property}
*/
// size_domain
int d_fun::size_domain(void) const
{   return ptr_->Domain(); }
int a_fun::size_domain(void) const
{   return a_ptr_->Domain(); }
//
// size_range
int d_fun::size_range(void) const
{   return ptr_->Range(); }
int a_fun::size_range(void) const
{   return a_ptr_->Range(); }
//
// size_var
int d_fun::size_var(void) const
{   return ptr_->size_var(); }
int a_fun::size_var(void) const
{   return a_ptr_->size_var(); }
//
// size_op
int d_fun::size_op(void) const
{   return ptr_->size_op(); }
int a_fun::size_op(void) const
{   return a_ptr_->size_op(); }
//
// size_order
int d_fun::size_order(void) const
{   return ptr_->size_order(); }
int a_fun::size_order(void) const
{   return a_ptr_->size_order(); }
/*
------------------------------------------------------------------------------
{xrst_begin cpp_fun_new_dynamic}

Change The Dynamic Parameters
#############################

Syntax
******

| *f*\ ``.new_dynamic`` ( *dynamic* )

f
*
This is either a
:ref:`d_fun<cpp_fun_ctor@syntax@d_fun>` or
:ref:`a_fun<cpp_fun_ctor@syntax@a_fun>` function object.

dynamic
*******
If *f* is a ``d_fun`` or ``a_fun`` ,
this argument has prototype

| |tab| ``const vec_double&`` *dynamic*
| |tab| ``const vec_a_double&`` *dynamic*

and its size must be the same as the size of
:ref:`dynamic<cpp_independent@dynamic>` in the corresponding call to
``independent`` .
It specifies new values for the dynamic parameters in *f* .

size_order
**********
After this call
:ref:`f_size_order()<cpp_fun_property@size_order>` is zero.

Example
*******
See :ref:`fun_dynamic_xam_cpp`.
{xrst_end cpp_fun_new_dynamic}
*/
// BEGIN_NEW_DYNAMIC_SOURCE
void d_fun::new_dynamic(const std::vector<double>& dynamic)
{   CPPAD_PY_ASSERT_KNOWN(
        dynamic.size() == ptr_->size_dyn_ind() ,
        "cppad_py::d_fun::new_dynamic dynamic.size() error"
    );
    ptr_->new_dynamic(dynamic);
    return;
}
void a_fun::new_dynamic(const std::vector<a_double>& adynamic)
{   CPPAD_PY_ASSERT_KNOWN(
        adynamic.size() == a_ptr_->size_dyn_ind() ,
        "cppad_py::a_fun::new_dynamic adynamic.size() error"
    );
    CppAD::vector< CppAD::AD<double> > au = ad_vec_std2cppad(adynamic);
    a_ptr_->new_dynamic(au);
    return;
}
// END_NEW_DYNAMIC_SOURCE

/*
------------------------------------------------------------------------------
{xrst_begin cpp_fun_jacobian}

{xrst_spell
}

Jacobian of an AD Function
##########################

Syntax
******
*J* = *f*\ ``.jacobian`` ( *x* )

f
*
This is either a
:ref:`d_fun<cpp_fun_ctor@syntax@d_fun>` or
:ref:`a_fun<cpp_fun_ctor@syntax@a_fun>` function object.
Upon return, the zero order
:ref:`taylor_coefficients<cpp_fun_forward@taylor_coefficient>` in *f*
correspond to the value of *x* .
The other Taylor coefficients in *f* are unspecified.

f(x)
****
We use the notation :math:`f: \B{R}^n \rightarrow \B{R}^m`
for the function corresponding to *f* .
Note that *n* is the size of :ref:`ax<cpp_fun_ctor@ax>`
and *m* is the size of :ref:`ay<cpp_fun_ctor@ay>`
in to the constructor for *f* .

x
*
If *f* is a ``d_fun`` or ``a_fun`` ,
this argument has prototype

| |tab| ``const vec_double&`` *x*
| |tab| ``const vec_a_double&`` *x*

and its size must be *n* .
It specifies the argument value at we are computing the Jacobian
:math:`f'(x)`.

J
*
If *f* is a ``d_fun`` or ``a_fun`` ,
the result has prototype

| |tab| ``vec_double`` *J*
| |tab| ``vec_a_double`` *J*

respectively and its size is *m* ``*`` *n* .
For *i* between zero and *m* -1
and *j* between zero and *n* -1 ,

.. math::

    J [ i * n + j ] = \frac{ \partial f_i }{ \partial x_j } (x)

{xrst_toc_hidden
    example/cplusplus/fun_jacobian_xam.cpp
}
Example
*******
:ref:`fun_jacobian_xam_cpp`

{xrst_end cpp_fun_jacobian}
*/
std::vector<double> d_fun::jacobian(const std::vector<double>& x)
{   CPPAD_PY_ASSERT_KNOWN(
        x.size() == ptr_->Domain() ,
        "cppad_py::d_fun::jacobian x.size() error"
    );
    return ptr_->Jacobian(x);
}
std::vector<a_double> a_fun::jacobian(const std::vector<a_double>& ax)
{   CPPAD_PY_ASSERT_KNOWN(
        ax.size() == a_ptr_->Domain() ,
        "cppad_py::a_fun::jacobian ax.size() error"
    );
    CppAD::vector< CppAD::AD<double> > au = ad_vec_std2cppad(ax);
    CppAD::vector< CppAD::AD<double> > av = a_ptr_->Jacobian(au);
    return ad_vec_cppad2std(av);
}
/*
------------------------------------------------------------------------------
{xrst_begin cpp_fun_hessian}

{xrst_spell
}

Hessian of an AD Function
#########################

Syntax
******
*H* = *f*\ ``.hessian`` ( *x* , *w* )

f
*
This is either a
:ref:`d_fun<cpp_fun_ctor@syntax@d_fun>` or
:ref:`a_fun<cpp_fun_ctor@syntax@a_fun>` function object.
Upon return, the zero order
:ref:`taylor_coefficients<cpp_fun_forward@taylor_coefficient>` in *f*
correspond to the value of *x* .
The other Taylor coefficients in *f* are unspecified.

f(x)
****
We use the notation :math:`f: \B{R}^n \rightarrow \B{R}^m`
for the function corresponding to *f* .
Note that *n* is the size of :ref:`ax<cpp_fun_ctor@ax>`
and *m* is the size of :ref:`ay<cpp_fun_ctor@ay>`
in to the constructor for *f* .

g(x)
****
We use the notation :math:`g: \B{R}^n \rightarrow \B{R}`
for the function defined by

.. math::

    g(x) = \sum_{i=0}^{n-1} w_i f_i (x)

x
*
If *f* is a ``d_fun`` or ``a_fun`` ,
this argument has prototype

| |tab| ``const vec_double&`` *x*
| |tab| ``const vec_a_double&`` *x*

and its size must be *n* .
It specifies the argument value at we are computing the Hessian
:math:`g^{(2)}(x)`.

w
*
If *f* is a ``d_fun`` or ``a_fun`` ,
this argument has prototype

| |tab| ``const vec_double&`` *w*
| |tab| ``const vec_a_double&`` *w*

and its size must be *m* .
It specifies the vector *w* in the definition of :math:`g(x)` above.

H
*
If *f* is a ``d_fun`` or ``a_fun`` ,
the result has prototype

| |tab| ``vec_double`` *H*
| |tab| ``vec_a_double`` *H*

and its size is *n* ``*`` *n* .
For *i* between zero and *n* -1
and *j* between zero and *n* -1 ,

.. math::

    H [ i * n + j ] = \frac{ \partial^2 g }{ \partial x_i \partial x_j } (x)

{xrst_toc_hidden
    example/cplusplus/fun_hessian_xam.cpp
}
Example
*******
:ref:`fun_hessian_xam_cpp`

{xrst_end cpp_fun_hessian}
*/
std::vector<double> d_fun::hessian(
    const std::vector<double>& x  ,
    const std::vector<double>& w  )
{   CPPAD_PY_ASSERT_KNOWN(
        x.size() == ptr_->Domain() ,
        "cppad_py::d_fun::hessian:: x.size() error"
    );
    CPPAD_PY_ASSERT_KNOWN(
        w.size() == ptr_->Range() ,
        "cppad_py::d_fun::hessian:: w.size() error"
    );
    return ptr_->Hessian(x, w);
}
std::vector<a_double> a_fun::hessian(
    const std::vector<a_double>& ax  ,
    const std::vector<a_double>& aw  )
{   CPPAD_PY_ASSERT_KNOWN(
        ax.size() == a_ptr_->Domain() ,
        "cppad_py::d_fun::hessian:: x.size() error"
    );
    CPPAD_PY_ASSERT_KNOWN(
        aw.size() == a_ptr_->Range() ,
        "cppad_py::d_fun::hessian:: w.size() error"
    );
    //
    CppAD::vector< CppAD::AD<double> > au = ad_vec_std2cppad(ax);
    CppAD::vector< CppAD::AD<double> > av = ad_vec_std2cppad(aw);
    CppAD::vector< CppAD::AD<double> > az = a_ptr_->Hessian(au, av);
    return ad_vec_cppad2std(az);
}
/*
------------------------------------------------------------------------------
{xrst_begin cpp_fun_forward}

{xrst_spell
    xp
    yp
}

Forward Mode AD
###############

Syntax
******
*yp* = *f*\ ``.forward`` ( *p* , *xp* )

Taylor Coefficient
******************
For a function :math:`g(t)` of a scalar argument :math:`t \in \B{R}`,
the *p*-th order Taylor coefficient is its
``p`` -th order derivative divided by *p* factorial
and evaluated at :math:`t = 0`; i.e.,

.. math::

    g^{(p)} (0) /  p !

f
*
This is either a
:ref:`d_fun<cpp_fun_ctor@syntax@d_fun>` or
:ref:`a_fun<cpp_fun_ctor@syntax@a_fun>` function object.
Note that its state is changed by this operation because
all the Taylor coefficient that it calculates for every
variable in recording are stored.
See more discussion of this fact under the heading
:ref:`p<cpp_fun_forward@p>` below.

f(x)
****
We use the notation :math:`f: \B{R}^n \rightarrow \B{R}^m`
for the function corresponding to *f* .
Note that *n* is the size of :ref:`ax<cpp_fun_ctor@ax>`
and *m* is the size of :ref:`ay<cpp_fun_ctor@ay>`
in to the constructor for *f* .

X(t)
****
We use the notation :math:`X : \B{R} \rightarrow \B{R}^n`
for a function that the calling routine chooses.

Y(t)
****
We define the function :math:`Y : \B{R} \rightarrow \B{R}^n`
by :math:`Y(t) = f(X(t))`.

p
*
This argument has prototype

| |tab| ``int`` *p*

and is non-negative.
It is the order of the Taylor coefficient being calculated.
If there was no call to ``forward`` for this *f* ,
the value of *p* must be zero.
Otherwise, it must be between zero and one greater that its
value for the previous call using this *f* .
After this call, the Taylor coefficients for orders zero though *p* ,
and for every variable in the recording, will be stored in *f* .

size_order
==========
After this call,
:ref:`f_size_order()<cpp_fun_property@size_order>` is *p* +1 .

xp
**
If *f* is a ``d_fun`` or ``a_fun`` ,
this argument has prototype

| |tab| ``const vec_double&`` *xp*
| |tab| ``const vec_a_double&`` *xp*

respectively and its size must be *n* .
It specifies the *p*-th order Taylor coefficients for *X(t* ) .

yp
**
If *f* is a ``d_fun`` or ``a_fun`` ,
the result has prototype

| |tab| ``vec_double&`` *yp*
| |tab| ``vec_a_double&`` *yp*

respectively and its size is *m* .
It is the *p*-th order Taylor coefficients for :math:`Y(t)`.

{xrst_toc_hidden
    example/cplusplus/fun_forward_xam.cpp
}
Example
*******
:ref:`fun_forward_xam_cpp`

{xrst_end cpp_fun_forward}
*/
std::vector<double> d_fun::forward(int p, const std::vector<double>& xp)
{   CPPAD_PY_ASSERT_KNOWN(
        xp.size() == ptr_->Domain() ,
        "cppad_py::d_fun::forward xp.size() error"
    );
    return ptr_->Forward(p, xp);
}
std::vector<a_double> a_fun::forward(int p, const std::vector<a_double>& axp)
{   CPPAD_PY_ASSERT_KNOWN(
        axp.size() == a_ptr_->Domain() ,
        "cppad_py::a_fun::forward axp.size() error"
    );
    CppAD::vector< CppAD::AD<double> > aup = ad_vec_std2cppad(axp);
    CppAD::vector< CppAD::AD<double> > avp =  a_ptr_->Forward(p, aup);
    return ad_vec_cppad2std(avp);
}
/*
-------------------------------------------------------------------------------
{xrst_begin cpp_fun_reverse}

{xrst_spell
    xq
    yq
}

Reverse Mode AD
###############

Syntax
******
*xq* = *f*\ ``.reverse`` ( *q* , *yq* )

f
*
This is either a
:ref:`d_fun<cpp_fun_ctor@syntax@d_fun>` or
:ref:`a_fun<cpp_fun_ctor@syntax@a_fun>` function object
and is effectively ``const`` .
(Some details that are not visible to the user may change.)

Notation
********

f(x)
====
We use the notation :math:`f: \B{R}^n \rightarrow \B{R}^m`
for the function corresponding to *f* .
Note that *n* is the size of :ref:`ax<cpp_fun_ctor@ax>`
and *m* is the size of :ref:`ay<cpp_fun_ctor@ay>`
in to the constructor for *f* .

X(t), S
=======
This is the same function as
:ref:`x(t)<cpp_fun_forward@x(t)>` in the previous call to
*f*\ ``.forward`` .
We use :math:`S \in \B{R}^{n \times q}` to denote the Taylor coefficients
of :math:`X(t)`.

Y(t), T
=======
This is the same function as
:ref:`y(t)<cpp_fun_forward@y(t)>` in the previous call to
*f*\ ``.forward`` .
We use :math:`T \in \B{R}^{m \times q}` to denote the Taylor coefficients
of :math:`Y(t)`.
We also use the notation :math:`T(S)` to express the fact that
the Taylor coefficients for :math:`Y(t)` are a function of the
Taylor coefficients of :math:`X(t)`.

G(T)
====
We use the notation :math:`G : \B{R}^{m \times p} \rightarrow \B{R}`
for a function that the calling routine chooses.

q
*
This argument has prototype

| |tab| ``int`` *q*

and is positive.
It is the number of the Taylor coefficient (for each variable)
that we are computing the derivative with respect to.
It must be greater than zero, and
less than or equal
the number of Taylor coefficient stored in *f* ; i.e.,
:ref:`f_size_order()<cpp_fun_property@size_order>`.

yq
**
If *f* is a ``d_fun`` or ``a_fun`` ,
this argument has prototype

| |tab| ``const vec_double&`` *yq*
| |tab| ``const vec_a_double&`` *yq*

and its size must be *m* ``*`` *q* .
For 0 <= *i* < *m* and 0 <= *k* < *q* ,
*yq* [ *i* ``*`` *q* + *k* ] is the partial derivative of
:math:`G(T)` with respect to the *k*-th order Taylor coefficient
for the *i*-th component function; i.e.,
the partial derivative of :math:`G(T)` w.r.t. :math:`Y_i^{(k)} (t) / k !`.

xq
**
If *f* is a ``d_fun`` or ``a_fun`` ,
the result has prototype

| |tab| ``const vec_double&`` *xq*
| |tab| ``const vec_a_double&`` *xq*

respectively and its size is *n* ``*`` *q* .
For 0 <= *j* < *n* and 0 <= *k* < *q* ,
*xq* [ *j* ``*`` *q* + *k* ] is the partial derivative of
:math:`G(T(S))` with respect to the *k*-th order Taylor coefficient
for the *j*-th component function; i.e.,
the partial derivative of
:math:`G(T(S))` w.r.t. :math:`S_j^{(k)} (t) / k !`.

{xrst_toc_hidden
    example/cplusplus/fun_reverse_xam.cpp
}
Example
*******
:ref:`fun_reverse_xam_cpp`

{xrst_end cpp_fun_reverse}
*/
std::vector<double> d_fun::reverse(int q, const std::vector<double>& yq)
{   CPPAD_PY_ASSERT_KNOWN(
        yq.size() == q * ptr_->Range() ,
        "cppad_py::d_fun::reverse yq.size() error"
    );
    return ptr_->Reverse(q, yq);
}
std::vector<a_double> a_fun::reverse(int q, const std::vector<a_double>& ayq)
{   CPPAD_PY_ASSERT_KNOWN(
        ayq.size() == q * a_ptr_->Range() ,
        "cppad_py::a_fun::reverse yq.size() error"
    );
    CppAD::vector< CppAD::AD<double> > avq = ad_vec_std2cppad(ayq);
    CppAD::vector< CppAD::AD<double> > auq =  a_ptr_->Reverse(q, avq);
    return ad_vec_cppad2std(auq);
}
/*
------------------------------------------------------------------------------
{xrst_begin cpp_fun_optimize}

{xrst_spell
}

Optimize an AD Function
#######################

Syntax
******
*f*\ ``.optimize`` ()

Purpose
*******
This reduces the number of operations
(hence to time and memory) used to compute the function
stored in *f*
On the other hand, the optimization may take a significant amount
of time and memory.

f
*
This object is a
:ref:`d_fun<cpp_fun_ctor@syntax@d_fun>`.
Optimizing this *f* also optimizes the
corresponding :ref:`a_fun<cpp_fun_ctor@syntax@a_fun>`.

{xrst_toc_hidden
    example/cplusplus/fun_optimize_xam.cpp
}
Example
*******
:ref:`fun_optimize_xam_cpp`

{xrst_end cpp_fun_optimize}
*/
void d_fun::optimize(void)
{   ptr_->optimize(); }
/*
----------------------------------------------------------------------------
{xrst_begin cpp_fun_json}

{xrst_spell
    json
}

Json Representation of AD Computational Graph
#############################################

Syntax
******

| *json* = *f*\ ``.to_json`` ()
| *f*\ ``.from_json`` ()

f
*
This is a :ref:`d_fun<cpp_fun_ctor@syntax@d_fun>` object.

json
****
is a Json representation of the computation graph corresponding to
*f* ; see the CppAD documentation for
`json_ad_graph <https://coin-or.github.io/CppAD/doc/json_ad_graph.htm>`_.

to_json
*******
In this case, the function object *f* is ``const`` and
the return value *json* has prototype

| |tab| ``std::string`` *json*

from_json
*********
In this case, *json* has prototype

| |tab| ``const std::string&`` *json*

and the function *f* so it corresponds to *json* .

{xrst_toc_hidden
    example/cplusplus/fun_json_xam.cpp
}
Examples
********
:ref:`fun_to_json_xam_cpp`,
:ref:`fun_from_json_xam_cpp`.

{xrst_end cpp_fun_json}
*/
// to_json
std::string d_fun::to_json(void) const
{   return ptr_->to_json(); }
void d_fun::from_json(const std::string& json)
{   return ptr_->from_json(json); }
/*
----------------------------------------------------------------------------
{xrst_begin cpp_check_for_nan}

Check For Nan In Function or Derivative Results
###############################################

Syntax
******

| *f*\ ``.check_for_nan``\ ( *b* )

f
*
is a
:ref:`d_fun<cpp_fun_ctor@syntax@d_fun>` function object.

b
*
This argument has prototype

| |tab| ``int`` *b*

If *b* is true and
:ref:`get_cppad_sh@settings@build_type` is ``debug`` ,
*f* will generate an assert when ``nan`` occurs in its function
or derivative values.
Otherwise, it will just pass back the ``nan`` values.

Example
*******
{xrst_toc_list
    example/cplusplus/fun_check_for_nan_xam.cpp
}

{xrst_end cpp_check_for_nan}
*/
void d_fun::check_for_nan(bool b)
{   ptr_->check_for_nan(b);
}

} // END_CPPAD_PY_NAMESPACE
