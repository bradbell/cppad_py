# ifndef CPPAD_PY_SPARSE_HPP
# define CPPAD_PY_SPARSE_HPP
// SPDX-License-Identifier: GPL-3.0-or-later
// SPDX-FileCopyrightText: Bradley M. Bell <bradbell@seanet.com>
// SPDX-FileContributor: 2017-22 Bradley M. Bell
// ----------------------------------------------------------------------------
# include <vector>
# include <cppad/utility/sparse_rcv.hpp>
# include <cppad/py/public_lib.hpp>

// declarations without definitions
namespace CppAD {
   template <class SizeVector> class sparse_rc;
   class sparse_jac_work;
   class sparse_hes_work;
}

namespace cppad_py { // BEGIN_CPPAD_PY_NAMESPACE

// Swig class that acts the same as CppAD::sparse_rc< std::vector<size_t> >
class CPPAD_PY_LIB_PUBLIC sparse_rc
{  // private members are not in Swig interface
   private:
   // sparse_rc< std::vector<size_t> > representation
   CppAD::sparse_rc< std::vector<size_t> >* ptr_;
   // -----------------------------------------------------------------------
   // forbidden default member functions
   sparse_rc(const sparse_rc& other)
   {  assert(false); }
   void operator=(const sparse_rc& other)
   {  assert(false); }
   // -----------------------------------------------------------------------
   // public members not in Swig interface (see %ignore ptr)
   public:
   const CppAD::sparse_rc< std::vector<size_t> >* ptr(void) const;
   CppAD::sparse_rc< std::vector<size_t> >* ptr(void);
   // -----------------------------------------------------------------------
   // public members in Swig interface
   public:
   // constructor
   sparse_rc(void);
   // destructor
   ~sparse_rc(void);
   // resize
   void resize(int nr, int nc, int nnz);
   // number of rows in matrix
   int nr(void) const;
   // number of columns in matrix
   int nc(void) const;
   // number of possibly non-zero elements in matrix
   int nnz(void) const;
   // set row and column for a possibly non-zero element
   void put(int k, int r, int c);
   // row indices
   std::vector<int> row(void) const;
   // column indices
   std::vector<int> col(void) const;
   // row-major order
   std::vector<int> row_major(void) const;
   // column-major order
   std::vector<int> col_major(void) const;
   // -----------------------------------------------------------------------
};

// Swig class that acts the same as
// CppAD::sparse_rcv< std::vector<size_t>, std::vector<double> >
class CPPAD_PY_LIB_PUBLIC sparse_rcv
{  // private members are not in Swig interface
   private:
   // CppAD representation
   CppAD::sparse_rcv< std::vector<size_t>, std::vector<double> >* ptr_;
   // -----------------------------------------------------------------------
   // forbidden default member functions
   sparse_rcv(void)
   {  assert(false); }
   // -----------------------------------------------------------------------
   // public members not in Swig interface (see %ignore ptr)
   public:
   CppAD::sparse_rcv< std::vector<size_t> , std::vector<double> >* ptr(void);
   // -----------------------------------------------------------------------
   // public members are in Swig interface
   public:
   // constructors
   sparse_rcv(const sparse_rc& pattern);
   sparse_rcv(const sparse_rcv& other);
   // destructor
   ~sparse_rcv(void);
   // set k-th possibly non-zero value
   void put(int k, const double v);
   // number of rows in matrix
   int nr(void) const;
   // number of columns in matrix
   int nc(void) const;
   // number of possibly non-zero elements in matrix
   int nnz(void) const;
   // row indices
   std::vector<int> row(void) const;
   // column indices
   std::vector<int> col(void) const;
   // value of possibly non-zero matrix elements
   std::vector<double> val(void) const;
   // row-major order
   std::vector<int> row_major(void) const;
   // column-major order
   std::vector<int> col_major(void) const;
};

// Swig class that acts the same as CppAD::sparse_jac_work
class CPPAD_PY_LIB_PUBLIC sparse_jac_work
{  // private members not in Swig interface
   private:
   // CppAD::sparse_rc< std::vector<size_t> > representation
   CppAD::sparse_jac_work* ptr_;
   // -----------------------------------------------------------------------
   // public members not in Swig interface (see %ignore ptr)
   public:
   CppAD::sparse_jac_work* ptr(void);
   // -----------------------------------------------------------------------
   // public members are in Swig interface
   public:
   // constructor
   sparse_jac_work(void);
   // destructor
   ~sparse_jac_work(void);
   // clear
   void clear(void);
};


// Swig class that acts the same as CppAD::sparse_hes_work
class CPPAD_PY_LIB_PUBLIC sparse_hes_work
{  // private members not in Swig interface
   private:
   // CppAD::sparse_rc< std::vector<size_t> > representation
   CppAD::sparse_hes_work* ptr_;
   // -----------------------------------------------------------------------
   // public members not in Swig interface (see %ignore ptr)
   public:
   CppAD::sparse_hes_work* ptr(void);
   // -----------------------------------------------------------------------
   // public members are in Swig interface
   public:
   // constructor
   sparse_hes_work(void);
   // destructor
   ~sparse_hes_work(void);
   // clear
   void clear(void);
};

} // END_CPPAD_PY_NAMESPACE

# endif
