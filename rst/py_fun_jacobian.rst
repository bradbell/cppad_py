.. _py_fun_jacobian-name:

!!!!!!!!!!!!!!!
py_fun_jacobian
!!!!!!!!!!!!!!!

.. raw:: html

   <a href="_sources/py_fun_jacobian.rst.txt">View page source</a>

.. meta::
   :keywords: py_fun_jacobian, jacobian, an, ad, function

.. index:: py_fun_jacobian, jacobian, an, ad, function

.. _py_fun_jacobian-title:

Jacobian of an AD Function
##########################

.. meta::
   :keywords: syntax

.. index:: syntax

.. _py_fun_jacobian@Syntax:

Syntax
******
*J* = *f*\ ``.jacobian`` ( *x* )

.. meta::
   :keywords: f

.. index:: f

.. _py_fun_jacobian@f:

f
*
This is either a
:ref:`d_fun<py_fun_ctor@Syntax@d_fun>` or
:ref:`a_fun<py_fun_ctor@Syntax@a_fun>` function object.
Upon return, the zero order
:ref:`taylor_coefficients<py_fun_forward@Taylor Coefficient>`
in *f* correspond to the value of *x* .
The other Taylor coefficients in *f* are unspecified.

.. meta::
   :keywords: f(x)

.. index:: f(x)

.. _py_fun_jacobian@f(x):

f(x)
****
We use the notation :math:`f: \B{R}^n \rightarrow \B{R}^m`
for the function corresponding to *f* .
Note that *n* is the size of :ref:`ax<py_fun_ctor@ax>`
and *m* is the size of :ref:`ay<py_fun_ctor@ay>`
in to the constructor for *f* .

.. meta::
   :keywords: x

.. index:: x

.. _py_fun_jacobian@x:

x
*
If *f* is a ``d_fun`` or ``a_fun`` ,
*x* is a numpy vector with ``float`` ( ``a_double`` ) elements
and size *n* .
It specifies the argument value at we are computing the Jacobian
:math:`f'(x)`.

.. meta::
   :keywords: j

.. index:: j

.. _py_fun_jacobian@J:

J
*
The result is a numpy matrix with ``float`` ( ``a_double`` ) elements,
*m* rows, and ``n`` columns.
For *i* between zero and *m* -1
and *j* between zero and *n* -1 ,

.. math::

   J [ i,  j ] = \frac{ \partial f_i }{ \partial x_j } (x)

.. meta::
   :keywords: example

.. index:: example

.. _py_fun_jacobian@Example:

Example
*******
:ref:`fun_jacobian_xam_py-name`

.. toctree::
   :maxdepth: 1
   :hidden:

   fun_jacobian_xam_py
