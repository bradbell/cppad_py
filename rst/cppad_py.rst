.. _cppad_py-name:

!!!!!!!!
cppad_py
!!!!!!!!

.. raw:: html

   <a href="_sources/cppad_py.rst.txt">View page source</a>

.. comment:  -------------------------------------------------------------
   default automatic indexing command for all cppad_py documentation

.. comment:  -------------------------------------------------------------
   Latex macros used throughout Cppad Py documentation

.. meta::
   :keywords: cppad_py, c++, object, library, python, interface, to, cppad

.. index:: cppad_py, c++, object, library, python, interface, to, cppad

.. _cppad_py-title:

A C++ Object Library and Python Interface to CppAD
##################################################

.. meta::
   :keywords: version

.. index:: version

.. _cppad_py@Version:

Version
*******
cppad_py-2022.12.30

.. meta::
   :keywords: git, repository

.. index:: git, repository

.. _cppad_py@Git Repository:

Git Repository
**************
`<https://github.com/bradbell/cppad_py>`_

.. meta::
   :keywords: purpose

.. index:: purpose

.. _cppad_py@Purpose:

Purpose
*******

#. Provide a connection from Python to the
   Algorithmic Differentiation (AD) package Cppad; see :ref:`py_lib-name`.
#. Provide an AD object library; see :ref:`cpp_lib-name`.
#. Provide a concrete example of how
   `cppad_swig <https://github.com/bradbell/cppad_swig>`_
   can be used to connect any scripting language to CppAD.

.. meta::
   :keywords: getting, started

.. index:: getting, started

.. _cppad_py@Getting Started:

Getting Started
***************
After you :ref:`configure<setup_py@Configure>` and
:ref:`install<setup_py@Install>` cppad_py,
the following example is a good place to get started using it:
:ref:`fun_jacobian_xam_py-title`.

.. meta::
   :keywords: numerical, examples

.. index:: numerical, examples

.. _cppad_py@Numerical Examples:

Numerical Examples
******************
The following is a link to some numerical examples:
:ref:`numeric_xam-name`.

.. meta::
   :keywords: c++, function, speed

.. index:: c++, function, speed

.. _cppad_py@C++ Function Speed:

C++ Function Speed
******************
One can use Cppad Py to get faster function evaluation in scripting Python,
when the sequence of floating point operations does not depend on the
independent variables.
Once an :ref:`py_fun-name` is recorded, zero order
:ref:`forward_mode<py_fun_forward-name>` can be used to
effectively evaluate the function in C++ instead of Python.

.. meta::
   :keywords: license

.. index:: license

.. _cppad_py@License:

License
*******
This program is distributed under the terms of the
GNU General Public License version 3.0 or later see
`gpl-3.0.txt <http://www.gnu.org/licenses/gpl-3.0.txt>`_.

.. meta::
   :keywords: children

.. index:: children

.. _cppad_py@Children:

Children
********

.. csv-table::
   :header:  "Child", "Title"
   :widths: auto

   "setup_py", :ref:`setup_py-title`
   "numeric_xam", :ref:`numeric_xam-title`
   "library", :ref:`library-title`
   "release_notes", :ref:`release_notes-title`

.. toctree::
   :maxdepth: 1
   :hidden:

   setup_py
   numeric_xam
   library
   release_notes
