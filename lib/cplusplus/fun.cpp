/* -----------------------------------------------------------------------------
           cppad_py: A C++ Object Library and Python Interface to Cppad
            Copyright (C) 2017-18 Bradley M. Bell (bradbell@seanet.com)
                This program is distributed under the terms of the
                GNU General Public License version 3.0 or later see
                      https://www.gnu.org/licenses/gpl-3.0.txt
----------------------------------------------------------------------------- */
# include <cppad/cppad.hpp>
# include <cppad/py/fun.hpp>
# include <cppad/py/error.hpp>

namespace cppad_py { // BEGIN_CPPAD_PY_NAMESPACE

/*
-------------------------------------------------------------------------------
$begin cpp_independent$$
$spell
	vec
	const
	cppad_py
$$

$section Declare Independent Variables and Start Recording$$

$head Syntax$$
$icode%ax% = cppad_py::independent(%x%)%$$

$head x$$
This argument has prototype
$codei%
	const vec_double& %x%
%$$
Its specifies the number of independent variables
and their values during the recording.
We use the notation $icode%n% = %x%.size()%$$
to denote the number of independent variables.

$head ax$$
The result has prototype
$codei%
	vec_a_double& %ax%
%$$
This is the vector of independent variables.
It has size $icode n$$ and for
$icode%i% = 0%$$ to $icode%n%-1%$$
$codei%
	%ax%[%i%].value() == %x%[%i%]
%$$

$head Purpose$$
This starts a recording of the $cref a_double$$ operations.
This recording is terminated, and the information is stored,
by calling the $cref/d_fun constructor/cpp_fun_ctor/$$.
It is terminated, and the information is lost,
by calling $cref/abort_recording/cpp_abort_recording/$$.

$head Example$$
All of the c++ $code d_fun$$ examples use this function.

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
	for(size_t j = 0; j < n; j++)
		result[j] = a_double( &ax[j] );
	return result;
}
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
	lib/example/cplusplus/fun_abort_xam.cpp
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
$$

$section Stop Current Recording and Store in an d_fun Object$$

$head Syntax$$
$icode%f% = cppad_py::d_fun(%ax%, %ay%)%$$

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
The result has prototype
$codei%
	cppad_py::d_fun %f%
%$$
It has a representation for the $cref a_double$$ operations
that mapped the independent variables to the dependent variables.
These operations define the function that can be differentiated.

$head Example$$
All of the $code d_fun$$ examples use an $code d_fun$$ constructor.

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

$section Properties of an AD Function$$

$head Syntax$$
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
This object has prototype
$codei%
	const d_fun %f%
%$$

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

$children%
	lib/example/cplusplus/fun_property_xam.cpp
%$$
$head Example$$
$cref fun_property_xam.cpp$$

$end
*/
// size_domain
int d_fun::size_domain(void) const
{	return ptr_->Domain(); }
// size_range
int d_fun::size_range(void) const
{	return ptr_->Range(); }
// size_var
int d_fun::size_var(void) const
{	return ptr_->size_var(); }
// size_op
int d_fun::size_op(void) const
{	return ptr_->size_op(); }
// size_order
int d_fun::size_order(void) const
{	return ptr_->size_order(); }
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
This object has prototype
$codei%
	d_fun %f%
%$$
Note that its state is changed by this operation.
The zero order
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
This argument has prototype
$codei%
	const vec_double& %x%
%$$
and its size must be $icode n$$.
It specifies the argument value at we are computing the Jacobian
$latex f'(x)$$.

$head J$$
The result has prototype
$codei%
	vec_double %J%
%$$
and its size is $icode%m%*%n%$$.
For $icode i$$ between zero and $icode%m%-1%$$
and $icode j$$ between zero and $icode%n%-1%$$,
$latex \[
	J [ i * n + j ] = \frac{ \partial f_i }{ \partial x_j } (x)
\] $$

$children%
	lib/example/cplusplus/fun_jacobian_xam.cpp
%$$
$head Example$$
$cref fun_jacobian_xam.cpp$$


$end
*/
std::vector<double> d_fun::jacobian(const std::vector<double>& x)
{	return ptr_->Jacobian(x);
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
This object has prototype
$codei%
	d_fun %f%
%$$
Note that its state is changed by this operation.
The zero order
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
This argument has prototype
$codei%
	const vec_double& %x%
%$$
and its size must be $icode n$$.
It specifies the argument value at we are computing the Hessian
$latex g^{(2)}(x)$$.

$head w$$
This argument has prototype
$codei%
	const vec_double& %w%
%$$
and its size must be $icode m$$.
It specifies the vector $icode w$$ in the definition of $latex g(x)$$ above.

$head H$$
The result has prototype
$codei%
	vec_double %H%
%$$
and its size is $icode%n%*%n%$$.
For $icode i$$ between zero and $icode%n%-1%$$
and $icode j$$ between zero and $icode%n%-1%$$,
$latex \[
	H [ i * n + j ] = \frac{ \partial^2 g }{ \partial x_i \partial x_j } (x)
\] $$

$children%
	lib/example/cplusplus/fun_hessian_xam.cpp
%$$
$head Example$$
$cref fun_hessian_xam.cpp$$

$end
*/
std::vector<double> d_fun::hessian(
	const std::vector<double>& x  ,
	const std::vector<double>& w  )
{	return ptr_->Hessian(x, w);
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
This object has prototype
$codei%
	d_fun %f%
%$$
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
This argument has prototype
$codei%
	const vec_double& %xp%
%$$
and its size must be $icode n$$.
It specifies the $th p$$ order Taylor coefficients for $icode X(t)$$.

$head yp$$
The result has prototype
$codei%
	vec_double %yp%
%$$
and its size is $icode m$$.
It is the $th p$$ order Taylor coefficients for $latex Y(t)$$.

$children%
	lib/example/cplusplus/fun_forward_xam.cpp
%$$
$head Example$$
$cref fun_forward_xam.cpp$$

$end
*/
std::vector<double> d_fun::forward(int p, const std::vector<double>& xp)
{	return ptr_->Forward(p, xp);
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
This object has prototype
$codei%
	d_fun %f%
%$$
Note that it is effectively $code const$$,
but some details that are not visible to the user may change,
so it is not declared $code const$$.

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
This argument has prototype
$codei%
	const vec_double& %yq%
%$$
and its size must be $icode%m%*%q%$$.
For $icode%0% <= %i% < %m%$$ and $icode%0% <= %k% < %q%$$,
$icode%yq%[ %i% * %q% + %k% ]%$$ is the partial derivative of
$latex G(T)$$ with respect to the $th k$$ order Taylor coefficient
for the $th i$$ component function; i.e.,
the partial derivative of $latex G(T)$$ w.r.t. $latex Y_i^{(k)} (t) / k !$$.

$head xq$$
The result has prototype
$codei%
	vec_double %xq%
%$$
and its size is $icode%n%*%q%$$.
For $icode%0% <= %j% < %n%$$ and $icode%0% <= %k% < %q%$$,
$icode%yq%[ %j% * %q% + %k% ]%$$ is the partial derivative of
$latex G(T(S))$$ with respect to the $th k$$ order Taylor coefficient
for the $th j$$ component function; i.e.,
the partial derivative of
$latex G(T(S))$$ w.r.t. $latex S_j^{(k)} (t) / k !$$.

$children%
	lib/example/cplusplus/fun_reverse_xam.cpp
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
This object has prototype
$codei%
	d_fun %f%
%$$

$children%
	lib/example/cplusplus/fun_optimize_xam.cpp
%$$
$head Example$$
$cref fun_optimize_xam.cpp$$

$end
*/
void d_fun::optimize(void)
{	ptr_->optimize(); }
// ----------------------------------------------------------------------------
} // END_CPPAD_PY_NAMESPACE
