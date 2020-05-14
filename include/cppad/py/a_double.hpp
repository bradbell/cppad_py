# ifndef CPPAD_PY_A_DOUBLE_HPP
# define CPPAD_PY_A_DOUBLE_HPP
/* -----------------------------------------------------------------------------
           cppad_py: A C++ Object Library and Python Interface to Cppad
            Copyright (C) 2017-20 Bradley M. Bell (bradbell@seanet.com)
                This program is distributed under the terms of the
                GNU General Public License version 3.0 or later see
                      https://www.gnu.org/licenses/gpl-3.0.txt
----------------------------------------------------------------------------- */
# include <vector>
# include <cppad/configure.hpp>
# include <cppad/py/public_lib.hpp>

// declarations without definitions
namespace CppAD {
	template <class Base> class AD;
}

// structure with exact same member data as AD<double>
struct a_double_data {
	// Base value corresponding to this object
	double                 value;
	// tape identifier correspoding to taddr
	CPPAD_TAPE_ID_TYPE     tape_id;
	// tape address for this object
	CPPAD_TAPE_ADDR_TYPE   taddr;
	// is this a dynamic parameter (or a variable)
	// when tape_id is for current tape and taddr is non-zero
	bool dynamic;
};

namespace cppad_py { // BEGIN_CPPAD_PY_NAMESPACE

// Swig class that acts the same as CppAD::AD<double>
class  CPPAD_PY_LIB_PUBLIC a_double
{	// private members are not in Swig interface
	private:
	// data for this object
	a_double_data        data_;
	// -----------------------------------------------------------------------
	// public members not in Swig interface (see %ignore ptr)
	public:
	// pointer to this as an AD<double> object
	CppAD::AD<double>* ptr(void);
	// const version of pointer to this as an AD<double> object
	const CppAD::AD<double>* ptr(void) const;
	// ctor from CppAD::AD<double>
	a_double(const CppAD::AD<double>* a_ptr);
	// -----------------------------------------------------------------------
	// public members in Swig interface
	public:
	// default ctor
	a_double(void);
	// destructor
	~a_double(void);
	// ctor from double
	a_double(const double& value);
	// ctor from a_double
	a_double(const a_double& ad);
	//
	// conversion to double
	double value(void) const;
	// is this object a paramemter
	bool parameter(void) const;
	// is this object a variable
	bool variable(void) const;
	// is the value of this object nearly equal
	bool near_equal(const a_double& ae);
	// convert possible variable to a parameter
	a_double var2par(void) const;
	//
	// unary + and -
	const a_double& operator+(void) const;
	a_double operator-(void) const;
	//
	// binary operators with AD result
	a_double operator+(const a_double& ad) const;
	a_double operator-(const a_double& ad) const;
	a_double operator*(const a_double& ad) const;
	a_double operator/(const a_double& ad) const;
	//
	a_double operator+(const double& d) const;
	a_double operator-(const double& d) const;
	a_double operator*(const double& d) const;
	a_double operator/(const double& d) const;
	//
	// comparison operators
	bool operator< (const a_double& ad) const;
	bool operator<=(const a_double& ad) const;
	bool operator> (const a_double& ad) const;
	bool operator>=(const a_double& ad) const;
	bool operator==(const a_double& ad) const;
	bool operator!=(const a_double& ad) const;
	//
	bool operator< (const double& d) const;
	bool operator<=(const double& d) const;
	bool operator> (const double& d) const;
	bool operator>=(const double& d) const;
	bool operator==(const double& d) const;
	bool operator!=(const double& d) const;
	//
	// assignment operators
	a_double operator+=(const a_double& ad);
	a_double operator-=(const a_double& ad);
	a_double operator*=(const a_double& ad);
	a_double operator/=(const a_double& ad);
	//
	a_double operator+=(const double& d);
	a_double operator-=(const double& d);
	a_double operator*=(const double& d);
	a_double operator/=(const double& d);
# ifndef SWIG
	// python swig does not want assignment operator declared
	a_double operator =(const a_double& ad);
	a_double operator =(const double& d);
# endif
	//
	// unary functions with AD result
	a_double abs(void) const;
	a_double acos(void) const;
	a_double asin(void) const;
	a_double atan(void) const;
	a_double cos(void) const;
	a_double cosh(void) const;
	a_double erf(void) const;
	a_double exp(void) const;
	a_double fabs(void) const;
	a_double log(void) const;
	a_double sin(void) const;
	a_double sinh(void) const;
	a_double sqrt(void) const;
	a_double tan(void) const;
	a_double tanh(void) const;
	//
	// conditional assignment
	void cond_assign(
		const char*     cop       ,
		const a_double& left      ,
		const a_double& right     ,
		const a_double& if_true   ,
		const a_double& if_false
	);
};

// Binary operations with double on left and a_double on right
a_double radd(const double& d, const a_double& ad);
a_double rsub(const double& d, const a_double& ad);
a_double rmul(const double& d, const a_double& ad);
a_double rdiv(const double& d, const a_double& ad);

// The binary pow function (operator in python but not c++)
a_double  pow(const a_double& ax, const a_double& ay);
a_double  pow(const a_double& ad, const double& d);
a_double  pow(const double& d, const a_double& ad);

} // END_CPPAD_PY_NAMESPACE

# endif
