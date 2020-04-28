/* -----------------------------------------------------------------------------
           cppad_py: A C++ Object Library and Python Interface to Cppad
            Copyright (C) 2017-20 Bradley M. Bell (bradbell@seanet.com)
                This program is distributed under the terms of the
                GNU General Public License version 3.0 or later see
                      https://www.gnu.org/licenses/gpl-3.0.txt
----------------------------------------------------------------------------- */
# include <cppad/cppad.hpp>
# include <cppad/py/fun.hpp>
# include <cppad/py/error.hpp>
# include <cppad/py/cppad_vec.hpp>

namespace cppad_py { // BEGIN_CPPAD_PY_NAMESPACE

/*
-------------------------------------------------------------------------------
$begin cpp_independent$$
$spell
	vec
	const
	cppad_py
	nx
	nd
$$

$section Declare Independent Variables and Start Recording$$

$head Syntax$$
$icode%ax% = cppad_py::independent(%x%)
%$$
$icode%a_both% = cppad_py::independent(%x%, %dynamic%)
%$$

$head Purpose$$
This starts recording $cref a_double$$ operations.
This recording is terminated, and the information is stored,
by calling the $cref/d_fun constructor/cpp_fun_ctor/$$.
It can be terminated, and the information is lost,
by calling $cref/abort_recording/cpp_abort_recording/$$.

$head x$$
This argument has prototype
$codei%
	const vec_double& %x%
%$$
Its specifies the number of independent variables
and their values during the recording.
We use the notation $icode%nx% = %x%.size()%$$
to denote the number of independent variables.

$head dynamic$$
This argument has prototype
$codei%
	const vec_double& %dynamic%
%$$
Its specifies the number of independent dynamic parameters
and their values during the recording.
We use the notation $icode%nd% = %dynamic%.size()%$$
to denote the number of independent variables.

$head ax$$
This result has prototype
$codei%
	vec_a_double& %ax%
%$$
and is the vector of independent variables.
It has size $icode nx$$ and for
$icode%i% = 0%$$ to $icode%n%-1%$$
$codei%
	%ax%[%i%] == %x%[%i%]
%$$

$head a_both$$
this result has prototype
$codei%
	vec_a_double& %a_both%
%$$
and is the vector of both the independent variables
and independent dynamic parameters.
It has size $icode%nx% + %nd%$$.
For $icode%i% = 0%$$ to $icode%nx%-1%$$
$codei%
	%a_both%[%i%] == %x%[%i%]
%$$
is the $th i$$ independent variable.
For $icode%i% = 0%$$ to $icode%nd%-1%$$
$codei%
	%a_both%[%nx% + %i%] == %dynamic%[%i%]
%$$
is the $th i$$ independent dynamic parameter.

$children%
	example/cplusplus/fun_dynamic_xam.cpp
%$$
$head Example$$
Most of the c++ $code d_fun$$ examples use the $icode ax$$
return syntax.
The $cref fun_dynamic_xam.cpp$$ example uses the $icode a_both$$
return syntax.

$end
*/
std::vector<a_double> independent(const std::vector<double>& x)
{	using CppAD::AD;
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
{	using CppAD::AD;
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
$begin cpp_abort_recording$$
$spell
	vec
	af
	const
	cppad_py
$$

$section Abort Recording$$

$head Syntax$$
$codei%cppad_py::abort_recording()%$$

$head Purpose$$
This aborts the current recording (if it exists)
started by the most recent call to $cref/independent/cpp_independent/$$.

$children%
	example/cplusplus/fun_abort_xam.cpp
%$$
$head Example$$
$cref/C++/fun_abort_xam.cpp/$$.

$end
*/
void abort_recording(void)
{	CppAD::AD<double>::abort_recording();
}
/*
-------------------------------------------------------------------------------
$begin cpp_fun_ctor$$
$spell
	vec
	af
	const
	cppad_py
	Taylor
$$

$section Stop Current Recording and Store Function Object$$

$head Syntax$$

$subhead d_fun$$
$icode%f% = cppad_py::d_fun(%ax%, %ay%)
%$$

$subhead a_fun$$
$icode%af% = cppad_py::a_fun(%f%)
%$$

$head ax$$
This argument has prototype
$codei%
	const vec_a_double& %ax%
%$$
and must be the same as
$cref/ax/cpp_independent/ax/$$
returned by the previous call to $code independent$$; i.e.,
it must be the independent variable vector.
We use the notation $icode%n% = %ax%.size()%$$
to denote the number of independent variables.

$head ay$$
This argument has prototype
$codei%
	const vec_a_double& %ax%
%$$
It specifies the dependent variables.
We use the notation $icode%m% = %ay%.size()%$$
to denote the number of dependent variables.

$head f$$
This result has prototype
$codei%
	cppad_py::d_fun %f%
%$$
It has a representation for the floating point operations
that mapped the independent variables to the dependent variables.
This object computes function and derivative values using $code double$$.

$head af$$
This result has prototype
$codei%
	cppad_py::a_fun %af%
%$$
It has a representation of the same function as $icode f$$.
This object computes function and derivative values using $code a_double$$.
Initially, there are not Taylor coefficient stored in $icode af$$; i.e.,
$cref/af.size_order()/cpp_fun_property/size_order/$$ is zero.

$head Example$$
All of the examples use these constructors.

$end
*/
// d_fun(void) (not yet documented or tested)
d_fun::d_fun(void)
{	ptr_ = new CppAD::ADFun<double>();
	CPPAD_PY_ASSERT_UNKNOWN( ptr_ != CPPAD_NULL );
}
// destructor
d_fun::~d_fun(void)
{	CPPAD_PY_ASSERT_UNKNOWN( ptr_ != CPPAD_NULL );
	delete ptr_;
}
// d_fun(ax, ay)
d_fun::d_fun(
	const std::vector<a_double>& ax ,
	const std::vector<a_double>& ay )
{	ptr_ = new CppAD::ADFun<double>();
	size_t n = ax.size();
	size_t m = ay.size();
	// copy and convert from Swig vector to Cppad vectors
	std::vector< CppAD::AD<double> > ax_copy(n), ay_copy(m);
	for(size_t j = 0; j < n; j++)
		ax_copy[j] = *( ax[j].ptr() );
	for(size_t i = 0; i < m; i++)
		ay_copy[i] = *( ay[i].ptr() );
	// store the recording
	ptr_->Dependent(ax_copy, ay_copy);
}
// --------------------------------------------------------------------------
// constructor
a_fun::a_fun(const d_fun& f)
{	a_ptr_ = new CppAD::ADFun< CppAD::AD<double>, double>();
	CPPAD_PY_ASSERT_UNKNOWN( a_ptr_ != CPPAD_NULL );
	*a_ptr_ = f.ptr_->base2ad();
}
// destructor
a_fun::~a_fun(void)
{	CPPAD_PY_ASSERT_UNKNOWN( a_ptr_ != CPPAD_NULL );
	delete a_ptr_;
}
/*
------------------------------------------------------------------------------
$begin cpp_fun_property$$
$spell
	vec
	af
	var
	op
	const
	Taylor
$$

$section Properties of a Function Object$$

$head Syntax$$
$codei%a_fun %f%(%f%)
%$$
$icode%n% = %f%.size_domain()
%$$
$icode%m% = %f%.size_range()
%$$
$icode%v% = %f%.size_var()
%$$
$icode%p% = %f%.size_op()
%$$
$icode%q% = %f%.size_order()
%$$

$head f$$
This is either a
$cref/d_fun/cpp_fun_ctor/Syntax/d_fun/$$ or
$cref/a_fun/cpp_fun_ctor/Syntax/a_fun/$$ function object
and is $code const$$.

$head size_domain$$
The return value has prototype
$codei%
	int %n%
%$$
and is the size of the vector
$cref/ax/cpp_fun_ctor/ax/$$ in the function constructor; i.e.,
the number of independent variables.

$head size_range$$
The return value has prototype
$codei%
	int %m%
%$$
and is the size of the vector
$cref/ay/cpp_fun_ctor/ay/$$ in the function constructor; i.e.,
the number of dependent variables.

$head size_var$$
The return value has prototype
$codei%
	int %v%
%$$
and is the number of variables in the function.
This includes the independent variables, dependent variables,
and any variables that are used to compute the dependent variables
from the independent variables.

$head size_op$$
The return value has prototype
$codei%
	int %p%
%$$
and is the number of atomic operations that are used to express
the dependent variables as a function of the independent variables.

$head size_order$$
The return value has prototype
$codei%
	int %q%
%$$
and is the number of Taylor coefficients currently stored in $icode f$$,
for every variable in the operation sequence corresponding to $icode f$$.
These coefficients are computed by $cref cpp_fun_forward$$.
This is different from the other function properties in that it can change
after each call to $icode%f%.forward%$$; see
$cref/size_order/cpp_fun_forward/p/size_order/$$ in the forward mode section.
The initial value for this property, when the object $icode f$$
or $icode af$$ is created, is zero.

$children%
	example/cplusplus/fun_property_xam.cpp
%$$
$head Example$$
$cref fun_property_xam.cpp$$

$end
*/
// size_domain
int d_fun::size_domain(void) const
{	return ptr_->Domain(); }
int a_fun::size_domain(void) const
{	return a_ptr_->Domain(); }
//
// size_range
int d_fun::size_range(void) const
{	return ptr_->Range(); }
int a_fun::size_range(void) const
{	return a_ptr_->Range(); }
//
// size_var
int d_fun::size_var(void) const
{	return ptr_->size_var(); }
int a_fun::size_var(void) const
{	return a_ptr_->size_var(); }
//
// size_op
int d_fun::size_op(void) const
{	return ptr_->size_op(); }
int a_fun::size_op(void) const
{	return a_ptr_->size_op(); }
//
// size_order
int d_fun::size_order(void) const
{	return ptr_->size_order(); }
int a_fun::size_order(void) const
{	return a_ptr_->size_order(); }
/*
------------------------------------------------------------------------------
$begin cpp_fun_new_dynamic$$
$spell
	const
	vec
$$

$section Change The Dynamic Parameters$$

$head Syntax$$
$icode%f%.new_dynamic(%dynamic%)
%$$

$head f$$
This is either a
$cref/d_fun/cpp_fun_ctor/Syntax/d_fun/$$ or
$cref/a_fun/cpp_fun_ctor/Syntax/a_fun/$$ function object.

$head dynamic$$
If $icode f$$ is a $code d_fun$$ or $code a_fun$$,
this argument has prototype
$codei%
	const vec_double&   %dynamic%
	const vec_a_double& %dynamic%
%$$
and its size must be the same as the size of
$cref/dynamic/cpp_independent/dynamic/$$ in the corresponding call to
$code independent$$.
It specifies new values for the dynamic parameters in $icode f$$.

$head size_order$$
After this call
$cref/f.size_order()/cpp_fun_property/size_order/$$ is zero.

$head Example$$
See $cref fun_dynamic_xam.cpp$$.
$end
*/
// BEGIN_NEW_DYNAMIC_SOURCE
void d_fun::new_dynamic(const std::vector<double>& dynamic)
{	if( dynamic.size() != ptr_->size_dyn_ind() )
		error_message("cppad_py::d_fun::new_dynamic dynamic.size() error");
	ptr_->new_dynamic(dynamic);
	return;
}
void a_fun::new_dynamic(const std::vector<a_double>& adynamic)
{	if( adynamic.size() != a_ptr_->size_dyn_ind() )
		error_message("cppad_py::a_fun::jacobian adynamic.size() error");
	std::vector< CppAD::AD<double> > au = vec2cppad_double(adynamic);
	a_ptr_->new_dynamic(au);
	return;
}
// END_NEW_DYNAMIC_SOURCE

/*
------------------------------------------------------------------------------
$begin cpp_fun_jacobian$$
$spell
	vec
	af
	Taylor
	const
	Jacobian
$$

$section Jacobian of an AD Function$$
$spell
	vec
$$

$head Syntax$$
$icode%J% = %f%.jacobian(%x%)%$$

$head f$$
This is either a
$cref/d_fun/cpp_fun_ctor/Syntax/d_fun/$$ or
$cref/a_fun/cpp_fun_ctor/Syntax/a_fun/$$ function object.
Upon return, the zero order
$cref/Taylor coefficients/cpp_fun_forward/Taylor Coefficient/$$ in $icode f$$
correspond to the value of $icode x$$.
The other Taylor coefficients in $icode f$$ are unspecified.

$head f(x)$$
We use the notation $latex f: \B{R}^n \rightarrow \B{R}^m$$
for the function corresponding to $icode f$$.
Note that $icode n$$ is the size of $cref/ax/cpp_fun_ctor/ax/$$
and $icode m$$ is the size of $cref/ay/cpp_fun_ctor/ay/$$
in to the constructor for $icode f$$.

$head x$$
If $icode f$$ is a $code d_fun$$ or $code a_fun$$,
this argument has prototype
$codei%
	const vec_double&   %x%
	const vec_a_double& %x%
%$$
and its size must be $icode n$$.
It specifies the argument value at we are computing the Jacobian
$latex f'(x)$$.

$head J$$
If $icode f$$ is a $code d_fun$$ or $code a_fun$$,
the result has prototype
$codei%
	vec_double   %J%
	vec_a_double %J%
%$$
respectively and its size is $icode%m%*%n%$$.
For $icode i$$ between zero and $icode%m%-1%$$
and $icode j$$ between zero and $icode%n%-1%$$,
$latex \[
	J [ i * n + j ] = \frac{ \partial f_i }{ \partial x_j } (x)
\] $$

$children%
	example/cplusplus/fun_jacobian_xam.cpp
%$$
$head Example$$
$cref fun_jacobian_xam.cpp$$


$end
*/
std::vector<double> d_fun::jacobian(const std::vector<double>& x)
{	if( x.size() != ptr_->Domain() )
		error_message("cppad_py::d_fun::jacobian x.size() error");
	return ptr_->Jacobian(x);
}
std::vector<a_double> a_fun::jacobian(const std::vector<a_double>& ax)
{	if( ax.size() != a_ptr_->Domain() )
		error_message("cppad_py::a_fun::jacobian ax.size() error");
	std::vector< CppAD::AD<double> > au = vec2cppad_double(ax);
	std::vector< CppAD::AD<double> > av = a_ptr_->Jacobian(au);
	return vec2a_double(av);
}
/*
------------------------------------------------------------------------------
$begin cpp_fun_hessian$$
$spell
	vec
	af
	Taylor
	const
$$

$section Hessian of an AD Function$$

$head Syntax$$
$icode%H% = %f%.hessian(%x%, %w%)%$$

$head f$$
This is either a
$cref/d_fun/cpp_fun_ctor/Syntax/d_fun/$$ or
$cref/a_fun/cpp_fun_ctor/Syntax/a_fun/$$ function object.
Upon return, the zero order
$cref/Taylor coefficients/cpp_fun_forward/Taylor Coefficient/$$ in $icode f$$
correspond to the value of $icode x$$.
The other Taylor coefficients in $icode f$$ are unspecified.

$head f(x)$$
We use the notation $latex f: \B{R}^n \rightarrow \B{R}^m$$
for the function corresponding to $icode f$$.
Note that $icode n$$ is the size of $cref/ax/cpp_fun_ctor/ax/$$
and $icode m$$ is the size of $cref/ay/cpp_fun_ctor/ay/$$
in to the constructor for $icode f$$.

$head g(x)$$
We use the notation $latex g: \B{R}^n \rightarrow \B{R}$$
for the function defined by
$latex \[
	g(x) = \sum_{i=0}^{n-1} w_i f_i (x)
\] $$

$head x$$
If $icode f$$ is a $code d_fun$$ or $code a_fun$$,
this argument has prototype
$codei%
	const vec_double&   %x%
	const vec_a_double& %x%
%$$
and its size must be $icode n$$.
It specifies the argument value at we are computing the Hessian
$latex g^{(2)}(x)$$.

$head w$$
If $icode f$$ is a $code d_fun$$ or $code a_fun$$,
this argument has prototype
$codei%
	const vec_double&   %w%
	const vec_a_double& %w%
%$$
and its size must be $icode m$$.
It specifies the vector $icode w$$ in the definition of $latex g(x)$$ above.

$head H$$
If $icode f$$ is a $code d_fun$$ or $code a_fun$$,
the result has prototype
$codei%
	vec_double   %H%
	vec_a_double %H%
%$$
and its size is $icode%n%*%n%$$.
For $icode i$$ between zero and $icode%n%-1%$$
and $icode j$$ between zero and $icode%n%-1%$$,
$latex \[
	H [ i * n + j ] = \frac{ \partial^2 g }{ \partial x_i \partial x_j } (x)
\] $$

$children%
	example/cplusplus/fun_hessian_xam.cpp
%$$
$head Example$$
$cref fun_hessian_xam.cpp$$

$end
*/
std::vector<double> d_fun::hessian(
	const std::vector<double>& x  ,
	const std::vector<double>& w  )
{	if( x.size() != ptr_->Domain() )
		error_message("cppad_py::d_fun::hessian:: x.size() error");
	if( w.size() != ptr_->Range() )
		error_message("cppad_py::d_fun::hessian:: w.size() error");
	return ptr_->Hessian(x, w);
}
std::vector<a_double> a_fun::hessian(
	const std::vector<a_double>& ax  ,
	const std::vector<a_double>& aw  )
{	if( ax.size() != a_ptr_->Domain() )
		error_message("cppad_py::d_fun::hessian:: x.size() error");
	if( aw.size() != a_ptr_->Range() )
		error_message("cppad_py::d_fun::hessian:: w.size() error");
	//
	std::vector< CppAD::AD<double> > au = vec2cppad_double(ax);
	std::vector< CppAD::AD<double> > av = vec2cppad_double(aw);
	std::vector< CppAD::AD<double> > az = a_ptr_->Hessian(au, av);
	return vec2a_double(az);
}
/*
------------------------------------------------------------------------------
$begin cpp_fun_forward$$
$spell
	af
	xp
	Taylor
	yp
	const
	vec
$$

$section Forward Mode AD$$

$head Syntax$$
$icode%yp% = %f%.forward(%p%, %xp%)%$$

$head Taylor Coefficient$$
For a function $latex g(t)$$ of a scalar argument $latex t \in \B{R}$$,
the $th p$$ order Taylor coefficient is its
$code p$$-th order derivative divided by $icode p$$ factorial
and evaluated at $latex t = 0$$; i.e.,
$latex \[
	g^{(p)} (0) /  p !
\]$$

$head f$$
This is either a
$cref/d_fun/cpp_fun_ctor/Syntax/d_fun/$$ or
$cref/a_fun/cpp_fun_ctor/Syntax/a_fun/$$ function object.
Note that its state is changed by this operation because
all the Taylor coefficient that it calculates for every
variable in recording are stored.
See more discussion of this fact under the heading
$cref/p/cpp_fun_forward/p/$$ below.

$head f(x)$$
We use the notation $latex f: \B{R}^n \rightarrow \B{R}^m$$
for the function corresponding to $icode f$$.
Note that $icode n$$ is the size of $cref/ax/cpp_fun_ctor/ax/$$
and $icode m$$ is the size of $cref/ay/cpp_fun_ctor/ay/$$
in to the constructor for $icode f$$.

$head X(t)$$
We use the notation $latex X : \B{R} \rightarrow \B{R}^n$$
for a function that the calling routine chooses.

$head Y(t)$$
We define the function $latex Y : \B{R} \rightarrow \B{R}^n$$
by $latex Y(t) = f(X(t))$$.

$head p$$
This argument has prototype
$codei%
	int %p%
%$$
and is non-negative.
It is the order of the Taylor coefficient being calculated.
If there was no call to $code forward$$ for this $icode f$$,
the value of $icode p$$ must be zero.
Otherwise, it must be between zero and one greater that its
value for the previous call using this $icode f$$.
After this call, the Taylor coefficients for orders zero though $icode p$$,
and for every variable in the recording, will be stored in $icode f$$.

$subhead size_order$$
After this call,
$cref/f.size_order()/cpp_fun_property/size_order/$$ is $icode%p%+1%$$.

$head xp$$
If $icode f$$ is a $code d_fun$$ or $code a_fun$$,
this argument has prototype
$codei%
	const vec_double&   %xp%
	const vec_a_double& %xp%
%$$
respectively and its size must be $icode n$$.
It specifies the $th p$$ order Taylor coefficients for $icode X(t)$$.

$head yp$$
If $icode f$$ is a $code d_fun$$ or $code a_fun$$,
the result has prototype
$codei%
	vec_double&   %yp%
	vec_a_double& %yp%
%$$
respectively and its size is $icode m$$.
It is the $th p$$ order Taylor coefficients for $latex Y(t)$$.

$children%
	example/cplusplus/fun_forward_xam.cpp
%$$
$head Example$$
$cref fun_forward_xam.cpp$$

$end
*/
std::vector<double> d_fun::forward(int p, const std::vector<double>& xp)
{	if( xp.size() != ptr_->Domain() )
		error_message("cppad_py::d_fun::forward xp.size() error");
	return ptr_->Forward(p, xp);
}
std::vector<a_double> a_fun::forward(int p, const std::vector<a_double>& axp)
{	if( axp.size() != a_ptr_->Domain() )
		error_message("cppad_py::a_fun::forward axp.size() error");
	std::vector< CppAD::AD<double> > aup = vec2cppad_double(axp);
	std::vector< CppAD::AD<double> > avp =  a_ptr_->Forward(p, aup);
	return vec2a_double(avp);
}
/*
-------------------------------------------------------------------------------
$begin cpp_fun_reverse$$
$spell
	vec
	af
	xq
	Taylor
	yq
	const
$$

$section Reverse Mode AD$$

$head Syntax$$
$icode%xq% = %f%.reverse(%q%, %yq%)%$$

$head f$$
This is either a
$cref/d_fun/cpp_fun_ctor/Syntax/d_fun/$$ or
$cref/a_fun/cpp_fun_ctor/Syntax/a_fun/$$ function object
and is effectively $code const$$.
(Some details that are not visible to the user may change.)

$head Notation$$

$subhead f(x)$$
We use the notation $latex f: \B{R}^n \rightarrow \B{R}^m$$
for the function corresponding to $icode f$$.
Note that $icode n$$ is the size of $cref/ax/cpp_fun_ctor/ax/$$
and $icode m$$ is the size of $cref/ay/cpp_fun_ctor/ay/$$
in to the constructor for $icode f$$.

$subhead X(t), S$$
This is the same function as
$cref/X(t)/cpp_fun_forward/X(t)/$$ in the previous call to
$icode%f%.forward%$$.
We use $latex S \in \B{R}^{n \times q}$$ to denote the Taylor coefficients
of $latex X(t)$$.

$subhead Y(t), T$$
This is the same function as
$cref/Y(t)/cpp_fun_forward/Y(t)/$$ in the previous call to
$icode%f%.forward%$$.
We use $latex T \in \B{R}^{m \times q}$$ to denote the Taylor coefficients
of $latex Y(t)$$.
We also use the notation $latex T(S)$$ to express the fact that
the Taylor coefficients for $latex Y(t)$$ are a function of the
Taylor coefficients of $latex X(t)$$.

$subhead G(T)$$
We use the notation $latex G : \B{R}^{m \times p} \rightarrow \B{R}$$
for a function that the calling routine chooses.

$head q$$
This argument has prototype
$codei%
	int %q%
%$$
and is positive.
It is the number of the Taylor coefficient (for each variable)
that we are computing the derivative with respect to.
It must be greater than zero, and
less than or equal
the number of Taylor coefficient stored in $icode f$$; i.e.,
$cref/f.size_order()/cpp_fun_property/size_order/$$.

$head yq$$
If $icode f$$ is a $code d_fun$$ or $code a_fun$$,
this argument has prototype
$codei%
	const vec_double&   %yq%
	const vec_a_double& %yq%
%$$
and its size must be $icode%m%*%q%$$.
For $icode%0% <= %i% < %m%$$ and $icode%0% <= %k% < %q%$$,
$icode%yq%[ %i% * %q% + %k% ]%$$ is the partial derivative of
$latex G(T)$$ with respect to the $th k$$ order Taylor coefficient
for the $th i$$ component function; i.e.,
the partial derivative of $latex G(T)$$ w.r.t. $latex Y_i^{(k)} (t) / k !$$.

$head xq$$
If $icode f$$ is a $code d_fun$$ or $code a_fun$$,
the result has prototype
$codei%
	const vec_double&   %xq%
	const vec_a_double& %xq%
%$$
respectively and its size is $icode%n%*%q%$$.
For $icode%0% <= %j% < %n%$$ and $icode%0% <= %k% < %q%$$,
$icode%xq%[ %j% * %q% + %k% ]%$$ is the partial derivative of
$latex G(T(S))$$ with respect to the $th k$$ order Taylor coefficient
for the $th j$$ component function; i.e.,
the partial derivative of
$latex G(T(S))$$ w.r.t. $latex S_j^{(k)} (t) / k !$$.

$children%
	example/cplusplus/fun_reverse_xam.cpp
%$$
$head Example$$
$cref fun_reverse_xam.cpp$$

$end
*/
std::vector<double> d_fun::reverse(int q, const std::vector<double>& yq)
{	if( yq.size() != q * ptr_->Range() )
		error_message("cppad_py::d_fun::reverse yq.size() error");
	return ptr_->Reverse(q, yq);
}
std::vector<a_double> a_fun::reverse(int q, const std::vector<a_double>& ayq)
{	if( ayq.size() != q * a_ptr_->Range() )
		error_message("cppad_py::a_fun::reverse yq.size() error");
	std::vector< CppAD::AD<double> > avq = vec2cppad_double(ayq);
	std::vector< CppAD::AD<double> > auq =  a_ptr_->Reverse(q, avq);
	return vec2a_double(auq);
}
/*
------------------------------------------------------------------------------
$begin cpp_fun_optimize$$
$spell
	af
$$

$section Optimize an AD Function$$

$head Syntax$$
$icode%f%.optimize()%$$

$head Purpose$$
This reduces the number of operations
(hence to time and memory) used to compute the function
stored in $icode f$$
On the other hand, the optimization may take a significant amount
of time and memory.

$head f$$
This object is a
$cref/d_fun/cpp_fun_ctor/Syntax/d_fun/$$.
Optimizing this $icode f$$ also optimizes the
corresponding $cref/a_fun/cpp_fun_ctor/Syntax/a_fun/$$.

$children%
	example/cplusplus/fun_optimize_xam.cpp
%$$
$head Example$$
$cref fun_optimize_xam.cpp$$

$end
*/
void d_fun::optimize(void)
{	ptr_->optimize(); }
/*
----------------------------------------------------------------------------
$begin cpp_fun_json$$
$spell
	json
	std
	CppAD
	const
$$

$section Json Representation of AD Computational Graph$$

$head Syntax$$
$icode%json% = %f%.to_json()
%$$

$head f$$
This is a $cref/d_fun/cpp_fun_ctor/Syntax/d_fun/$$ object
and is $code const$$.

$head to_json$$
The return value has prototype
$codei%
	std::string %json%
%$$
and is a Json representation of the computation graph corresponding to
$icode f$$; see the CppAD documentation for
$href%https://coin-or.github.io/CppAD/doc/json_ad_graph.htm%json_ad_graph%$$.

$children%
    example/cplusplus/fun_json_xam.cpp
%$$
$head Example$$
$cref fun_to_json_xam.cpp$$

$end
*/
// to_json
std::string d_fun::to_json(void) const
{	return ptr_->to_json(); }

} // END_CPPAD_PY_NAMESPACE
