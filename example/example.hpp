# ifndef CPPAD_SWIG_EXAMPLE_EXAMPLE_HPP
# define CPPAD_SWIG_EXAMPLE_EXAMPLE_HPP
/* -----------------------------------------------------------------------------
           cppad_swig: A C++ Object Library and SWIG Interface to CppAD
            Copyright (C) 2017-17 Bradley M. Bell (bradbell@seanet.com)
                This program is distributed under the terms of the
            GNU Affero General Public License version 3.0 or later see
                       http://www.gnu.org/licenses/agpl.txt
----------------------------------------------------------------------------- */
# include <vector>
// BEGIN function prototypes
int         factorial_by_val(int n);
const char* message_of_void();
void        add_by_ptr(int x, int y, int* result);
int         max_array_by_ptr(int n, const int* x);
double      max_std_vector_double(const std::vector<double>& x);
const char* raise_exception(const char* message) throw(const char*);
// END function prototypes
/*
$begin example_hpp$$
$spell
	ptr
	std
$$

$section Example C++ Functions$$

$head Prototypes$$
$srcfile%example/example.hpp%0
	%// BEGIN function prototypes%// END function prototypes%$$

$head factorial_by_val$$
$subhead Specification$$
The return value is the factorial of the argument $icode n$$.
$subhead Implementation$$
$srcfile%example/example.cpp%0
	%// BEGIN factorial_by_val%// END factorial_by_val%$$

$head message_of_void$$
$subhead Specification$$
The return value is the text $code OK$$.
$subhead Implementation$$
$srcfile%example/example.cpp%0
	%// BEGIN message_of_void%// END message_of_void%$$

$head add_by_ptr$$
$subhead Specification$$
The input value of $icode result$$ does not matter.
Upon return $icode%result% = %x% + %y%$$.
$subhead Implementation$$
$srcfile%example/example.cpp%0
	%// BEGIN add_by_ptr%// END add_by_ptr%$$

$head max_array_by_ptr$$
$subhead Specification$$
The array $icode x$$ has length $icode n$$ and the return value
is the maximum of the elements of $icode x$$.
$subhead Implementation$$
$srcfile%example/example.cpp%0
	%// BEGIN max_array_by_ptr%// END max_array_by_ptr%$$

$head max_std_vector_double$$
$subhead Specification$$
The return value is the maximum of the elements of $icode x$$.
$subhead Implementation$$
$srcfile%example/example.cpp%0
	%// BEGIN max_std_vector_double%// END max_std_vector_double%$$


$head raise_exception$$
$subhead Specification$$
It $icode message$$ is the empty C string,
the return value is the string corresponding to the previous
call to $code raise_exception$$ when $icode message$$ was non-empty.
If $icode message$$ is non-empty,
the message is store, so it can be retrieved later,
and the following exception is thrown:
$codei%
	throw %message%;
%$$
The message storage is done using a static variable and hence is
not thread safe.
$subhead Implementation$$
$srcfile%example/example.cpp%0
	%// BEGIN raise_exception%// END raise_exception%$$

$end
------------------------------------------------------------------------------
*/


class normal_class
{	private:
		int value_;
	public:
		// ctor
		normal_class(void);
		normal_class(int value);
		// destructor
		~normal_class(void);
		// int
		int value(void) const;
		// additon
		normal_class operator+(const normal_class& right) const;
		// equality
		bool operator==(const normal_class& right) const;
};

template <class Type> class template_class
{	private:
		Type value_;
	public:
		// ctor
		template_class(const Type& value) : value_(value)
		{ }
		// value
		Type value(void) const
		{	return value_; }
		// addition
		template_class operator+(const template_class& right) const
		{	return template_class( value_ + right.value_ ); }
		// equality
		bool operator==(const template_class& right) const
		{	return (value_ == right.value_); }
};


# endif
