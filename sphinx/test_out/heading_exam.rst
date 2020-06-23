|

:ref:`sphinxrst_py<sphinxrst_py>` > heading_exam

.. meta::
   :keywords: heading, example

.. index:: heading, example

.. _heading_exam:

===============
Heading Example
===============


.. literalinclude:: ../../sphinx/test_in/heading.py
    :lines: 29-66

.. meta::
   :keywords: child, sections

.. index:: child, sections

.. _heading_exam.child_sections:

Child Sections
--------------
The heading above is an example heading for the
:ref:`children<sphinxrst_py.heading_links.children>`
of a
:ref:`parent section<sphinxrst_py.table_of_contents.parent_section>`.

.. toctree::
   :maxdepth: 1

   heading_res

----

sphinxrst input file: ``sphinx/test_in/heading.py``
