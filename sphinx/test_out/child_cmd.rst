!!!!!!!!!
child_cmd
!!!!!!!!!

.. toctree::
   :maxdepth: 1
   :hidden:

   no_parent_exam

.. meta::
   :keywords: child_cmd, children, commands

.. index:: child_cmd, children, commands

.. _child_cmd:

Children Commands
#################
.. contents::
   :local:

.. meta::
   :keywords: syntax

.. index:: syntax

.. _child_cmd.syntax:

Syntax
******

.. meta::
   :keywords: children

.. index:: children

.. _child_cmd.syntax.children:

children
========
| ``{xsrst_children``
|   *file_1*
|   ...
|   *file_n*
| :code:`}`

.. meta::
   :keywords: child_list

.. index:: child_list

.. _child_cmd.syntax.child_list:

child_list
==========
| ``{xsrst_child_list``
|   *file_1*
|   ...
|   *file_n*
| :code:`}`

.. meta::
   :keywords: child_table

.. index:: child_table

.. _child_cmd.syntax.child_table:

child_table
===========
| ``{xsrst_child_table``
|   *file_1*
|   ...
|   *file_n*
| :code:`}`

.. meta::
   :keywords: purpose

.. index:: purpose

.. _child_cmd.purpose:

Purpose
*******
A section can specify a set of files for which the
:ref:`parent section<begin_cmd.parent_section>` of each file
is a child of the current section.
(If there is not parent section in a file,
all the sections in the file are children of the current section.)
This is done using the commands above at the
:ref:`beginning of a line<xsrst_py.notation.beginning_of_a_line>`.

.. meta::
   :keywords: file, names

.. index:: file, names

.. _child_cmd.file_names:

File Names
**********
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
*****
The child list and child table commands also place
links to all the children of the current at the location of the command.
The links are displayed using the title for each section.
The child table command includes the section name next to the title.
You can place a heading directly before the links to make them easier to find.

.. meta::
   :keywords: example

.. index:: example

.. _child_cmd.example:

Example
*******
.. csv-table::
    :header:  "Child", "Title"
    :widths: 20, 80

    "no_parent_exam", :ref:`no_parent_exam`

----

xsrst input file: ``bin/xsrst.py``
