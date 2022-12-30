.. _mixed_optimize_fixed-name:

!!!!!!!!!!!!!!!!!!!!
mixed_optimize_fixed
!!!!!!!!!!!!!!!!!!!!

.. raw:: html

   <a href="_sources/mixed_optimize_fixed.rst.txt">View page source</a>

.. meta::
   :keywords: mixed_optimize_fixed, optimize, the, fixed, effects

.. index:: mixed_optimize_fixed, optimize, the, fixed, effects

.. _mixed_optimize_fixed-title:

Optimize The Fixed Effects
##########################

.. meta::
   :keywords: syntax

.. index:: syntax

.. _mixed_optimize_fixed@Syntax:

Syntax
******

.. literalinclude:: ../../lib/python/cppad_py/mixed.py
   :lines: 688-700
   :language: py

.. meta::
   :keywords: purpose

.. index:: purpose

.. _mixed_optimize_fixed@Purpose:

Purpose
*******
This routine maximizes, with respect to the fixed effect :math:`\theta`,
the Laplace approximation for the likelihood of the data and fixed effects.

.. math::
   \B{p} ( z | \theta ) \B{p} ( \theta ) \int_{-\infty}^{+\infty}
      \B{p} ( y | \theta , u ) \B{p}( u | \theta ) \B{d} u

If there are no random effects,
there is no Laplace approximation of the integral above, and
this routine maximizes :math:`\B{p} ( z | \theta ) \B{p} ( \theta )` ;
see :ref:`mixed_fix_likelihood-title`.
It also is no data, this routine maximizes :math:`\B{p} ( \theta )`.

.. meta::
   :keywords: argument, types

.. index:: argument, types

.. _mixed_optimize_fixed@Argument Types:

Argument Types
**************
The arguments *fixed_ipopt_options* and *random_ipopt_options*
have type ``str``.  All the other arguments are
numpy vectors with elements of type ``float``.

.. meta::
   :keywords: limits

.. index:: limits

.. _mixed_optimize_fixed@Limits:

Limits
******
As a lower (upper) limit, the value ``None`` is minus (plus) infinity;
i.e., no lower (upper) limit.

.. meta::
   :keywords: fixed_lower, (fixed_upper)

.. index:: fixed_lower, (fixed_upper)

.. _mixed_optimize_fixed@fixed_lower (fixed_upper):

fixed_lower (fixed_upper)
*************************
has length *n_fixed* and is the lower (upper) limit for the fixed effects.

.. meta::
   :keywords: fix_constraint_lower, (fix_constraint_upper)

.. index:: fix_constraint_lower, (fix_constraint_upper)

.. _mixed_optimize_fixed@fix_constraint_lower (fix_constraint_upper):

fix_constraint_lower (fix_constraint_upper)
*******************************************
has length equal to the
:ref:`py_fun_property@size_range` for the
:ref:`mixed_fix_constraint-title`
and is the corresponding lower (upper) limit.

.. meta::
   :keywords: random_lower, (random_upper)

.. index:: random_lower, (random_upper)

.. _mixed_optimize_fixed@random_lower (random_upper):

random_lower (random_upper)
***************************
has length *n_random* and is the lower (upper) limit for the random effects.
(The Laplace approximation assumes these bounds are not active.)

.. meta::
   :keywords: fixed_in, (random_in)

.. index:: fixed_in, (random_in)

.. _mixed_optimize_fixed@fixed_in (random_in):

fixed_in (random_in)
********************
has length *n_fixed* (*n_random*) and is the initial value used during
optimization of the fixed (random) effects.
If *fixed_in* (*random_in*) is ``None``, the value
*fixed_init* (*random_init*) is used; see
:ref:`mixed_ctor@fixed_init`, :ref:`mixed_ctor@random_init` .

.. meta::
   :keywords: fixed_scale

.. index:: fixed_scale

.. _mixed_optimize_fixed@fixed_scale:

fixed_scale
***********
has length *n_fixed* and is the value of the fixed at which the
fixed effect objective is scaled so its derivative is near one.
The value ``None`` corresponds to *fixed_scale* equal to *fixed_in*.

.. meta::
   :keywords: fixed_ipopt_options

.. index:: fixed_ipopt_options

.. _mixed_optimize_fixed@fixed_ipopt_options:

fixed_ipopt_options
*******************
This contains the options for optimizing the fixed effects.
Each line of an options argument corresponds to an ipopt option
and is terminated by a ``\n`` character.
Each line has three non-empty tokens separated by one or more spaces.
The first token in each line is ``String``, ``Integer``, or ``Numeric``;
see below.

.. meta::
   :keywords: ipopt, options

.. index:: ipopt, options

.. _mixed_optimize_fixed@fixed_ipopt_options@ipopt options:

ipopt options
=============
See the `ipopt options <https://coin-or.github.io/Ipopt/OPTIONS.html>`_
documentation for a list of the options and how they affect the
optimization.

