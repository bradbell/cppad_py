.. _py_fun_property-name:

!!!!!!!!!!!!!!!
py_fun_property
!!!!!!!!!!!!!!!

.. raw:: html

   <a href="_sources/py_fun_property.rst.txt">View page source</a>

.. meta::
   :keywords: py_fun_property, properties, function, object

.. index:: py_fun_property, properties, function, object

.. _py_fun_property-title:

Properties of a Function Object
###############################

.. meta::
   :keywords: syntax

.. index:: syntax

.. _py_fun_property@Syntax:

Syntax
******

| *n* = *f*\ ``.size_domain`` ()
| *m* = *f*\ ``.size_range`` ()
| *v* = *f*\ ``.size_var`` ()
| *p* = *f*\ ``.size_op`` ()
| *q* = *f*\ ``.size_order`` ()

.. meta::
   :keywords: f

.. index:: f

.. _py_fun_property@f:

f
*
This is either a
:ref:`d_fun<py_fun_ctor@Syntax@d_fun>` or
:ref:`a_fun<py_fun_ctor@Syntax@a_fun>` function object
and is constant; i.e., not changed.

.. meta::
   :keywords: size_domain

.. index:: size_domain

.. _py_fun_property@size_domain:

size_domain
***********
The return value *n* is an ``int``
and is the size of the vector
:ref:`ax<py_fun_ctor@ax>` in the function constructor; i.e.,
the number of independent variables.

.. meta::
   :keywords: size_range

.. index:: size_range

.. _py_fun_property@size_range:

size_range
**********
The return value *m* is an ``int``
and is the size of the vector
:ref:`ay<py_fun_ctor@ay>` in the function constructor; i.e.,
the number of dependent variables.

.. meta::
   :keywords: size_var

.. index:: size_var

.. _py_fun_property@size_var:

size_var
********
The return value *v* is an ``int``
and is the number of variables in the function.
This includes the independent variables, dependent variables,
and any variables that are used to compute the dependent variables
from the independent variables.

.. meta::
   :keywords: size_op

.. index:: size_op

.. _py_fun_property@size_op:

size_op
*******
The return value *p* is an ``int``
and is the number of atomic operations that are used to express
the dependent variables as a function of the independent variables.

.. meta::
   :keywords: size_order

.. index:: size_order

.. _py_fun_property@size_order:

size_order
**********
The return value *q* is an ``int``
and is the number of Taylor coefficients currently stored in *f* ,
for every variable in the operation sequence corresponding to *f* .
These coefficients are computed by :ref:`py_fun_forward-name`.
This is different from the other function properties in that it can change
after each call to *f*\ ``.forward`` ; see
:ref:`size_order<py_fun_forward@p@size_order>` in the forward mode section.

.. meta::
   :keywords: example

.. index:: example

.. _py_fun_property@Example:

Example
*******
:ref:`fun_property_xam_py-name`

.. toctree::
   :maxdepth: 1
   :hidden:

   fun_property_xam_py
