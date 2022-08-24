// --------------------------------------------------------------------------
//         cppad_py: A C++ Object Library and Python Interface to Cppad
//          Copyright (C) 2017-22 Bradley M. Bell (bradbell@seanet.com)
//              This program is distributed under the terms of the
//              GNU General Public License version 3.0 or later see
//                    https://www.gnu.org/licenses/gpl-3.0.txt
/*
------------------------------------------------------------------------------
{xrst_begin_parent file_exam}

File Example
############

{xrst_literal
    // BEGIN_SRC
    // END_SRC
}

{xrst_end file_exam}
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
{xrst_begin file_res}

File Result
###########

factorial
*********
{xrst_literal
    // BEGIN_FACTORIAL
    // END_FACTORIAL
}

square
******
{xrst_literal
    // BEGIN_SQUARE
    // END_SQUARE
}

{xrst_end file_res}
------------------------------------------------------------------------------
*/
// END_SRC
