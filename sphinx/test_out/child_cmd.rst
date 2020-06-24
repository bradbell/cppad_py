|

:ref:`xsrst_py<xsrst_py>` > child_cmd

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

| ``{xsrst_children``
|   *file_1* 
|   ... 
|   *file_n* 
| :code:`}`
|
| ``{xsrst_child_link``
|   *file_1* 
|   ... 
|   *file_n* 
| :code:`}`

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
:ref:`beginning of a line<xsrst_py.notation.beginning_of_a_line>`.

.. meta::
   :keywords: file, names

.. index:: file, names

.. _child_cmd.file_names:

File Names
----------
A new line character must precede and follow each 
of the file names *file_1* ... *file_n*.
Leading and trailing white space is not included in the names
The file names are  relative to the directory where ``xsrst.py``
is executed; i.e., the top directory for this git repository.
This may seem verbose, but it makes it easier to write scripts
that move files and automatically change references to them.

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

xsrst input file: ``bin/xsrst.py``
