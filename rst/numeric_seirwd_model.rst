.. _numeric_seirwd_model-name:

!!!!!!!!!!!!!!!!!!!!
numeric_seirwd_model
!!!!!!!!!!!!!!!!!!!!

.. raw:: html

   <a href="_sources/numeric_seirwd_model.rst.txt">View page source</a>

.. meta::
   :keywords: numeric_seirwd_model, susceptible, exposed, infectious, recovered, death, model

.. index:: numeric_seirwd_model, susceptible, exposed, infectious, recovered, death, model

.. _numeric_seirwd_model-title:

A Susceptible Exposed Infectious Recovered and Death Model
##########################################################

.. meta::
   :keywords: purpose

.. index:: purpose

.. _numeric_seirwd_model@Purpose:

Purpose
*******
This routine can be used with ``ad_double`` .

.. meta::
   :keywords: syntax

.. index:: syntax

.. _numeric_seirwd_model@Syntax:

Syntax
******

| *seirwd_all* =  ``seirwd_model`` (
| |tab| *method* , *t_all* , *p_all* , *initial* , *n_step* = 1
| )

.. meta::
   :keywords: notation

.. index:: notation

.. _numeric_seirwd_model@Notation:

Notation
********

.. csv-table::
 :widths: 4, 34

 :math:`S(t)`, size of the Susceptible group
 :math:`E(t)`, size of the Exposed group
 :math:`I(t)`, size of the Infectious group
 :math:`R(t)`, size Recovered group
 :math:`W(t)`, size of the group that will die
 :math:`D(t)`, size of the group that has died
 :math:`\alpha(t)`, infectious group size exponent
 :math:`\beta(t)`, infectious rate
 :math:`\sigma(t)`, incubation rate
 :math:`\gamma(t)`, recovery rate
 :math:`\xi(t)`, loss of immunity rate
 :math:`\chi(t)`, excess mortality rate
 :math:`\delta(t)`, delay between infectious and death

.. meta::
   :keywords: ode

.. index:: ode

.. _numeric_seirwd_model@ODE:

ODE
***
The ordinary differential equation for this model is:

.. math::

   \begin{array}{rcll}
   \dot{S} & = & - \beta  S I^\alpha  & + \xi    R             \\
   \dot{E} & = & + \beta  S I^\alpha  & - \sigma E             \\
   \dot{I} & = & + \sigma E           & - ( \gamma + \chi )  I \\
   \dot{R} & = & + \gamma I           & - \xi    R             \\
   \dot{W} & = & + \chi   I           & - \delta W             \\
   \dot{D} & = & + \delta W           &
   \end{array}

where we dropped the time dependence in the equations above.
This model does not account for death by other causes.
It is similar to the standard
`SEIRS <https://www.idmod.org/docs/hiv/model-seir.html>`_ model
with the following differences:

#. The total population :math:`N` is not included in this model,
   so the units for :math:`\beta` are different.
#. This model tracks death due to the condition using the compartments W and D.

.. meta::
   :keywords: method

.. index:: method

.. _numeric_seirwd_model@method:

method
******
This ``str`` must be either ``runge4`` or ``rosen3`` .
It determines if :ref:`runge4_step<numeric_runge4_step-name>` or
:ref:`rosen3_step<numeric_rosen3_step-name>` is used to solve the ODE.

.. meta::
   :keywords: t_all

.. index:: t_all

.. _numeric_seirwd_model@t_all:

t_all
*****
The argument *t_all* is a vector that is monotone
increasing or decreasing.
The type of its elements can be ``float`` or ``a_double`` .
The smaller the spacing between time points, the more accurate
the approximation is.
Note two points can be equal; i.e., no zero spacing.
We call *t_all* [0] the initial time and
*t_all* [-1] the final time.

.. meta::
   :keywords: p_all

.. index:: p_all

.. _numeric_seirwd_model@p_all:

p_all
*****
This argument is a list of dictionaries.
The i-th element of the list has the following *key* ,
*value* pairs:

.. csv-table::
 :widths: 7, 8

 *key* , *value*
 ``'alpha'`` , :math:`\alpha( t_i )`
 ``'beta'`` , :math:`\beta( t_i )`
 ``'sigma'`` , :math:`\sigma( t_i )`
 ``'gamma'`` , :math:`\gamma( t_i )`
 ``'xi'`` , :math:`\xi( t_i )`
 ``'chi'`` , :math:`\chi( t_i )`
 ``'delta'`` , :math:`\delta( t_i )`

where *t_i* is the time *t_all* [ *i* ] .
The type of *value* can be ``float`` or ``a_double`` .
Each of the these parameters will be linearly interpolated
for times between the those in *t_all* .

.. meta::
   :keywords: alpha

.. index:: alpha

.. _numeric_seirwd_model@p_all@alpha:

alpha
=====
There is a special restriction that :math:`\alpha(t)` must be
constant; i.e. :math:`\alpha( t_i ) = \alpha( t_0 )` for
all :math:`i`.
This is because talking the derivative of :math:`I^\alpha`
respect to :math:`I` has a special representation when :math:`\alpha = 1`.
Using a special representation for that case would not work with AD
unless :math:`\alpha` is constant.

.. meta::
   :keywords: initial

.. index:: initial

.. _numeric_seirwd_model@initial:

initial
*******
is a vector of length four containing the initial values for
S, E, I, R, W, D in that order.
The type of its elements can be ``float`` or ``a_double`` .

.. meta::
   :keywords: n_step

.. index:: n_step

.. _numeric_seirwd_model@n_step:

n_step
******
This is the number of numerical integration steps to use for each
time interval in the *t_all* array.
It must be an ``int`` greater or equal one.
The larger *n_step* the more computational effort and the more
accurate the solution.  The default value is for *n_step* is one.

.. meta::
   :keywords: seirwd_all

.. index:: seirwd_all

.. _numeric_seirwd_model@seirwd_all:

seirwd_all
**********
The return value *seirwd_all* is a numpy matrix with row dimension
equal to the number of elements in *t_all* and column dimension
equal to six. The value *seirwd_all* [ *i* , *j* ] is the
approximate solution for the j-th compartment at time *t_all* [ *i* ] .
The compartments have the same order as in *initial* and
``seirwd`` [0, *:* is equal to *initial* .
The sequence of floating point operations only depends on *t_all*
and the operations used to compute *p_fun* .

.. meta::
   :keywords: conservation, mass

.. index:: conservation, mass

.. _numeric_seirwd_model@Conservation of Mass:

Conservation of Mass
********************
Note that the sum of S, E, I, R, W, and D should be constant; i.e.,
up to numerical accuracy, it not depend on time.

.. meta::
   :keywords: example

.. index:: example

.. _numeric_seirwd_model@Example:

Example
*******
:ref:`numeric_seirwd_model_xam_py-name`

.. meta::
   :keywords: source, code

.. index:: source, code

.. _numeric_seirwd_model@Source Code:

Source Code
***********

.. literalinclude:: ../../example/python/numeric/seirwd_model.py
   :lines: 6-185
   :language: py

.. toctree::
   :maxdepth: 1
   :hidden:

   numeric_seirwd_model_xam_py
