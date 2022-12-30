.. _cpp_fun_json-name:

!!!!!!!!!!!!
cpp_fun_json
!!!!!!!!!!!!

.. raw:: html

   <a href="_sources/cpp_fun_json.rst.txt">View page source</a>

.. meta::
   :keywords: cpp_fun_json, json, representation, ad, computational, graph

.. index:: cpp_fun_json, json, representation, ad, computational, graph

.. _cpp_fun_json-title:

Json Representation of AD Computational Graph
#############################################

.. meta::
   :keywords: syntax

.. index:: syntax

.. _cpp_fun_json@Syntax:

Syntax
******

| *json* = *f*\ ``.to_json`` ()
| *f*\ ``.from_json`` ()

.. meta::
   :keywords: f

.. index:: f

.. _cpp_fun_json@f:

f
*
This is a :ref:`d_fun<cpp_fun_ctor@Syntax@d_fun>` object.

.. meta::
   :keywords: json

.. index:: json

.. _cpp_fun_json@json:

json
****
is a Json representation of the computation graph corresponding to
*f* ; see the CppAD documentation for
`json_ad_graph <https://coin-or.github.io/CppAD/doc/json_ad_graph.htm>`_.

.. meta::
   :keywords: to_json

.. index:: to_json

.. _cpp_fun_json@to_json:

to_json
*******
In this case, the function object *f* is ``const`` and
the return value *json* has prototype

| |tab| ``std::string`` *json*

.. meta::
   :keywords: from_json

.. index:: from_json

.. _cpp_fun_json@from_json:

from_json
*********
In this case, *json* has prototype

| |tab| ``const std::string&`` *json*

and the function *f* so it corresponds to *json* .

.. meta::
   :keywords: examples

.. index:: examples

.. _cpp_fun_json@Examples:

Examples
********
:ref:`fun_to_json_xam_cpp-name`,
:ref:`fun_from_json_xam_cpp-name`.

.. toctree::
   :maxdepth: 1
   :hidden:

   fun_to_json_xam_cpp
   fun_from_json_xam_cpp
