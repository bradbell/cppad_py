.. _a_double_property-name:

!!!!!!!!!!!!!!!!!
a_double_property
!!!!!!!!!!!!!!!!!

.. raw:: html

   <a href="_sources/a_double_property.rst.txt">View page source</a>

.. meta::
   :keywords: a_double_property, properties, an, a_double, object

.. index:: a_double_property, properties, an, a_double, object

.. _a_double_property-title:

Properties of an a_double Object
################################

.. meta::
   :keywords: syntax

.. index:: syntax

.. _a_double_property@Syntax:

Syntax
******
| *d* = *ad*\ ``.value`` ()
| *p* = *ad*\ ``.parameter`` ()
| *v* = *ad*\ ``.variable`` ()
| *e* = *ad*\ ``.near_equal`` ( *aother* )
| *ap* = *ad*\ ``.var2par`` ()

.. meta::
   :keywords: ad

.. index:: ad

.. _a_double_property@ad:

ad
**
This object has c++ prototype

| |tab| ``const a_double&`` *ad*

.. meta::
   :keywords: value

.. index:: value

.. _a_double_property@value:

value
*****
The result *d* has c++ prototype

| |tab| ``double`` *d*

It is the value of *ad* , as a constant function.

.. meta::
   :keywords: restriction

.. index:: restriction

.. _a_double_property@value@Restriction:

Restriction
===========
The object *ad* must not depend on the
:ref:`independent<cpp_independent-name>`
variables when *ad*\ ``.value`` () is called.
If it does depend on the independent variables,
you will have to wait until the current recording is terminated
before you can access its value; see
:ref:`var2par<a_double_property@var2par>` below.

.. meta::
   :keywords: parameter

.. index:: parameter

.. _a_double_property@parameter:

parameter
*********
The result *p* has c++ prototype

| |tab| ``bool`` *p*

It is true if *ad* represent a constant functions; i.e.,
*ad* not depend on the independent variables.

.. meta::
   :keywords: variable

.. index:: variable

.. _a_double_property@variable:

variable
********
The result *v* has c++ prototype

| |tab| ``bool`` *v*

It is true if *ad* is not a constant function; i.e.,
*ad* depends on the independent variables.

.. meta::
   :keywords: near_equal

.. index:: near_equal

.. _a_double_property@near_equal:

near_equal
**********
The argument *aother* ,
and the result *e* , c++ have prototype

| |tab| ``const a_double&`` *aother*
| |tab| ``bool`` *e*

The result is true if *ad* is nearly equal to *aother* .
To be specific, the result is

.. math::

   | d - o | \leq 100 \; \varepsilon \; ( |d| + |o| )

where *d* and *o* are the value corresponding to
*ad* and *aother* and
:math:`\varepsilon` is machine epsilon corresponding
to the type ``double`` .

.. meta::
   :keywords: var2par

.. index:: var2par

.. _a_double_property@var2par:

var2par
*******
The result has c++ prototype

| |tab| ``a_double`` *ap*

It has the same value as *ad* and is sure to be a parameter
( *ad* may or may not be a variable).
This can be useful when you want to access the value of *ad*
while is a variable; :ref:`value<a_double_property@value>` above.

.. meta::
   :keywords: example

.. index:: example

.. _a_double_property@Example:

Example
*******
:ref:`c++<a_double_property_xam_cpp-name>`,
:ref:`python<a_double_property_xam_py-name>`.

.. toctree::
   :maxdepth: 1
   :hidden:

   a_double_property_xam_cpp
   a_double_property_xam_py
