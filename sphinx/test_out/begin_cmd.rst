|

:ref:`sphinxrst_py<sphinxrst_py>` > begin_cmd

.. |space| unicode:: 0xA0

.. meta::
   :keywords: begin, and, end, commands

.. index:: begin, and, end, commands

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
- ``{sphinxrst_begin`` *section_name*:code:`}`
- ``{sphinxrst_end`` *section_name*:code:`}`

.. meta::
   :keywords: section

.. index:: section

.. _begin_cmd.section:

Section
-------
The start (end) of a section of the input file is indicated by a
begin (end) command at the
:ref:`beginning of a line<sphinxrst_py.notation.beginning_of_a_line>`.

.. meta::
   :keywords: section_name

.. index:: section_name

.. _begin_cmd.section_name:

section_name
------------
A *section_name* is a non-empty sequence of the following characters:
a-z, 0-9, and underbar ``_``.

.. meta::
   :keywords: output, file

.. index:: output, file

.. _begin_cmd.output_file:

Output File
-----------
The output file corresponding to *section_name* is

|space| |space| |space| |space|
:ref:`sphinx_dir<sphinxrst_py.command_line_arguments.sphinx_dir>`
``/sphinxrst/`` *section_name* ``.rst``

----

sphinxrst input file: ``bin/sphinxrst.py``
