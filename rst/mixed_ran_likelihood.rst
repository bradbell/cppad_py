.. _mixed_ran_likelihood-name:

!!!!!!!!!!!!!!!!!!!!
mixed_ran_likelihood
!!!!!!!!!!!!!!!!!!!!

.. raw:: html

   <a href="_sources/mixed_ran_likelihood.rst.txt">View page source</a>

.. meta::
   :keywords: mixed_ran_likelihood, random, effects, likelihood

.. index:: mixed_ran_likelihood, random, effects, likelihood

.. _mixed_ran_likelihood-title:

Random Effects Likelihood
#########################

.. meta::
   :keywords: syntax

.. index:: syntax

.. _mixed_ran_likelihood@Syntax:

Syntax
******
*v* = *ran_likelihood*\ ``.forward`` (0, *theta* , *u* )

.. meta::
   :keywords: ran_likelihood

.. index:: ran_likelihood

.. _mixed_ran_likelihood@ran_likelihood:

ran_likelihood
**************
is a :ref:`d_fun<py_fun_ctor@Syntax@d_fun>` representation
of the negative log of the
:ref:`random effects likelihood <mixed@Notation@Random Effects Likelihood>`

.. math::

   r( \theta , u )
   =
   v_0 ( \theta , u )
   =
   - \log [ \B{p} ( y | \theta , u ) \B{p} ( u | \theta ) ]

The function :math:`v_0 ( \theta , u )`
is assumed to be a smooth w.r.t the vector :math:`( \theta , u )`.

.. meta::
   :keywords: theta

.. index:: theta

.. _mixed_ran_likelihood@theta:

theta
*****
is a numpy vector with ``float`` elements and size
:ref:`mixed_ctor@fixed_init@n_fixed`
containing a value for the fixed effects.

.. meta::
   :keywords: u

.. index:: u

.. _mixed_ran_likelihood@u:

u
*
is a numpy vector with ``float`` elements and size
:ref:`mixed_ctor@random_init@n_random`
containing a value for the random effects.

.. meta::
   :keywords: v

.. index:: v

.. _mixed_ran_likelihood@v:

v
*
is a numpy vector with ``float`` elements and size 1.

.. meta::
   :keywords: none

.. index:: none

.. _mixed_ran_likelihood@None:

None
****
The value *ran_likelihood* = ``None``
corresponds to the random effects likelihood
being constant w.r.t. :math:`( \theta , u )`.

.. meta::
   :keywords: example

.. index:: example

.. _mixed_ran_likelihood@Example:

Example
*******
:ref:`mixed_ran_likelihood_xam_py-name`

.. toctree::
   :maxdepth: 1
   :hidden:

   mixed_ran_likelihood_xam_py
