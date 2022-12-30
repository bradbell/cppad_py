.. _numeric_covid_19_xam_py-name:

!!!!!!!!!!!!!!!!!!!!!!!
numeric_covid_19_xam_py
!!!!!!!!!!!!!!!!!!!!!!!

.. raw:: html

   <a href="_sources/numeric_covid_19_xam_py.rst.txt">View page source</a>

.. meta::
   :keywords: numeric_covid_19_xam_py, example, fitting, an, seirwd, model, for, covid-19

.. index:: numeric_covid_19_xam_py, example, fitting, an, seirwd, model, for, covid-19

.. _numeric_covid_19_xam_py-title:

Example Fitting an SEIRWD Model for Covid-19
############################################

.. meta::
   :keywords: covariates

.. index:: covariates

.. _numeric_covid_19_xam_py@Covariates:

Covariates
**********
In this example there are two covariates that
affect the infectious rate :math:`\beta`:
social mobility :math:`c_0 (t)`,
Covid-19 testing :math:`c_1 (t)`, and
scaled time :math:`c_2 (t)`.
The covariates are known functions of time.
The mobility covariate has been shifted and scaled
so it is in the interval [-1, 0].
The testing covariate has been shifted and scaled
so it is in the interval [0, 1].
Note that the maximum mobility and the minimum testing corresponds to the
normal (baseline) condition.
The scaled time covariate is shifted and scaled version of time so that
it is in the interval [0, 1] with the first data point corresponding to
time zero. It is assumed here that the baseline condition corresponds
to time zero.

.. meta::
   :keywords: model, ode

.. index:: model, ode

.. _numeric_covid_19_xam_py@Model ODE:

Model ODE
*********
We use the :ref:`seirwd<numeric_seirwd_model-name>` model and notation.

.. meta::
   :keywords: beta(t)

.. index:: beta(t)

.. _numeric_covid_19_xam_py@Model ODE@beta(t):

beta(t)
=======
Our model for the infectious rate is

.. math::

   \beta(t) = \bar{\beta} \exp[ m_0 c_0 (t) + m_1 c_1 (t) + m_2 c_2 (t) ]

where :math:`\bar{\beta}` is the baseline value for the infectious rate,
:math:`m_0` is the social covariate multiplier, and
:math:`m_1` is the Covid-19 testing covariate multiplier.
The baseline value :math:`\bar{\beta}` is the infectious rate corresponding
to all the covariates being zero.
The covariate multipliers, and the baseline infectious rate, are unknown.

.. meta::
   :keywords: other, rates

.. index:: other, rates

.. _numeric_covid_19_xam_py@Model ODE@Other Rates:

Other Rates
===========
The other rates
:math:`\alpha(t)`,
:math:`\sigma(t)`,
:math:`\gamma(t)`,
:math:`\xi(t)`,
:math:`\chi(t)`,
:math:`\delta(t)`,
constant functions with known values:

.. literalinclude:: ../../example/python/numeric/covid_19_xam.py
   :lines: 78-83
   :language: py

All of theses rates must be non-negative.

.. meta::
   :keywords: initial, values

.. index:: initial, values

.. _numeric_covid_19_xam_py@Model ODE@Initial Values:

Initial Values
==============
The initial size of the Recovered group :math:`R(0)`
and of the Death group :math:`D(0)` is zero.
We use fraction of the total population for sizes, so the sum of the
other initial values is one.
We treat the initial
Infected group :math:`I(0)`, and
Will die group :math:`W(0)`,
as unknown parameters in the model.
We would like to also solve for the initial exposed population but
that model has identifiability problems, so
we use the following approximation for the initial exposed group

.. math::

   E(0) = I(0) \gamma / \sigma

The initial Susceptible group :math:`S(0)` is
expressed as a function of the other initial conditions:

.. math::

   S(0) = 1 - E(0) - I(0) - W(0)

.. meta::
   :keywords: ode, solver

.. index:: ode, solver

.. _numeric_covid_19_xam_py@Model ODE@Ode Solver:

Ode Solver
==========
There are two choices for *ode_method* ,
the method used to solve the ODE:
:ref:`runge4<numeric_runge4_step-name>` and
:ref:`rosen3<numeric_rosen3_step-name>`.
In addition, we can choose *ode_n_step* ,
the number of step to take for each time interval in *t_all* ,
before it is sub-sampled using the
:ref:`sample_interval<numeric_covid_19_xam_py@Data@sample_interval>`.

.. literalinclude:: ../../example/python/numeric/covid_19_xam.py
   :lines: 123-124
   :language: py

.. meta::
   :keywords: unknown, parameters

.. index:: unknown, parameters

