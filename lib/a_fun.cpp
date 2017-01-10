/* -----------------------------------------------------------------------------
           cppad_swig: A C++ Object Library and Swig Interface to Cppad
            Copyright (C) 2017-17 Bradley M. Bell (bradbell@seanet.com)
                This program is distributed under the terms of the
            GNU Affero General Public License version 3.0 or later see
                       http://www.gnu.org/licenses/agpl.txt
----------------------------------------------------------------------------- */
# include <cppad/cppad.hpp>
# include <cppad/swig/a_fun.hpp>

namespace cppad_swig { // BEGIN_CPPAD_SWIG_NAMESPACE

/*
-------------------------------------------------------------------------------
$begin independent$$
$spell
	Cppad
	Perl
	py
	const
$$

$section Declare Independent Variables and Start Recording$$

$head Syntax$$
$icode%ax% = %module_ref_%independent(%x%)%$$

$head module_ref_$$
This is a reference to the Cppad Swig module which is
language dependent as follows:
$table
C++        $cnext $code cppad_swig::$$ $rnext
Octave     $cnext $code m_cppad.$$     $rnext
Perl       $cnext $code pm_cppad::$$   $rnext
Python     $cnext $code py_cppad.$$
$tend

$head x$$
This argument has prototype
$codei%
	const vector_double& %x%
%$$
Its specifies the number of independent variables
and their values during the recording.
We use the notation $icode%n% = %x%.size()%$$
to denote the number of independent variables.

$head ax$$
The result has prototype
$codei%
	vector_ad& %ax%
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
	af
	const
	perl
$$

$section Abort Recording$$

$head Syntax$$
$icode%module_ref_%abort_recording(%x%)%$$

$head Purpose$$
This aborts the current recording (if it exists)
started by the most recent call to $cref independent$$.

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
	af
	const
$$

$section Stop Current Recording and Store in an a_fun Object$$

$head Syntax$$
$icode%af% = %model_ref_%a_fun(%ax%, %ay%)%$$

$head ax$$
This argument has prototype
$codei%
	const vector_ad& %ax%
%$$
It must be the same as
$cref/ax/independent/ax/$$ in the previous call to $code independent$$.
To be specific, it must be the original independent variables.
We use the notation $icode%n% = %ax%.size()%$$
to denote the number of independent variables.

$head ay$$
This argument has prototype
$codei%
	const vector_ad& %ax%
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
All of the $code a_fun$$ examples use this function.

$end
*/
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

// forward(p, xp)
std::vector<double> a_fun::forward(int p, const std::vector<double>& xp)
{	return ptr_->Forward( size_t(p), xp);
}

} // END_CPPAD_SWIG_NAMESPACE
