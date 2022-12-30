.. _mixed_ctor-name:

!!!!!!!!!!
mixed_ctor
!!!!!!!!!!

.. raw:: html

   <a href="_sources/mixed_ctor.rst.txt">View page source</a>

.. meta::
   :keywords: mixed_ctor, mixed, class, constructor

.. index:: mixed_ctor, mixed, class, constructor

.. _mixed_ctor-title:

Mixed Class Constructor
#######################

.. meta::
   :keywords: syntax

.. index:: syntax

.. _mixed_ctor@Syntax:

Syntax
******

.. literalinclude:: ../../lib/python/cppad_py/mixed.py
   :lines: 190-200
   :language: py

.. meta::
   :keywords: mixed_obj

.. index:: mixed_obj

.. _mixed_ctor@mixed_obj:

mixed_obj
*********
We refer to the value returned by this constructor as *mixed_obj*.

.. meta::
   :keywords: fixed_init

.. index:: fixed_init

.. _mixed_ctor@fixed_init:

fixed_init
**********
is a numpy vector with ``float`` elements.
It specifies a value of the fixed effects for which the
likelihood and prior functions can be evaluated and is used to
initialize *mixed_obj*.
This vector must be non-empty and the default value ``None`` is not valid.

.. meta::
   :keywords: n_fixed

.. index:: n_fixed

.. _mixed_ctor@fixed_init@n_fixed:

n_fixed
=======
We use the notation *n_fixed* for the length of *fixed_init* .

.. meta::
   :keywords: random_init

.. index:: random_init

.. _mixed_ctor@random_init:

random_init
***********
is a numpy vector with ``float`` elements.
It specifies a value of the random effects for which the
likelihood and prior functions can be evaluated and is used to
initialize *mixed_obj*.
The default value for this argument ``None`` corresponds
to the empty vector.

.. meta::
   :keywords: n_random

.. index:: n_random

.. _mixed_ctor@random_init@n_random:

n_random
========
We use the notation *n_random* for the length of *random_init* .

.. meta::
   :keywords: quasi_fixed

.. index:: quasi_fixed

.. _mixed_ctor@quasi_fixed:

quasi_fixed
***********
is True (False) if a quasi-Newton method (Newton method) is used to
optimize the fixed effects. The Newton method requires computation
of second derivatives.

.. meta::
   :keywords: bool_sparsity

.. index:: bool_sparsity

.. _mixed_ctor@bool_sparsity:

bool_sparsity
*************
is True (False) if CppAD should use boolean sparsity patterns
(set sparsity patterns) for its internal calculations

.. meta::
   :keywords: a_rcv

.. index:: a_rcv

.. _mixed_ctor@A_rcv:

A_rcv
*****
Is a :ref:`sparse_rcv<py_sparse_rcv-name>` representation of the
random constraint matrix :math:`A`; i.e.
:math:`A \cdot \hat{u} ( \theta ) = 0`
where :math:`\hat{u} ( \theta )` is the
optimal random effects as a function of the fixed effects.
The value ``None`` corresponds to no random constraint.

.. meta::
   :keywords: warning

.. index:: warning

.. _mixed_ctor@warning:

warning
*******
is a python function that gets called when *mixed_obj*
has a warning to report; see :ref:`mixed_warning-title`.
The value ``None`` corresponds to ignoring all warning messages.

.. meta::
   :keywords: fix_likelihood

.. index:: fix_likelihood

.. _mixed_ctor@fix_likelihood:

fix_likelihood
**************
see :ref:`mixed_fix_likelihood-title` .
The value ``None`` corresponds to no fixed effects likelihood.

.. meta::
   :keywords: fix_constraint

.. index:: fix_constraint

.. _mixed_ctor@fix_constraint:

fix_constraint
**************
see :ref:`mixed_fix_constraint-title` .
The value ``None`` corresponds to no constraint function
for the fixed effects (one can still have bound constraints).

.. meta::
   :keywords: ran_likelihood

.. index:: ran_likelihood

.. _mixed_ctor@ran_likelihood:

ran_likelihood
**************
see :ref:`mixed_ran_likelihood-title` .
The value ``None`` corresponds to no random effects likelihood.

.. meta::
   :keywords: example

.. index:: example

.. _mixed_ctor@Example:

Example
*******
:ref:`mixed_ctor_xam_py-name`

.. toctree::
   :maxdepth: 1
   :hidden:

   mixed_ctor_xam_py