.. _numeric_covid_19_xam_py@Unknown Parameters:

Unknown Parameters
******************
The unknown parameter vector in this model is

.. math::

   x = [ m_0, m_1, m_2, I(0), W(0), \bar{\beta} ]

.. literalinclude:: ../../example/python/numeric/covid_19_xam.py
   :lines: 136-136
   :language: py

.. meta::
   :keywords: maximum, likelihood

.. index:: maximum, likelihood

.. _numeric_covid_19_xam_py@Unknown Parameters@Maximum Likelihood:

Maximum Likelihood
==================
We use a Gaussian likelihood for each of the differences in the
cumulative deaths. The unknown parameters are estimated by maximizing the
product of these likelihoods; i.e., the differences are modeled as being
independent. The covariance of the estimates is approximated
by the inverse of the observed information matrix.
AD is used to compute first and second derivatives of the likelihood
w.r.t. the unknown parameters :math:`x`.
These derivatives are used during optimization as well as for
computing the observed information matrix.

.. meta::
   :keywords: model, bounds

.. index:: model, bounds

.. _numeric_covid_19_xam_py@Unknown Parameters@Model Bounds:

Model Bounds
============
The infection rate :math:`\beta(t)` must be non-negative; i.e.,

.. math::

   0 \leq \bar{\beta} \exp[ m_0 c_0 (t) + m_1 c_1 (t) + m_2 c_2 (t) ]

is true for all :math:`t`.
In addition, the size of the groups can not be negative.
It is sufficient to enforce this constraint on the initial conditions; i.e.,

.. math::

   \begin{array}{lcr}
   0   &  \leq & \bar{\beta }   \\
   0   &  \leq & I(0)            \\
   0   & \leq  & W(0)
   \end{array}

.. meta::
   :keywords: actual, bounds

.. index:: actual, bounds

.. _numeric_covid_19_xam_py@Unknown Parameters@Actual Bounds:

Actual Bounds
=============
The following actual upper and lower bounds for the unknown parameters
are used as an as an aid to the optimizer:

.. literalinclude:: ../../example/python/numeric/covid_19_xam.py
   :lines: 721-725
   :language: py

where *x_sim* is the
:ref:`simulation<numeric_covid_19_xam_py@Data@Simulation>` value
for the unknown parameters and *actual_bound_factor* is chosen below.
The problem has not really been solved if bounds,
other than the model bounds above, are active at the solution of the
optimization problem.

.. literalinclude:: ../../example/python/numeric/covid_19_xam.py
   :lines: 186-186
   :language: py

.. meta::
   :keywords: data

.. index:: data

.. _numeric_covid_19_xam_py@Data:

Data
****
The data in this model is the cumulative number of deaths,
as a fraction of the total population and as a function of time.
We assume that new deaths are recorded for time intervals
and the cumulative deaths is the sum of these recordings.
For this reason, we model the difference of the cumulative deaths
between time points as independent.

.. meta::
   :keywords: sample_interval

.. index:: sample_interval

.. _numeric_covid_19_xam_py@Data@sample_interval:

sample_interval
===============
It is possible to sub-sample the data in order to reduce noise.
The cumulative death data is just sub-sampled since the reduces noise by
the summing the differences corresponding to a longer time period.
The covariate data is averaged over the sample interval.
The *sample_interval* must be either one or a positive even integer
(even so an original data point corresponds to the center of the interval).

.. literalinclude:: ../../example/python/numeric/covid_19_xam.py
   :lines: 207-207
   :language: py

.. meta::
   :keywords: data_file

.. index:: data_file

.. _numeric_covid_19_xam_py@Data@data_file:

data_file
=========
If the data file name is the empty string, the cumulative death data,
and corresponding covariates, are simulated by the program.
Otherwise, the data file must be a CSV file with the following columns:
*day* , *death* , *mobility* , *testing* .
In this case the data file is used for the
cumulative death and corresponding covariates.

.. literalinclude:: ../../example/python/numeric/covid_19_xam.py
   :lines: 219-221
   :language: py

.. meta::
   :keywords: coefficient, variation

.. index:: coefficient, variation

.. _numeric_covid_19_xam_py@Data@Coefficient of Variation:

Coefficient of Variation
========================
This is the coefficient of variation for the differences
in the cumulative death data as a fraction, not a percent.
If this value is zero, a CV of zero is used for data simulation
and a CV of one in the definition of the likelihood.
This enables checking that the unknown parameters can be accurately
identified using perfect data.
For real data (when *data_file* is not empty)
this value should be adjusted so that the average residual has variance one.

.. literalinclude:: ../../example/python/numeric/covid_19_xam.py
   :lines: 235-235
   :language: py

