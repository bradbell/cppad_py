# ifndef CPPAD_SWIG_EXAMPLE_SWIG_EXAMPLE_HPP
# define CPPAD_SWIG_EXAMPLE_SWIG_EXAMPLE_HPP
/* -----------------------------------------------------------------------------
           cppad_swig: A C++ Object Library and SWIG Interface to CppAD
            Copyright (C) 2017-17 Bradley M. Bell (bradbell@seanet.com)
                This program is distributed under the terms of the
            GNU Affero General Public License version 3.0 or later see
                       http://www.gnu.org/licenses/agpl.txt
----------------------------------------------------------------------------- */
# include <vector>

int         factorial_by_val(int n);
const char* message_of_void();
void        add_by_ptr(int x, int y, int* result);
int         max_array_by_ptr(int n, int* x);
const char* raise_exception(const char* message) throw(const char*);
double      max_std_vector_double(const std::vector<double>& x);

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
