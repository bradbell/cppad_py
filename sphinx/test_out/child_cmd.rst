|

:ref:`sphinxrst_py<sphinxrst_py>` > child_cmd

.. meta::
   :keywords: children, and, child, links, commands

.. index:: children, and, child, links, commands

.. _child_cmd:

=================================
Children and Child Links Commands
=================================

.. meta::
   :keywords: syntax

.. index:: syntax

.. _child_cmd.syntax:

Syntax
------
- ``{sphinxrst_children%``
  *file_1* :code:`%` ... :code:`%` *file_n* :code:`%}`
- ``{sphinxrst_child_link%``
  *file_1* :code:`%` ... :code:`%` *file_n* :code:`%}`

.. meta::
   :keywords: purpose

.. index:: purpose

.. _child_cmd.purpose:

Purpose
-------
A section can specify a set of files for which
the first section in each file (parent section for each file)
is a child of the current section.
This is done using the commands above at the
:ref:`beginning of a line<sphinxrst_py.notation.beginning_of_a_line>`.

.. meta::
   :keywords: white, space

.. index:: white, space

.. _child_cmd.white_space:

White Space
-----------
Leading and trailing white space is not included in the file names.
In addition, and empty file name is ignored.
This enables one to put the command on multiple input lines.

.. meta::
   :keywords: links

.. index:: links

.. _child_cmd.links:

Links
-----
The child link command also places
links to all the children of the current at the location of the command.
You can place a heading directly before the links to make them easier to find.

.. meta::
   :keywords: example

.. index:: example

.. _child_cmd.example:

Example
-------
.. toctree::
   :maxdepth: 1

   children_exam


----

sphinxrst input file: ``bin/sphinxrst.py``
