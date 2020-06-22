|

:ref:`sphinxrst_py<sphinxrst_py>` > children_command

.. _children_command:

================
Children Command
================

.. _children_command.syntax:

Syntax
------
``{sphinxrst_children%`` *file_1* :code:`%` ... :code:`%` *file_n* :code:`%}`

.. _children_command.purpose:

Purpose
-------
A section can specify a set of files for which
the first section in each file (parent section for each file)
is a child of the current section.
This is done using the command above at the
:ref:`beginning of a line<sphinxrst_py.notation.beginning_of_a_line>`.

.. _children_command.white_space:

White Space
-----------
Leading and trailing white space is not included in the file names.
In addition, and empty file name is ignored.
This enables one to put the command on multiple input lines.

.. _children_command.links:

Links
-----
Links to all the children of the current section are placed
at the location of the children command.
You can place a heading directly before the links to make them easier to find.

.. _children_command.example:

Example
-------
.. toctree::
   :maxdepth: 1

   children_exam


----

sphinxrst input file: ``bin/sphinxrst.py``
