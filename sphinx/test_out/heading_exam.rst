!!!!!!!!!!!!
heading_exam
!!!!!!!!!!!!

.. toctree::
   :maxdepth: 1
   :hidden:

   heading_res

.. meta::
   :keywords: heading_exam, heading, example

.. index:: heading_exam, heading, example

.. _heading_exam:

Heading Example
###############
.. contents::
   :local:


.. literalinclude:: ../../../sphinx/test_in/heading.py
    :lines: 30-70
    :language: py

.. meta::
   :keywords: child, sections

.. index:: child, sections

.. _heading_exam.child_sections:

Child Sections
**************
The heading above (Child Sections) is an example heading for the
:ref:`children<xrst_py@links_to_headings@children>`
of a
:ref:`parent section<xrst_py@table_of_contents@parent_section>`.

.. csv-table::
    :header: "Child", "Title"
    :widths: 20, 80

    "heading_res", :ref:`@heading_res`

----

xrst input file: ``sphinx/test_in/heading.py``
