|

:ref:`xsrst_py<xsrst_py>` > begin_cmd

.. |space| unicode:: 0xA0

.. meta::
   :keywords: begin_cmd, begin, and, end, commands

.. index:: begin_cmd, begin, and, end, commands

.. _begin_cmd:

======================
Begin and End Commands
======================

.. meta::
   :keywords: syntax

.. index:: syntax

.. _begin_cmd.syntax:

Syntax
------
- ``{xsrst_begin``        *section_name*:code:`}`
- ``{xsrst_begin_parent`` *section_name*:code:`}`
- ``{xsrst_end``          *section_name*:code:`}`

.. meta::
   :keywords: section

.. index:: section

.. _begin_cmd.section:

Section
-------
The start (end) of a section of the input file is indicated by a
begin (end) command at the
:ref:`beginning of a line<xsrst_py.notation.beginning_of_a_line>`.

.. meta::
   :keywords: section_name

.. index:: section_name

.. _begin_cmd.section_name:

section_name
------------
The *section_name* is a non-empty sequence of the following characters:
a-z, 0-9, and underbar ``_``.
A link is included in the index under the section name
to the first heading the section.
The section name is also added to the html keyword meta data.

.. meta::
   :keywords: output, file

.. index:: output, file

.. _begin_cmd.output_file:

Output File
-----------
The output file corresponding to *section_name* is

|space| |space| |space| |space|
:ref:`sphinx_dir<xsrst_py.command_line_arguments.sphinx_dir>`
``/xsrst/`` *section_name* ``.rst``

.. meta::
   :keywords: parent, section

.. index:: parent, section

.. _begin_cmd.parent_section:

Parent Section
--------------
There can be at most one begin parent command in an input file.
In this case there must be other sections in the file
and they are child of the parent section.
The parent section is a child
of the section that included this file using a :ref:`child command<child_cmd>`.

If there is no parent command in an input file,
all the sections in the file are children
of the section that included this file using a :ref:`child command<child_cmd>`.

----

xsrst input file: ``bin/xsrst.py``
