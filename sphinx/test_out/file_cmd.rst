|

:ref:`xsrst_py<xsrst_py>` > file_cmd

.. |space| unicode:: 0xA0
.. |tab| replace:: |space| |space| |space| |space|

.. meta::
   :keywords: file_cmd, file, command

.. index:: file_cmd, file, command

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

| ``{xsrst_file``
| |tab| *start*
| |tab| *stop*
| :code:`}`
|
| ``{xsrst_file``
| |tab| *start*
| |tab| *stop*
| |tab| *file_name*
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
Leading and trailing white space is not included in
*start*, *stop* or *file_name*.
The new line character separates these tokens.

.. meta::
   :keywords: file_name

.. index:: file_name

.. _file_cmd.file_name:

file_name
---------
If *file_name* is not in the syntax,
the code block is in the current input file.
Otherwise, the code block is in *file_name*.
This file name is relative to the directory where ``xsrst.py``
is executed; i.e., the top directory for this git repository.
This may seem verbose, but it makes it easier to write scripts
that move files and automatically change references to them.

.. meta::
   :keywords: start

.. index:: start

.. _file_cmd.start:

start
-----
The code block starts with the line following the occurence
of the text *start* in *file_name*.
If this is the same as the file containing the command,
the text *start* in the command will not match itself.
There must be one and only one occurence of *start* in *file_name*,
not counting the command itself when the files are the same.

.. meta::
   :keywords: stop

.. index:: stop

.. _file_cmd.stop:

stop
----
The code block ends with the line before the occurence
of the text *start* in *file_name*.
If this is the same as the file containing the command,
the text *stop* in the command will not match itself.
There must be one and only one occurence of *stop* in *file_name*,
not counting the command itself when the files are the same.

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
