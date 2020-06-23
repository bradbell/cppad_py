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
``{xsrst_file%`` *file_name* :code:`%` *start* :code:`%` *stop* :code:`%}`

.. meta::
   :keywords: purpose

.. index:: purpose

.. _file_cmd.purpose:

Purpose
-------
A code block, from any file, is included by the command above at the
:ref:`beginning of a line<xsrst_py.notation.beginning_of_a_line>`.

.. meta::
   :keywords: white, space

.. index:: white, space

.. _file_cmd.white_space:

White Space
-----------
Leading and trailing white space is not included in
*file_name*, *start*, or *end*.
This enables one to put the command on multiple input lines.

.. meta::
   :keywords: file_name

.. index:: file_name

.. _file_cmd.file_name:

file_name
---------
If *file_name* is empty, the current input file is used.
Otherwise *file_name* is relative to the directory where ``xsrst.py``
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
The code block ends with the occurence
of the text *stop* at the beginning of a line and after *start*.
There can only be one occurence of *stop* at the beginning of a line
and after *start* and it must come after *start*.
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