.. meta::
   :keywords: string

.. index:: string

.. _mixed_optimize_fixed@fixed_ipopt_options@String:

String
======
An Ipopt string option is specified by a line containing
the following syntax:

| |tab| ``String`` *name* *value*

.. meta::
   :keywords: integer

.. index:: integer

.. _mixed_optimize_fixed@fixed_ipopt_options@Integer:

Integer
=======
An Ipopt integer option specified specifies by a line containing
the following syntax:

| |tab| ``Integer`` *name* *value*

.. meta::
   :keywords: numeric

.. index:: numeric

.. _mixed_optimize_fixed@fixed_ipopt_options@Numeric:

Numeric
=======
An Ipopt numeric option specified specifies by a line containing
the following syntax:

| |tab| ``Numeric`` *name* *value*

.. meta::
   :keywords: derivative_test

.. index:: derivative_test

.. _mixed_optimize_fixed@fixed_ipopt_options@derivative_test:

derivative_test
===============
If the string option is ``derivative_test``, *value* can be
``none``, ``first-order``, ``second-order``, ``only-second-order``.
If second order derivatives are tested,
:ref:`quasi_fixed<mixed_ctor@quasi_fixed>` must be false.
In addition to the standard ipopt options above, *value* can be
``adaptive`` or ``trace-adaptive`` which uses a special derivative
tester that adapts its step sizes for each argument component.

.. meta::
   :keywords: hessian_approximation

.. index:: hessian_approximation

.. _mixed_optimize_fixed@fixed_ipopt_options@hessian_approximation:

hessian_approximation
=====================
If *quasi_fixed* is true, this string option (if present) must have value
``limit_memory``.

.. meta::
   :keywords: max_iter

.. index:: max_iter

.. _mixed_optimize_fixed@fixed_ipopt_options@max_iter:

max_iter
========
This integer option has a special *value* -1.
In this case ipopt is run with ``max_iter`` equal to zero,
and the return solution corresponds to the input value of the
fixed effects.

.. meta::
   :keywords: nlp_scaling_method

.. index:: nlp_scaling_method

.. _mixed_optimize_fixed@fixed_ipopt_options@nlp_scaling_method:

nlp_scaling_method
==================
The objective and constraint function are automatically scaled by
cppad_mixed and it is an error to specify this option.

.. meta::
   :keywords: random_ipopt_options

.. index:: random_ipopt_options

.. _mixed_optimize_fixed@random_ipopt_options:

random_ipopt_options
********************
This contains the options for optimizing the random effects.
It has the same format as *fixed_ipopt_options*, but does
not have the special exceptions to the normal Ipopt options; e.g.,
``adaptive`` is not available as a ``derivative_test`` *value*.

.. meta::
   :keywords: solution

.. index:: solution

.. _mixed_optimize_fixed@solution:

solution
********
All the fields in the return value *solution*
are numpy vectors with elements of type ``float``.

.. meta::
   :keywords: fixed_opt

.. index:: fixed_opt

.. _mixed_optimize_fixed@solution@fixed_opt:

fixed_opt
=========
The value *solution*\ ``.fixed_opt`` has length
*n_fixed* and is the final value of the fixed effects
(after optimization).
If the *max_iter* is -1, it is equal to *fixed_in*.

.. meta::
   :keywords: fixed_lag

.. index:: fixed_lag

.. _mixed_optimize_fixed@solution@fixed_lag:

fixed_lag
=========
The value *solution*\ ``.fixed_lag`` has length
*n_fixed* and is the Lagrange multipliers for
the fixed effects lower (upper) bounds if it is greater than (less than)
zero.

.. meta::
   :keywords: fix_con_lag

.. index:: fix_con_lag

.. _mixed_optimize_fixed@solution@fix_con_lag:

fix_con_lag
===========
The value *solution*\ ``.fix_con_lag`` is a Lagrange multipliers for
the fixed effects lower (upper) bounds if it is greater than (less than).
Its length is the same as the return value for the fixed effects constraint
function.

.. meta::
   :keywords: ran_con_lag

.. index:: ran_con_lag

.. _mixed_optimize_fixed@solution@ran_con_lag:

ran_con_lag
===========
The value *solution*\ ``.ran_con_lag`` is a Lagrange multipliers for the
rand effects constraint function.
Its length is the same as the random constrain matrix :math:`A` ; see
:ref:`A_rcv<mixed_ctor@A_rcv>`.

.. meta::
   :keywords: examples

.. index:: examples

.. _mixed_optimize_fixed@Examples:

Examples
********

- :ref:`mixed_optimize_fixed_1_py-title`
- :ref:`mixed_optimize_fixed_2_py-title`

.. toctree::
   :maxdepth: 1
   :hidden:

   mixed_optimize_fixed_1_py
   mixed_optimize_fixed_2_py
