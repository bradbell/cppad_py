/* -----------------------------------------------------------------------------
           cppad_py: A C++ Object Library and Python Interface to Cppad
         Copyright (C) 2017-22 Bradley M. Bell (bradbell@seanet.com)
            This program is distributed under the terms of the
            GNU General Public License version 3.0 or later see
                      https://www.gnu.org/licenses/gpl-3.0.txt
----------------------------------------------------------------------------- */
# include <cppad/py/cpp_convert.hpp>
namespace cppad_py { // BEGIN_CPPAD_PY_NAMESPACE
/*
-------------------------------------------------------------------------------
{xrst_begin_parent cpp_convert}
{xrst_spell
   cppad
}

Convert Objects Between cppad_mixed and cppad_py
################################################

Children
********
{xrst_toc_table
}

{xrst_end cpp_convert}
-------------------------------------------------------------------------------
{xrst_begin ad_vec_std2cppad}
{xrst_spell
   cppad
}


Convert AD Vector From Standard to CppAD
########################################

Syntax
******

| *v_out* =  ``cppad_py::ad_vec_std2cppad`` ( *v_in* )

Prototype
*********
{xrst_literal
   // BEGIN_AD_VEC_STD2CPPAD
   // END_AD_VEC_STD2CPPAD
}

{xrst_end ad_vec_std2cppad}
*/

// BEGIN_AD_VEC_STD2CPPAD
CppAD::vector< CppAD::AD<double> >
ad_vec_std2cppad(const std::vector<a_double>& v_in )
// END_AD_VEC_STD2CPPAD
{  CppAD::vector< CppAD::AD<double> > v_out( v_in.size() );
   for(size_t i = 0; i < v_in.size(); ++i)
      v_out[i] = *( v_in[i].ptr() );
   return v_out;
}
/*
-------------------------------------------------------------------------------
{xrst_begin ad_vec_cppad2std}
{xrst_spell
   cppad
}


Convert AD Vector From CppAD to Standard
########################################

Syntax
******

| *v_out* =  ``cppad_py::ad_vec_cppad2std`` ( *v_in* )

Prototype
*********
{xrst_literal
   // BEGIN_AD_VEC_CPPAD2STD
   // END_AD_VEC_CPPAD2STD
}

{xrst_end ad_vec_cppad2std}
*/

// BEGIN_AD_VEC_CPPAD2STD
std::vector<a_double>
ad_vec_cppad2std(const CppAD::vector< CppAD::AD<double> >& v_in )
// END_AD_VEC_CPPAD2STD
{  std::vector<a_double> v_out( v_in.size() );
   for(size_t i = 0; i < v_in.size(); ++i)
      *(v_out[i].ptr()) = v_in[i];
   return v_out;
}
/*
-------------------------------------------------------------------------------
{xrst_begin d_vec_std2cppad}
{xrst_spell
   cppad
}


Convert double Vector From Standard to CppAD
############################################

Syntax
******

| *v_out* =  ``cppad_py::d_vec_std2cppad`` ( *v_in* )

Prototype
*********
{xrst_literal
   // BEGIN_D_VEC_STD2CPPAD
   // END_D_VEC_STD2CPPAD
}

{xrst_end d_vec_std2cppad}
*/

// BEGIN_D_VEC_STD2CPPAD
CppAD::vector<double>
d_vec_std2cppad(const std::vector<double>& v_in )
// END_D_VEC_STD2CPPAD
{  CppAD::vector<double> v_out( v_in.size() );
   for(size_t i = 0; i < v_in.size(); ++i)
      v_out[i] = v_in[i];
   return v_out;
}
/*
-------------------------------------------------------------------------------
{xrst_begin d_vec_cppad2std}
{xrst_spell
   cppad
}


Convert double Vector From CppAD to Standard
############################################

Syntax
******

| *v_out* =  ``cppad_py::d_vec_cppad2std`` ( *v_in* )

Prototype
*********
{xrst_literal
   // BEGIN_D_VEC_CPPAD2STD
   // END_D_VEC_CPPAD2STD
}

{xrst_end d_vec_cppad2std}
*/

// BEGIN_D_VEC_CPPAD2STD
std::vector<double>
d_vec_cppad2std(const CppAD::vector<double>& v_in )
// END_D_VEC_CPPAD2STD
{  std::vector<double> v_out( v_in.size() );
   for(size_t i = 0; i < v_in.size(); ++i)
      v_out[i] = v_in[i];
   return v_out;
}

/*
-------------------------------------------------------------------------------
{xrst_begin mixed2sparse_rcv}
{xrst_spell
   cppad
   rcv
}

Convert Sparse Matrix from cppad_mixed to cppad_py
##################################################

Syntax
******

| *sparse_out* = ``cppad_py::mixed2sparse_rcv`` ( *sparse_in* )

Prototype
*********
{xrst_literal
   // BEGIN_MIXED2SPARSE_RCV
   // END_MIXED2SPARSE_RCV
}

Restriction
***********
This routine is only available when
:ref:`include_mixed <get_cppad_sh@Settings@include_mixed>` is true.

{xrst_end mixed2sparse_rcv}
*/
# ifdef INCLUDE_MIXED
// BEGIN_MIXED2SPARSE_RCV
sparse_rcv
mixed2sparse_rcv(const CppAD::mixed::d_sparse_rcv& mixed_rcv)
// END_MIXED2SPARSE_RCV
{  size_t nr  = mixed_rcv.nr();
   size_t nc  = mixed_rcv.nc();
   size_t nnz = mixed_rcv.nnz();
   sparse_rc result_rc;
   result_rc.resize(nr, nc, nnz);
   for(size_t k = 0; k < nnz; ++k)
      result_rc.put(k, mixed_rcv.row()[k], mixed_rcv.col()[k]);
   // --------------------------------------------------
   // cppad_py::sparse_rcv corresponding to result
   cppad_py::sparse_rcv result_rcv( result_rc );
   for(size_t k = 0; k < nnz; ++k)
      result_rcv.put(k, mixed_rcv.val()[k]);
   //
   return result_rcv;
}
# endif // INCLUDE_MIXED
// ----------------------------------------------------------------------------


} // END_CPPAD_PY_NAMESPACE
