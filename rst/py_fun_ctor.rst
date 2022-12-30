.. _py_fun_ctor-name:

!!!!!!!!!!!
py_fun_ctor
!!!!!!!!!!!

.. raw:: html

   <a href="_sources/py_fun_ctor.rst.txt">View page source</a>

.. meta::
   :keywords: py_fun_ctor, stop, current, recording, store, function, object

.. index:: py_fun_ctor, stop, current, recording, store, function, object

.. _py_fun_ctor-title:

Stop Current Recording and Store Function Object
################################################

.. meta::
   :keywords: syntax

.. index:: syntax

.. _py_fun_ctor@Syntax:

Syntax
******

.. meta::
   :keywords: d_fun

.. index:: d_fun

.. _py_fun_ctor@Syntax@d_fun:

d_fun
=====

| *f* =  ``cppad_py.d_fun`` ( *ax* , *ay* )
| *f* =  ``cppad_py.d_fun`` ()

.. meta::
   :keywords: a_fun

.. index:: a_fun

.. _py_fun_ctor@Syntax@a_fun:

a_fun
=====

| *af* =  ``cppad_py.a_fun`` ( *f* )

.. meta::
   :keywords: ax

.. index:: ax

.. _py_fun_ctor@ax:

ax
**
This argument must be the same as
:ref:`ax<py_independent@ax>`
returned by the previous call to ``independent`` ; i.e.,
it must be the independent variable vector.
We use *n*
to denote the number of independent variables (the size of *ax* ).

.. meta::
   :keywords: ay

.. index:: ay

.. _py_fun_ctor@ay:

ay
**
This argument is a numpy array with ``a_double`` elements.
It specifies the dependent variables.
We use *m*
to denote the number of dependent variables (the size of *ay* ).

.. meta::
   :keywords: f

.. index:: f

.. _py_fun_ctor@f:

f
*
This result is a function object that
has a representation for the floating point operations
that mapped the independent variables *ax*
to the dependent variables *ay* .
This object computes function and derivative values using
``double``

.. meta::
   :keywords: empty, function

.. index:: empty, function

.. _py_fun_ctor@f@Empty Function:

Empty Function
==============
In the case where *ax* and *ay* are not present
the function is 'empty' and all its sizes are zero; see
:ref:`cpp_fun_property-name`.

.. meta::
   :keywords: af

.. index:: af

.. _py_fun_ctor@af:

af
**
This result is a function object that
has a representation for the same function as *f* .
This object computes function and derivative values using
``a_double``
Initially, there are not Taylor coefficient stored in *af* ; i.e.,
:ref:`af_size_order()<py_fun_property@size_order>` is zero.

.. meta::
   :keywords: example

.. index:: example

.. _py_fun_ctor@Example:

Example
*******
All of the examples use the ``d_fun`` constructor.
The example :ref:`a_fun_xam_py-name` demonstrates the purpose of
``a_fun`` objects.

.. toctree::
   :maxdepth: 1
   :hidden:

   a_fun_xam_py
