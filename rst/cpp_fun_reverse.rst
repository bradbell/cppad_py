.. _cpp_fun_reverse-name:

!!!!!!!!!!!!!!!
cpp_fun_reverse
!!!!!!!!!!!!!!!

.. raw:: html

   <a href="_sources/cpp_fun_reverse.rst.txt">View page source</a>

.. meta::
   :keywords: cpp_fun_reverse, reverse, mode, ad

.. index:: cpp_fun_reverse, reverse, mode, ad

.. _cpp_fun_reverse-title:

Reverse Mode AD
###############

.. meta::
   :keywords: syntax

.. index:: syntax

.. _cpp_fun_reverse@Syntax:

Syntax
******
*xq* = *f*\ ``.reverse`` ( *q* , *yq* )

.. meta::
   :keywords: f

.. index:: f

.. _cpp_fun_reverse@f:

f
*
This is either a
:ref:`d_fun<cpp_fun_ctor@Syntax@d_fun>` or
:ref:`a_fun<cpp_fun_ctor@Syntax@a_fun>` function object
and is effectively ``const`` .
(Some details that are not visible to the user may change.)

.. meta::
   :keywords: notation

.. index:: notation

.. _cpp_fun_reverse@Notation:

Notation
********

.. meta::
   :keywords: f(x)

.. index:: f(x)

.. _cpp_fun_reverse@Notation@f(x):

f(x)
====
We use the notation :math:`f: \B{R}^n \rightarrow \B{R}^m`
for the function corresponding to *f* .
Note that *n* is the size of :ref:`ax<cpp_fun_ctor@ax>`
and *m* is the size of :ref:`ay<cpp_fun_ctor@ay>`
in to the constructor for *f* .

.. meta::
   :keywords: x(t),, s

.. index:: x(t),, s

.. _cpp_fun_reverse@Notation@X(t), S:

X(t), S
=======
This is the same function as
:ref:`x(t)<cpp_fun_forward@X(t)>` in the previous call to
*f*\ ``.forward`` .
We use :math:`S \in \B{R}^{n \times q}` to denote the Taylor coefficients
of :math:`X(t)`.

.. meta::
   :keywords: y(t),, t

.. index:: y(t),, t

.. _cpp_fun_reverse@Notation@Y(t), T:

Y(t), T
=======
This is the same function as
:ref:`y(t)<cpp_fun_forward@Y(t)>` in the previous call to
*f*\ ``.forward`` .
We use :math:`T \in \B{R}^{m \times q}` to denote the Taylor coefficients
of :math:`Y(t)`.
We also use the notation :math:`T(S)` to express the fact that
the Taylor coefficients for :math:`Y(t)` are a function of the
Taylor coefficients of :math:`X(t)`.

.. meta::
   :keywords: g(t)

.. index:: g(t)

.. _cpp_fun_reverse@Notation@G(T):

G(T)
====
We use the notation :math:`G : \B{R}^{m \times p} \rightarrow \B{R}`
for a function that the calling routine chooses.

.. meta::
   :keywords: q

.. index:: q

.. _cpp_fun_reverse@q:

q
*
This argument has prototype

| |tab| ``int`` *q*

and is positive.
It is the number of the Taylor coefficient (for each variable)
that we are computing the derivative with respect to.
It must be greater than zero, and
less than or equal
the number of Taylor coefficient stored in *f* ; i.e.,
:ref:`f_size_order()<cpp_fun_property@size_order>`.

.. meta::
   :keywords: yq

.. index:: yq

.. _cpp_fun_reverse@yq:

yq
**
If *f* is a ``d_fun`` or ``a_fun`` ,
this argument has prototype

| |tab| ``const vec_double&`` *yq*
| |tab| ``const vec_a_double&`` *yq*

and its size must be *m* ``*`` *q* .
For 0 <= *i* < *m* and 0 <= *k* < *q* ,
*yq* [ *i* ``*`` *q* + *k* ] is the partial derivative of
:math:`G(T)` with respect to the *k*-th order Taylor coefficient
for the *i*-th component function; i.e.,
the partial derivative of :math:`G(T)` w.r.t. :math:`Y_i^{(k)} (t) / k !`.

.. meta::
   :keywords: xq

.. index:: xq

.. _cpp_fun_reverse@xq:

xq
**
If *f* is a ``d_fun`` or ``a_fun`` ,
the result has prototype

| |tab| ``const vec_double&`` *xq*
| |tab| ``const vec_a_double&`` *xq*

respectively and its size is *n* ``*`` *q* .
For 0 <= *j* < *n* and 0 <= *k* < *q* ,
*xq* [ *j* ``*`` *q* + *k* ] is the partial derivative of
:math:`G(T(S))` with respect to the *k*-th order Taylor coefficient
for the *j*-th component function; i.e.,
the partial derivative of
:math:`G(T(S))` w.r.t. :math:`S_j^{(k)} (t) / k !`.

.. meta::
   :keywords: example

.. index:: example

.. _cpp_fun_reverse@Example:

Example
*******
:ref:`fun_reverse_xam_cpp-name`

.. toctree::
   :maxdepth: 1
   :hidden:

   fun_reverse_xam_cpp
