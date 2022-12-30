.. _cpp_fun_hessian-name:

!!!!!!!!!!!!!!!
cpp_fun_hessian
!!!!!!!!!!!!!!!

.. raw:: html

   <a href="_sources/cpp_fun_hessian.rst.txt">View page source</a>

.. meta::
   :keywords: cpp_fun_hessian, hessian, an, ad, function

.. index:: cpp_fun_hessian, hessian, an, ad, function

.. _cpp_fun_hessian-title:

Hessian of an AD Function
#########################

.. meta::
   :keywords: syntax

.. index:: syntax

.. _cpp_fun_hessian@Syntax:

Syntax
******
*H* = *f*\ ``.hessian`` ( *x* , *w* )

.. meta::
   :keywords: f

.. index:: f

.. _cpp_fun_hessian@f:

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

.. _cpp_fun_hessian@f(x):

f(x)
****
We use the notation :math:`f: \B{R}^n \rightarrow \B{R}^m`
for the function corresponding to *f* .
Note that *n* is the size of :ref:`ax<cpp_fun_ctor@ax>`
and *m* is the size of :ref:`ay<cpp_fun_ctor@ay>`
in to the constructor for *f* .

.. meta::
   :keywords: g(x)

.. index:: g(x)

.. _cpp_fun_hessian@g(x):

g(x)
****
We use the notation :math:`g: \B{R}^n \rightarrow \B{R}`
for the function defined by

.. math::

   g(x) = \sum_{i=0}^{n-1} w_i f_i (x)

.. meta::
   :keywords: x

.. index:: x

.. _cpp_fun_hessian@x:

x
*
If *f* is a ``d_fun`` or ``a_fun`` ,
this argument has prototype

| |tab| ``const vec_double&`` *x*
| |tab| ``const vec_a_double&`` *x*

and its size must be *n* .
It specifies the argument value at we are computing the Hessian
:math:`g^{(2)}(x)`.

.. meta::
   :keywords: w

.. index:: w

.. _cpp_fun_hessian@w:

w
*
If *f* is a ``d_fun`` or ``a_fun`` ,
this argument has prototype

| |tab| ``const vec_double&`` *w*
| |tab| ``const vec_a_double&`` *w*

and its size must be *m* .
It specifies the vector *w* in the definition of :math:`g(x)` above.

.. meta::
   :keywords: h

.. index:: h

.. _cpp_fun_hessian@H:

H
*
If *f* is a ``d_fun`` or ``a_fun`` ,
the result has prototype

| |tab| ``vec_double`` *H*
| |tab| ``vec_a_double`` *H*

and its size is *n* ``*`` *n* .
For *i* between zero and *n* -1
and *j* between zero and *n* -1 ,

.. math::

   H [ i * n + j ] = \frac{ \partial^2 g }{ \partial x_i \partial x_j } (x)

.. meta::
   :keywords: example

.. index:: example

.. _cpp_fun_hessian@Example:

Example
*******
:ref:`fun_hessian_xam_cpp-name`

.. toctree::
   :maxdepth: 1
   :hidden:

   fun_hessian_xam_cpp
