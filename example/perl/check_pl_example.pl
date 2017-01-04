# -----------------------------------------------------------------------------
#         cppad_swig: A C++ Object Library and Swig Interface to CppAD
#          Copyright (C) 2017-17 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#          GNU Affero General Public License version 3.0 or later see
#                     http://www.gnu.org/licenses/agpl.txt
# -----------------------------------------------------------------------------
# The script uses the $ in its perl syntax
# $OMhelpKeyCharacter=&
#
# &begin check_pl_example.pl&& &newlinech #&&
# &spell
#	std
#	pl
#	ptr
#	Perl
# &&
#
# &section Perl Script That Tests pl_example Swig Module&&
#
# &head Load the Module&&
# &srccode%cpp%
use pl_example;
# %&&
#
# &head Initialize Error Count&&
# &srccode%cpp%
$error_count = 0;
# %&&
#
# &head factorial_by_value&&
# &srccode%cpp%
if( pl_example::factorial_by_value(4) == 24 )
{	print "pl_example::factorial_by_value: OK\n"; }
else
{	print "pl_example::factorial_by_value: Error\n";
	$error_count = $error_count + 1;
}
# %&&
# see C++ &cref/factorial_by_value/example_function/factorial_by_value/&&.
#
# &head message_of_void&&
# &srccode%cpp%
if( pl_example::message_of_void() == "OK" )
{	print "pl_example::message_of_void: OK\n"; }
else
{	print "pl_example::message_of_void: Error\n";
	$error_count = $error_count + 1;
}
# %&&
# see C++ &cref/message_of_void/example_function/message_of_void/&&.
#
# &head int_class&&
# &srccode%cpp%
$obj = new pl_example::int_class();
pl_example::add_by_ptr(3, 4, $obj);
if( $obj->value() == 7 )
{	print "pl_example::add_by_ptr: OK\n"; }
else
{	print "pl_example::add_by_ptr: Error\n";
	$error_count = $error_count + 1;
}
# %&&
# see Swig &cref/int_class/example.i/int_class/&& and
# C++ &cref/add_by_ptr/example_function/add_by_ptr/&&.
#
# &head int_array_ptr&&
# &srccode%cpp%
$n = 10;
$array_ptr = pl_example::new_int_array_ptr($n);
for($i = 0; $i < $n; $i++)
{	pl_example::int_array_ptr_setitem($array_ptr, $i, 2 * $i); }
#
if( pl_example::max_array_by_ptr($n, $array_ptr) == 18 )
{	print "pl_example::max_array_by_ptr: pointer: OK\n"; }
else
{	print "pl_example::max_array_by_ptr: pointer: Error\n";
	$error_count = $error_count + 1;
}
pl_example::delete_int_array_ptr($array_ptr);
# %&&
# see Swig &cref/int_array_ptr/example.i/int_array_ptr/&& and
# C++ &cref/max_array_by_ptr/example_function/max_array_by_ptr/&&.
#
# &head int_array_class&&
# &srccode%cpp%
$n         = 10;
$array_obj = new pl_example::int_array_class($n);
for($i = 0; $i < $n; $i++)
{	$array_obj[$i] = 2 * i; }
if( pl_example::max_array_by_ptr($n, $array_obj) == 18 )
{	print "pl_example::max_array_by_ptr: class: OK\n"; }
else
{	print "pl_example::max_array_by_ptr: class: Error\n";
	$error_count = $error_count + 1;
}
# %&&
# see Swig &cref/int_array_class/example.i/int_array_class/&& and
# C++ &cref/max_array_by_ptr/example_function/max_array_by_ptr/&&.
#
# &head vector_double&&
# &srccode%cpp%
$n   = 10;
$vec = new pl_example::vector_double($n);
for($i = 0; $i < $n; $i++)
{	$vec->set($i, 2.0 * $i); }
#
if( pl_example::max_std_vector_double($vec) == 18.0 )
{	print "pl_example::max_std_vector_double: class: OK\n"; }
else
{	print "pl_example::max_std_vector_double: class: Error\n";
	$error_count = $error_count + 1;
}
# %&&
# see Swig &cref/vector_double/example.i/vector_double/&& and
# C++ &cref/max_std_vector_double/example_function/max_std_vector_double/&&.
#
# &head raise_exception&&
# &srccode%cpp%
$message = "";
eval { pl_example::raise_exception("test message\n"); };
if( $@ )
{	$message = pl_example::raise_exception(""); }
if( $message == "test message" )
{	print "pl_example::pl_example::raise_exception: OK\n"; }
else
{	print "pl_example::raise_exception.message_of_void: Error\n";
	$error_count = $error_count + 1;
}
# %&&
# see C++ &cref/raise_exception/example_function/raise_exception/&&.
#
# &head normal_class&&
# &srccode%cpp%
$two   = new pl_example::normal_class(2);
$three = new pl_example::normal_class(3);
$five  = $two + $three;
$check = new pl_example::normal_class(5);
$ok    = $five == $check;
$ok    = $ok and 4 < $five->value()  and $five->value() < 6;
if( ok )
{	print "pl_example::normal_class: OK\n"; }
else
{	print "pl_example::normal_class: Error\n";
	$error_count = $error_count + 1;
}
# %&&
# see C++ &cref example_normal_class&&.
#
# &head double_class&&
# &srccode%cpp%
$two   = new pl_example::double_class(2.0);
$three = new pl_example::double_class(3.0);
$five  = $two + $three;
$check = new pl_example::double_class(5.0);
$ok    = $five == $check;
$ok    = $ok and 4.5 < $five->value()  and $five->value() < 5.5;
if( ok )
{	print "pl_example::double_class: OK\n"; }
else
{	print "pl_example::double_class: Error\n";
	$error_count = $error_count + 1;
}
# %&&
# see Swig &cref/double_class/example.i/double_class/&&.
#
# &head Set Exit Code&&
# &srccode%cpp%
if( $error_count == 0 )
{	exit 0; }
exit 1;
# %&&
#
# &end
