.. _cpp_fun_jacobian-name:

!!!!!!!!!!!!!!!!
cpp_fun_jacobian
!!!!!!!!!!!!!!!!

.. raw:: html

   <a href="_sources/cpp_fun_jacobian.rst.txt">View page source</a>

.. meta::
   :keywords: cpp_fun_jacobian, jacobian, an, ad, function

.. index:: cpp_fun_jacobian, jacobian, an, ad, function

.. _cpp_fun_jacobian-title:

Jacobian of an AD Function
##########################

.. meta::
   :keywords: syntax

.. index:: syntax

.. _cpp_fun_jacobian@Syntax:

Syntax
******
*J* = *f*\ ``.jacobian`` ( *x* )

.. meta::
   :keywords: f

.. index:: f

.. _cpp_fun_jacobian@f:

f
*
This is either a
:ref:`d_fun<cpp_fun_ctor@Syntax@d_fun>` or
:ref:`a_fun<cpp_fun_ctor@Syntax@a_fun>` function object.
Upon return, the zero order
:ref:`taylor_coefficients<cpp_fun_forward@Taylor Coefficient>` in *f*
correspond to the value of *x* .
The other Taylor coefficients in *f* are unspecified.

.. meta::
   :keywords: f(x)

.. index:: f(x)

.. _cpp_fun_jacobian@f(x):

f(x)
****
We use the notation :math:`f: \B{R}^n \rightarrow \B{R}^m`
for the function corresponding to *f* .
Note that *n* is the size of :ref:`ax<cpp_fun_ctor@ax>`
and *m* is the size of :ref:`ay<cpp_fun_ctor@ay>`
in to the constructor for *f* .

.. meta::
   :keywords: x

.. index:: x

.. _cpp_fun_jacobian@x:

x
*
If *f* is a ``d_fun`` or ``a_fun`` ,
this argument has prototype

| |tab| ``const vec_double&`` *x*
| |tab| ``const vec_a_double&`` *x*

and its size must be *n* .
It specifies the argument value at we are computing the Jacobian
:math:`f'(x)`.

.. meta::
   :keywords: j

.. index:: j

.. _cpp_fun_jacobian@J:

J
*
If *f* is a ``d_fun`` or ``a_fun`` ,
the result has prototype

| |tab| ``vec_double`` *J*
| |tab| ``vec_a_double`` *J*

respectively and its size is *m* ``*`` *n* .
For *i* between zero and *m* -1
and *j* between zero and *n* -1 ,

.. math::

   J [ i * n + j ] = \frac{ \partial f_i }{ \partial x_j } (x)

.. meta::
   :keywords: example

.. index:: example

.. _cpp_fun_jacobian@Example:

Example
*******
:ref:`fun_jacobian_xam_cpp-name`

.. toctree::
   :maxdepth: 1
   :hidden:

   fun_jacobian_xam_cpp
