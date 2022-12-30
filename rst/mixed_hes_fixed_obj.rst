.. _mixed_hes_fixed_obj-name:

!!!!!!!!!!!!!!!!!!!
mixed_hes_fixed_obj
!!!!!!!!!!!!!!!!!!!

.. raw:: html

   <a href="_sources/mixed_hes_fixed_obj.rst.txt">View page source</a>

.. meta::
   :keywords: mixed_hes_fixed_obj, hessian, fixed, effects, objective

.. index:: mixed_hes_fixed_obj, hessian, fixed, effects, objective

.. _mixed_hes_fixed_obj-title:

Hessian of Fixed Effects Objective
##################################

.. meta::
   :keywords: syntax

.. index:: syntax

.. _mixed_hes_fixed_obj@Syntax:

Syntax
******

.. literalinclude:: ../../lib/python/cppad_py/mixed.py
   :lines: 980-984
   :language: py

.. meta::
   :keywords: purpose

.. index:: purpose

.. _mixed_hes_fixed_obj@Purpose:

Purpose
*******
We are given a value for the fixed effects :math:`\theta`
and the corresponding optimal value for the random effects
:math:`\hat{u} ( \theta )`.
This routine computes the hessian, with respect to the fixed effects,
of the negative log of the Laplace approximation for the
fixed effects objective

.. math::
   \B{p} ( z | \theta ) \B{p} ( \theta ) \int_{-\infty}^{+\infty}
      \B{p} ( y | \theta , u ) \B{p}( u | \theta ) \B{d} u

If there is no data,  and not random effects,
the return value is the Hessian of
:math:`- \log [ \B{p} ( \theta ) ]` .

.. meta::
   :keywords: hes_fixed_obj_rcv

.. index:: hes_fixed_obj_rcv

.. _mixed_hes_fixed_obj@hes_fixed_obj_rcv:

hes_fixed_obj_rcv
*****************
The argument *hes_fixed_obj_rcv* is a
:ref:`py_sparse_rcv <py_sparse_rcv-name>` matrix.
The input value of this argument does not matter.
Upon return it contains the lower triangle of the Hessian
(the Hessian is symmetric).

.. meta::
   :keywords: fixed_vec

.. index:: fixed_vec

.. _mixed_hes_fixed_obj@fixed_vec:

fixed_vec
*********
The argument *fixed_vec* is a numpy vector with ``float`` elements
and length *n_fixed*. It contains the value of the fixed effects
:math:`\theta` at which the Hessian is evaluated.
This vector can't be ``None``.

.. meta::
   :keywords: random_opt

.. index:: random_opt

.. _mixed_hes_fixed_obj@random_opt:

random_opt
**********
The argument *random_opt* is a numpy vector with ``float`` elements
and length *n_random*.
It contains the optional value for the random effects,
which is a function of the fixed effects and denoted by
:math:`\hat{u} ( \theta )` .
This vector can't be ``None``.

.. meta::
   :keywords: examples

.. index:: examples

.. _mixed_hes_fixed_obj@Examples:

Examples
********

-  :ref:`mixed_hes_fixed_obj_xam_py-title`

.. toctree::
   :maxdepth: 1
   :hidden:

   mixed_hes_fixed_obj_xam_py
