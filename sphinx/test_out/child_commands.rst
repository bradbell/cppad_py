|

:ref:`sphinxrst_py<sphinxrst_py>` > child_commands

.. _child_commands:

==============
Child Commands
==============

.. _child_commands.syntax:

Syntax
------
- ``{sphinxrst_children%`` 
  *file_1* :code:`%` ... :code:`%` *file_n* :code:`%}`
- ``{sphinxrst_child_link%`` 
  *file_1* :code:`%` ... :code:`%` *file_n* :code:`%}`

.. _child_commands.purpose:

Purpose
-------
A section can specify a set of files for which
the first section in each file (parent section for each file)
is a child of the current section.
This is done using the commands above at the
:ref:`beginning of a line<sphinxrst_py.notation.beginning_of_a_line>`.

.. _child_commands.white_space:

White Space
-----------
Leading and trailing white space is not included in the file names.
In addition, and empty file name is ignored.
This enables one to put the command on multiple input lines.

.. _child_commands.links:

Links
-----
The child link command also places
links to all the children of the current at the location of the command.
You can place a heading directly before the links to make them easier to find.

.. _child_commands.example:

Example
-------
.. toctree::
   :maxdepth: 1

   children_exam


----

sphinxrst input file: ``bin/sphinxrst.py``
