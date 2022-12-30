.. _py_fun_json-name:

!!!!!!!!!!!
py_fun_json
!!!!!!!!!!!

.. raw:: html

   <a href="_sources/py_fun_json.rst.txt">View page source</a>

.. meta::
   :keywords: py_fun_json, json, representation, ad, computation, graph

.. index:: py_fun_json, json, representation, ad, computation, graph

.. _py_fun_json-title:

Json Representation of AD Computation Graph
###########################################

.. meta::
   :keywords: syntax

.. index:: syntax

.. _py_fun_json@Syntax:

Syntax
******

| *json* = *f*\ ``.to_json`` ()
| *f*\ ``.from_json(json`` )

.. meta::
   :keywords: f

.. index:: f

.. _py_fun_json@f:

f
*
This is a :ref:`d_fun<py_fun_ctor@Syntax@d_fun>` function object.

.. meta::
   :keywords: json

.. index:: json

.. _py_fun_json@json:

json
****
is a ``str`` containing
a Json representation of the computation graph corresponding to
*f* ; see the CppAD documentation for
`json_ad_graph <https://coin-or.github.io/CppAD/doc/json_ad_graph.htm>`_.

.. meta::
   :keywords: to_json

.. index:: to_json

.. _py_fun_json@to_json:

to_json
*******
In this case, the function object *f* is constant and
the return value *json* is created.

.. meta::
   :keywords: from_json

.. index:: from_json

.. _py_fun_json@from_json:

from_json
*********
In this case, the argument *json* is constant and
the function *f* is changed so it corresponds to *json* .

.. meta::
   :keywords: examples

.. index:: examples

.. _py_fun_json@Examples:

Examples
********
:ref:`fun_to_json_xam_py-name`,
:ref:`fun_from_json_xam_py-name`.

.. toctree::
   :maxdepth: 1
   :hidden:

   fun_to_json_xam_py
   fun_from_json_xam_py
