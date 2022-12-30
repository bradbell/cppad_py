.. _mixed_hes_random_obj-name:

!!!!!!!!!!!!!!!!!!!!
mixed_hes_random_obj
!!!!!!!!!!!!!!!!!!!!

.. raw:: html

   <a href="_sources/mixed_hes_random_obj.rst.txt">View page source</a>

.. meta::
   :keywords: mixed_hes_random_obj, hessian, random, effects, objective

.. index:: mixed_hes_random_obj, hessian, random, effects, objective

.. _mixed_hes_random_obj-title:

Hessian of Random Effects Objective
###################################

.. meta::
   :keywords: syntax

.. index:: syntax

.. _mixed_hes_random_obj@Syntax:

Syntax
******

.. literalinclude:: ../lib/python/cppad_py/mixed.py
   :lines: 1084-1088
   :language: py

.. meta::
   :keywords: purpose

.. index:: purpose

.. _mixed_hes_random_obj@Purpose:

Purpose
*******
We are given a value for the fixed effects :math:`\theta`,
and the corresponding random effects :math:`u` .
This routine the hessian, with respect to the random effects,
of the negative log of random effects objective; i.e.,
:ref:`ran_likelihood <mixed_ran_likelihood@ran_likelihood>`

.. math::
   \B{p} ( y | \theta , u ) \B{p}( u | \theta ) \B{d} u

If there is no data, the return value is the Hessian of
:math:`- \log [ \B{p} ( u | \theta ) ]` w.r.t :math:`u` .

.. meta::
   :keywords: hes_random_obj_rcv

.. index:: hes_random_obj_rcv

.. _mixed_hes_random_obj@hes_random_obj_rcv:

hes_random_obj_rcv
******************
The argument *hes_random_obj_rcv* is a
:ref:`py_sparse_rcv <py_sparse_rcv-name>` matrix.
The input value of this argument does not matter.
Upon return it contains the lower triangle of the Hessian
(the Hessian is symmetric).

.. meta::
   :keywords: fixed_vec

.. index:: fixed_vec

.. _mixed_hes_random_obj@fixed_vec:

fixed_vec
*********
The argument *fixed_vec* is a numpy vector with ``float`` elements
and length *n_fixed*. It contains the value of the fixed effects
:math:`\theta` at which the Hessian is evaluated.
This vector can't be ``None``.

.. meta::
   :keywords: random_vec

.. index:: random_vec

.. _mixed_hes_random_obj@random_vec:

random_vec
**********
The argument *random_vec* is a numpy vector with ``float`` elements
and length *n_random*.
It contains the value for the random effects at which the Hessian
is evaluated.,
This vector can't be ``None``.

.. meta::
   :keywords: examples

.. index:: examples

.. _mixed_hes_random_obj@Examples:

Examples
********

-  :ref:`mixed_hes_random_obj_xam_py-title`

.. toctree::
   :maxdepth: 1
   :hidden:

   mixed_hes_random_obj_xam_py
