# ifndef CPPAD_PY_BUILD_TYPE_HPP
# define CPPAD_PY_BUILD_TYPE_HPP
// SPDX-License-Identifier: GPL-3.0-or-later
// SPDX-FileCopyrightText: Bradley M. Bell <bradbell@seanet.com>
// SPDX-FileContributor: 2017-23 Bradley M. Bell
// ----------------------------------------------------------------------------
/*
-----------------------------------------------------------------------------
{xrst_begin build_type}

Get The cppad_py build_type
###########################

Prototype
*********
{xrst_literal
   // BEGIN PROTOTYPE
   // END PROTOTYPE
}

{xrst_toc_hidden
   example/cplusplus/build_type_xam.cpp
   example/python/core/build_type_xam.py
}
Example
*******
:ref:`c++<build_type_xam.cpp-name>`,
:ref:`python<build_type_xam.py-name>`.

{xrst_end build_type}
*/
# include <cppad/py/build_type.hpp>

namespace cppad_py {

   // BEGIN PROTOTYPE
   const char* build_type(void)
   // END PROTOTYPE
   {
# ifdef NDEBUG
      return "release";
# else
      return "debug";
# endif
   }
}


# endif
