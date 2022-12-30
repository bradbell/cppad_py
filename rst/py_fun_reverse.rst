.. _py_fun_reverse-name:

!!!!!!!!!!!!!!
py_fun_reverse
!!!!!!!!!!!!!!

.. raw:: html

   <a href="_sources/py_fun_reverse.rst.txt">View page source</a>

.. meta::
   :keywords: py_fun_reverse, reverse, mode, ad

.. index:: py_fun_reverse, reverse, mode, ad

.. _py_fun_reverse-title:

Reverse Mode AD
###############

.. meta::
   :keywords: syntax

.. index:: syntax

.. _py_fun_reverse@Syntax:

Syntax
******
*xq* = *f*\ ``.reverse`` ( *q* , *yq* )

.. meta::
   :keywords: f

.. index:: f

.. _py_fun_reverse@f:

f
*
This is either a
:ref:`d_fun<py_fun_ctor@Syntax@d_fun>` or
:ref:`a_fun<py_fun_ctor@Syntax@a_fun>` function object
and is effectively constant; i.e., not changed.

.. meta::
   :keywords: notation

.. index:: notation

.. _py_fun_reverse@Notation:

Notation
********

.. meta::
   :keywords: f(x)

.. index:: f(x)

.. _py_fun_reverse@Notation@f(x):

f(x)
====
We use the notation :math:`f: \B{R}^n \rightarrow \B{R}^m`
for the function corresponding to *f* .
Note that *n* is the size of :ref:`ax<py_fun_ctor@ax>`
and *m* is the size of :ref:`ay<py_fun_ctor@ay>`
in to the constructor for *f* .

.. meta::
   :keywords: x(t),, s

.. index:: x(t),, s

.. _py_fun_reverse@Notation@X(t), S:

X(t), S
=======
This is the same function as
:ref:`x(t)<py_fun_forward@X(t)>` in the previous call to
*f*\ ``.forward`` .
We use :math:`S \in \B{R}^{n \times q}` to denote the Taylor coefficients
of :math:`X(t)`.

.. meta::
   :keywords: y(t),, t

.. index:: y(t),, t

.. _py_fun_reverse@Notation@Y(t), T:

Y(t), T
=======
This is the same function as
:ref:`y(t)<py_fun_forward@Y(t)>` in the previous call to
*f*\ ``.forward`` .
We use :math:`T \in \B{R}^{m \times q}` to denote the Taylor coefficients
of :math:`Y(t)`.
We also use the notation :math:`T(S)` to express the fact that
the Taylor coefficients for :math:`Y(t)` are a function of the
Taylor coefficients of :math:`X(t)`.

.. meta::
   :keywords: g(t)

.. index:: g(t)

.. _py_fun_reverse@Notation@G(T):

G(T)
====
We use the notation :math:`G : \B{R}^{m \times p} \rightarrow \B{R}`
for a function that the calling routine chooses.

.. meta::
   :keywords: q

.. index:: q

.. _py_fun_reverse@q:

q
*
This argument has type ``int`` and is positive.
It is the number of the Taylor coefficient (for each variable)
that we are computing the derivative with respect to.
It must be greater than zero, and less than or equal
the number of Taylor coefficient stored in *f* ; i.e.,
:ref:`f_size_order()<py_fun_property@size_order>`.

.. meta::
   :keywords: yq

.. index:: yq

.. _py_fun_reverse@yq:

yq
**
If *f* is a ``d_fun`` ( ``a_fun`` ) object, *yq*
is a numpy vector with ``float`` ( ``a_double`` ) elements,
*m* rows and *q* columns.
For 0 <= *i* < *m* and 0 <= *k* < *q* ,
*yq* [ *i* , *k* ] is the partial derivative of
:math:`G(T)` with respect to the *k*-th order Taylor coefficient
for the *i*-th component function; i.e.,
the partial derivative of :math:`G(T)` w.r.t. :math:`Y_i^{(k)} (t) / k !`.

.. meta::
   :keywords: xq

.. index:: xq

.. _py_fun_reverse@xq:

xq
**
The result is a numpy vector with ``float`` ( ``a_double`` ) elements,
*n* rows and *q* columns.
For 0 <= *j* < *n* and 0 <= *k* < *q* ,
*xq* [ *j* , *k* ] is the partial derivative of
:math:`G(T(S))` with respect to the *k*-th order Taylor coefficient
for the *j*-th component function; i.e.,
the partial derivative of
:math:`G(T(S))` w.r.t. :math:`S_j^{(k)} (t) / k !`.

.. meta::
   :keywords: example

.. index:: example

.. _py_fun_reverse@Example:

Example
*******
:ref:`fun_reverse_xam_py-name`

.. toctree::
   :maxdepth: 1
   :hidden:

   fun_reverse_xam_py
