// --------------------------------------------------------------------------
//         cppad_py: A C++ Object Library and Python Interface to Cppad
//          Copyright (C) 2017-20 Bradley M. Bell (bradbell@seanet.com)
//              This program is distributed under the terms of the
//              GNU General Public License version 3.0 or later see
//                    https://www.gnu.org/licenses/gpl-3.0.txt
/*
------------------------------------------------------------------------------
{xsrst_begin_parent file_exam}

File Example
############

{xsrst_file
    // BEGIN_SRC
    // END_SRC
}

{xsrst_end file_exam}
------------------------------------------------------------------------------
*/
// BEGIN_SRC
// BEGIN_FACTORIAL
template<class T> factorial(const T& n)
{   if n == static_cast<T>(1)
        return n;
    return n * factorial(n - 1);
}
// END_FACTORIAL
//
// BEGIN_SQUARE
template<class T> square(const T& x)
// END_SQUARE
{   return x * x;
}
/*
------------------------------------------------------------------------------
{xsrst_begin file_res}

File Result
###########

factorial
*********
{xsrst_file
    // BEGIN_FACTORIAL
    // END_FACTORIAL
}

square
******
{xsrst_file
    // BEGIN_SQUARE
    // END_SQUARE
}

{xsrst_end file_res}
------------------------------------------------------------------------------
*/
// END_SRC
