|

:ref:`xsrst_py<xsrst_py>` > file_cmd

.. meta::
   :keywords: file, command

.. index:: file, command

.. _file_cmd:

============
File Command
============

.. meta::
   :keywords: syntax

.. index:: syntax

.. _file_cmd.syntax:

Syntax
------

| ``{xsrst_file`` *start*
|   *stop*
| :code:`}`
|
| ``{xsrst_file`` *start*
|   *stop*
|   *file_name*
| :code:`}`

.. meta::
   :keywords: purpose

.. index:: purpose

.. _file_cmd.purpose:

Purpose
-------
A code block, from any where in any file,
is included by the command above at the
:ref:`beginning of a line<xsrst_py.notation.beginning_of_a_line>`.

.. meta::
   :keywords: white, space

.. index:: white, space

.. _file_cmd.white_space:

White Space
-----------
Leading white space is not included in
*start*, *stop* or *file_name*.
The new line character terminates these tokens.

.. meta::
   :keywords: file_name

.. index:: file_name

.. _file_cmd.file_name:

file_name
---------
If *file_name* is not in the syntax,
the code block is in the current input file.
Otherwise, the code block is in *file_name*,
which is relative to the directory where ``xsrst.py``
is executed; i.e., the top directory for this git repository.

.. meta::
   :keywords: start

.. index:: start

.. _file_cmd.start:

start
-----
The code block starts with the occurence
of the text *start* at the beginning of a line in *file_name*.
There can only be one occurence of *start* at the beginning
of a line in *file_name*.

.. meta::
   :keywords: stop

.. index:: stop

.. _file_cmd.stop:

stop
----
The code block ends with the first occurence
of the text *stop* at the beginning of a line and after *start*.
The lines containing *start* and *stop* in *file_name* are not included in
the code block.

.. meta::
   :keywords: spell, checking

.. index:: spell, checking

.. _file_cmd.spell_checking:

Spell Checking
--------------
Spell checking is **not** done for these code blocks.

.. meta::
   :keywords: example

.. index:: example

.. _file_cmd.example:

Example
-------
.. toctree::
   :maxdepth: 1

   file_block_exam


----

xsrst input file: ``bin/xsrst.py``
