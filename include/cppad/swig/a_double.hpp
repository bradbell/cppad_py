# ifndef CPPAD_SWIG_A_DOUBLE_HPP
# define CPPAD_SWIG_A_DOUBLE_HPP
/* -----------------------------------------------------------------------------
           cppad_swig: A C++ Object Library and Swig Interface to Cppad
            Copyright (C) 2017-17 Bradley M. Bell (bradbell@seanet.com)
                This program is distributed under the terms of the
            GNU Affero General Public License version 3.0 or later see
                       http://www.gnu.org/licenses/agpl.txt
----------------------------------------------------------------------------- */
# include <vector>
# include <cppad/configure.hpp>
# ifdef SWIG
#	define CPPAD_SWIG_LIB_PUBLIC
# else
#	include <cppad_swig_lib_export.h>
# endif

/*
$begin a_double$$

$section The C++ a_double Class$$

$childtable%lib/a_double.cpp%$$

$end
*/

// declarations without definitions
namespace CppAD {
	template <class Base> class AD;
}

/// structure with exact same member data as AD<double>
struct a_double_data {
	/// Base value corresponding to this object
	double                 value;
	/// tape identifier correspoding to taddr
	CPPAD_TAPE_ID_TYPE     tape_id;
	/// tape address for this object
	CPPAD_TAPE_ADDR_TYPE   taddr;
};

namespace cppad_swig { // BEGIN_CPPAD_SWIG_NAMESPACE

/// Swig class that acts the same as CppAD::AD<double>
class  CPPAD_SWIG_LIB_PUBLIC a_double
{	// private members are not in Swig interface
	private:
	/// data for this object
	a_double_data        data_;
	// -----------------------------------------------------------------------
	// public members not in Swig interface (see %ignore ptr)
	public:
	/// pointer to this as an AD<double> object
	CppAD::AD<double>* ptr(void);
	/// const version of pointer to this as an AD<double> object
	const CppAD::AD<double>* ptr(void) const;
	/// ctor from CppAD::AD<double>
	a_double(const CppAD::AD<double>* ad_ptr);
	// -----------------------------------------------------------------------
	// public members in Swig interface
	public:
	// BEGIN a_double_ctor
	a_double(void);
	a_double(const double& d);
	a_double(const a_double& ad);
	// END a_double_ctor
	/// destructor
	~a_double(void);
	/// conversion to double
	double value(void) const;
	// binary operators with a_double result
	a_double operator+(const a_double& ad) const;
	a_double operator-(const a_double& ad) const;
	a_double operator*(const a_double& ad) const;
	a_double operator/(const a_double& ad) const;
	// comparison operators
	bool operator< (const a_double& ad) const;
	bool operator<=(const a_double& ad) const;
	bool operator> (const a_double& ad) const;
	bool operator>=(const a_double& ad) const;
	bool operator==(const a_double& ad) const;
	bool operator!=(const a_double& ad) const;
	// computed assignment operators
	a_double operator+=(const a_double& ad);
	a_double operator-=(const a_double& ad);
	a_double operator*=(const a_double& ad);
	a_double operator/=(const a_double& ad);
};

} // END_CPPAD_SWIG_NAMESPACE

# endif