Note this is the noise level in the original data before it is
sub-sampled using
:ref:`sample_interval<numeric_covid_19_xam_py@Data@sample_interval>`.

.. meta::
   :keywords: simulation

.. index:: simulation

.. _numeric_covid_19_xam_py@Data@Simulation:

Simulation
==========
If *data_file* is the empty string, the data is simulated using
the following values for the
:ref:`unknown_parameters<numeric_covid_19_xam_py@Unknown Parameters>`:

.. literalinclude:: ../../example/python/numeric/covid_19_xam.py
   :lines: 247-252
   :language: py

.. meta::
   :keywords: weighted, residuals

.. index:: weighted, residuals

.. _numeric_covid_19_xam_py@Data@Weighted Residuals:

Weighted Residuals
==================
If *death_data_cv* is zero, :math:`\lambda = 1`, otherwise
:math:`\lambda` is equal to

| |tab| *death_data_cv* ``* sqrt`` ( *sample_interval* )

.
(Note that the standard deviation of a sum of independent values is the
square root of the sum of the variance of each of the values.)
Let :math:`y_i` be the i-th value for the cumulative death data.
The weighted residuals (some times referred to as just the residuals) are

.. math::

   r_i = \frac{ ( y_{i+1} - y_i ) - [ D( t_{i+1} ) - D( t_i ) ] }{
   \lambda ( y_{i+1} - y_i ) }

where :math:`D(t)` is the model for the cumulative data
given the fit results.
The time corresponding to :math:`r_i` is :math:`( t_{i+1} + t_i ) / 2`.
We put the data difference in the denominator,
instead of the model difference,
because it is constant with respect to the unknown parameters.

.. meta::
   :keywords: random, seed

.. index:: random, seed

.. _numeric_covid_19_xam_py@Random Seed:

Random Seed
***********
This is the random seed used to simulate noise in the data.
If this value is zero, the system clock is used to choose the random seed.

.. literalinclude:: ../../example/python/numeric/covid_19_xam.py
   :lines: 285-285
   :language: py

.. meta::
   :keywords: random, start

.. index:: random, start

.. _numeric_covid_19_xam_py@Random Start:

Random Start
************
The optimizer needs a good starting point in order to succeed.
This is the number of random points, between the lower and upper limits,
that are checked. The point with the best objective value is chosen
as the starting point for the optimization.

.. literalinclude:: ../../example/python/numeric/covid_19_xam.py
   :lines: 295-295
   :language: py

.. meta::
   :keywords: display, fit, results

.. index:: display, fit, results

.. _numeric_covid_19_xam_py@Display Fit Results:

Display Fit Results
*******************
If you set this variable to True,
a printout and a plot of the fit results is generated.

.. literalinclude:: ../../example/python/numeric/covid_19_xam.py
   :lines: 303-303
   :language: py

.. meta::
   :keywords: plot

.. index:: plot

.. _numeric_covid_19_xam_py@Display Fit Results@Plot:

Plot
====
There are three plots all with time on the x-axis.
The first contains the size for all the compartments, except S,
as a fraction of the total population.
The second contains the model and data for the death difference values.
The third contains the weighted residuals corresponding to the death
difference data.

.. meta::
   :keywords: printout

.. index:: printout

.. _numeric_covid_19_xam_py@Display Fit Results@Printout:

Printout
========

#. The following statistics for the weighted data residuals is printed:
   the maximum, minimum, average, and average of square.
#. A table with the following columns is printed:

   .. csv-table::
       :widths: 9, 43

       *x_name* , name of the unknown parameter
       *x_fit* , fit result for the unknown parameter
       *x_lower* , lower bound used for the fit
       *x_upper* , upper bound used for the fit
       *std_error* , asymptotic standard error for the parameter

#. If *data_file* is empty,
   a table is printed with the following columns is also printed:

   .. csv-table::
       :widths: 9, 53

       *x_name* , name of the unknown parameter
       *x_sim* , known parameter value used during simulation
       *x_fit* , fit result for the unknown parameter
       *rel_error* , relative error for fit versus simulation
       *residual* , *std_error* weighted residual for fit versus simulation

.. meta::
   :keywords: debug, output

.. index:: debug, output

.. _numeric_covid_19_xam_py@Debug Output:

Debug Output
************
If this flag is true a lot of debugging output is printed.

.. literalinclude:: ../../example/python/numeric/covid_19_xam.py
   :lines: 347-347
   :language: py

.. meta::
   :keywords: source, code

.. index:: source, code

.. _numeric_covid_19_xam_py@Source Code:

Source Code
***********

.. literalinclude:: ../../example/python/numeric/covid_19_xam.py
   :lines: 359-830
   :language: py
