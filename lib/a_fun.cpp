/* -----------------------------------------------------------------------------
           cppad_swig: A C++ Object Library and Swig Interface to Cppad
            Copyright (C) 2017-17 Bradley M. Bell (bradbell@seanet.com)
                This program is distributed under the terms of the
            GNU Affero General Public License version 3.0 or later see
                       http://www.gnu.org/licenses/agpl.txt
----------------------------------------------------------------------------- */
# include <cppad/cppad.hpp>
# include <cppad/swig/a_fun.hpp>
# include <cppad/swig/other.hpp>

namespace cppad_swig { // BEGIN_CPPAD_SWIG_NAMESPACE

/*
-------------------------------------------------------------------------------
$begin independent$$
$spell
	vec
	Cppad
	Perl
	py
	const
$$

$section Declare Independent Variables and Start Recording$$

$head Syntax$$
$icode%ax% = %module_ref% independent(%x%)%$$

$head module_ref$$
This is a $cref/module reference/module/Module Reference/$$
for the particular language.

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
This starts a recording of the $cref a_double$$ operation.
This recording is terminated, and the information is stored,
by calling the $cref/a_fun constructor/a_fun_ctor/$$.
It is terminated, and the information is lost,
by calling $cref abort_recording$$.

$head Example$$
All of the $code a_fun$$ examples use this function.

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
$begin abort_recording$$
$spell
	vec
	af
	const
	perl
$$

$section Abort Recording$$

$head Syntax$$
$icode%module_ref% abort_recording(%x%)%$$

$head Purpose$$
This aborts the current recording (if it exists)
started by the most recent call to $cref independent$$.

$head module_ref$$
This is a $cref/module reference/module/Module Reference/$$
for the particular language.

$children%
	build/lib/example/cplusplus/a_fun_abort_xam.cpp%
	build/lib/example/octave/a_fun_abort_xam.m%
	build/lib/example/perl/a_fun_abort_xam.pm%
	build/lib/example/python/a_fun_abort_xam.py
%$$
$head Example$$
$cref/C++/a_fun_abort_xam.cpp/$$,
$cref/Octave/a_fun_abort_xam.m/$$,
$cref/Perl/a_fun_abort_xam.pm/$$,
$cref/Python/a_fun_abort_xam.py/$$.

$end
*/
void abort_recording(void)
{	CppAD::AD<double>::abort_recording();
}
/*
-------------------------------------------------------------------------------
$begin a_fun_ctor$$
$spell
	vec
	af
	const
$$

$section Stop Current Recording and Store in an a_fun Object$$

$head Syntax$$
$icode%af% = %model_ref_%a_fun(%ax%, %ay%)%$$

$head ax$$
This argument has prototype
$codei%
	const vec_a_double& %ax%
%$$
It must be the same as
$cref/ax/independent/ax/$$ in the previous call to $code independent$$.
To be specific, it must be the original independent variables.
We use the notation $icode%n% = %ax%.size()%$$
to denote the number of independent variables.

$head ay$$
This argument has prototype
$codei%
	const vec_a_double& %ax%
%$$
It specifies the dependent variables.
We use the notation $icode%m% = %ax%.size()%$$
to denote the number of dependent variables.

$head af$$
The result has prototype
$codei%
	a_fun %af%
%$$
It has a representation for the $cref a_double$$ operations
that mapped the independent variables to the dependent variables.
These operations define the function that can be differentiated.

$head Example$$
All of the $code a_fun$$ examples use an $code a_fun$$ constructor.

$end
*/
// a_fun(void) (not yet documented or tested)
a_fun::a_fun(void)
{	ptr_ = new CppAD::ADFun<double>();
	CPPAD_ASSERT_UNKNOWN( ptr_ != CPPAD_NULL );
}
// destructor
a_fun::~a_fun(void)
{	if( ptr_ != CPPAD_NULL )
	CPPAD_ASSERT_UNKNOWN( ptr_ != CPPAD_NULL );
	delete ptr_;
}
// a_fun(ax, ay)
a_fun::a_fun(
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
$begin a_fun_jacobian$$
$spell
	vec
	af
	Taylor
	const
	Perl
	Jacobian
$$

$section Jacobian of an AD Function$$
$spell
	vec
$$

$head Syntax$$
$icode%J% = %af%.jacobian(%x%)%$$

$head af$$
This object has prototype
$codei%
	a_fun %af%
%$$
Note that its state is changed by this operation.
The zero order
$cref/Taylor coefficients/a_fun_forward/Taylor Coefficient/$$ in $icode af$$
correspond to the value of $icode x$$.
The other Taylor coefficients in $icode af$$ are unspecified.

$head f(x)$$
We use the notation $latex f: \B{R}^n \rightarrow \B{R}^m$$
for the function corresponding to $icode af$$.
Note that $icode n$$ is the size of $cref/ax/a_fun_ctor/ax/$$
and $icode m$$ is the size of $cref/ay/a_fun_ctor/ay/$$
in to the constructor for $icode af$$.

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
	build/lib/example/cplusplus/a_fun_jacobian_xam.cpp%
	build/lib/example/octave/a_fun_jacobian_xam.m%
	build/lib/example/perl/a_fun_jacobian_xam.pm%
	build/lib/example/python/a_fun_jacobian_xam.py
%$$
$head Example$$
$cref/C++/a_fun_jacobian_xam.cpp/$$,
$cref/Octave/a_fun_jacobian_xam.m/$$,
$cref/Perl/a_fun_jacobian_xam.pm/$$,
$cref/Python/a_fun_jacobian_xam.py/$$.


$end
*/
std::vector<double> a_fun::jacobian(const std::vector<double>& x)
{	return ptr_->Jacobian(x);
}
/*
------------------------------------------------------------------------------
$begin a_fun_hessian$$
$spell
	vec
	af
	Taylor
	const
	Perl
$$

$section Hessian of an AD Function$$
$spell
	vec
$$

$head Syntax$$
$icode%H% = %af%.hessian(%x%, %w%)%$$

$head af$$
This object has prototype
$codei%
	a_fun %af%
%$$
Note that its state is changed by this operation.
The zero order
$cref/Taylor coefficients/a_fun_forward/Taylor Coefficient/$$ in $icode af$$
correspond to the value of $icode x$$.
The other Taylor coefficients in $icode af$$ are unspecified.

$head f(x)$$
We use the notation $latex f: \B{R}^n \rightarrow \B{R}^m$$
for the function corresponding to $icode af$$.
Note that $icode n$$ is the size of $cref/ax/a_fun_ctor/ax/$$
and $icode m$$ is the size of $cref/ay/a_fun_ctor/ay/$$
in to the constructor for $icode af$$.

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
	build/lib/example/cplusplus/a_fun_hessian_xam.cpp%
	build/lib/example/octave/a_fun_hessian_xam.m%
	build/lib/example/perl/a_fun_hessian_xam.pm%
	build/lib/example/python/a_fun_hessian_xam.py
%$$
$head Example$$
$cref/C++/a_fun_hessian_xam.cpp/$$,
$cref/Octave/a_fun_hessian_xam.m/$$,
$cref/Perl/a_fun_hessian_xam.pm/$$,
$cref/Python/a_fun_hessian_xam.py/$$.


$end
*/
std::vector<double> a_fun::hessian(
	const std::vector<double>& x  ,
	const std::vector<double>& w  )
{	return ptr_->Hessian(x, w);
}
/*
------------------------------------------------------------------------------
$begin a_fun_forward$$
$spell
	vec
	af
	xp
	Taylor
	yp
	const
	Perl
$$

$section Forward Mode AD$$
$spell
	vec
	xp
$$

$head Syntax$$
$icode%yp% = %af%.forward(%p%, %xp%)%$$

$head Taylor Coefficient$$
For a function $latex g(t)$$ of a scalar argument $latex t \in \B{R}$$,
the $th p$$ order Taylor coefficient is its
$code p$$-th order derivative divided by $icode p$$ factorial
and evaluated at $latex t = 0$$; i.e.,
$latex \[
	g^{(p)} (0) /  p !
\]$$

$head af$$
This object has prototype
$codei%
	a_fun %af%
%$$
Note that its state is changed by this operation because it keeps
all the Taylor coefficient that it calculates for every
variable in recording it stored.
See more discussion of this fact under the heading
$cref/p/a_fun_forward/p/$$ below.

$head f(x)$$
We use the notation $latex f: \B{R}^n \rightarrow \B{R}^m$$
for the function corresponding to $icode af$$.
Note that $icode n$$ is the size of $cref/ax/a_fun_ctor/ax/$$
and $icode m$$ is the size of $cref/ay/a_fun_ctor/ay/$$
in to the constructor for $icode af$$.

$head X(t)$$
We use the notation $latex X : \B{R} \rightarrow \B{R}^n$$
for a function that the calling routine chooses.

$head Y(t)$$
We define the function $latex Y : \B{R} \rightarrow \B{R}^n$$
by $latex Y(t) = f(X(t))$$.

$head p$$
This argument has prototype
$codei%
	size_t %p%
%$$
i.e., it is a positive integer.
Its value is the order of the Taylor coefficient being calculated.
If there was no call to $code forward$$ for this $icode af$$,
the value of $icode p$$ must be zero.
Otherwise, it must be between zero and one greater that its
value for the previous call using this $icode af$$.
After this call, the Taylor coefficients for orders zero though $icode p$$,
and for every variable in the recording, will be stored in $icode af$$.

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
	build/lib/example/cplusplus/a_fun_forward_xam.cpp%
	build/lib/example/octave/a_fun_forward_xam.m%
	build/lib/example/perl/a_fun_forward_xam.pm%
	build/lib/example/python/a_fun_forward_xam.py
%$$
$head Example$$
$cref/C++/a_fun_forward_xam.cpp/$$,
$cref/Octave/a_fun_forward_xam.m/$$,
$cref/Perl/a_fun_forward_xam.pm/$$,
$cref/Python/a_fun_forward_xam.py/$$.


$end
*/
std::vector<double> a_fun::forward(size_t p, const std::vector<double>& xp)
{	return ptr_->Forward(p, xp);
}
/*
-------------------------------------------------------------------------------
$begin a_fun_reverse$$
$spell
	vec
	af
	xq
	Taylor
	yq
	const
	Perl
$$

$section Reverse Mode AD$$

$head Syntax$$
$icode%xq% = %af%.reverse(%q%, %yq%)%$$

$head af$$
This object has prototype
$codei%
	a_fun %af%
%$$
Note that it is effectively $code const$$,
but some details that are not visible to the user may change,
so it is not declared $code const$$.

$head Notation$$

$subhead f(x)$$
We use the notation $latex f: \B{R}^n \rightarrow \B{R}^m$$
for the function corresponding to $icode af$$.
Note that $icode n$$ is the size of $cref/ax/a_fun_ctor/ax/$$
and $icode m$$ is the size of $cref/ay/a_fun_ctor/ay/$$
in to the constructor for $icode af$$.

$subhead X(t), S$$
This is the same function as
$cref/X(t)/a_fun_forward/X(t)/$$ in the previous call to
$icode%af%.forward%$$.
We use $latex S \in \B{R}^{n \times q}$$ to denote the Taylor coefficients
of $latex X(t)$$.

$subhead Y(t), T$$
This is the same function as
$cref/Y(t)/a_fun_forward/Y(t)/$$ in the previous call to
$icode%af%.forward%$$.
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
	size_t %q%
%$$
Its value is the number of the Taylor coefficient (for each variable)
that we are computing the derivative with respect to.
It must be greater than zero, and
less than or equal $icode%p% + 1%$$,
the number of Taylor coefficient stored in $icode af$$.
(The number of Taylor coefficients is equal to $icode%p%+1%$$ where
$cref/p/a_fun_forward/p/$$ is the order for the previous $code forward$$
call using $icode af$$.)

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
	build/lib/example/cplusplus/a_fun_reverse_xam.cpp%
	build/lib/example/octave/a_fun_reverse_xam.m%
	build/lib/example/perl/a_fun_reverse_xam.pm%
	build/lib/example/python/a_fun_reverse_xam.py
%$$
$head Example$$
$cref/C++/a_fun_reverse_xam.cpp/$$,
$cref/Octave/a_fun_reverse_xam.m/$$,
$cref/Perl/a_fun_reverse_xam.pm/$$,
$cref/Python/a_fun_reverse_xam.py/$$.


$end
*/
std::vector<double> a_fun::reverse(size_t q, const std::vector<double>& yq)
{	if( yq.size() != q * ptr_->Range() )
		error_message("cppad_swig::a_fun::reverse yq.size() error");
	return ptr_->Reverse(q, yq);
}
/*
------------------------------------------------------------------------------
$begin a_fun_optimize$$
$spell
	af
	Perl
$$

$section Optimize an AD Function$$

$head Syntax$$
$icode%af%.optimize()%$$

$head Purpose$$
This reduces the number of operations
(hence to time and memory) used to compute the function
stored in $icode af$$
On the other hand, the optimization may take a significant amount
of time and memory.

$head af$$
This object has prototype
$codei%
	a_fun %af%
%$$


$children%
	build/lib/example/cplusplus/a_fun_optimize_xam.cpp%
	build/lib/example/octave/a_fun_optimize_xam.m%
	build/lib/example/perl/a_fun_optimize_xam.pm%
	build/lib/example/python/a_fun_optimize_xam.py
%$$
$head Example$$
$cref/C++/a_fun_optimize_xam.cpp/$$,
$cref/Octave/a_fun_optimize_xam.m/$$,
$cref/Perl/a_fun_optimize_xam.pm/$$,
$cref/Python/a_fun_optimize_xam.py/$$.


$end
*/
void a_fun::optimize(void)
{	ptr_->optimize(); }
/*
------------------------------------------------------------------------------
$begin a_fun_property$$
$spell
	vec
	ind
	dep
$$

$section Properties of an AD Function$$
$spell
	vec
	af
	var
	op
	const
	Perl
$$

$head Syntax$$
$icode%n% = %af%.size_ind()
%$$
$icode%m% = %af%.size_dep()
%$$
$icode%v% = %af%.size_var()
%$$
$icode%p% = %af%.size_op()
%$$

$head af$$
This object has prototype
$codei%
	const a_fun %af%
%$$

$head size_ind$$
The return value has prototype
$codei%
	size_t %n%
%$$
an is the size of the vector
$cref/ax/a_fun_ctor/ax/$$ in the function constructor; i.e.,
the number of independent variables.

$head size_dep$$
The return value has prototype
$codei%
	size_t %m%
%$$
an is the size of the vector
$cref/ay/a_fun_ctor/ay/$$ in the function constructor; i.e.,
the number of dependent variables.

$head size_var$$
The return value has prototype
$codei%
	size_t %v%
%$$
an is the number of variables in the function.
This includes the independent variables, dependent variables,
and any variables that are used to compute the dependent variables
from the independent variables.

$head size_op$$
The return value has prototype
$codei%
	size_t %p%
%$$
an is the number of atomic operations that are used to express
the dependent variables as a function of the independent variables.

$children%
	build/lib/example/cplusplus/a_fun_property_xam.cpp%
	build/lib/example/octave/a_fun_property_xam.m%
	build/lib/example/perl/a_fun_property_xam.pm%
	build/lib/example/python/a_fun_property_xam.py
%$$
$head Example$$
$cref/C++/a_fun_property_xam.cpp/$$,
$cref/Octave/a_fun_property_xam.m/$$,
$cref/Perl/a_fun_property_xam.pm/$$,
$cref/Python/a_fun_property_xam.py/$$.

$end
*/
// size_ind
size_t a_fun::size_ind(void) const
{	return ptr_->Domain(); }
// size_dep
size_t a_fun::size_dep(void) const
{	return ptr_->Range(); }
// size_var
size_t a_fun::size_var(void) const
{	return ptr_->size_var(); }
// size_op
size_t a_fun::size_op(void) const
{	return ptr_->size_op(); }
// ----------------------------------------------------------------------------
} // END_CPPAD_SWIG_NAMESPACE
