|

:ref:`sphinxrst_py<sphinxrst_py>` > file_command

.. _file_command:

============
File Command
============

.. _file_command.syntax:

Syntax
------
``{sphinxrst_file%`` *file_name* :code:`%` *start* :code:`%` *stop* :code:`%}`

.. _file_command.purpose:

Purpose
-------
A code block, from any file, is included by the command above at the
:ref:`beginning of a line<sphinxrst_py.notation.beginning_of_a_line>`.

.. _file_command.white_space:

White Space
-----------
Leading and trailing white space is not included in
*file_name*, *start*, or *end*.
This enables one to put the command on multiple input lines.

.. _file_command.file_name:

file_name
---------
If *file_name* is empty, the current input file is used.
Otherwise *file_name* is relative to the directory where ``sphinxrst.py``
is executed; i.e., the top directory for this git repository.

.. _file_command.start:

start
-----
The code block starts with the occurence
of the text *start* at the beginning of a line in *file_name*.
There can only be one occurence of *start* at the beginning
of a line in *file_name*.

.. _file_command.stop:

stop
----
The code block ends with the occurence
of the text *stop* at the beginning of a line and after *start*.
There can only be one occurence of *stop* at the beginning of a line
and after *start* and it must come after *start*.
The lines containing *start* and *stop* in *file_name* are not included in
the code block.

.. _file_command.spell_checking:

Spell Checking
--------------
Spell checking is **not** done for these code blocks.

.. _file_command.example:

Example
-------
.. toctree::
   :maxdepth: 1

   file_block_exam


----

sphinxrst input file: ``bin/sphinxrst.py``
