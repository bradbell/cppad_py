.. _py_fun_forward-name:

!!!!!!!!!!!!!!
py_fun_forward
!!!!!!!!!!!!!!

.. raw:: html

   <a href="_sources/py_fun_forward.rst.txt">View page source</a>

.. meta::
   :keywords: py_fun_forward, forward, mode, ad

.. index:: py_fun_forward, forward, mode, ad

.. _py_fun_forward-title:

Forward Mode AD
###############

.. meta::
   :keywords: syntax

.. index:: syntax

.. _py_fun_forward@Syntax:

Syntax
******
*yp* = *f*\ ``.forward`` ( *p* , *xp* )

.. meta::
   :keywords: taylor, coefficient

.. index:: taylor, coefficient

.. _py_fun_forward@Taylor Coefficient:

Taylor Coefficient
******************
For a function :math:`g(t)` of a scalar argument :math:`t \in \B{R}`,
the *p*-th order Taylor coefficient is its
``p`` -th order derivative divided by *p* factorial
and evaluated at :math:`t = 0`; i.e.,

.. math::

   g^{(p)} (0) /  p !

.. meta::
   :keywords: f

.. index:: f

.. _py_fun_forward@f:

f
*
This is either a
:ref:`d_fun<py_fun_ctor@Syntax@d_fun>` or
:ref:`a_fun<py_fun_ctor@Syntax@a_fun>` function object.
Note that its state is changed by this operation because
all the Taylor coefficient that it calculates for every
variable in recording are stored.
See more discussion of this fact under the heading
:ref:`p<py_fun_forward@p>` below.

.. meta::
   :keywords: f(x)

.. index:: f(x)

.. _py_fun_forward@f(x):

f(x)
****
We use the notation :math:`f: \B{R}^n \rightarrow \B{R}^m`
for the function corresponding to *f* .
Note that *n* is the size of :ref:`ax<py_fun_ctor@ax>`
and *m* is the size of :ref:`ay<py_fun_ctor@ay>`
in to the constructor for *f* .

.. meta::
   :keywords: x(t)

.. index:: x(t)

.. _py_fun_forward@X(t):

X(t)
****
We use the notation :math:`X : \B{R} \rightarrow \B{R}^n`
for a function that the calling routine chooses.

.. meta::
   :keywords: y(t)

.. index:: y(t)

.. _py_fun_forward@Y(t):

Y(t)
****
We define the function :math:`Y : \B{R} \rightarrow \B{R}^n`
by :math:`Y(t) = f(X(t))`.

.. meta::
   :keywords: p

.. index:: p

.. _py_fun_forward@p:

p
*
This argument has type ``int`` and is non-negative.
Its value is the order of the Taylor coefficient being calculated.
If there was no call to ``forward`` for this *f* ,
the value of *p* must be zero.
Otherwise, it must be between zero and one greater that its
value for the previous call using this *f* .
After this call, the Taylor coefficients for orders zero though *p* ,
and for every variable in the recording, will be stored in *f* .

.. meta::
   :keywords: size_order

.. index:: size_order

.. _py_fun_forward@p@size_order:

size_order
==========
After this call,
:ref:`f_size_order()<py_fun_property@size_order>` is *p* +1 .

.. meta::
   :keywords: xp

.. index:: xp

.. _py_fun_forward@xp:

xp
**
If *f* is a ``d_fun`` ( ``a_fun`` ) object, *xp*
is a numpy vector with ``float`` ( ``a_double`` ) elements
and size *n* .
It specifies the *p*-th order Taylor coefficients for *X(t* ) .

.. meta::
   :keywords: yp

.. index:: yp

.. _py_fun_forward@yp:

yp
**
The result is a numpy vector with ``float`` ( ``a_double`` ) elements
and size *m* .
It is the *p*-th order Taylor coefficients for :math:`Y(t)`.

.. meta::
   :keywords: example

.. index:: example

.. _py_fun_forward@Example:

Example
*******
:ref:`fun_forward_xam_py-name`

.. toctree::
   :maxdepth: 1
   :hidden:

   fun_forward_xam_py
